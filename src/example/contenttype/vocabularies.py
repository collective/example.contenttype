from plone.app.vocabularies.catalog import StaticCatalogVocabulary
from zope.interface import provider
from zope.schema.interfaces import IVocabularyFactory


@provider(IVocabularyFactory)
def DocumentVocabularyFactory(context=None):
    return StaticCatalogVocabulary(
        {
            'portal_type': ['Document', 'News Item'],
            'sort_on': 'sortable_title',
        }
    )
