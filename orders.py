from connection import server_url, hash_query, get_authorize
from model import Order, OrderResponse

import requests


def post_order(order: Order):
    """

    :return: 주문 결과 (매수 취소 시 uuid 필요)
    """

    query_hash = hash_query(order.model_dump())
    headers = get_authorize(query_hash)

    response = requests.post(f"{server_url}/v1/orders", headers=headers, json=order.model_dump())
    return response.json()


def cancel_order(order: OrderResponse):
    """

    :param order: 선택 주문 정보
    :return:

    todo: 모델 맞게 수정
    """
    params = {
        'uuid': order.uuid
    }

    query_hash = hash_query(params)
    headers = get_authorize(query_hash)

    response = requests.delete(server_url + '/v1/order', params=params, headers=headers)

    return response.json()


def get_orders():

    query_hash = hash_query({'states[]': ['wait']})
    headers = get_authorize(query_hash)

    response = requests.get(f"{server_url}/v1/orders", headers=headers)
    return response.json()
