import requests
r = requests.get('https://api.github.com/events')
r.status_code
r.headers['content-type']
# r.text
r.encoding
r.json()


######### 传递URL
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get("http://httpbin.org/get", params=payload)
r.url


######### 定制请求头部
header = {'user-agent': 'safari'}
r = requests.get("http://httpbin.org/get", headers=header)
