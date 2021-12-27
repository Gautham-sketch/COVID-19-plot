import pandas as pd
import plotly.express as pe

reader = pd.read_csv("COVID19data.csv")
display = pe.scatter(reader, x="date", y="cases", title="Covid 19 Cases", color="country", size="Percentage")
display.show()