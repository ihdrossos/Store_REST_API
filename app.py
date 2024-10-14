import uuid

from flask import Flask, request
from db import items, stores


app = Flask("__name__")


# start app like: flask run
@app.get("/stores")
def get_stores():
    return {"stores": list(stores.values())}



@app.get("/stores/<string:store_id>")
def get_store(store_id):
    try:
        return stores[store_id]
    except KeyError:
        return {"message": "Store not found"}, 404



@app.get("/item/<string:item_id>")
def get_item(item_id):
    try:
        return stores[item_id]
    except KeyError:
        return {"message": "Item not found"}, 404



@app.get("/item")
def get_all_items():
    return {"items": list(items.values())}



@app.post("/stores")
def create_store():
    # to kaneis get() eite apo to insomnia eite apo tin efarmogi
    store_data = request.get_json()
    store_id   = uuid.uuid4().hex
    store = {**store_data, "id":store_id}
    stores[store_id] = store
    return store, 201



# add items to store
# search first for store
@app.post("/item")
def create_item(name):
    item_data = request.get_json() # einai gia ta items kai oxi gia to store, to onoma toy store einai apo to url -> <string:name>
    if item_data["store_id"] not in stores:
        return {"message": "Store not found"}, 404
    item_id = uuid.uuid4().hex
    item =  {**item_data, "id": item_id}
    items[item_id]= item
    return item, 201



