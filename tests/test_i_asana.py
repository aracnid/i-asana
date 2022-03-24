"""Test functions for i_asana.py.
"""
from aracnid_logger import Logger
import pytest

import i_asana as asn

# initialize logging
logger = Logger(__name__).get_logger()

# initialize module variables
project_id = '1201859291658493'  # BrewOps

@pytest.fixture(name='asana')
def fixture_asana_interface():
    """Pytest fixture to initialize and return the AsanaInterface object.
    """
    return asn.AsanaInterface()

def test_init_asana(asana):
    """Tests Asana initialization.
    """
    assert asana

    asana.client.options['client_name'] = 'brewbot'
    me = asana.client.users.me()

    assert me['workspaces'][0]['name'] == 'lakeannebrewhouse.com'
