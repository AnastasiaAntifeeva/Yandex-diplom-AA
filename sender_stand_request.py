import requests
import data
import configuration


# создаем новый заказ

def post_new_order(order_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDERS,  # подставляем полный url
                         json=order_body)  # тут тело

# Выполнить запрос на получение заказа по треку заказа
def get_order(order_track):
    params = {"t": order_track}
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDERS, params=params)

