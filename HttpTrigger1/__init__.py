import logging

import azure.functions as func
import requests
import json

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    weather_url = "https://api.open-meteo.com/v1/forecast?latitude=48.8534&longitude=2.3488&hourly=temperature_2m"
    response = requests.get(url=weather_url)
    try:
        data = json.loads(response.text)
        res = {"temperature": data.get("current_weather").get("temperature")}
    except:
        res = {"temperature": 1000}
    return res