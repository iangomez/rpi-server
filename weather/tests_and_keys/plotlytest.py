import plotly.plotly as py
from plotly.graph_objs import Scatter, Layout, Figure
import time
import random

username = 'iangomez'
api_key = '3xuBUMW9DUtzbexvoi4Z'
stream_token = 'ij7mbpznls'

py.sign_in(username, api_key)

trace1 = Scatter(
    x=[],
    y=[],
    stream=dict(
        token=stream_token,
        maxpoints=200
    )
)

layout = Layout(
    title='Raspberry Pi Streaming Sensor Data'
)

fig = Figure(data=[trace1], layout=layout)

print(py.plot(fig, filename='Raspberry Pi Streaming Example Values'))

i = 0
stream = py.Stream(stream_token)
stream.open()

#the main sensor reading loop
while True:
    sensor_data = input("input \n")
    stream.write({'x': i, 'y': int(sensor_data)})
    i += 1
    # delay between stream posts
    time.sleep(0.25)
    if sensor_data == 0:
        print('break')
        break
