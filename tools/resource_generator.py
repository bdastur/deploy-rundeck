#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
resource generator: The script reads an ansible inventory file and generates a 
rundeck format resource.yaml file. 

The script can be used as the resource model source.
'''

import argparse
import pyansible.ansiInventory as inventory
import yaml


def parse_arguments():
    parser = argparse.ArgumentParser(prog="rdeck_resources.py",
                                     description="Generate Resource data")
    parser.add_argument("--inventory",
                        help="Ansible inventory file",
                        required=True)
    parser.add_argument("--username",
                        help="Username",
                        required=True)
    parser.add_argument("--destination",
                        help="Path to the resource file",
                        required=True)
    parser.add_argument("--group",
                        help="Ansible host group",
                        required=False)

    args = parser.parse_args()

    return args


def generate_resources_yaml(hostlist, username, yamlfile):
    host_str = ""
    for hostobj in hostlist:
        if hostobj['group'] == "all":
            continue
        for host in hostobj['hostlist']:
            host_str = host_str + \
                host + ":" + " \n" + \
                "  tags: " + hostobj['group'] + "\n" + \
                "  osFamily: unix" + "\n" + \
                "  username: " + username + "\n" + \
                "  osArch: amd64" + "\n" + \
                "  osVersion: 3.10.0-229.20.1.el7.x86_64" + "\n" + \
                "  description: Rundeck node" + "\n" + \
                "  nodename: " + host + "\n" + \
                "  hostname: " + host + "\n" + \
                "  osName: Linux" + "\n"

    with open(yamlfile, 'w') as outfile:
        outfile.write(host_str)


def main():
    args = parse_arguments()
    inv = inventory.AnsibleInventory(args.inventory)

    if args.group is None:
        hostlist = inv.get_hosts()
    else:
        hostlist = inv.get_hosts(group=args.group)

    for host in hostlist:
        print "HOST: ", host

    generate_resources_yaml(hostlist, 
                            args.username,
                            args.destination)


if __name__ == '__main__':
    main()

