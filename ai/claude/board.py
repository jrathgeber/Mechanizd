import dash
from dash import html, dcc
from dash.dependencies import Input, Output, State

app = dash.Dash(__name__)

contacts = [
    {"name": "John Doe", "email": "john@example.com"},
    {"name": "Jane Smith", "email": "jane@example.com"},
    {"name": "Bob Johnson", "email": "bob@example.com"},
]

app.layout = html.Div([
    html.H1("Contact List"),
    html.Ul([
        html.Li([
            html.Span(f"{contact['name']} - {contact['email']}"),
            html.Button("Send Email", id=f"btn-{i}", n_clicks=0, style={"marginLeft": "10px"})
        ]) for i, contact in enumerate(contacts)
    ]),
    html.Div(id="output")
])

@app.callback(
    Output("output", "children"),
    [Input(f"btn-{i}", "n_clicks") for i in range(len(contacts))],
    prevent_initial_call=True
)
def send_email(*args):
    ctx = dash.callback_context
    if not ctx.triggered:
        return dash.no_update
    button_id = ctx.triggered[0]["prop_id"].split(".")[0]
    index = int(button_id.split("-")[1])
    return f"Email sent to {contacts[index]['name']} at {contacts[index]['email']}"

if __name__ == "__main__":
    app.run_server(debug=True)