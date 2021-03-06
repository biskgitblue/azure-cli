# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# pylint: disable=line-too-long
from collections import OrderedDict

from azure.cli.core.commands import cli_command
from azure.cli.core.commands.arm import cli_generic_update_command
from azure.cli.core._util import empty_on_404

from .custom import (_auth_client_factory, _graph_client_factory)


def transform_definition_list(result):
    return [OrderedDict([('Name', r['properties']['roleName']), ('Type', r['properties']['type']),
                         ('Description', r['properties']['description'])]) for r in result]


def transform_assignment_list(result):
    return [OrderedDict([('Principal', r['properties']['principalName']),
                         ('Role', r['properties']['roleDefinitionName']),
                         ('Scope', r['properties']['scope'])]) for r in result]


def get_role_definition_op(operation_name):
    return 'azure.mgmt.authorization.operations.role_definitions_operations' \
           '#RoleDefinitionsOperations.{}'.format(operation_name)


def get_role_definitions(_):
    return _auth_client_factory().role_definitions


def get_graph_client_applications(_):
    return _graph_client_factory().applications


def get_graph_client_service_principals(_):
    return _graph_client_factory().service_principals


def get_graph_client_users(_):
    return _graph_client_factory().users


def get_graph_client_groups(_):
    return _graph_client_factory().groups


cli_command(__name__, 'role definition list',
            'azure.cli.command_modules.role.custom#list_role_definitions',
            table_transformer=transform_definition_list)
cli_command(__name__, 'role definition delete',
            'azure.cli.command_modules.role.custom#delete_role_definition')
cli_command(__name__, 'role definition create',
            'azure.cli.command_modules.role.custom#create_role_definition')
cli_generic_update_command(__name__, 'role definition update',
                           get_role_definition_op('get'),
                           get_role_definition_op('create_or_update'),
                           get_role_definitions)

cli_command(__name__, 'role assignment delete',
            'azure.cli.command_modules.role.custom#delete_role_assignments')
cli_command(__name__, 'role assignment list',
            'azure.cli.command_modules.role.custom#list_role_assignments',
            table_transformer=transform_assignment_list)
cli_command(__name__, 'role assignment create',
            'azure.cli.command_modules.role.custom#create_role_assignment')

cli_command(__name__, 'ad app create', 'azure.cli.command_modules.role.custom#create_application',
            get_graph_client_applications)
cli_command(__name__, 'ad app delete', 'azure.cli.command_modules.role.custom#delete_application',
            get_graph_client_applications)
cli_command(__name__, 'ad app list', 'azure.cli.command_modules.role.custom#list_apps',
            get_graph_client_applications)
cli_command(__name__, 'ad app show', 'azure.cli.command_modules.role.custom#show_application',
            get_graph_client_applications, exception_handler=empty_on_404)
cli_command(__name__, 'ad app update', 'azure.cli.command_modules.role.custom#update_application',
            get_graph_client_applications)

cli_command(__name__, 'ad sp create',
            'azure.cli.command_modules.role.custom#create_service_principal')
cli_command(__name__, 'ad sp delete',
            'azure.cli.command_modules.role.custom#delete_service_principal',
            get_graph_client_service_principals)
cli_command(__name__, 'ad sp list', 'azure.cli.command_modules.role.custom#list_sps',
            get_graph_client_service_principals)
cli_command(__name__, 'ad sp show', 'azure.cli.command_modules.role.custom#show_service_principal',
            get_graph_client_service_principals, exception_handler=empty_on_404)

# RBAC related
cli_command(__name__, 'ad sp create-for-rbac',
            'azure.cli.command_modules.role.custom#create_service_principal_for_rbac')
cli_command(__name__, 'ad sp reset-credentials',
            'azure.cli.command_modules.role.custom#reset_service_principal_credential')

cli_command(__name__, 'ad user delete',
            'azure.graphrbac.operations.users_operations#UsersOperations.delete',
            get_graph_client_users)
cli_command(__name__, 'ad user show',
            'azure.graphrbac.operations.users_operations#UsersOperations.get',
            get_graph_client_users,
            exception_handler=empty_on_404)
cli_command(__name__, 'ad user list', 'azure.cli.command_modules.role.custom#list_users',
            get_graph_client_users)
cli_command(__name__, 'ad user create', 'azure.cli.command_modules.role.custom#create_user',
            get_graph_client_users)

cli_command(__name__, 'ad group delete',
            'azure.graphrbac.operations.groups_operations#GroupsOperations.delete',
            get_graph_client_groups)
cli_command(__name__, 'ad group show',
            'azure.graphrbac.operations.groups_operations#GroupsOperations.get',
            get_graph_client_groups,
            exception_handler=empty_on_404)
cli_command(__name__, 'ad group list', 'azure.cli.command_modules.role.custom#list_groups',
            get_graph_client_groups)
