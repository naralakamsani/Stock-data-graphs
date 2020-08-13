from bokeh.plotting import figure, show, output_file
from pandas_datareader import data
import datetime

#Define the time frames durring which the stock data is taken
start=datetime.datetime(2019,6,1)
end=datetime.datetime(2020,2,10)

#Read and load the data
df=data.DataReader("AAPL", "yahoo", start=start,end=end)

#Define if the stocks increased or decreased on a given day.
def inc_dec(c,o):
    if c>o:
        value = "Increase"
    elif c<o:
        value = "Decrease"
    else:
        value = "Equal"
    return value

#Add the status of increase or decrease of stocks in a data to the dataset
df["status"]=[inc_dec(c,o) for c,o in zip(df.Close,df.Open)]

#Add the average stock for each day to dataset
df["middle"]=(df.Open+df.Close)/2

#Add change in price of stock per each day to dataset
df["change"]=abs(df.Open-df.Close)

#Define basic properties of the graph
p=figure(x_axis_type='datetime',width=1500,height=750,title="Stock Price Change Per_Day",sizing_mode="scale_width")
p.grid.grid_line_alpha=0.3

#define twelve_hours in milliseconds
twelve_hours=12*60*60*1000

#plot the two parts of candle stick graph
#Plot all the segments
p.segment(df.index,df.High,df.index,df.Low,color="black")

#Plot the rectangles of a candle stick where stock prices increase on the day
p.rect(df.index[df.status=="Increase"],df.middle[df.status=="Increase"], twelve_hours,df.change[df.status=="Increase"],fill_color="green",line_color="black")

#Plot rectangles of a candle stick where stock prices decrease on the day, in the same plane as the previous one
p.rect(df.index[df.status=="Decrease"],df.middle[df.status=="Decrease"], twelve_hours,df.change[df.status=="Decrease"],fill_color="red",line_color="black")

#Convert graph to html
output_file("stock_price_change_per_day.html")

#Show the graph
show(p)




