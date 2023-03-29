from example.contenttype.manyexamples.staff_names import employee_names
from plone import api
from Products.CMFPlone.interfaces import INonInstallable
from zope.interface import implementer


import logging
import random

logger = logging.getLogger("example.contenttype")


@implementer(INonInstallable)
class HiddenProfiles(object):
    def getNonInstallableProfiles(self):
        """Hide uninstall profile from site-creation and quickinstaller."""
        return [
            "example.contenttype:uninstall",
        ]


def post_install(context):
    """Post install script"""
    # Do something at the end of the installation of this package.


def uninstall(context):
    """Uninstall script"""
    # Do something at the end of the uninstallation of this package.


def create_many_examples(context):
    number_of_employees = 300
    logger.info("*** Create many examples.")
    portal = api.portal.get()
    staff = api.content.create(type="Document", title="Example Staff", container=portal)
    employees_folder = api.content.create(
        type="Document", title="Employees", container=staff
    )
    supervisors_folder = api.content.create(
        type="Document", title="Supervisors", container=staff
    )

    ens = employee_names["items"]

    employees = []
    supervisors = []
    for i in range(number_of_employees):
        # Employee
        title = f'Employee {ens[i]["first_name"]} {ens[i]["last_name"]}'
        employee = api.content.create(
            type="example", title=title, container=employees_folder
        )
        api.content.transition(employee, "publish")
        employees.append(employee)

        # Supervisor
        title = f'Supervisor {ens[i]["first_name_supervisor"]} {ens[i]["last_name_supervisor"]}'
        supervisor = api.content.create(
            type="example", title=title, container=supervisors_folder
        )
        api.content.transition(supervisor, "publish")
        supervisors.append(supervisor)

    for i in range(number_of_employees):
        # first relation
        rint = random.randint(0, number_of_employees - 1)
        api.relation.create(
            source=employees[i],
            target=supervisors[rint],
            relationship="relationlist_field_named_staticcatalogvocabulary",
        )
        # second relation
        rint = random.randint(0, number_of_employees - 1)
        api.relation.create(
            source=employees[i],
            target=supervisors[rint],
            relationship="relationlist_field_named_staticcatalogvocabulary",
        )

    logger.info("*** Many examples created and related.")
