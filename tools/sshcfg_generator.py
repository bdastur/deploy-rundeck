#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
ssh config generator: 
In environments where access to resources/nodes is possible only through a
jumphost, to be able to access the host a ssh tunnel needs to be created.

The script configures the .ssh/config file with the proxycommand to enable
accessing the hosts.
'''

import argparse
import pyansible.ansiInventory as inventory

JUMPHOST = "jump1.ash2.symcpe.net"

def parse_arguments():
    parser = argparse.ArgumentParser(prog="sshcfg_generator.py",
                                     description="Generate ssh config")
    parser.add_argument("--inventory",
                        help="Ansible inventory file",
                        required=True)
    parser.add_argument("--username",
                        help="Username to access the host",
                        required=True)
    parser.add_argument("--destination",
                        help="Path to the resource file",
                        required=True)
    parser.add_argument("--group",
                        help="Ansible host group",
                        required=False)

    args = parser.parse_args()

    return args


def generate_ssh_proxyconfig(hostlist, username, destfile):
    proxycfg_str = ""

    # Create jumphost proxy cfg.

    for hostobj in hostlist:
        for host in hostobj['hostlist']:
            proxycfg_str = proxycfg_str + "\n" + \
                "Host " + host + "\n" + \
                "  User " + username + "\n" + \
                "  Hostname " + host + "\n" + \
                "  Port 22" + "\n" + \
                "  ProxyCommand ssh -q -W %h:%p " + JUMPHOST + "\n" 

    print "proxycfg str: ", proxycfg_str

    with open(destfile, 'w') as outfile:
        outfile.write(proxycfg_str)


def main():
    args = parse_arguments()
    inv = inventory.AnsibleInventory(args.inventory)

    if args.group is None:
        hostlist = inv.get_hosts(group="all")
    else:
        hostlist = inv.get_hosts(group=args.group)

    for host in hostlist:
        print "HOST: ", host

    generate_ssh_proxyconfig(hostlist, args.username, 
                             args.destination)


if __name__ == '__main__':
    main()




