#!/usr/bin/env python
import consul
import requests
import argparse


class ConsulCleanUp:
    def __init__(self, _consul):
        self.c = _consul
        self.node_map = {node['Node']: node['Address'] for node in self.c.catalog.nodes()[1]}

    def get_critical_service(self, dc_list=None, tag=None):
        if not dc_list:
            dc_list = [str(dc) for dc in self.c.catalog.datacenters()]
        services = []
        for _ in dc_list:
            services.extend(self.c.health.state('critical', dc=_)[1])
            if tag:
                services.extend(filter(lambda service: tag not in list(service['ServiceTags']), services))
        return services

    def deregister(self, services):
        for service in services:
            requests.put(
                'http://{0}:8500/v1/agent/service/deregister/{1}'.format(self.node_map[service['Node']],
                                                                         service["ServiceID"]))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Cleanup consul services')
    parser.add_argument('--host', help='The consul host to connect to', default='127.0.0.1')
    parser.add_argument('--port', help='The consul port to connect to', default='8500')
    parser.add_argument('--tag', help='filter tag')
    args = parser.parse_args()
    c = consul.Consul(host=args.host, port=args.port)
    cc = ConsulCleanUp(c)
    cc.deregister(cc.get_critical_service(tag=args.tag))
    print "deregister successfully"
