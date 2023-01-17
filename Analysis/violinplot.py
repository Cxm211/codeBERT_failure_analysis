import plotly.graph_objects as go

import pandas as pd

df = pd.read_csv("pythonsensitivity.csv")

fig = go.Figure()

days = ['M=0,H=0', 'M=1,H=1', 'M=0,H=1', 'M=1,H=0']

for day in days:
    fig.add_trace(go.Violin(x=df['human_machine_clone_label_category'][df['human_machine_clone_label_category'] == day],
                            y=df['mutation_sensitivity'][df['human_machine_clone_label_category'] == day],
                            name=day,
                            box_visible=True,
                            meanline_visible=True,
                            points="all",))
fig.update_layout(
    font=dict(
        family="Courier New, monospace",
        size=28,  # Set the font size here
        color="Black"
    )
)
fig.show()

df = pd.read_csv("java_sensitivity.csv")

fig = go.Figure()

days = ['M=0,H=0', 'M=1,H=1', 'M=0,H=1', 'M=1,H=0']

for day in days:
    fig.add_trace(go.Violin(x=df['human_machine_clone_label_category'][df['human_machine_clone_label_category'] == day],
                            y=df['mutation_sensitivity'][df['human_machine_clone_label_category'] == day],
                            name=day,
                            box_visible=True,
                            meanline_visible=True,
                            points="all",))
fig.update_layout(
    font=dict(
        family="Courier New, monospace",
        size=28,  # Set the font size here
        color="Black"
    )
)
fig.show()