"""Test functions for webhooks.
"""
from aracnid_logger import Logger


# initialize logging
logger = Logger(__name__).get_logger()

# initialize module variables
PROJECT_ID = '1202019477793832'  # TEST
SECTION_ID = '1202019477793835'
BASE_URL = 'https://z11rzncz-5000.use.devtunnels.ms/'

# def test_create_webhook(asn):
#     """Tests creating a webhook.
#     """
#     url = f'{BASE_URL}asana/webhook'

#     webhook = asn.create_webhook(
#         resource=PROJECT_ID,
#         url=url
#     )

#     assert webhook

def test_read_users(asn):
    """Tests reading multiple users.
    """
    user_list = asn.read_users()

    assert user_list
    assert len(user_list) > 0

def test_read_user(asn):
    """Tests reading a single user.
    """
    user_id = '1110399299365173'

    user = asn.read_user(user_id)

    assert user

def test_read_user_none(asn):
    """Tests reading a single user for an ID that doesn't exist.
    """
    user_id = '1111111111111111'

    user = asn.read_user(user_id)

    assert not user


# def test_delete_webhook(asn):
#     """Tests deleting a webhook.
#     """
#     # get a list of webhooks
#     webhook_list = asn.read_webhooks(resource_id=PROJECT_ID)
#     if len(webhook_list) == 0:
#         # create webhook if one doesn't already exist
#         webhook = asn.create_webhook(
#             resource=PROJECT_ID,
#             url=f'{BASE_URL}asana/webhook'
#         )
#         webhook_list = asn.read_webhooks(resource_id=PROJECT_ID)

#     # delete a webhook
#     webhook_id = webhook_list[0].gid
#     asn.delete_webhook(webhook_id)

#     # verify webhook was deleted
#     webhook = asn.read_webhook(webhook_id)
#     assert webhook is None

# def test_delete_webhooks(asn):
#     """Tests deleting all webhooks for a given resource.
#     """
#     # get a list of webhooks
#     webhook_list = asn.read_webhooks(resource_id=PROJECT_ID)
#     if len(webhook_list) == 0:
#         # create webhook if one doesn't already exist
#         asn.create_webhook(
#             resource=PROJECT_ID,
#             url=f'{BASE_URL}asana/webhook'
#         )
#         webhook_list = asn.read_webhooks(resource_id=PROJECT_ID)

#     # delete webhooks
#     asn.delete_webhooks(resource_id=PROJECT_ID)

#     # verify webhook was deleted
#     webhook_list = asn.read_webhooks(resource_id=PROJECT_ID)
#     assert len(webhook_list) == 0
