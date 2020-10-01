#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 14:09:08 2020

@author: emmet
"""

from flask import Flask 
import redis 

app = Flask(__name__) 
 
@app.route('/logs') 
def print_logs():
    output = ''
    try:
        conn = redis.StrictRedis(host='redis', port=8080)
        for key in conn.scan_iter("log.analysis_server*"):
            value = str(conn.get(key))
            output += str(key) + value + '<br>'
    except Exception as ex:
        output = 'Error:' + str(ex)
    return output

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')