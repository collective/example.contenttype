from zope.interface import provider
from zope.schema.interfaces import IVocabularyFactory
from plone.app.vocabularies.catalog import StaticCatalogVocabulary


@provider(IVocabularyFactory)
def DocumentVocabularyFactory(context=None):
    return StaticCatalogVocabulary({
        'portal_type': 'Document',
        'sort_on': 'sortable_title',
    })
