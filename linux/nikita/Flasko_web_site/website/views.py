from flask import Blueprint, render_template, request, flash
from .db import create_note, get_note

views = Blueprint('views', __name__)
collection_note = 'note'

@views.route('/home', methods=['GET', 'POST'])
def notes():
    paper = collection_note
    print(request.form)
    
    if request.method == 'POST':
        print(request.form)
        note = request.form.get('note')
        if len(note) < 1:
            flash('Note is too short!', category="error")
        else:
            create_note(note)
            flash('Note created successfully!', category="success")
            note_doc = get_note(note)
            if note_doc:  
                paper = request.form.get('note') 
                print(paper)
    print(request.method)         
    return render_template("home.html", result=paper)
