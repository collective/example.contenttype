from plone.app.textfield import RichText
from plone.autoform import directives
from plone.dexterity.content import Container

from plone.namedfile.field import NamedBlobFile
from plone.namedfile.field import NamedBlobImage
from plone.schema import Email
from plone.schema import JSONField

from plone.supermodel import model
from plone.supermodel.directives import fieldset
from plone.supermodel.directives import primary

from z3c.relationfield.schema import RelationChoice
from z3c.relationfield.schema import RelationList

from zope import schema
from zope.interface import implementer

import json


MIXEDFIELD_SCHEMA = json.dumps(
    {
        "type": "object",
        "properties": {
            "items": {"type": "array", "items": {"type": "object", "properties": {}}}
        },
    }
)


class IExample(model.Schema):
    """Dexterity-Schema with common field-types."""

    fieldset(
        "basicfields",
        label="Text, Boolean, Email",
        fields=(
            # "title",
            # "description",
            "richtext_field",
            "bool_field",
            "email_field",
            "uri_field",
        ),
    )

    fieldset(
        "numberfields",
        label="Number",
        fields=("int_field", "float_field"),
    )

    fieldset(
        "datetimefields",
        label="Date and time",
        fields=(
            "datetime_field",
            "date_field",
        ),
    )

    fieldset(
        "choicefields",
        label="Choice",
        fields=(
            "choice_field",
            "list_field",
            "tuple_field",
            "set_field",
        ),
    )

    fieldset(
        "relationfields_volto",
        label="Relation fields – Volto",
        fields=(
            "relationchoice_field_named_staticcatalogvocabulary",
            "relationlist_field_named_staticcatalogvocabulary",
        ),
    )

    fieldset(
        "filefields",
        label="File",
        fields=("file_field", "image_field"),
    )

    # fieldset(
    #     "datagrid",
    #     label="Datagrid field",
    #     fields=("history_field",),
    # )

    # Default fields
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

    # text_field = schema.Text(
    #     title="Text Field",
    #     description="zope.schema.Text",
    #     required=False,
    #     missing_value="",
    #     default="",
    # )

    # textline_field = schema.TextLine(
    #     title="Textline field",
    #     description="A simple input field (zope.schema.TextLine)",
    #     required=False,
    # )

    richtext_field = RichText(
        title="RichText field",
        description="This uses a richtext editor. (plone.app.textfield.RichText)",
        max_length=2000,
        required=False,
    )

    bool_field = schema.Bool(
        title="Boolean field",
        description="zope.schema.Bool",
        required=False,
    )

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

    # Choice fields
    choice_field = schema.Choice(
        title="Choice field",
        description="zope.schema.Choice",
        values=["One", "Two", "Three"],
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

    # File and image fields
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

    """Relation fields like Volto likes it

    RelationChoice and RelationList with named StaticCatalogVocabulary

    StaticCatalogVocabulary registered with same name as field/relation.
    This allowes Volto relations control panel to restrict potential targets.
    """

    relationchoice_field_named_staticcatalogvocabulary = RelationChoice(
        title="RelationChoice – named StaticCatalogVocabulary – Select widget",
        description="field/relation: relationchoice_field_named_staticcatalogvocabulary",
        vocabulary="relationchoice_field_named_staticcatalogvocabulary",
        required=False,
    )
    directives.widget(
        "relationchoice_field_named_staticcatalogvocabulary",
        frontendOptions={
            "widget": "select",
        },
    )

    relationlist_field_named_staticcatalogvocabulary = RelationList(
        title="RelationList – named StaticCatalogVocabulary – Select widget",
        description="field/relation: relationlist_field_named_staticcatalogvocabulary",
        value_type=RelationChoice(
            vocabulary="relationlist_field_named_staticcatalogvocabulary",
        ),
        required=False,
        default=[],
        missing_value=[],
    )
    directives.widget(
        "relationlist_field_named_staticcatalogvocabulary",
        frontendOptions={
            "widget": "select",
        },
    )

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

    # # Datagrid field
    # # See https://training.plone.org/mastering-plone/dexterity_reference.html#mixedfield-datagrid-field
    # # Be sure to provide a widget 'history_widget' in frontend code.
    # directives.widget("history_field", frontendOptions={"widget": "history_widget"})
    # history_field = JSONField(
    #     title="Mixedfield: datagrid field for Plone",
    #     required=False,
    #     schema=MIXEDFIELD_SCHEMA,
    #     widget="history_widget",
    #     default={"items": []},
    #     missing_value={"items": []},
    # )


@implementer(IExample)
class Example(Container):
    """Example instance class"""
