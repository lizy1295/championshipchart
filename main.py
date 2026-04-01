import pygal
import csv
from pygal import Bar

# Create a chart
chart = Bar(title = 'Olympic medals')

# Add data to the chart
#open and read the data correctly
with open('medals.csv') as f:
  reader = csv.reader(f)
  
  for row in reader:
    chart.add(row[0], int(row[1]))  # Add data to the chart
chart.render_to_file('Medals.svg')
# Display the chart
import webbrowser
import os
webbrowser.open('file://' + os.path.abspath('Medals.svg'))