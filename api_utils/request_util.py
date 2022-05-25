import request

def simple_request(url, method="GET", **kwargs):
    return request(method, url)