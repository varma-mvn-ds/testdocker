from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///notes.db'
app.config['SECRET_KEY'] = os.getenv('secret_key')
db = SQLAlchemy()

print('secret_key for database', os.getenv('secret_key'))
print('xyz_key', os.getenv('xyz_key'))

db.init_app(app) # connection between db and app
app.app_context().push()

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Note {self.id}>'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        note_content = request.form['content']
        if note_content:
            new_note = Note(content=note_content)
            db.session.add(new_note)
            db.session.commit()
            return redirect(url_for('index'))
    notes = Note.query.all()
    return render_template('index.html', notes=notes)

if __name__ == '__main__':
    db.create_all()
    app.run(host='0.0.0.0', port=8080)
