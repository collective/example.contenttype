# -*- coding: utf-8 -*-
from plone.app.textfield import RichText
from plone.app.vocabularies.catalog import CatalogSource
from plone.app.vocabularies.catalog import StaticCatalogVocabulary
from plone.app.z3cform.widget import AjaxSelectFieldWidget
from plone.app.z3cform.widget import RelatedItemsFieldWidget
from plone.app.z3cform.widget import SelectFieldWidget
from plone.autoform import directives
from plone.dexterity.content import Container

from plone.namedfile.field import NamedBlobFile
from plone.namedfile.field import NamedBlobImage
from plone.schema import Email

# from plone.schema import (
#     Dict,
# )  # take Dict field from plone.schema to use the widget attribute
from plone.supermodel import model
from plone.supermodel.directives import fieldset
from plone.supermodel.directives import primary

from z3c.form.browser.checkbox import CheckBoxFieldWidget
from z3c.form.browser.radio import RadioFieldWidget
from z3c.relationfield.schema import RelationChoice
from z3c.relationfield.schema import RelationList
from zope import schema
from zope.interface import implementer

from zope.interface import Interface


class IExample(model.Schema):
    """Dexterity-Schema with all field-types."""

    # The most used fields
    # textline, text, bool, richtext, email

    fieldset(
        "numberfields",
        label="Number fields",
        fields=("int_field", "float_field"),
    )

    fieldset(
        "datetimefields",
        label="Date and time fields",
        fields=(
            "datetime_field",
            "date_field",
            # "time_field",
            # "timedelta_field",
        ),
    )

    fieldset(
        "choicefields",
        label="Choice and Multiple Choice fields",
        fields=(
            "choice_field",
            "choice_field_radio",
            "choice_field_select",
            "choice_field_voc",
            "list_field",
            "list_field_checkbox",
            "list_field_select",
            "list_field_voc_unconstrained",
            "tuple_field",
            "set_field",
            "set_field_checkbox",
        ),
    )

    fieldset(
        "relationfields",
        label="Relation fields",
        fields=(
            "relationchoice_field",
            "relationlist_field",
            "relationchoice_field_constrained",
            "relationlist_field_constrained",
            "relationlist_field_search_mode",
            "relationchoice_field_staticcatalogvocabulary",
            "relationchoice_field_named_staticcatalogvocabulary",
            # "relationchoice_field_radio",
            "relationlist_field_select",
            "relationlist_field_checkbox",
            # "relationchoice_field_ajax_select",
            # "relationlist_field_ajax_select",
        ),
    )

    fieldset(
        "uuidrelationfields",
        label="Relation widgets with uuids",
        fields=(
            "uuid_choice_field",
            "uuid_list_field",
            "uuid_choice_field_constrained",
            "uuid_list_field_constrained",
            "uuid_list_field_search_mode",
            # "uuid_choice_field_select",
            # "uuid_choice_field_radio",
            "uuid_list_field_select",
            "uuid_list_field_checkbox",
            # "uuid_choice_field_ajax_select",
            # "uuid_list_field_ajax_select",
        ),
    )

    fieldset(
        "filefields",
        label="File fields",
        fields=("file_field", "image_field"),
    )

    fieldset(
        "otherfields",
        label="Other fields",
        fields=(
            "uri_field",
            "sourcetext_field",
            "ascii_field",
            "bytesline_field",
            "asciiline_field",
            "pythonidentifier_field",
            "dottedname_field",
            # 'dict_field',
            # "vocabularyterms_field",
            # "vocabularytermstranslation_field",
            # 'dict_field_with_choice',
        ),
    )

    primary("title")
    title = schema.TextLine(
        title="Primary Field (Textline)",
        description="zope.schema.TextLine",
        required=True,
    )

    description = schema.TextLine(
        title="Description (Textline)",
        description="zope.schema.TextLine",
        required=False,
    )

    text_field = schema.Text(
        title="Text Field",
        description="zope.schema.Text",
        required=False,
        missing_value="",
    )

    textline_field = schema.TextLine(
        title="Textline field",
        description="A simple input field (zope.schema.TextLine)",
        required=False,
    )

    bool_field = schema.Bool(
        title="Boolean field",
        description="zope.schema.Bool",
        required=False,
    )

    choice_field = schema.Choice(
        title="Choice field",
        description="zope.schema.Choice",
        values=["One", "Two", "Three"],
        required=True,
    )

    directives.widget(choice_field_radio=RadioFieldWidget)
    choice_field_radio = schema.Choice(
        title="Choice field with radio boxes",
        description="zope.schema.Choice",
        values=["One", "Two", "Three"],
        required=False,
    )

    choice_field_voc = schema.Choice(
        title="Choicefield with values from named vocabulary",
        description="zope.schema.Choice",
        vocabulary="plone.app.vocabularies.PortalTypes",
        required=False,
    )

    directives.widget(choice_field_select=SelectFieldWidget)
    choice_field_select = schema.Choice(
        title="Choicefield with select2 widget",
        description="zope.schema.Choice",
        vocabulary="plone.app.vocabularies.PortalTypes",
        required=False,
    )

    list_field = schema.List(
        title="List field",
        description="zope.schema.List",
        value_type=schema.Choice(
            values=["Beginner", "Advanced", "Professional"],
        ),
        required=False,
        missing_value=[],
        default=[],
    )

    directives.widget(list_field_checkbox=CheckBoxFieldWidget)
    list_field_checkbox = schema.List(
        title="List field with checkboxes",
        description="zope.schema.List",
        value_type=schema.Choice(
            values=["Beginner", "Advanced", "Professional"],
        ),
        required=False,
        missing_value=[],
        default=[],
    )

    directives.widget(list_field_select=SelectFieldWidget)
    list_field_select = schema.List(
        title="List field with select widget",
        description="zope.schema.List",
        value_type=schema.Choice(
            values=["Beginner", "Advanced", "Professional"],
        ),
        required=False,
        missing_value=[],
        default=[],
    )

    list_field_voc_unconstrained = schema.List(
        title="List field with values from vocabulary but not constrained to them.",
        description="zope.schema.List",
        value_type=schema.TextLine(),
        required=False,
        missing_value=[],
    )
    directives.widget(
        "list_field_voc_unconstrained",
        AjaxSelectFieldWidget,
        vocabulary="plone.app.vocabularies.PortalTypes",
        pattern_options={
            "closeOnSelect": False,  # Select2 option to leave dropdown open for multiple selection
        },
    )

    tuple_field = schema.Tuple(
        title="Tuple field",
        description="zope.schema.Tuple",
        value_type=schema.Choice(
            values=["Beginner", "Advanced", "Professional"],
        ),
        required=False,
        missing_value=(),
        default=(),
    )

    set_field = schema.Set(
        title="Set field",
        description="zope.schema.Set",
        value_type=schema.Choice(
            values=["Beginner", "Advanced", "Professional"],
        ),
        required=False,
        missing_value=set(),
        default=set(),
    )

    directives.widget(set_field_checkbox=CheckBoxFieldWidget)
    set_field_checkbox = schema.Set(
        title="Set field with checkboxes",
        description="zope.schema.Set",
        value_type=schema.Choice(
            values=["Beginner", "Advanced", "Professional"],
        ),
        required=False,
        missing_value=set(),
        default=set(),
    )

    # File fields
    image_field = NamedBlobImage(
        title="Image field",
        description="A upload field for images (plone.namedfile.field.NamedBlobImage)",
        required=False,
    )

    file_field = NamedBlobFile(
        title="File field",
        description="A upload field for files (plone.namedfile.field.NamedBlobFile)",
        required=False,
    )

    # Date and Time fields
    datetime_field = schema.Datetime(
        title="Datetime field",
        description="Uses a date and time picker (zope.schema.Datetime)",
        required=False,
    )

    date_field = schema.Date(
        title="Date field",
        description="Uses a date picker (zope.schema.Date)",
        required=False,
    )

    # time_field = schema.Time(
    #     title="Time field",
    #     description="zope.schema.Time",
    #     required=False,
    # )

    # timedelta_field = schema.Timedelta(
    #     title="Timedelta field",
    #     description="zope.schema.Timedelta",
    #     required=False,
    # )

    # Relation Fields
    relationchoice_field = RelationChoice(
        title="Relationchoice field",
        description="z3c.relationfield.schema.RelationChoice",
        vocabulary="plone.app.vocabularies.Catalog",
        required=False,
    )

    relationlist_field = RelationList(
        title="RelationList",
        description="relationlist_field: z3c.relationfield.schema.RelationList",
        default=[],
        value_type=RelationChoice(vocabulary="plone.app.vocabularies.Catalog"),
        required=False,
        missing_value=[],
    )

    relationchoice_field_constrained = RelationChoice(
        title="Relationchoice field (only allows Documents)",
        description="z3c.relationfield.schema.RelationChoice",
        vocabulary="plone.app.vocabularies.Catalog",
        required=False,
    )
    directives.widget(
        "relationchoice_field_constrained",
        RelatedItemsFieldWidget,
        pattern_options={"selectableTypes": ["Document"]},
    )

    relationlist_field_constrained = RelationList(
        title="Relationlist Field (only allows Documents and Events)",
        description="z3c.relationfield.schema.RelationList",
        default=[],
        value_type=RelationChoice(vocabulary="plone.app.vocabularies.Catalog"),
        required=False,
        missing_value=[],
    )
    directives.widget(
        "relationlist_field_constrained",
        RelatedItemsFieldWidget,
        pattern_options={"selectableTypes": ["Document", "Event"]},
    )

    relationlist_field_search_mode = RelationList(
        title="Relationlist Field in Search Mode (constrained to published Documents and Events)",
        description="z3c.relationfield.schema.RelationList",
        default=[],
        value_type=RelationChoice(
            source=CatalogSource(
                portal_type=["Document", "Event"], review_state="published"
            )
        ),
        required=False,
        missing_value=[],
    )
    directives.widget(
        "relationlist_field_search_mode",
        RelatedItemsFieldWidget,
        pattern_options={
            "baseCriteria": [  # This is a optimization that limits the catalog-query
                {
                    "i": "portal_type",
                    "o": "plone.app.querystring.operation.selection.any",
                    "v": ["Document", "Event"],
                },
                {
                    "i": "review_state",
                    "o": "plone.app.querystring.operation.selection.any",
                    "v": "published",
                },
            ],
            "mode": "search",
        },
    )

    # From here on we use other widgets than the default RelatedItemsFieldWidget

    # # This one also works in Volto!
    # # All other options use the default ObjectWidget in Volto so far.
    relationchoice_field_staticcatalogvocabulary = RelationChoice(
        title="RelationChoice – StaticCatalogVocabulary – Object Browser (Classic: Select Widget)",
        description="relationchoice_field_staticcatalogvocabulary",
        vocabulary=StaticCatalogVocabulary(
            {
                "portal_type": ["Document", "Event"],
                "review_state": "published",
            }
        ),
        required=False,
    )
    directives.widget(
        "relationchoice_field_staticcatalogvocabulary",
        SelectFieldWidget,
        frontendOptions={
            "widget": "object_browser",
            "widgetProps": {"mode": "link", "return": "single"},
        },
    )

    # Named StaticCatalogVocabulary
    relationchoice_field_named_staticcatalogvocabulary = RelationChoice(
        title="RelationChoice – named StaticCatalogVocabulary – Object Browser (Classic: Select Widget)",
        description="relationchoice_field_named_staticcatalogvocabulary",
        vocabulary="relationchoice_field_named_staticcatalogvocabulary",
        required=False,
    )
    directives.widget(
        "relationchoice_field_named_staticcatalogvocabulary",
        SelectFieldWidget,
        frontendOptions={
            "widget": "object_browser",
            "widgetProps": {"mode": "link", "return": "single"},
        },
    )

    # relationchoice_field_radio = RelationChoice(
    #     title="RelationChoice with Radio Widget (and customized title-template)",
    #     vocabulary=StaticCatalogVocabulary(
    #         {
    #             "portal_type": ["Document", "Event"],
    #             "review_state": "published",
    #         },
    #         title_template="{brain.Title}",
    #     ),  # Set a custom vocabulary item title
    #     required=False,
    # )
    # directives.widget(
    #     "relationchoice_field_radio",
    #     RadioFieldWidget,
    # )

    relationlist_field_select = RelationList(
        title="RelationList with select widget with items from a named vocabulary",
        value_type=RelationChoice(
            vocabulary="example.vocabularies.documents",
        ),
        required=False,
    )
    directives.widget(
        "relationlist_field_select",
        SelectFieldWidget,
        pattern_options={
            "closeOnSelect": False,  # Select2 option to leave dropdown open for multiple selection
        },
    )

    relationlist_field_checkbox = RelationList(
        title="RelationList with Checkboxes",
        value_type=RelationChoice(
            vocabulary="example.vocabularies.documents",
        ),
        required=False,
    )
    directives.widget(
        "relationlist_field_checkbox",
        CheckBoxFieldWidget,
    )

    # relationchoice_field_ajax_select = RelationChoice(
    #     title="Relationchoice Field with AJAXSelect",
    #     description="z3c.relationfield.schema.RelationChoice",
    #     vocabulary=StaticCatalogVocabulary(
    #         {
    #             "portal_type": ["Document", "Event"],
    #         }
    #     ),
    #     required=False,
    # )
    # directives.widget(
    #     "relationchoice_field_ajax_select",
    #     AjaxSelectFieldWidget,
    #     vocabulary=StaticCatalogVocabulary(
    #         {
    #             "portal_type": ["Document", "Event"],
    #         }
    #     ),
    #     pattern_options={  # Options for Select2
    #         "minimumInputLength": 2,  # - Don't query until at least two characters have been typed
    #         "ajax": {"quietMillis": 500},  # - Wait 500ms after typing to make query
    #     },
    # )

    # relationlist_field_ajax_select = RelationList(
    #     title="Relationlist Field with AJAXSelect",
    #     description="z3c.relationfield.schema.RelationList",
    #     value_type=RelationChoice(
    #         vocabulary=StaticCatalogVocabulary(
    #             {
    #                 "portal_type": ["Document", "Event"],
    #                 "review_state": "published",
    #             }
    #         )
    #     ),
    #     required=False,
    # )
    # directives.widget(
    #     "relationlist_field_ajax_select",
    #     AjaxSelectFieldWidget,
    #     vocabulary=StaticCatalogVocabulary(
    #         {
    #             "portal_type": ["Document", "Event", "Folder"],
    #         },
    #         title_template="{brain.Type}: {brain.Title} at {path}",
    #     ),  # Custom item rendering
    #     pattern_options={  # Options for Select2
    #         "minimumInputLength": 2,  # - Don't query until at least two characters have been typed
    #         "ajax": {"quietMillis": 500},  # - Wait 500ms after typing to make query
    #     },
    # )

    # These look like relationsfields (see above) but only store the uuid(s) of the selected target
    # as a string in a the field instead of a RelationValue.
    # A good way to use these is in combination with a index that allows you to query these connenctions.
    uuid_choice_field = schema.Choice(
        title="Choice field with RelatedItems widget storing uuids",
        description="zope.schema.Choice",
        vocabulary="plone.app.vocabularies.Catalog",
        required=False,
    )
    directives.widget("uuid_choice_field", RelatedItemsFieldWidget)

    uuid_list_field = schema.List(
        title="List Field with RelatedItems widget storing uuids",
        description="zope.schema.List",
        default=[],
        value_type=schema.Choice(vocabulary="plone.app.vocabularies.Catalog"),
        required=False,
        missing_value=[],
    )
    directives.widget("uuid_list_field", RelatedItemsFieldWidget)

    uuid_choice_field_constrained = schema.Choice(
        title="Choice field with RelatedItems widget storing uuids (only allows Documents)",
        description="zope.schema.Choice",
        vocabulary="plone.app.vocabularies.Catalog",
        required=False,
    )
    directives.widget(
        "uuid_choice_field_constrained",
        RelatedItemsFieldWidget,
        pattern_options={"selectableTypes": ["Document"]},
    )

    uuid_list_field_constrained = schema.List(
        title="List Field with RelatedItems widget storing uuids (only allows Documents and Events)",
        description="zope.schema.List",
        default=[],
        value_type=schema.Choice(vocabulary="plone.app.vocabularies.Catalog"),
        required=False,
        missing_value=[],
    )
    directives.widget(
        "uuid_list_field_constrained",
        RelatedItemsFieldWidget,
        pattern_options={"selectableTypes": ["Document", "Folder"]},
    )

    uuid_list_field_search_mode = schema.List(
        title="List Field with RelatedItems widget in Search Mode storing uuids",
        description="zope.schema.List",
        default=[],
        value_type=schema.Choice(
            source=CatalogSource(
                portal_type=["Document", "Event"], review_state="published"
            )
        ),
        required=False,
        missing_value=[],
    )
    directives.widget(
        "uuid_list_field_search_mode",
        RelatedItemsFieldWidget,
        pattern_options={
            "selectableTypes": ["Document", "Folder"],
            "basePath": "",  # Start the search at the portal root
            "mode": "search",
        },
    )

    # From here on we use other widgets than the default RelatedItemsFieldWidget

    # uuid_choice_field_select = schema.Choice(
    #     title="UUID Choice with select widget storing uuids",
    #     vocabulary=StaticCatalogVocabulary(
    #         {
    #             "portal_type": ["Document", "Event"],
    #             "review_state": "published",
    #         }
    #     ),
    #     required=False,
    # )
    # directives.widget(
    #     "uuid_choice_field_select",
    #     SelectFieldWidget,
    # )

    # uuid_choice_field_radio = schema.Choice(
    #     title="RelationChoice with Radio widget storing uuids",
    #     vocabulary=StaticCatalogVocabulary(
    #         {
    #             "portal_type": ["Document", "Event"],
    #             "review_state": "published",
    #         },
    #         title_template="{brain.Title}",
    #     ),  # Set a custom vocabulary item title
    #     required=False,
    # )
    # directives.widget(
    #     "uuid_choice_field_radio",
    #     RadioFieldWidget,
    # )

    uuid_list_field_select = schema.List(
        title="RelationList with select widget with items from a named vocabulary storing uuids",
        value_type=schema.Choice(
            vocabulary="example.vocabularies.documents",
        ),
        required=False,
    )
    directives.widget(
        "uuid_list_field_select",
        SelectFieldWidget,
        pattern_options={
            "closeOnSelect": False,  # Select2 option to leave dropdown open for multiple selection
        },
    )

    uuid_list_field_checkbox = schema.List(
        title="RelationList with Checkboxes storing uuids",
        value_type=schema.Choice(
            vocabulary="example.vocabularies.documents",
        ),
        required=False,
    )
    directives.widget(
        "uuid_list_field_checkbox",
        CheckBoxFieldWidget,
    )

    # uuid_choice_field_ajax_select = schema.Choice(
    #     title="Relationchoice Field with AJAXSelect storing uuids",
    #     description="zope.schema.Choice with StaticCatalogVocabulary and AjaxSelectFieldWidget. Documents and Event only.",
    #     vocabulary=StaticCatalogVocabulary(
    #         {
    #             "portal_type": ["Document", "Event"],
    #         }
    #     ),
    #     required=False,
    # )
    # directives.widget(
    #     "uuid_choice_field_ajax_select",
    #     AjaxSelectFieldWidget,
    #     vocabulary=StaticCatalogVocabulary(
    #         {
    #             "portal_type": ["Document", "Event"],
    #         }
    #     ),
    #     pattern_options={  # Options for Select2
    #         "minimumInputLength": 2,  # - Don't query until at least two characters have been typed
    #         "ajax": {"quietMillis": 500},  # - Wait 500ms after typing to make query
    #     },
    # )

    # uuid_list_field_ajax_select = schema.List(
    #     title="Relationlist Field with AJAXSelect storing uuids",
    #     description="zope.schema.List with StaticCatalogVocabulary and AjaxSelectFieldWidget. Published Documents and Event only.",
    #     value_type=schema.Choice(
    #         vocabulary=StaticCatalogVocabulary(
    #             {
    #                 "portal_type": ["Document", "Event"],
    #                 "review_state": "published",
    #             }
    #         )
    #     ),
    #     required=False,
    # )
    # directives.widget(
    #     "uuid_list_field_ajax_select",
    #     AjaxSelectFieldWidget,
    #     vocabulary=StaticCatalogVocabulary(
    #         {
    #             "portal_type": ["Document", "Event"],
    #             "review_state": "published",
    #         },
    #         title_template="{brain.Type}: {brain.Title} at {path}",
    #     ),  # Custom item rendering
    #     pattern_options={  # Options for Select2
    #         "minimumInputLength": 2,  # - Don't query until at least two characters have been typed
    #         "ajax": {"quietMillis": 500},  # - Wait 500ms after typing to make query
    #         "closeOnSelect": False,  # - Leave dropdown open for multiple selection
    #     },
    # )

    # Number fields
    int_field = schema.Int(
        title="Integer Field (e.g. 12)",
        description="zope.schema.Int",
        required=False,
    )

    float_field = schema.Float(
        title="Float field, e.g. 12.7",
        description="zope.schema.Float",
        required=False,
    )

    # Text fields
    email_field = Email(
        title="Email field",
        description="A simple input field for a email (plone.schema.email.Email)",
        required=False,
    )

    uri_field = schema.URI(
        title="URI field",
        description="A simple input field for a URLs (zope.schema.URI)",
        required=False,
    )

    richtext_field = RichText(
        title="RichText field",
        description="This uses a richtext editor. (plone.app.textfield.RichText)",
        max_length=2000,
        required=False,
    )

    sourcetext_field = schema.SourceText(
        title="SourceText field",
        description="zope.schema.SourceText",
        required=False,
    )

    ascii_field = schema.ASCII(
        title="ASCII field",
        description="zope.schema.ASCII",
        required=False,
    )

    bytesline_field = schema.BytesLine(
        title="BytesLine field",
        description="zope.schema.BytesLine",
        required=False,
    )

    asciiline_field = schema.ASCIILine(
        title="ASCIILine field",
        description="zope.schema.ASCIILine",
        required=False,
    )

    pythonidentifier_field = schema.PythonIdentifier(
        title="PythonIdentifier field",
        description="zope.schema.PythonIdentifier",
        required=False,
    )

    dottedname_field = schema.DottedName(
        title="DottedName field",
        description="zope.schema.DottedName",
        required=False,
    )

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

    # vocabularyterms_field = Dict(  # we use the plone.schema field Dict not zope.schema field to use the attribute 'widget'
    #     title=u"Vocabulary terms field",
    #     description=u"plone.schema.Dict field with value_type schema.TextLine and frontend widget 'VocabularyTermsWidget'",
    #     required=False,
    #     key_type=schema.TextLine(
    #         title=u"Key",
    #         required=False,
    #     ),
    #     value_type=schema.TextLine(
    #         title=u"Value",
    #         required=False,
    #     ),
    #     widget="vocabularyterms",  # we use the widget attribute to apply the frontend widget VocabularyWidget
    # )

    # vocabularytermstranslation_field = Dict(  # we use the plone.schema field Dict not zope.schema field to use the attribute 'widget'
    #     title=u"Vocabulary terms field with translations",
    #     description=u"plone.schema.Dict field with value_type Dict and frontend widget 'VocabularyTermsWidget'",
    #     required=False,
    #     key_type=schema.TextLine(
    #         title=u"Key",
    #         required=False,
    #     ),
    #     value_type=Dict(  # we use the plone.schema field Dict not zope.schema field to use the attribute 'widget'
    #         title=u"Term translation",
    #         description=u"plone.schema.Dict field for translations of vocabulary term",
    #         required=True,
    #         key_type=schema.TextLine(
    #             title=u"Key",
    #             required=False,
    #         ),
    #         value_type=schema.TextLine(
    #             title=u"Value",
    #             required=False,
    #         ),
    #     ),
    #     widget="vocabularyterms",  # we use the widget attribute to apply the frontend widget VocabularyWidget
    # )

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


@implementer(IExample)
class Example(Container):
    """Example instance class"""
