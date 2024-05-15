from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import JSONResponse


app = FastAPI()

inprogress_orders = {}

@app.post("/")
async def handle_request(request: Request):

    payload = await request.json()

    intent = payload['queryResult']['intent']['displayName']
    parameters = payload['queryResult']['parameters']
    output_contexts = payload['queryResult']['outputContexts']

    if intent == "track.order - context:ongoing-tracking":
        return JSONResponse(content={
            "fulfillmentText": f"Recieved =={intent}== in the backend"
            })
