# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# coding: utf-8
# pylint: skip-file
from msrest.serialization import Model


class Event(Model):
    """Event.

    :param event_name: The event type for which this notification is enabled
     (i.e. AutoShutdown, Cost). Possible values include: 'AutoShutdown', 'Cost'
    :type event_name: str or :class:`NotificationChannelEventType
     <azure.mgmt.devtestlabs.models.NotificationChannelEventType>`
    """

    _attribute_map = {
        'event_name': {'key': 'eventName', 'type': 'str'},
    }

    def __init__(self, event_name=None):
        self.event_name = event_name
