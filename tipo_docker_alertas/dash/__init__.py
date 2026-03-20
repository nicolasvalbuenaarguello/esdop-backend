# pip install dash
# pip install dash-renderer
# pip install dash-html-components
# pip install dash-core-components
# pip install importlib-metadata
# pip install pandas
# py -m pip install plotly
# py -m pip install cufflinks
# python -m venv env_2
# python -m pip install plotly

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from dash.dependencies import Input, Output

from model.estadistica import *