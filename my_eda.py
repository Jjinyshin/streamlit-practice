import sweetviz as sv
import pandas as pd

my_dataframe = pd.read_csv("titanic.csv")

my_report = sv.analyze(my_dataframe)
my_report.show_html()