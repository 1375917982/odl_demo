import httplib2

http = httplib2.Http()

base_url = 'http://192.168.231.128:8080/'

url = base_url
response, content = http.request(uri=url, method='GET')
cookie = response.get('set-cookie').replace('; Path=/','')
print(cookie)
headers = {'Cookie': cookie, 'Content-Type': 'application/x-www-form-urlencoded'}
url = base_url + 'j_security_check'
body = 'j_username=hupeng&j_password=123456'
response, content = http.request(uri=url, method='POST', body=body, headers=headers)
url = base_url
headers = {'Cookie':cookie}
response, content = http.request(uri=url, method='GET', headers=headers)
cookie_list = response.get('set-cookie').split('; Path=/,')
cookie = ''
for cook in cookie_list:
    if cookie == '':
        cookie = cookie + cook.replace('; Path=/', '')
    else:
        cookie = cookie + '; ' + cook.replace('; Path=/', '')


url = base_url + 'controller/nb/v2/flowprogrammer/default/node/OF/00:00:00:00:00:02/staticFlow/Flyye2'
headers = {'Cookie':cookie,'Accept':'application/json'}
response, content = http.request(uri=url, method='GET', headers=headers)

content = content.decode('utf8')
print(content)

