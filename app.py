'''The main Flask App file'''
from flask import Flask, render_template
from data import get_data

app = Flask(__name__)


@app.route('/')
def hello():
    '''This function renders the index.html file'''
    data = get_data()
    print(data)
    return render_template(
        'index.html',
        song_name=data[0],
        artist_name=data[1],
        album_name=data[2],
        song_url=data[3],
        album_url=data[4]
    )


if __name__ == '__main__':
    app.run(debug=True)
