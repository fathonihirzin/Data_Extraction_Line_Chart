## DATA EXTRACTION
from datetime import datetime

import os

os.chdir('./FIX/2_Line_Chart/') #set file location
timestamp_data = []
sends_package_data = []


def data_table(txt_file):
 
  with open('soal_chart_bokeh.txt','r') as file_handle:
# Loop through each line in the file
    for line in file_handle:
        if line.startswith("Timestamp"): #get the datetime
            start = line.find("Timestamp")
            end = line.find("C")
            timestamp = line[start+11:end]
            date_format = '%Y-%m-%d %H:%M:%S'
            timestamp = datetime.strptime(timestamp, date_format)
            timestamp_data.append(timestamp)

        if line.startswith("[  5]   0.00-10.00  sec"): #get the speed
            start = line.find(" sec ")
            end = line.find("Mbytes")
            sends_package = line[start+6:end-47]
            sends_package = sends_package.lstrip()
            sends_package = float(sends_package)
            if sends_package > 250:
               sends_package = sends_package/1000            
            sends_package_data.append(sends_package)

  print("Timestamp: ", timestamp_data)
  print("Speed: ", sends_package_data)

data_table("soal_chart_bokeh.txt")

#Importing the modules
from bokeh.plotting import figure, output_file, show 
from bokeh.models import DatetimeTickFormatter, NumeralTickFormatter

#Set data to x,y
x = timestamp_data
y = sends_package_data

#Figure
p = figure(
   title = "NETWORK TESTING\n",
   x_axis_label = "Date Time",
   y_axis_label = "Speed (Mbps)"
)

#Render
p.line(x, y, color="blue", line_width=2)

#Formating
p.yaxis[0].formatter = NumeralTickFormatter(format="0.00")
p.xaxis[0].formatter = DatetimeTickFormatter(days="%m/%d/%Y\n%H:%M:%S")

#Show
show(p)