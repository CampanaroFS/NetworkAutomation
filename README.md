# Intro

This is a project where we will be using python to do network automation. The plan is to be documenting the taks done and based on that create a folder related to that so anyone can use it.

# Projects
## 1.- Render Cisco interface Config using python and json

In this project we will be using python to render a Cisco interface configuration. The idea is to have a json file with the interface configuration and based on that render the configuration. The idea is to have a json file like this:

```json
[
  {
    "interface": "GigabitEthernet1/0/1",
    "description": "LAN",
    "ip_address": "10.0.0.0",
    "subnet_mask": "255.255.255.0",
    "shut_down": "no shutdown",
    "speed": "1000", #
    "duplex": "full"
  },
]
```
The result should be writen on a file so it can be used later.


## 2. Render Cisco interface Config using python, json and jinja2

Using similar json file as before, we will be using jinja2 to render the configuration. The idea is to have a jinja2 template file and based on that render the configuration.
```json
[
  {
    "interface": "GigabitEthernet1/0/1",
    "description": "LAN",
    "ip_address": "10.0.0.0",
    "subnet_mask": "255.255.255.0",
    "enabled": true,
    "speed": "1000", # optional
    "duplex": "full" # optional
  },
]
```
The result should be writen on a file so it can be used later.

## 3 Push the interface config to a device using SSH

## 4 Push the interface config to a device using RESTCONF

## 5 Push the interface config to a device using NETCONF

## 6 Script to validate configuration being pushed
