#!/usr/bin/python
import speedtest
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint
import datetime
import csv

servers = []
pp = pprint.PrettyPrinter()
now = datetime.datetime.now()

def insert_error():
    tableName = "error.csv"
    row = [datetime.datetime.now()]
    with open(tableName, 'a') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(row)
    csvFile.close()
    exit()


def get_speed():
    global results
    s = speedtest.Speedtest()
    s.get_servers(servers)
    s.get_best_server()
    s.download()
    s.upload()
    s.results.share()
    return s.results


try:
    results = get_speed()
except:
    insert_error()



scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('Project-a9c411992d1a.json', scope)
client = gspread.authorize(creds)
sheet = client.open_by_key('1NCDOdFtQrJyf-nT4sJijvnoHkZiIG7C8BJPkYPqjdRc').sheet1

# results_dict = results.dict()
# insert
row = [now.strftime("%Y-%m-%d %X"),
       round(results.ping, 2),
       round((results.download / 1000.0 / 1000.0), 2),
       round((results.upload / 1000.0 / 1000.0), 2)]

sheet.append_row(row)