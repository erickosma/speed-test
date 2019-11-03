#!/usr/bin/python
import speedtest
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint
import datetime

servers = []
pp = pprint.PrettyPrinter()
now = datetime.datetime.now()

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('Project-a9c411992d1a.json', scope)
client = gspread.authorize(creds)

s = speedtest.Speedtest()
s.get_servers(servers)
s.get_best_server()
s.download()
s.upload()
s.results.share()

results = s.results
# results_dict = results.dict()

sheet = client.open_by_key('1NCDOdFtQrJyf-nT4sJijvnoHkZiIG7C8BJPkYPqjdRc').sheet1
# insert
row = [now.strftime("%Y-%m-%d %X"),
       round(results.ping, 2),
       round((results.download / 1000.0 / 1000.0), 2),
       round((results.upload / 1000.0 / 1000.0), 2)]

sheet.append_row(row)
