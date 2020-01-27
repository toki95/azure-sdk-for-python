# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ConnectToTargetSqlMISyncTaskInput(Model):
    """Input for the task that validates connection to Azure SQL Database Managed
    Instance online scenario.

    All required parameters must be populated in order to send to Azure.

    :param target_connection_info: Required. Connection information for Azure
     SQL Database Managed Instance
    :type target_connection_info:
     ~azure.mgmt.datamigration.models.MiSqlConnectionInfo
    :param azure_app: Required. Azure Active Directory Application the DMS
     instance will use to connect to the target instance of Azure SQL Database
     Managed Instance and the Azure Storage Account
    :type azure_app: ~azure.mgmt.datamigration.models.AzureActiveDirectoryApp
    """

    _validation = {
        'target_connection_info': {'required': True},
        'azure_app': {'required': True},
    }

    _attribute_map = {
        'target_connection_info': {'key': 'targetConnectionInfo', 'type': 'MiSqlConnectionInfo'},
        'azure_app': {'key': 'azureApp', 'type': 'AzureActiveDirectoryApp'},
    }

    def __init__(self, *, target_connection_info, azure_app, **kwargs) -> None:
        super(ConnectToTargetSqlMISyncTaskInput, self).__init__(**kwargs)
        self.target_connection_info = target_connection_info
        self.azure_app = azure_app