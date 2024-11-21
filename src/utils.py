#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 21:25:13 2024

@author: sergej
"""

import requests

def fetch_lovecraft(url):
    hp_text = requests.get(url)
    return(hp_text.text)