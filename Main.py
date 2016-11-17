import httplib2
import time

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
        return eval(content.decode())
    '''
    得到网络中的节点信息
    '''
    def get_hosts(self, address,container_name='default', username="admin", password="admin"):
        http = httplib2.Http()
        http.add_credentials(name=username, password=password)
        headers = {'Accept': 'application/json'}
        response, content = http.request(uri=self.url + "/controller/nb/v2/hosttracker/" + str(container_name) + "/address/" + str(address),
                                         headers=headers)
        return content.decode()
        # return eval(str(content.decode()).replace("false", '"false"'))
    '''
    流表规则下发
    '''
    def install_flow(self, node, ip_from, ip_to, container_name='default'):
        http = httplib2.Http()
        http.add_credentials('admin', 'admin')
        headers = {'Accept': 'application/json'}
        flow_name = 'flow_' + str(int(time.time()*1000))
        body = '{"installInHw":"true","name":"' + flow_name + '",' \
               '"node":{"id":"' + node + '","type":"OF"},' \
               '"priority":"500","etherType":"0x800",' \
               '"nwSrc":"' + ip_from + '","nwDst":"' + ip_to + '","actions":["SET_NW_TOS=63"]}'

        '''
        ********* Body里面所有可选的参数 ***********
        <?xml version="1.0" encoding="UTF-8"?>
        <flowConfig>
          <tpSrc>...</tpSrc>
          <protocol>...</protocol>
          <vlanId>...</vlanId>
          <node>
            <type>...</type>
            <id>...</id>
          </node>
          <vlanPriority>...</vlanPriority>
          <idleTimeout>...</idleTimeout>
          <priority>...</priority>
          <ingressPort>...</ingressPort>
          <tosBits>...</tosBits>
          <name>...</name>
          <hardTimeout>...</hardTimeout>
          <dlDst>...</dlDst>
          <installInHw>...</installInHw>
          <etherType>...</etherType>
          <actions>...</actions>
          <actions>...</actions>
          <!--...more "actions" elements...-->
          <cookie>...</cookie>
          <dlSrc>...</dlSrc>
          <nwSrc>...</nwSrc>
          <nwDst>...</nwDst>
          <tpDst>...</tpDst>
        </flowConfig>
        '''
        headers = {'Content-type': 'application/json'}
        print(body)
        response, content = http.request(uri=self.url + '/controller/nb/v2/flowprogrammer/' + container_name + '/node/OF/' + str(node) + '/staticFlow/' + flow_name, body=body, method='PUT',headers=headers)
        print(content.decode())
    def get_info(self, container_name='default', username="admin", password="admin"):
        http = httplib2.Http()
        http.add_credentials(name=username, password=password)
        headers = {'Accept': 'application/json'}
        response, content = http.request(
            uri=self.url + "/controller/nb/v2/switchmanager/default/nodes",
            headers=headers)
        return content.decode()



odl = OdlUtil('127.0.0.1', '8080')
odl.install_flow('00:00:00:00:00:00:00:02','10.0.0.1','10.0.0.3')
# result = odl.get_hosts("10.0.0.2")
# print(odl.get_info())
# print(result)


