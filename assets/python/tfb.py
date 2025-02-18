"""A collection of functions used across multiple notebooks.

Functions:

    save_fig_html(fig, str, str) -> None
"""
from bs4 import BeautifulSoup
import plotly.graph_objects as go
import numpy as np
from scipy import optimize

# plotly figure template
FIG_TEMPLATE = dict(
    layout=go.Layout(
        template='plotly_white',
        autosize=False,
        margin=dict(l=60, r=25, b=55, t=20, pad=4),
        font=dict(
            family='sans-serif',
            size=14
        ),
        hovermode='closest',
        xaxis=dict(
            automargin=False,
            showline=True,
            linecolor='#444',
            linewidth=2,
            mirror=True,
            tickmode='linear', ticks='outside',
            minor=dict(tickmode='linear', ticks='outside'),
            zeroline=False,
        ),
        yaxis=dict(
            automargin=True,
            showline=True,
            linecolor='#444',
            linewidth=2,
            mirror=True,
            ticks='outside',
            minor=dict(tickmode='linear', ticks='outside'),
            zeroline=False,
        ),
        hoverlabel=dict(align='left'),
    )
)

# plotly figure config
FIG_CONFIG = {
    'responsive': True, # must be True to auto-scale when resizing
    'autosizable': True, # doesn't impact auto rescaling
    'showAxisDragHandles': False,
    'displaylogo': False,
    'displayModeBar': 'hover',
    'doubleClick': 'reset',
    'modeBarButtonsToRemove': [
        'select2d',
        'lasso2d',
        'zoom2d',
        'zoomIn2d',
        'zoomOut2d',
        'pan2d',
        'autoScale2d',
        'hoverClosestCartesian',
        'hoverCompareCartesian',
        'toggleSpikelines',
        'resetScale2d',
    ],
    'toImageButtonOptions': {
        'format': 'png', # one of png, svg, jpeg, webp
        'filename': 'tfb-plot',
        'height': 450,
        'width': 600,
        'scale': 2
    },
}

# function for saving figures to HTML
def save_fig_html(fig, format, name, **kwargs):
    """Saves Plotly figure to HTML and applies TFB_CONFIG.

    Args:
        fig: A Plotly figure.
        format: A str indicating figure size. Either 'large' or 'small'.
        name: The output file name as a str. '.html' will be appended if not there.
        kwargs: Used to set Plotly figure parameters.

    Example:
        save_fig_html(fig, format='small', name=f'./fig-name-small', 
            style='aspect-ratio:600/600;', legend_font_size=8)
    """
    file_name = f'./{name}.html'

    if kwargs.get('update_figure', True):
        match format:
            case 'large':
                if len([d for d in fig.data if type(d) in [go.Trace, go.Scatter]]) > 0:
                    fig.update_traces(
                        line_width=kwargs.get('line_width', 2), 
                        marker_size=kwargs.get('marker_size', 8),
                        selector=kwargs.get('selector', None),
                    )
                fig.update_shapes(
                    line_width=kwargs.get('line_width', 2)
                )
                fig.update_layout(
                    font_size=kwargs.get('font_size', 14)
                )
                fig.update_annotations(
                    font_size=kwargs.get('font_size', 14)
                )
            case 'small':
                if len([d for d in fig.data if type(d) in [go.Trace, go.Scatter]]) > 0:
                    fig.update_traces(
                        line_width=kwargs.get('line_width', 1), 
                        marker_size=kwargs.get('marker_size', 6),
                        selector=kwargs.get('selector', None),
                    )
                fig.update_shapes(
                    line_width=kwargs.get('line_width', 1)
                )
                fig.update_layout(
                    font_size=kwargs.get('font_size', 10), 
                    legend_font_size=kwargs.get('legend_font_size', 10)
                )
                fig.update_annotations(
                    font_size=kwargs.get('font_size', 10)
                )

    fig_html = fig.to_html(
        config=kwargs.get('config', FIG_CONFIG),
        include_plotlyjs=False, 
        full_html=False, 
    )
    fig_soup = BeautifulSoup(fig_html, 'html.parser')
    fig_soup.div['class'] = f'plotly-div-{format}'
    if kwargs.get('style', None):
        fig_soup.div['style'] = kwargs.get('style')
    with open(file_name, 'wb') as fout:
        fout.write(fig_soup.prettify('utf-8'))


def plot_data_and_fit(fig, x, y, **kwargs):
    print_coefficients = kwargs.pop('print_coefficients', False)
    
    # plot data
    fig.add_trace(go.Scatter(
        x=x, y=y,
        mode='markers', 
        **kwargs,
    ))

    # calculate fit coefficients
    coefs = np.polyfit(x, y, 1)
    poly = np.poly1d(coefs)
    if print_coefficients: 
        print(f'CR >= 1: {coefs[1]:.2f} + {coefs[0]:.2f}*CR')
    
    # plot fit
    kwargs['hoverinfo'] = 'skip'
    kwargs['showlegend'] = False
    if kwargs.get('line', None):
        kwargs['line']['dash'] = 'solid'
    fig.add_trace(go.Scatter(
        x=x, y=poly(x),
        mode='lines', 
        **kwargs,
    ))
    
    return fig


def piecewise_linear(x, x0, y0, k1, k2):
    #return np.piecewise(x, [x < x0], [lambda x:k1*x + y0-k1*x0, lambda x:k2*x + y0-k2*x0])
    return np.piecewise(x, [x < 20], [lambda x:k1*x + y0-k1*20, lambda x:k2*x + y0-k2*20])

def plot_data_and_fit_piecewise(fig, x, y, **kwargs):
    row = kwargs.pop('row') if 'row' in kwargs else 1
    col = kwargs.pop('col') if 'col' in kwargs else 1
    
    # plot data
    fig.add_trace(go.Scatter(
        x=x, y=y,
        mode='markers', 
        **kwargs,
    ), row=row, col=col)

    # plot fit
    kwargs['hoverinfo'] = 'skip'
    kwargs['showlegend'] = False
    kwargs['line_dash'] = 'solid'
    p, e = optimize.curve_fit(piecewise_linear, x, y)
    xr = np.linspace(1,30,30)
    fig.add_trace(go.Scatter(
        x=xr, 
        y=piecewise_linear(xr, *p),
        mode='lines', 
        **kwargs,
    ), row=row, col=col)
    return fig, piecewise_linear(xr, *p)