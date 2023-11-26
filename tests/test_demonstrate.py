"""Test functions for demonstration purposes.
"""
from aracnid_logger import Logger

import asana

# initialize logging
logger = Logger(__name__).get_logger()

# initialize module variables
PROJECT_ID = '1201859291658493'  # BrewOps


def test_get_project_by_id(asn):
    """Tests project get functionality.
    """
    result = asn.projects.get_project(PROJECT_ID)

    assert result.data.gid == PROJECT_ID
    assert result.data.name == '[LABH] BrewOps'

def test_get_tasks_for_project(asn):
    """Tests get_tasks_for_project functionality.
    """
    tasks = asn.tasks.get_tasks_for_project(PROJECT_ID, limit=10)
    for task in tasks.data:
        assert task
        logger.info(task.name)

def test_get_section_id_from_task(asn):
    """Tests get_task functionality.
    """
    task = asn.read_task('1202999621605567')
    assert task.memberships[0].section.gid
    assert task.memberships[0].section.name == 'Fermenting'

    task = asn.read_task('1202998731310349')
    assert task.memberships[0].section.gid
    assert task.memberships[0].section.name == 'Serving'

    task = asn.read_task('1205092860586670')
    assert task.memberships[0].section.gid
    assert task.memberships[0].section.name == 'Weekly'

def test_get_task_by_name(asn):
    """Tests get task functionality by name.
    """
    workspace_id = '1108879292936985'
    result = asn.tasks.search_tasks_for_workspace(
        workspace_id,
        text='2023-W30'
    )

    assert result
    assert isinstance(result, asana.models.task_response_array.TaskResponseArray)
