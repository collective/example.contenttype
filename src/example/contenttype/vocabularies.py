from plone import api
from zope.interface import implementer
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
                value=brain.getObject(),
                token=brain.UID,
                title=u'{} ({})'.format(brain.Title, brain.getPath()),
            ))
        return SimpleVocabulary(terms)

DocumentVocabularyFactory = DocumentVocabulary()
