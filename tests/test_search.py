"""Test functions for i_asana.py.
"""
from aracnid_logger import Logger
import pytest

import i_asana

# initialize logging
logger = Logger(__name__).get_logger()

# initialize module variables
PROJECT_ID = '1202019477793832'  # TEST
SECTION_ID = '1202019477793835'

@pytest.fixture(name='asn')
def fixture_asana_interface():
    """Pytest fixture to initialize and return the AsanaInterface object.
    """
    return i_asana.AsanaInterface()

def test_read_subtasks(asn):
    """Tests read_subtasks() function.
    """
    task_id = '1202019477793844'
    task_list = asn.read_subtasks(task_id=task_id)

    assert task_list
    assert task_list[0].name == 'READ: subtask-1'

def test_read_subtask_by_name(asn):
    """Tests read_subtask_by_name() function.
    """
    task_id = '1202019477793844'
    task = asn.read_subtask_by_name(
        task_id=task_id,
        name='READ: subtask-2'
    )

    assert task
    assert task.gid == '1202019477793847'

def test_read_subtask_by_name_regex(asn):
    """Tests read_subtask_by_name() function with regex argument.
    """
    task_id = '1202019477793844'
    task = asn.read_subtask_by_name(
        task_id=task_id,
        name='^READ by regex',
        regex=True
    )

    assert task
    assert task.gid == '1205419546504122'
