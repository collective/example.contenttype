import six
from plone import api
from plone.uuid.interfaces import IUUID
from zope.interface import implementer
from zope.schema.interfaces import IVocabularyTokenized
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary
from plone.app.vocabularies.catalog import StaticCatalogVocabulary


@implementer(IVocabularyFactory)
class DocumentVocabulary(object):
    def __call__(self, context=None):
        return StaticCatalogVocabulary({
            'portal_type': 'Document',
            'sort_on': 'sortable_title',
        })


DocumentVocabularyFactory = DocumentVocabulary()
