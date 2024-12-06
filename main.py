from flask import Flask, request, redirect, url_for

app = Flask(__name__)

notes = []

@app.route('/')
def home():
    notes_html = ''.join(f'<div class="note">{note}</div>' for note in notes)
    return f'''
    <!doctype html>
    <html lang="en">
      <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <title>Notes App</title>
        <link rel="stylesheet" href="/static/css/styles.css">
      </head>
      <body>
        <h1>Notes App</h1>
        <form action="/add_note" method="post">
          <input type="text" name="note" placeholder="Enter your note">
          <button type="submit">Add Note</button>
        </form>
        <div id="notes">
          {notes_html}
        </div>
      </body>
    </html>
    '''

@app.route('/add_note', methods=['POST'])
def add_note():
    note = request.form['note']
    notes.append(note)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
