"""Test functions for i-Asana import.
"""
from i_asana import __version__

def test_version():
    """Tests that i-Asana was imported successfully.
    """
    assert __version__
    assert __version__ == '1.0.0-alpha.5'
    