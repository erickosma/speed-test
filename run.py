#!/usr/bin/python
# -*- coding: utf-8 -*-

import speedtest

servers = []

s = speedtest.Speedtest()
s.get_servers(servers)
s.get_best_server()
s.download()
s.upload()
s.results.share()

results = s.results
# results_dict = results.dict()

print(results.ping)
print((results.download / 1000.0 / 1000.0))
print((results.upload / 1000.0 / 1000.0))
