from flask import Flask, render_template, request, redirect
import weather
import db


app = Flask(__name__)

collection_clients = 'clients'
collection_weather = 'weather'


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if len(email) == 0 or len(password) == 0:
            return render_template('error.html'), 400
        
        query = {
            "email": email
        }

        client_inf = db.get_data(collection_clients, query)

        if client_inf == None:
            return redirect('/signup')  # Return the redirect response
        else: 
            if client_inf['password'] == password:
                # TODO: redirect to result
                return redirect('/weather')
            else:
                return render_template('error.html'), 400
            
    else:
        return render_template('login.html')



@app.route("/signup", methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        if len(email) == 0 or len(password) == 0:
            return render_template('error.html')

        client_info = {
            'email': email,
            'password': password
        }

        query = {
            "email": email
        }

        if db.get_data(collection_clients, query) == None:
            db.save_doc(collection_clients, client_info)

        return redirect('/login')
    
    elif request.method == 'GET':
        return render_template('signup.html')
    

@app.route("/weather", methods=['GET', 'POST'])
def weather_forecast():

    if request.method == 'GET':
        return render_template('weather.html')
    
    elif request.method == 'POST':
        city = request.form['city']
        if len(city) == 0:
            return render_template('error.html'), 400
        
        query = {
            'city': city
        }
        
        weather_info = weather.getforecast(city)
        if weather_info != None:
            weather_info["city"] = city
            if db.get_data(collection_weather, query) != None:
                db.del_doc(collection_weather, query)
            db.save_doc(collection_weather, weather_info)
            return render_template('weather.html', forecast=weather_info)
        else:

            weather_saved = db.get_data(collection_weather, query) 
            if weather_saved != None:
                return render_template('weather.html', forecast=weather_saved)
            else:
                return render_template('error.html'), 404
