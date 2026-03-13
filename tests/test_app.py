import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from dash.testing.application_runners import import_app


def test_header_present(dash_duo):
    app = import_app("app")
    dash_duo.start_server(app)

    header = dash_duo.find_element("h1")
    assert header is not None


def test_graph_present(dash_duo):
    app = import_app("app")
    dash_duo.start_server(app)

    graph = dash_duo.find_element("#sales-chart")
    assert graph is not None


def test_region_picker_present(dash_duo):
    app = import_app("app")
    dash_duo.start_server(app)

    radio = dash_duo.find_element("#region-filter")
    assert radio is not None
