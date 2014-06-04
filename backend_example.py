# Run with `python backend_example.py`

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def json_demo():
    data = {
        "name": "Razzi Abuissa",
        "age": 21,
        "email": "razzi53@gmail.com",
        "interests": [
            "coding",
            "entrepreneurship",
            "environmentalism"
        ],
        "work_history": {
            "Penncycle": "September 2012 to March 2014",
            "Venmo": "Summer 2014",
            "DuPont": "Summer 2013",
            "Penn Chemistry department": "Summer 2012",
        }
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
