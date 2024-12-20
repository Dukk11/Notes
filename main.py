from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
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
          <!-- Notes will be displayed here -->
        </div>
      </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
