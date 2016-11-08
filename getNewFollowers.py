#coding:utf-8
from twitter import Twitter,OAuth
import datetime
import openpyxl
import pandas as pd
import itertools




def followers_flow():
    t = Twitter(auth=OAuth('791474940721717248-TVq1kCyv77L7rvENC6QxYbuxQgXho1U',
                           'RpThT3CosLg5pCooMKQeD4UzMDj1gkdckdNWiGMBXQ7ZT',
                           'pgtc5X4Hw0UfZciKKMTOGgHYm',
                           'tiXQUbLuVnIMJkgOUTXufubCoGRCXQr6AWmVSp8ZwxB5kJyE0H'))

    data = t.users.show(screen_name='ONgov')
    time = datetime.datetime.now().strftime("%Y-%m-%d")
    row = [time, data['followers_count']]

    wb = openpyxl.load_workbook("ongovFollowers.xlsx")
    ws = wb.active
    result = decide(time,ws)
    if result=='1':
        print("Do not need to update")
        exit()
    else:
        print('Need to update')
        addrow(row,ws)
        wb.save("ongovFollowers.xlsx")

def decide(time,ws):
    data = ws.values
    cols = next(data)[0:]
    data = list(data)
    data = (itertools.islice(r, 0, None) for r in data)
    df = pd.DataFrame(data, columns=cols)
    t = '0'
    for r in df['Date']:
        if (time == r):
            t = '1'
    return t

def addrow(row,ws):
    ws.append(row)

if __name__ == "__main__":
    print("This program is being run by itself")
    followers_flow()