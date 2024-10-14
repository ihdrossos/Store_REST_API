stores = [
          {"name": "My Store",
           "items": [{'name': 'chair', 'price':15.99}]
          },
        {"name": "My Store 2",
           "items": [{'name': 'desktop', 'price':1500.99}]
          }
     ]





for store in stores:
    print(store)
    stg = store["items"]
    print(stg[0]['price'])
    store_items = store.items()

