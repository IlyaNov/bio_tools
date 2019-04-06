import plotly.graph_objs as go
import plotly.offline as offline


def plot(stat_data):

    data = go.Scatter(
            x=stat_data['V_means'],
            y=stat_data['I_means'],
            name='sinc(x)',
            error_y=dict(
                type='data',
                array=stat_data['I_sem'],
                visible=True
            )
        )

    layout = go.Layout(
        xaxis=dict(
            showgrid=False,
            showticklabels=True,
            ticks='inside',
            tickwidth=2,
            ticklen=5,
            tickfont=dict(
                family='Arial',
                size=12,
                color='rgb(82, 82, 82)',
            ),
        ),
        yaxis=dict(
            showgrid=False,
            zeroline=True,
            showticklabels=True,
            ticks='inside',
            tickwidth=2,
            ticklen=5,
            tickfont=dict(
                family='Arial',
                size=12,
                color='rgb(82, 82, 82)',
            )
        ))


    fig = go.Figure([data],layout=layout)
    offline.plot(fig, 'I/V curve.png')