import httplib2

class OdlUtil:
    url = ''
    def __init__(self, host, port):
        self.url = 'http://' + host + ':' + str(port)
    '''
    得到网络中的拓扑信息
    '''
    def get_topology(self, container_name='default', username="admin", password="admin"):
        http = httplib2.Http()
        http.add_credentials(name=username, password=password)
        headers = {'Accept': 'application/json'}
        response, content = http.request(uri=self.url + '/controller/nb/v2/topology/' + str(container_name), headers=headers)
        return content.decode()
odl = OdlUtil('127.0.0.1', '8080')
print(odl.get_topology(username="admin", password="admin"))