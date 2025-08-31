from flask import Flask, render_template

app = Flask(__name__)

links_data = [
    {
        "Title": "My Portfolio",
        "url": "https://www.google.com"
    },
    {
        "Title": "My Favourite Tech Blog",
        "url": "https://www.google.com"
    },
    {
        "Title": "My Secret Folder!!!",
        "url": "https://www.google.com"
    }
]

@app.route('/')
def home():
    """_summary_
    """
    return render_template('index.html', links=links_data)

if __name__ == '__main__':
    app.run(debug=True, port=5001)