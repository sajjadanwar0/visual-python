### Plotly / Dash
- First release in 2017
- Javsacript

Dash is a framework for building interactive analytic applications and
dashboards using plotly. Uses Flask and React to build easy visualizations.

- Leverage Pandas DataFrames and plotly visualizations
- Very customizable with custom HTML and CSS
- Open source (MIT license) is full featured and maintained
- Supported by a company and includes a Enterprise-level paid tier with
enhanced capabilities.


#### Why do need additional tools ?
Many of the tools that we have reviewed allow some level of interactivity.

However, we need additional tooling if we:

- We want to link multiple plots togather
- We would like to customize how users interactively explore the data
- We need to fine-grained control of the HTML + CSS presentation
- We need to allow user to upload or download the data

Dash include may advanced concepts that are powerful but take time to learn

- Knowledge of HTML and CSS is helpful


#### Getting Started
- python -m pip install dash
- python -m pip install jupyter-dash

- Runs as python app.py
- Also run from within the notebook
- Behind the scenes uses the flask to serve up the app



### Dash Components
### Layout ---Controls application appearance

###### HTML/CSS
from dash import html
- html.Div
- html.H1|H2|H3

full list https://dash.plotly.com/dash-html-components


###### Core Components
Graph placements & Interactive Widgets

from dash import dcc

- dcc.Dropdown|Slider|ChecList, etc
- dcc.Graph
  

Full list https://dash.plotly.com/dash-core-components


###### Callbacks:
Python functions that are automatically called to update page

Python/Pandas code
from dash import Input, Output

- @app.callback()
- Define Output() and Input()
- Filter Data
- Create plotly graph




### Callbacks: Interactivity 




#### Advanced Topics
* Upload and download files
* Maintaining state
* Caching
* Chaining callbacks
* Specialized plots types for bioinformatics,geography
* Using bootstrap components
* Deploying Flask-based app
* Enterprise deployment(commercial product)


#### Pros:
* Uses plotly express plots
* Support many widgets types
* Many options for customizations
* Open source & Commercials offerings


#### Cons:
* Can be verbose for simple apps
* Deployment for multi user is complex



#### Recommendations:
* Maybe overkill for simple exploratory analysis
* Will reward the user that spends time learning all the components
* Commercial offerings maybe needed for enterprise level deployment
