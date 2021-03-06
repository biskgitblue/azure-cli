# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# coding: utf-8
# pylint: skip-file
from msrest.serialization import Model


class SubscriptionNotificationProperties(Model):
    """SubscriptionNotificationProperties.

    :param tenant_id:
    :type tenant_id: str
    """

    _attribute_map = {
        'tenant_id': {'key': 'tenantId', 'type': 'str'},
    }

    def __init__(self, tenant_id=None):
        self.tenant_id = tenant_id
