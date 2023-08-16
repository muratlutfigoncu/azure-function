import logging

import azure.functions as func
import requests
import json

def make_http_request():
    url =  "https://api.open-meteo.com/v1/forecast?latitude=48.8534&longitude=2.3488&hourly=temperature_2m&current_weather=true"

    try:
        response = requests.get(url, headers={})
        response.raise_for_status() 

        return response.text
    except requests.exceptions.RequestException as e:
        return f'Error: {e}'

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    response = make_http_request()

    headers = {
        'Access-Control-Allow-Origin': '*',  # You can specify specific domains here instead of '*'
        'Access-Control-Allow-Methods': 'GET,OPTIONS',
        'Access-Control-Allow-Headers': 'Content-Type,Authorization',
        'Access-Control-Allow-Credentials': 'true'
    }
    if req.method == 'OPTIONS':
        return func.HttpResponse(headers=headers)
    
    try:
        data = json.loads(response)
        logging.info(data)
        logging.info(data.get("current_weather").get("temperature"))
        res = func.HttpResponse(
            json.dumps({"temperature" : data.get("current_weather").get("temperature")}),
            mimetype="application/json",
        )
    except:
        res = func.HttpResponse(
            json.dumps({"temperature": 1000}),
            mimetype="application/json",
            headers=headers
        )
    return res