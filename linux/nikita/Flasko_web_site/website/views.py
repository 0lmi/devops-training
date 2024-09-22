from flask import Blueprint, render_template, request, flash, redirect
from .db import create_note, find_note, delete_note

views = Blueprint('views', __name__)
collection_note = 'note'

@views.route('/home', methods=['GET', 'POST'])
def notes():
    if request.method == 'POST':
        note_html = request.form.get('note_html')
        if len(note_html) < 1:
            flash('Note should have atleast 1 character', category='error')
            return render_template("home.html", boolean=True)    
        else:
            create_note(note_html)
            flash('Note created!', category='success')
            
          
    all_notes = find_note()
    return render_template("home.html", all_notes=all_notes)