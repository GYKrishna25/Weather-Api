import os
# from getpass import getpass
from dotenv import load_dotenv
import requests
from flask import Flask, request, render_template, jsonify

# from getpass import getpass
# # Prompt user to enter API key securely
# api_key = getpass('Enter your API key: ')
# # Set the API key as an environment variable
# os.environ['OPENAI_API_KEY'] = api_key
# # Access the API key from environment variables
# retrieved_api_key = os.getenv('OPENAI_API_KEY')

load_dotenv(".env")
default_api_key = os.getenv('API_KEY')

def api_key_retrieval(APIKEY):
    if APIKEY:
        print("API Key retrieved successfully!")
    else:
        print("Failed to retrieve API Key")


app = Flask(__name__)

@app.route('/')
def weather_homepage():
    return render_template("index.html")

@app.route("/weatherapp", methods=['POST'])
def get_weatherdata():
    url = "https://api.openweathermap.org/data/2.5/weather"

    city = request.form.get("city"),
    units = request.form.get('units'),
    user_api_key = request.form.get('appid')

    api_key = user_api_key if user_api_key else default_api_key

    api_key_retrieval(api_key)
    
    payload = {
        'q': city,
        'units' : units,
        'appid' : api_key
    }
    response = requests.get(url, params=payload)
    data = response.json()

    # Return data directly, Flask will automatically convert it to JSON
    return f"data: {data}" # Flask will handle conversion to JSON

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5002)
