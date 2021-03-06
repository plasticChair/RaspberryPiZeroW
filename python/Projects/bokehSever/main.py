from bokeh.server.server import Server
from bokeh.application import Application
from bokeh.application.handlers.function import FunctionHandler
from bokeh.plotting import figure, ColumnDataSource

from bokeh.plotting import figure, output_file, show

import pandas as pd
from bokeh.plotting import Figure
from bokeh.models import ColumnDataSource, TextInput, Button, Panel, Tabs, Label, DataTable, TableColumn
from bokeh.layouts import Row, Column, widgetbox
from bokeh.io import curdoc, show, output_notebook
from sqlalchemy import create_engine


from random import random

from bokeh.layouts import column
from bokeh.models import Button
from bokeh.palettes import RdYlBu3
from bokeh.plotting import figure, curdoc






output_file("test.html")

def make_document(doc):
    fig = figure(title='Line plot!', sizing_mode='scale_width')
    fig.line(x=[1, 2, 3], y=[1, 4, 9])

    doc.title = "Hello, world!"
    doc.add_root(fig)

apps = {'/': Application(FunctionHandler(make_document))}





# create a plot and style its properties
p = figure(x_range=(0, 100), y_range=(0, 100), toolbar_location=None)
p.border_fill_color = 'black'
p.background_fill_color = 'black'
p.outline_line_color = None
p.grid.grid_line_color = None

# add a text renderer to our plot (no data yet)
r = p.text(x=[], y=[], text=[], text_color=[], text_font_size="20pt",
           text_baseline="middle", text_align="center")

i = 0

ds = r.data_source

# create a callback that will add a number in a random location
def callback():
    global i

    # BEST PRACTICE --- update .data in one step with a new dict
    new_data = dict()
    new_data['x'] = ds.data['x'] + [random()*70 + 15]
    new_data['y'] = ds.data['y'] + [random()*70 + 15]
    new_data['text_color'] = ds.data['text_color'] + [RdYlBu3[i%3]]
    new_data['text'] = ds.data['text'] + [str(i)]
    ds.data = new_data

    i = i + 1

# add a button widget and configure with the call back
button = Button(label="Press Me")
button.on_click(callback)

# put the button and plot in a layout and add to the document
curdoc().add_root(column(button, p))


server = Server(apps, port=5000)
server.start()


while True:
    None
