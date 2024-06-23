# This is a sample Python script.
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def main():
    # Use a breakpoint in the code line below to debug your script.
    ###Import file
    df = pd.read_csv(r"/home/peter/Téléchargements/NVDA.csv")

    #Transformation column to date type
    df['Date']= pd.to_datetime(df['Date'])

    #Add SMA column function
    def SMA(value):
            df.insert(0,"SMA"+str(value) ,float(0))
            df["SMA"+str(value)]=df['Adj Close'].rolling(value).mean()

    #Call to SMA function
    SMA(50)
    SMA(100)
    SMA(200)


    #make subplots
    fig = make_subplots(specs=[[{"secondary_y": True}]])

    #Drawn candlestick chart
    fig.add_trace(go.Candlestick(x=df['Date'],
                open=df['Open'],
                high=df['High'],
                low=df['Low'],
                close=df['Close'],name="Price"), secondary_y=False,)

    #Add SMA's
    fig.add_trace( go.Scatter(x=df['Date'], y=df['SMA50'] ,name='SMA50', line=dict(color='#FFFF99') ), secondary_y=False )
    fig.add_trace( go.Scatter(x=df['Date'], y=df['SMA100'],name='SMA100', line=dict(color='#99FFCC') ) , secondary_y=False)
    fig.add_trace( go.Scatter(x=df['Date'], y=df['SMA200'],name='SMA200',line=dict(color='#FF99FF') ), secondary_y=False)

    #Add Volume chart
    fig.add_trace( go.Bar(x=df['Date'], y=df['Volume'],name='Volume',marker=dict(color='#9999FF') ) , secondary_y=True)

    #Add autorange to layout and change color background
    fig.update_layout(yaxis=dict(autorange=True, fixedrange=False) ,paper_bgcolor='rgba(224,224,224,99)', plot_bgcolor='rgba(0,0,0,100)' )

    #clean grid lines
    fig.update_yaxes(showgrid=False )

    #Display
    fig.show()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()