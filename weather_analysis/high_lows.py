import csv
from datetime import datetime
from matplotlib import pyplot as plt
filename='sitka_weather_2014.csv'
dates=[]
highs=[]
lows=[]
with open(filename) as f:
    reader=csv.reader(f)
    header_row=next(reader)
    for row in reader:
        date=datetime.strptime(row[0],'%Y-%m-%d')
        high=int(row[1])
        low=int(row[3])
        dates.append(date)
        highs.append(high)
        lows.append(low)
    fig=plt.figure(dpi=128,figsize=(10,6))
    plt.plot(dates,highs,c='red',alpha=0.5)
    plt.plot(dates, lows, c='blue',alpha=0.5)
    plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)
    plt.title("Sitka temperatures",fontsize=24)
    plt.xlabel('',fontsize=16)
    plt.ylabel('Tempature (F)',fontsize=16)
    fig.autofmt_xdate()
    plt.tick_params(axis='both',which='major',labelsize=16)
    plt.show()
