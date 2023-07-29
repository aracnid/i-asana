"""Test functions for i_asana.py.
"""
from aracnid_logger import Logger
import pytest

import i_asana as asn

# initialize logging
logger = Logger(__name__).get_logger()

# initialize module variables
PROJECT_ID = '1201859291658493'  # BrewOps

@pytest.fixture(name='asana')
def fixture_asana_interface():
    """Pytest fixture to initialize and return the AsanaInterface object.
    """
    return asn.AsanaInterface()

def test_get_project_by_id(asana):
    """Tests project get functionality.
    """
    result = asana.client.projects.get_project(PROJECT_ID)

    assert result['gid'] == PROJECT_ID
    assert result['name'] == '[LABH] BrewOps'

def test_get_tasks_for_project(asana):
    """Tests get_tasks_for_project functionality.
    """
    tasks = asana.client.tasks.get_tasks_for_project(PROJECT_ID)
    for task in tasks:
        assert task
        logger.info(task['name'])

def test_get_section_id_from_task(asana):
    """Tests get_task functionality.
    """
    task = asana.client.tasks.get_task('1202999621605567')
    section_id = task['memberships'][0]['section']['gid']
    section_name = task['memberships'][0]['section']['name']

    assert section_id
    assert section_name == 'Fermenting'

    task = asana.client.tasks.get_task('1202998731310349')
    section_id = task['memberships'][0]['section']['gid']
    section_name = task['memberships'][0]['section']['name']

    assert section_id
    assert section_name == 'Serving'

    task = asana.client.tasks.get_task('1205092860586670')
    section_id = task['memberships'][0]['section']['gid']
    section_name = task['memberships'][0]['section']['name']

    assert section_id
    assert section_name == 'Weekly'

def test_get_task_by_name(asana):
    """Tests get task functionality by name.
    """
    workspace_id = '1108879292936985'
    result = asana.client.tasks.search_tasks_for_workspace(workspace_id,
        {
            'text': '2023-W30'
        }
    )

    assert result
