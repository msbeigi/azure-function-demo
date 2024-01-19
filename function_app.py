import azure.functions as func
import datetime
import json
import logging
import azure.functions as func
from azure.storage.queue import QueueService
from azure.storage.table import TableService, Entity

app = func.FunctionApp()

@app.route(route="HttpSampleProcessor", auth_level=func.AuthLevel.ANONYMOUS)
def HttpSampleProcessor(req: func.HttpRequest) -> func.HttpResponse:
    # logging.info('Python HTTP trigger function processed a request.')

    # name = req.params.get('name')
    # if not name:
    #     try:
    #         req_body = req.get_json()
    #     except ValueError:
    #         pass
    # else:
    #     name = req_body.get('name')

    # if name:
    #     return func.HttpResponse(f"\nHello, {name}. This HTTP triggered function executed successfully.")
    # else:
    #     return func.HttpResponse(
    #          "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
    #          status_code=200
    #     )
    try:
        req_body = req.get_json()
        name = req_body.get('name')

        if name:
                return func.HttpResponse(json.dumps({"message": f"Hello, {name}!"}), mimetype="application/json")
        else:
                return func.HttpResponse("Invalid input. 'name' parameter is required.", status_code=400)
    except ValueError:
        return func.HttpResponse("Invalid JSON input.", status_code=400)