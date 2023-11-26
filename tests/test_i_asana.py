"""Test functions for i_asana.py.
"""
from datetime import date, datetime, timedelta
from aracnid_logger import Logger

# initialize logging
logger = Logger(__name__).get_logger()

# initialize module variables
PROJECT_ID = '1202019477793832'  # TEST
SECTION_ID = '1202019477793835'


def test_init_asana(asn):
    """Tests asn initialization.
    """
    assert asn

    user_me = asn.users.get_user('me')

    assert user_me.data.workspaces[0].name == 'lakeannebrewhouse.com'

def test_create_task_no_due_date(asn):
    """Tests create_task() function.
    """
    task = asn.create_task(
        name='CREATE: no-due-date',
        project_id=PROJECT_ID
    )

    assert task

def test_create_task_due_date(asn):
    """Tests create_task() function.
    """
    start_date = date.today()
    due_date = start_date + timedelta(days=5)

    task = asn.create_task(
        name='CREATE: start-date',
        start=start_date,
        due=due_date,
        project_id=PROJECT_ID
    )

    assert task
    assert task.start_on == start_date

def test_create_task_due_datetime(asn):
    """Tests create_task() function.
    """
    due_datetime = datetime.now().replace(microsecond=0).astimezone()

    task = asn.create_task(
        name='CREATE: due-datetime',
        due=due_datetime,
        project_id=PROJECT_ID
    )

    assert task
    assert task.due_at == due_datetime

def test_create_task_start_date(asn):
    """Tests create_task() function.
    """
    due_date = date.today()

    task = asn.create_task(
        name='CREATE: due-date',
        due=due_date,
        project_id=PROJECT_ID
    )

    assert task
    assert task.due_on == due_date

def test_create_task_in_section(asn):
    """Tests create_task() function.
    """
    task = asn.create_task(
        name='CREATE: in-section',
        project_id=PROJECT_ID,
        section_id=SECTION_ID
    )

    assert task
    assert task.memberships[0].section.gid == SECTION_ID

def test_create_subtask_in_task(asn):
    """Tests create_task() function.
    """
    parent_id = '1202019477793842'
    task = asn.create_task(
        name='CREATE: subtask',
        project_id=PROJECT_ID,
        section_id=SECTION_ID,
        parent_id=parent_id
    )

    assert task
    assert task.parent.gid == parent_id

def test_read_task(asn):
    """Tests read_task() function.
    """
    task_id = '1202021989637892'
    task = asn.read_task(task_id=task_id)

    assert task
    assert task.name == 'READ: no-due-date'

def test_get_due_date(asn):
    """Tests the get_due_date() function.
    """
    task_id = '1202019477793837'
    task = asn.read_task(task_id=task_id)
    due_date = task.due_on

    assert due_date
    assert isinstance(due_date, date)

def test_get_due_datetime(asn):
    """Tests the get_due_datetime() function.
    """
    task_id = '1202019477793839'
    task = asn.read_task(task_id=task_id)
    due_datetime = task.due_at

    assert due_datetime
    assert isinstance(due_datetime, datetime)

def test_update_task(asn):
    """Tests update_task() function.
    """
    task = asn.create_task(
        name='UPDATE: created',
        project_id=PROJECT_ID
    )
    assert task.name == 'UPDATE: created'

    task_id = task.gid
    task = asn.update_task(
        task_id=task_id,
        fields={
            'name': 'UPDATE: updated'
        }
    )

    assert task.name == 'UPDATE: updated'

def test_delete_task(asn):
    """Tests delete_task() function.
    """
    task = asn.create_task(
        name='DELETE: created',
        project_id=PROJECT_ID
    )
    assert task.name == 'DELETE: created'

    task_id = task.gid
    asn.delete_task(task_id=task_id)

    task = asn.read_task(task_id=task_id)

    assert task is None
