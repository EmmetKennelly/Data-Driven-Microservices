#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  6 21:30:30 2020

@author: emmet
"""
from slackclient import SlackClient
from kubernetes import client, config
import json
from datetime import datetime


def print_clock():
    now = datetime.now()
    clock = "%02d:%02d" % (now.hour, now.minute)
    print(clock)
    return clock


sc = SlackClient(token)

def remind(event, context):
    return sc.api_call(
                       "chat.postMessage",
                       channel="#kubeless",
                       text="""<!here> This is a reminder for you to please check your deplyment as it is still runnning.""",as_user=True)
