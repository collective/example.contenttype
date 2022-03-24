# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from example.contenttype.testing import EXAMPLE_CONTENTTYPE_INTEGRATION_TESTING
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from Products.CMFPlone.utils import get_installer

import unittest


class TestSetup(unittest.TestCase):
    """Test that example.contenttype is properly installed."""

    layer = EXAMPLE_CONTENTTYPE_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]
        self.installer = get_installer(self.portal, self.layer["request"])

    def test_product_installed(self):
        """Test if example.contenttype is installed."""
        self.assertTrue(self.installer.is_product_installed("example.contenttype"))

    def test_browserlayer(self):
        """Test that IExampleContenttypeLayer is registered."""
        from example.contenttype.interfaces import IExampleContenttypeLayer
        from plone.browserlayer import utils

        self.assertIn(IExampleContenttypeLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = EXAMPLE_CONTENTTYPE_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        self.installer = get_installer(self.portal, self.layer["request"])
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ["Manager"])
        self.installer.uninstall_product("example.contenttype")
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if example.contenttype is cleanly uninstalled."""
        self.assertFalse(self.installer.is_product_installed("example.contenttype"))

    def test_browserlayer_removed(self):
        """Test that IExampleContenttypeLayer is removed."""
        from example.contenttype.interfaces import IExampleContenttypeLayer
        from plone.browserlayer import utils

        self.assertNotIn(IExampleContenttypeLayer, utils.registered_layers())
