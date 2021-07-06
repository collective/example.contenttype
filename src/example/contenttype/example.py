# -*- coding: utf-8 -*-
# from collective.z3cform.datagridfield import DataGridFieldFactory
# from collective.z3cform.datagridfield import DictRow
# from plone.app.multilingual.browser.interfaces import make_relation_root_path
from plone.app.textfield import RichText
from plone.app.z3cform.widget import AjaxSelectFieldWidget
from plone.app.z3cform.widget import RelatedItemsFieldWidget
from plone.app.z3cform.widget import SelectFieldWidget
from plone.autoform import directives
from plone.dexterity.content import Container
from plone.namedfile.field import NamedBlobFile
from plone.namedfile.field import NamedBlobImage
from plone.schema import Email
from plone.schema import Dict  # take Dict field from plone.schema to use the widget attribute
from plone.supermodel import model
from plone.supermodel.directives import fieldset
from plone.supermodel.directives import primary
from z3c.form.browser.checkbox import CheckBoxFieldWidget
from z3c.form.browser.radio import RadioFieldWidget
from z3c.relationfield.schema import RelationChoice
from z3c.relationfield.schema import RelationList
from zope import schema
from zope.interface import implementer
# from zope.interface import Interface


# class IMyRowSchema(Interface):

#     choice_field = schema.Choice(
#         title=u'Choice Field',
#         vocabulary='plone.app.vocabularies.PortalTypes',
#         required=False,
#         )
#     directives.widget('objective', SelectFieldWidget)

#     textline_field = schema.TextLine(
#         title=u'Textline field',
#         required=False,
#         )

#     bool_field = schema.Bool(
#         title=u'Boolean field',
#         required=False,
#     )


class IExample(model.Schema):
    """Dexterity-Schema with all field-types."""

    # The most used fields
    # textline, text, bool, richtext, email

    # fieldset(
    #     'numberfields',
    #     label=u'Number fields',
    #     fields=('int_field', 'float_field'),
    # )

    # fieldset(
    #     'datetimefields',
    #     label=u'Date and time fields',
    #     fields=(
    #         'datetime_field',
    #         'date_field',
    #         # 'time_field',
    #         # 'timedelta_field',
    #     ),
    # )

    # fieldset(
    #     'choicefields',
    #     label=u'Choice and Multiple Choice fields',
    #     fields=(
    #         'choice_field',
    #         'choice_field_radio',
    #         'choice_field_select',
    #         'choice_field_voc',
    #         'list_field',
    #         'list_field_checkbox',
    #         'list_field_select',
    #         'list_field_voc_unconstrained',
    #         'tuple_field',
    #         'set_field',
    #         'set_field_checkbox',
    #     ),
    # )

    # fieldset(
    #     'relationfields',
    #     label=u'Relation fields',
    #     fields=('relationchoice_field', 'relationlist_field'),
    # )

    # fieldset(
    #     'filefields',
    #     label=u'File fields',
    #     fields=('file_field', 'image_field'),
    # )

    fieldset(
        'otherfields',
        label=u'Other fields',
        fields=(
            # 'uri_field',
            # 'sourcetext_field',
            # 'ascii_field',
            # 'bytesline_field',
            # 'asciiline_field',
            # 'pythonidentifier_field',
            # 'dottedname_field',
            # 'dict_field',
            'vocabularyterms_field',
            'vocabularytermstranslation_field',
            # 'dict_field_with_choice',
        ),
    )

    # fieldset(
    #     'datagrid',
    #     label=u'Datagrid field',
    #     fields=(
    #         'datagrid_field',
    #         ),
    # )

    primary('title')
    title = schema.TextLine(
        title=u'Primary Field (Textline)',
        description=u"zope.schema.TextLine",
        required=True,
        )

    description = schema.TextLine(
        title=u'Description (Textline)',
        description=u"zope.schema.TextLine",
        required=False,
        )

    text_field = schema.Text(
        title=u'Text Field',
        description=u"zope.schema.Text",
        required=False,
        missing_value=u'',
    )

    textline_field = schema.TextLine(
        title=u'Textline field',
        description=u'A simple input field (schema.TextLine)',
        required=False,
        )

    bool_field = schema.Bool(
        title=u'Boolean field',
        description=u"zope.schema.Bool",
        required=False,
    )

    choice_field = schema.Choice(
        title=u'Choice field',
        description=u"zope.schema.Choice",
        values=[u'One', u'Two', u'Three'],
        required=True,
        )

    # directives.widget(choice_field_radio=RadioFieldWidget)
    # choice_field_radio = schema.Choice(
    #     title=u'Choice field with radio boxes',
    #     description=u"zope.schema.Choice",
    #     values=[u'One', u'Two', u'Three'],
    #     required=False,
    #     )

    # choice_field_voc = schema.Choice(
    #     title=u'Choicefield with values from named vocabulary',
    #     description=u"zope.schema.Choice",
    #     vocabulary='plone.app.vocabularies.PortalTypes',
    #     required=False,
    #     )

    # directives.widget(choice_field_select=SelectFieldWidget)
    # choice_field_select = schema.Choice(
    #     title=u'Choicefield with select2 widget',
    #     description=u"zope.schema.Choice",
    #     vocabulary='plone.app.vocabularies.PortalTypes',
    #     required=False,
    #     )

    # list_field = schema.List(
    #     title=u'List field',
    #     description=u"zope.schema.List",
    #     value_type=schema.Choice(
    #         values=[u'Beginner', u'Advanced', u'Professional'],
    #         ),
    #     required=False,
    #     missing_value=[],
    #     )

    # directives.widget(list_field_checkbox=CheckBoxFieldWidget)
    # list_field_checkbox = schema.List(
    #     title=u'List field with checkboxes',
    #     description=u"zope.schema.List",
    #     value_type=schema.Choice(
    #         values=[u'Beginner', u'Advanced', u'Professional'],
    #         ),
    #     required=False,
    #     missing_value=[],
    #     )

    # directives.widget(list_field_select=SelectFieldWidget)
    # list_field_select = schema.List(
    #     title=u'List field with select widget',
    #     description=u"zope.schema.List",
    #     value_type=schema.Choice(
    #         values=[u'Beginner', u'Advanced', u'Professional'],
    #         ),
    #     required=False,
    #     missing_value=[],
    #     )

    # list_field_voc_unconstrained = schema.List(
    #     title=u'List field with values from vocabulary but not constrained to them.',
    #     description=u"zope.schema.List",
    #     value_type=schema.TextLine(),
    #     required=False,
    #     missing_value=[],
    #     )
    # directives.widget(
    #     'list_field_voc_unconstrained',
    #     AjaxSelectFieldWidget,
    #     vocabulary='plone.app.vocabularies.PortalTypes'
    # )

    # tuple_field = schema.Tuple(
    #     title=u'Tuple field',
    #     description=u"zope.schema.Tuple",
    #     value_type=schema.Choice(
    #         values=[u'Beginner', u'Advanced', u'Professional'],
    #         ),
    #     required=False,
    #     missing_value=(),
    #     )

    # set_field = schema.Set(
    #     title=u'Set field',
    #     description=u"zope.schema.Set",
    #     value_type=schema.Choice(
    #         values=[u'Beginner', u'Advanced', u'Professional'],
    #         ),
    #     required=False,
    #     missing_value={},
    #     )

    # directives.widget(set_field_checkbox=CheckBoxFieldWidget)
    # set_field_checkbox = schema.Set(
    #     title=u'Set field with checkboxes',
    #     description=u"zope.schema.Set",
    #     value_type=schema.Choice(
    #         values=[u'Beginner', u'Advanced', u'Professional'],
    #         ),
    #     required=False,
    #     missing_value={},
    #     )

    # # File fields
    # image_field = NamedBlobImage(
    #     title=u'Image field',
    #     description=u'A upload field for images (plone.namedfile.field.NamedBlobImage)',
    #     required=False,
    #     )

    # file_field = NamedBlobFile(
    #     title=u'File field',
    #     description=u'A upload field for files (plone.namedfile.field.NamedBlobFile)',
    #     required=False,
    #     )

    # # Date and Time fields
    # datetime_field = schema.Datetime(
    #     title=u'Datetime field',
    #     description=u'Uses a date and time picker (zope.schema.Datetime)',
    #     required=False,
    # )

    # date_field = schema.Date(
    #     title=u'Date field',
    #     description=u'Uses a date picker (zope.schema.Date)',
    #     required=False,
    # )

    # # time_field = schema.Time(
    # #     title=u'Time field',
    # #     description=u'zope.schema.Time',
    # #     required=False,
    # #     )

    # # timedelta_field = schema.Timedelta(
    # #     title=u'Timedelta field',
    # #     description=u'zope.schema.Timedelta',
    # #     required=False,
    # #     )

    # # Relation Fields
    # relationchoice_field = RelationChoice(
    #     title=u"Relationchoice field",
    #     description=u'z3c.relationfield.schema.RelationChoice',
    #     vocabulary='plone.app.vocabularies.Catalog',
    #     required=False,
    # )
    # directives.widget(
    #     "relationchoice_field",
    #     RelatedItemsFieldWidget,
    #     pattern_options={
    #         "selectableTypes": ["Document"],
    #         # "basePath": make_relation_root_path,
    #     },
    # )

    # relationlist_field = RelationList(
    #     title=u"Relationlist Field",
    #     description=u'z3c.relationfield.schema.RelationList',
    #     default=[],
    #     value_type=RelationChoice(vocabulary='plone.app.vocabularies.Catalog'),
    #     required=False,
    #     missing_value=[],
    # )
    # directives.widget(
    #     "relationlist_field",
    #     RelatedItemsFieldWidget,
    #     vocabulary='plone.app.vocabularies.Catalog',
    #     pattern_options={
    #         "selectableTypes": ["Document", "Folder"],
    #         # "basePath": make_relation_root_path,
    #     },
    # )

    # # Number fields
    # int_field = schema.Int(
    #     title=u"Integer Field (e.g. 12)",
    #     description=u"zope.schema.Int",
    #     required=False,
    # )

    # float_field = schema.Float(
    #     title=u"Float fiel, e.g. 12.",
    #     description=u"zope.schema.Float",
    #     required=False,
    # )

    # Text fields
    email_field = Email(
        title=u'Email field',
        description=u'A simple input field for a email (plone.schema.email.Email)',
        required=False,
    )

    # uri_field = schema.URI(
    #     title=u'URI field',
    #     description=u'A simple input field for a URLs (zope.schema.URI)',
    #     required=False,
    #     )

    # richtext_field = RichText(
    #     title=u'RichText field',
    #     description=u'This uses a richtext editor. (plone.app.textfield.RichText)',
    #     max_length=2000,
    #     required=False,
    #     )

    # sourcetext_field = schema.SourceText(
    #     title=u'SourceText field',
    #     description=u"zope.schema.SourceText",
    #     required=False,
    #     )

    # ascii_field = schema.ASCII(
    #     title=u'ASCII field',
    #     description=u"zope.schema.ASCII",
    #     required=False,
    #     )

    # bytesline_field = schema.BytesLine(
    #     title=u'BytesLine field',
    #     description=u"zope.schema.BytesLine",
    #     required=False,
    #     )

    # asciiline_field = schema.ASCIILine(
    #     title=u'ASCIILine field',
    #     description=u"zope.schema.ASCIILine",
    #     required=False,
    #     )

    # pythonidentifier_field = schema.PythonIdentifier(
    #     title=u'PythonIdentifier field',
    #     description=u"zope.schema.PythonIdentifier",
    #     required=False,
    #     )

    # dottedname_field = schema.DottedName(
    #     title=u'DottedName field',
    #     description=u"zope.schema.DottedName",
    #     required=False,
    #     )

    # dict_field = schema.Dict(
    #     title=u'Dict field',
    #     description=u"zope.schema.Dict",
    #     required=False,
    #     key_type=schema.TextLine(
    #         title=u'Key',
    #         required=False,
    #     ),
    #     value_type=schema.TextLine(
    #         title=u'Value',
    #         required=False,
    #     ),
    # )

    vocabularyterms_field = Dict(  # we use the plone.schema field Dict not zope.schema field to use the attribute 'widget'
        title=u'Vocabulary terms field',
        description=u"plone.schema.Dict field with value_type schema.TextLine and frontend widget 'VocabularyTermsWidget'",
        required=False,
        key_type=schema.TextLine(
            title=u'Key',
            required=False,
        ),
        value_type=schema.TextLine(
            title=u'Value',
            required=False,
        ),
        widget='vocabularyterms',  # we use the widget attribute to apply the frontend widget VocabularyWidget
    )

    vocabularytermstranslation_field = Dict(  # we use the plone.schema field Dict not zope.schema field to use the attribute 'widget'
        title=u'Vocabulary terms field with translations',
        description=u"plone.schema.Dict field with value_type Dict and frontend widget 'VocabularyTermsWidget'",
        required=False,
        key_type=schema.TextLine(
            title=u'Key',
            required=False,
        ),
        value_type=Dict(  # we use the plone.schema field Dict not zope.schema field to use the attribute 'widget'
            title=u'Term translation',
            description=u"plone.schema.Dict field for translations of vocabulary term",
            required=True,
            key_type=schema.TextLine(
                title=u'Key',
                required=False,
            ),
            value_type=schema.TextLine(
                title=u'Value',
                required=False,
            ),
        ),
        widget='vocabularyterms',  # we use the widget attribute to apply the frontend widget VocabularyWidget
    )

    # dict_field_with_choice = schema.Dict(
    #     title=u'Dict field with key and value as choice',
    #     description=u"zope.schema.Dict",
    #     required=False,
    #     key_type=schema.Choice(
    #         title=u'Key',
    #         values=[u'One', u'Two', u'Three'],
    #         required=False,
    #         ),
    #     value_type=schema.Set(
    #         title=u'Value',
    #         value_type=schema.Choice(
    #             values=[u'Beginner', u'Advanced', u'Professional'],
    #             ),
    #         required=False,
    #         missing_value={},
    #         ),
    #     )

    # datagrid_field = schema.List(
    #     title=u'Datagrid field',
    #     description=u"schema.List",
    #     value_type=DictRow(title=u'Table', schema=IMyRowSchema),
    #     default=[],
    #     required=False,
    # )
    # directives.widget('datagrid_field', DataGridFieldFactory)


@implementer(IExample)
class Example(Container):
    """Example instance class"""
