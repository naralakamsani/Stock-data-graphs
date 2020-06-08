#!/usr/bin/env python
# coding: utf-8

# In[130]:


from bokeh.plotting import figure, show, output_file
from pandas_datareader import data
import datetime

start=datetime.datetime(2019,6,1)
end=datetime.datetime(2020,2,10)

df=data.DataReader("AAPL", "yahoo", start=start,end=end)

def inc_dec(c,o):
    if c>o:
        value = "Increase"
    elif c<o:
        value = "Decrease"
    else:
        value = "Equal"
    return value
df["status"]=[inc_dec(c,o) for c,o in zip(df.Close,df.Open)]
df["middle"]=(df.Open+df.Close)/2
df["change"]=abs(df.Open-df.Close)

p=figure(x_axis_type='datetime',width=1500,height=750,title="Stock Price Change Per_Day",sizing_mode="scale_width")

p.grid.grid_line_alpha=0.3

twelve_hours=12*60*60*1000

p.segment(df.index,df.High,df.index,df.Low,color="black")
p.rect(df.index[df.status=="Increase"],df.middle[df.status=="Increase"], twelve_hours,df.change[df.status=="Increase"],fill_color="green",line_color="black")
p.rect(df.index[df.status=="Decrease"],df.middle[df.status=="Decrease"], twelve_hours,df.change[df.status=="Decrease"],fill_color="red",line_color="black")

output_file("stock_price_change_per_day.html")

show(p)




