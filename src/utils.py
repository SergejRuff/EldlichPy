#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 21:25:13 2024

@author: sergej
"""

import requests
import re 

def fetch_lovecraft(url):
    hp_text = requests.get(url)
    title_story = re.search(r'<title>"(.*?)"',hp_text.text).group(1)
    
    match = re.search(r'<div align="justify">(.*?)</div>', 
                      hp_text.text, re.DOTALL)
    
    text_content = match.group(1)
    text_content = re.sub(r'<.*?>', '', text_content)
    
    text_content = text_content.replace("&mdash;", "—").replace("&lt;", "<").replace("&gt;", ">")\
                           .replace("&amp;", "&").replace("&rdquo;", "”").replace("&ldquo;", "“")\
                           .replace("&rsquo;", "’").replace("&lsquo;", "‘").replace("&nbsp;", " ").replace("&quot;", '"')\
                           .replace("&apos;", "'").replace("&uuml;", "ü").replace("&eacute;", "é")


    return({"title":title_story,"text":text_content})