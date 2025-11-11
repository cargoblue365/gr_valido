# pip install Flask requests
import flask
from flask import Flask, jsonify, request, render_template
import requests

print(flask.__version__)

app = Flask(__name__)

AIRTABLE_TOKEN = "pathApM7HaebDYSvS"
BASE_ID = "GESTÃO DE AGREGADOS_VALIDO"      #"app1avrro5zomTG6o"  # substitua pelo seu ID correto
TABLE_NAME = "PROGRAMAÇÃO STATUS ESPELHAMENTO"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/dados')
def dados():
    headers = {"Authorization": f"Bearer {AIRTABLE_TOKEN}"}
    url = f"https://api.airtable.com/v0/{BASE_ID}/{TABLE_NAME}"
    r = requests.get(url, headers=headers)
    return jsonify(r.json())

if __name__ == '__main__':
    app.run(debug=True)



# python -m pip install Flask requests
# from flask,
# import Flask, jsonify, request, render_template
# print(flask.__version__)
# import requests


# app = Flask(__name__)

# AIRTABLE_TOKEN = "pathApM7HaebDYSvS"
# BASE_ID = "GESTÃO DE AGREGADOS_VALIDO"
# TABLE_NAME = "PROGRAMAÇÃO STATUS ESPELHAMENTO"

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/dados')
# def dados():
#     headers = {"Authorization": f"Bearer {AIRTABLE_TOKEN}"}
#     url = f"https://api.airtable.com/v0/{BASE_ID}/{TABLE_NAME}"
#     r = requests.get(url, headers=headers)
#     return jsonify(r.json())

# if __name__ == '__main__':
#     app.run(debug=True)
