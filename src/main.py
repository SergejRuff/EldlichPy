#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 20:58:50 2024

@author: sergej
"""

from utils import fetch_lovecraft
from sys import argv
import re 

def main():
    #url = argv[1]
    url = "https://www.hplovecraft.com/writings/texts/fiction/b.aspx"
    print(f"the current url: \n{url}\n")
    hp_text = fetch_lovecraft(url)
    #print(hp_text)
    title = re.search(r'<title>"(.*?)"',hp_text).group(1)
    print(f"the title of the selected work: \n'{title}' by H.P. Lovecraft")
    

if __name__ == '__main__':
    main()
