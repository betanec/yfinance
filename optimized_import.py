#!/usr/bin/python3

import time
import os.path
import http.client as hc
import pandas as pd
from bs4 import BeautifulSoup
from clint.textui import progress

def download_results(con=None):

    start = time.time()

    max_download = 380
    batch_size = 100 #constant


    if not con:
        con = hc.HTTPSConnection('www.finance.yahoo.com')

        all_results = []

        for offset in range(max_download//batch_size, -1, -1):
            if offset > 0:
                con.request('GET', '/cryptocurrencies?offset='+str(offset*batch_size)+'&count=100&guce_referrer=aHR0cHM6Ly9hd2F5LnZrLmNvbS8&guce_referrer_sig=AQAAAGQ-A3a1nflvpBlU0UigNjkJ0P9MMk2ffmSA2ctaQpHiSOI-f6f3kqGFEPFbZg1xEIiZuZ7pRXunLbH0XxKwTm8pUfgUwOyhPiOPo__57nimJbNbJQzFb4PiQxb40KSYRJITqikoZG334pZItcdLRBJZkIAVnfCJOdRui4K9wdSX')
            else:
                con.request('GET', '/cryptocurrencies')
                res = con.getresponse()
                print("Status :", res.status)
                body = res.read()
                soup = BeautifulSoup(body, 'html.parser')
                results = [i for i in soup.find_all('a', {'class' : 'Fw'})]
                print(body)

    print(results)

    end = time.time()
    print('Time :', end-start)

    return all_results

# говно которое не заработало с парсингом(хз поч)