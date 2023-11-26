"""Testing fixtures.
"""
import pytest

import i_asana


@pytest.fixture(name='asn')
def fixture_asana_interface():
    """Pytest fixture to initialize and return the AsanaInterface object.
    """
    return i_asana.AsanaInterface()

