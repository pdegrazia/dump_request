import requests
from requests_toolbelt.utils import dump


def dump_results(func):
    def decorator(*args, **kwargs):
        r = func(*args, **kwargs)
        data = dump.dump_all(r)
        print data.decode('utf-8')
    return decorator


@dump_results
def simple_get_request():
    resp = requests.get('https://workshare.pythonanywhere.com', headers={}, params={})
    return resp


if __name__ == '__main__':
    simple_get_request()
