from connection import server_url, hash_query, get_authorize
from model import Order

import requests


def post_order(order: Order):
    """

    :return: 주문 결과 (매수 취소 시 uuid 필요)
    """

    query_hash = hash_query(order.model_dump())
    headers = get_authorize(query_hash)

    response = requests.post(f"{server_url}/v1/orders", headers=headers, json=order.model_dump())
    return response.json()


def cancel_order(order_id: str):
    """

    :param order_id: 매수 uuid
    :return:

    todo: 모델 맞게 수정
    """
    params = {
        'uuid': order_id
    }

    query_hash = hash_query(params)
    headers = get_authorize(query_hash)

    requests.delete(server_url + '/v1/order', params=params, headers=headers)


def get_orders():

    query_hash = hash_query({})
    headers = get_authorize(query_hash)

    response = requests.get(f"{server_url}/v1/orders", headers=headers)
    return response
