from dash import Dash, html, dcc
import plotly.express as px

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

app = Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([

    html.H1("Simple HTML Only Site"),
    html.H2("Python visualizations"),
    html.Div([
        html.P("Annual fuel Cost", className="my-p-class", id="my-p-id")

    ],

        style={"color": "green", "fontSize": 16},
    ),
    dcc.Markdown("""
     ### Dash Support Markdown
     
     You can write simple text and format it with the markup like
     **bold text** and *italics*, [links](http://commonwork.org/help).
     You can also use :
     * lists
     * inline `code` snippets
     * and more
    
    """),

],
    style={
        "margin-left": "15px",
        "width": "55%",
        "backgroundColor": "lightgray",
    },
)

if __name__ == "__main__":
    app.run_server(debug=True)
