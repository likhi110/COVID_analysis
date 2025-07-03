import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
data = pd.read_csv("transformed_data.csv")
data2 = pd.read_csv("raw_data.csv")
print(data)
print(data.head())
print(data2.head())