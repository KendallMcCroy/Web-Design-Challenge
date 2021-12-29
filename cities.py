# Python program to convert
# CSV to HTML Table

import pandas as pd

# to read csv file named "samplee"
data = pd.read_csv("Resources\cities.csv")

weather_data = data.set_index("City_ID")

# to save as html file
# named as "raw data"
weather_data.to_html("raw_data.html")

# # assign it to a
# # variable (string)
# html_file = a.to_html()
