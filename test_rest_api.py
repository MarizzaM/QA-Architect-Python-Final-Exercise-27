import requests  # need to install in settings
import json
import pytest


class RestObject:
    def __init__(self, d):
        self.__dict__ = d

    def __str__(self):
        result = ""
        for k, v in self.__dict__.items():
            result += k
            result += " : "
            result += str(v)
            result += '\n'
        return result


def test_rest_api_get_coupon():
    resp = requests.get("http://127.0.0.1:5000/product/1")
    d = json.loads(resp.content)
    t = RestObject(d)
    assert t.id == 1
    assert t.name == 'Pen'
    assert t.price == 9.99
    assert t.quantity == 6


def test_rest_api_post_product():
    resp = requests.post("http://127.0.0.1:5000/product/",
                         data='{"name": "bamba", "price": 4.99, "quantity": 5}',
                         headers={"Content-type": "application/json"});
    print(f'Status code = {resp.status_code}');
    assert resp.status_code == 200
    resp_ = requests.get("http://127.0.0.1:5000/product/4")
    d = json.loads(resp_.content)
    t = RestObject(d)
    assert t.id == 4
    assert t.name == 'bamba'
    assert t.price == 4.99
    assert t.quantity == 5


def test_rest_api_update_product():
    resp = requests.put("http://127.0.0.1:5000/product/4",
                        data='{"name": "bambaba", "price": 44.99, "quantity": 555}',
                        headers={"Content-type": "application/json"});
    print(f'Status code = {resp.status_code}');
    assert resp.status_code == 200
    resp_ = requests.get("http://127.0.0.1:5000/product/4")
    d = json.loads(resp_.content)
    t = RestObject(d)
    assert t.id == 4
    assert t.name == 'bambaba'
    assert t.price == 44.99
    assert t.quantity == 555


def test_rest_api_del_product():
    resp = requests.delete("http://127.0.0.1:5000/product/4")
    print(f'Status code = {resp.status_code}');
    assert resp.status_code == 200
    resp_ = requests.get("http://127.0.0.1:5000/product/4")
    assert resp_.status_code == 500
