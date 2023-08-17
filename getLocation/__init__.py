import logging

import azure.functions as func
import json

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    res = func.HttpResponse(
            json.dumps({"location" : "Paris"}),
            mimetype="application/json",
        )
    return res
