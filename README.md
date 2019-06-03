# data_analyst

https://towardsdatascience.com/practical-statistics-visualization-with-python-plotly-770e96e35067?gi=53ed1b8233f1

Practical Statistics & Visualization With Python & Plotly

How to use Python and Plotly for statistical visualization, inference, and modeling

￼


May 15

One day last week, I was googling “statistics with Python”, the results were somewhat unfruitful. Most literature, tutorials and articles focus on statistics with R, because R is a language dedicated to statistics and has more statistical analysis features than Python.

In two excellent statistics books, “PracticalStatistics for Data Scientists” and “An Introduction to Statistical Learning”, the statistical concepts were all implemented in R.

Data science is a fusion of multiple disciplines, including statistics, computer science, information technology, and domain-specific fields. And we use powerful, open-source Python tools daily to manipulate, analyze, and visualize datasets.

And I would certainly recommend anyone interested in becoming a Data Scientist or Machine Learning Engineer to develop a deep understanding and practice constantly on statistical learning theories.

This prompts me to write a post for the subject. And I will use one dataset to review as many statistics concepts as I can and lets get started!

The Data

The data is the house prices data set that can be found here.



import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from plotly.offline import init_notebook_mode, iplot
import plotly.figure_factory as ff
import cufflinks
cufflinks.go_offline()
cufflinks.set_config_file(world_readable=True, theme='pearl')
import plotly.graph_objs as go
import plotly.plotly as py
import plotly
from plotly import tools
plotly.tools.set_credentials_file(username='XXX', api_key='XXX')
init_notebook_mode(connected=True)
pd.set_option('display.max_columns', 100)df = pd.read_csv('house_train.csv')
df.drop('Id', axis=1, inplace=True)
df.head()

Univariate Data Analysis

Univariate analysis is perhaps the simplest form of statistical analysis, and the key fact is that only one variable is involved.

Describing Data

Statistical summary for numeric data include things like the mean, min, and max of the data, can be useful to get a feel for how large some of the variables are and what variables may be the most important.

df.describe().T

Statistical summary for categorical or string variables will show “count”, “unique”, “top”, and “freq”.

table_cat = ff.create_table(df.describe(include=['O']).T, index=True, index_title='Categorical columns')
iplot(table_cat)

Histogram
Plot a histogram of SalePrice of all the houses in the data.
df['SalePrice'].iplot(
    kind='hist',
    bins=100,
    xTitle='price',
    linecolor='black',
    yTitle='count',
    title='Histogram of Sale Price')
    
    
    Boxplot
Plot a boxplot of SalePrice of all the houses in the data. Boxplots do not show the shape of the distribution, but they can give us a better idea about the center and spread of the distribution as well as any potential outliers that may exist. Boxplots and Histograms often complement each other and help us understand more about the data.
df['SalePrice'].iplot(kind='box', title='Box plot of SalePrice')


Histograms and Boxplots by Groups
Plotting by groups, we can see how a variable changes in response to another. For example, if there is a difference between house SalePrice with or with no central air conditioning. Or if house SalePrice varies according to the size of the garage, and so on.
Boxplot and histogram of house sale price grouped by with or with no air conditioning

trace0 = go.Box(
    y=df.loc[df['CentralAir'] == 'Y']['SalePrice'],
    name = 'With air conditioning',
    marker = dict(
        color = 'rgb(214, 12, 140)',
    )
)
trace1 = go.Box(
    y=df.loc[df['CentralAir'] == 'N']['SalePrice'],
    name = 'no air conditioning',
    marker = dict(
        color = 'rgb(0, 128, 128)',
    )
)

data = [trace0, trace1]
layout = go.Layout(
    title = "Boxplot of Sale Price by air conditioning"
)

fig = go.Figure(data=data,layout=layout)
py.iplot(fig)
