import six
from plone import api
from plone.uuid.interfaces import IUUID
from zope.interface import implementer
from zope.schema.interfaces import IVocabularyTokenized
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary


@implementer(IVocabularyFactory)
class DocumentVocabulary(object):
    def __call__(self, context=None):
        terms = []
        # Use getObject since the DataConverter expects a real object.
        for brain in api.content.find(portal_type='Document', sort_on='sortable_title'):
            terms.append(SimpleTerm(
                value=brain.UID,
                token=brain.UID,
                title=u'{} ({})'.format(brain.Title, brain.getPath()),
            ))
        return SimpleVocabulary(terms)

DocumentVocabularyFactory = DocumentVocabulary()


@implementer(IVocabularyTokenized)
class AJAXContentQueryVocabulary(object):
    """Simple Catalog vocabulary for use with AJAX Select field."""
    text_search_index = 'SearchableText'

    def __init__(self, context=None, **query):
        self.query = query
        self.context = context

    def __contains__(self, value):
        """used during validation to make sure the selected item is found with
        the specified query. Checks UUID values.
        """
        if not isinstance(value, six.string_types):
            # here we have a content and fetch the uuid as hex value
            value = IUUID(value)
        query = {'UID': value}
        catalog = api.portal.get_tool('portal_catalog')
        return bool(catalog.unrestrictedSearchResults(**query))

    def getTerm(self, value):
        if not isinstance(value, six.string_types):
            # here we have a content and fetch the uuid as hex value
            value = IUUID(value)
        query = {'UID': value}
        catalog = api.portal.get_tool('portal_catalog')
        brains = catalog.searchResults(**query)
        for b in brains:
            return SimpleTerm(
                title=u'{} ({})'.format(b.Title, b.getPath()),
                token=b.UID,
                value=b.UID,
            )

    getTermByToken = getTerm

    def search(self, query):
        """Required by plone.app.content.browser.vocabulary for simple queryable
        vocabs"""
        if not query.endswith(' '):
            query += '*'
        query = {self.text_search_index: query}
        query.update(self.query)
        catalog = api.portal.get_tool('portal_catalog')
        brains = catalog.searchResults(**query)
        return SimpleVocabulary([
            SimpleTerm(
                title=u'{} ({})'.format(b.Title, b.getPath()),
                token=b.UID,
                value=b.UID,
            ) for b in brains
        ])
