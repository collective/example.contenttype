from example.contenttype.example import IExample
from example.contenttype.testing import EXAMPLE_CONTENTTYPE_INTEGRATION_TESTING
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID

import unittest


class TestExample(unittest.TestCase):

    layer = EXAMPLE_CONTENTTYPE_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        setRoles(self.portal, TEST_USER_ID, ["Manager"])

    def test_example_creation(self):
        """Test type creation."""
        item = api.content.create(
            container=self.portal,
            type="example",
            id="example",
            title="Example",
        )
        self.assertEqual(item.portal_type, "example")
        self.assertTrue(IExample.providedBy(item))

    def test_example_render(self):
        """Test type creation."""
        item = api.content.create(
            container=self.portal,
            type="example",
            id="example",
            title="Example",
        )
        html = item()
        self.assertTrue(html)