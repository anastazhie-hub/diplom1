import configuration
import requests
import data

def post_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,  # подставялем полный url
                         json=body)  # тут тело

response = post_order(data.order_body)
print(response.status_code)
print(response.json())



def get_order_info():
    return requests.get(configuration.URL_SERVICE + configuration.FIND_ORDER_INFO_PATH,
                        params=data.order_track)

response = get_order_info()
print(response.status_code)
print(response.json())


