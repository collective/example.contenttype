# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import (
    applyProfile,
    FunctionalTesting,
    IntegrationTesting,
    PloneSandboxLayer,
)
from plone.testing import z2

import example.contenttype


class ExampleContenttypeLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=example.contenttype)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'example.contenttype:default')


EXAMPLE_CONTENTTYPE_FIXTURE = ExampleContenttypeLayer()


EXAMPLE_CONTENTTYPE_INTEGRATION_TESTING = IntegrationTesting(
    bases=(EXAMPLE_CONTENTTYPE_FIXTURE,),
    name='ExampleContenttypeLayer:IntegrationTesting',
)


EXAMPLE_CONTENTTYPE_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(EXAMPLE_CONTENTTYPE_FIXTURE,),
    name='ExampleContenttypeLayer:FunctionalTesting',
)


EXAMPLE_CONTENTTYPE_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        EXAMPLE_CONTENTTYPE_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='ExampleContenttypeLayer:AcceptanceTesting',
)
