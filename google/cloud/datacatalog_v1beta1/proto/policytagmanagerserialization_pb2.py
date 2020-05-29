# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/datacatalog_v1beta1/proto/policytagmanagerserialization.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.cloud.datacatalog_v1beta1.proto import (
    policytagmanager_pb2 as google_dot_cloud_dot_datacatalog__v1beta1_dot_proto_dot_policytagmanager__pb2,
)
from google.iam.v1 import policy_pb2 as google_dot_iam_dot_v1_dot_policy__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
    name="google/cloud/datacatalog_v1beta1/proto/policytagmanagerserialization.proto",
    package="google.cloud.datacatalog.v1beta1",
    syntax="proto3",
    serialized_options=b'\n$com.google.cloud.datacatalog.v1beta1B"PolicyTagManagerSerializationProtoP\001ZKgoogle.golang.org/genproto/googleapis/cloud/datacatalog/v1beta1;datacatalog\370\001\001\252\002 Google.Cloud.DataCatalog.V1Beta1\312\002 Google\\Cloud\\DataCatalog\\V1beta1\352\002#Google::Cloud::DataCatalog::V1beta1',
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\nJgoogle/cloud/datacatalog_v1beta1/proto/policytagmanagerserialization.proto\x12 google.cloud.datacatalog.v1beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a=google/cloud/datacatalog_v1beta1/proto/policytagmanager.proto\x1a\x1agoogle/iam/v1/policy.proto\x1a\x17google/api/client.proto"\x90\x01\n\x12SerializedTaxonomy\x12\x19\n\x0c\x64isplay_name\x18\x01 \x01(\tB\x03\xe0\x41\x02\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12J\n\x0bpolicy_tags\x18\x03 \x03(\x0b\x32\x35.google.cloud.datacatalog.v1beta1.SerializedPolicyTag"\x97\x01\n\x13SerializedPolicyTag\x12\x19\n\x0c\x64isplay_name\x18\x02 \x01(\tB\x03\xe0\x41\x02\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12P\n\x11\x63hild_policy_tags\x18\x04 \x03(\x0b\x32\x35.google.cloud.datacatalog.v1beta1.SerializedPolicyTag"\xa9\x01\n\x17ImportTaxonomiesRequest\x12;\n\x06parent\x18\x01 \x01(\tB+\xe0\x41\x02\xfa\x41%\x12#datacatalog.googleapis.com/Taxonomy\x12G\n\rinline_source\x18\x02 \x01(\x0b\x32..google.cloud.datacatalog.v1beta1.InlineSourceH\x00\x42\x08\n\x06source"]\n\x0cInlineSource\x12M\n\ntaxonomies\x18\x01 \x03(\x0b\x32\x34.google.cloud.datacatalog.v1beta1.SerializedTaxonomyB\x03\xe0\x41\x02"Z\n\x18ImportTaxonomiesResponse\x12>\n\ntaxonomies\x18\x01 \x03(\x0b\x32*.google.cloud.datacatalog.v1beta1.Taxonomy"\xc7\x01\n\x17\x45xportTaxonomiesRequest\x12;\n\x06parent\x18\x01 \x01(\tB+\xe0\x41\x02\xfa\x41%\x12#datacatalog.googleapis.com/Taxonomy\x12?\n\ntaxonomies\x18\x02 \x03(\tB+\xe0\x41\x02\xfa\x41%\n#datacatalog.googleapis.com/Taxonomy\x12\x1f\n\x15serialized_taxonomies\x18\x03 \x01(\x08H\x00\x42\r\n\x0b\x64\x65stination"d\n\x18\x45xportTaxonomiesResponse\x12H\n\ntaxonomies\x18\x01 \x03(\x0b\x32\x34.google.cloud.datacatalog.v1beta1.SerializedTaxonomy2\x92\x04\n\x1dPolicyTagManagerSerialization\x12\xd0\x01\n\x10ImportTaxonomies\x12\x39.google.cloud.datacatalog.v1beta1.ImportTaxonomiesRequest\x1a:.google.cloud.datacatalog.v1beta1.ImportTaxonomiesResponse"E\x82\xd3\xe4\x93\x02?":/v1beta1/{parent=projects/*/locations/*}/taxonomies:import:\x01*\x12\xcd\x01\n\x10\x45xportTaxonomies\x12\x39.google.cloud.datacatalog.v1beta1.ExportTaxonomiesRequest\x1a:.google.cloud.datacatalog.v1beta1.ExportTaxonomiesResponse"B\x82\xd3\xe4\x93\x02<\x12:/v1beta1/{parent=projects/*/locations/*}/taxonomies:export\x1aN\xca\x41\x1a\x64\x61tacatalog.googleapis.com\xd2\x41.https://www.googleapis.com/auth/cloud-platformB\x88\x02\n$com.google.cloud.datacatalog.v1beta1B"PolicyTagManagerSerializationProtoP\x01ZKgoogle.golang.org/genproto/googleapis/cloud/datacatalog/v1beta1;datacatalog\xf8\x01\x01\xaa\x02 Google.Cloud.DataCatalog.V1Beta1\xca\x02 Google\\Cloud\\DataCatalog\\V1beta1\xea\x02#Google::Cloud::DataCatalog::V1beta1b\x06proto3',
    dependencies=[
        google_dot_api_dot_annotations__pb2.DESCRIPTOR,
        google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,
        google_dot_api_dot_resource__pb2.DESCRIPTOR,
        google_dot_cloud_dot_datacatalog__v1beta1_dot_proto_dot_policytagmanager__pb2.DESCRIPTOR,
        google_dot_iam_dot_v1_dot_policy__pb2.DESCRIPTOR,
        google_dot_api_dot_client__pb2.DESCRIPTOR,
    ],
)


_SERIALIZEDTAXONOMY = _descriptor.Descriptor(
    name="SerializedTaxonomy",
    full_name="google.cloud.datacatalog.v1beta1.SerializedTaxonomy",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="display_name",
            full_name="google.cloud.datacatalog.v1beta1.SerializedTaxonomy.display_name",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b"\340A\002",
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="description",
            full_name="google.cloud.datacatalog.v1beta1.SerializedTaxonomy.description",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="policy_tags",
            full_name="google.cloud.datacatalog.v1beta1.SerializedTaxonomy.policy_tags",
            index=2,
            number=3,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=319,
    serialized_end=463,
)


_SERIALIZEDPOLICYTAG = _descriptor.Descriptor(
    name="SerializedPolicyTag",
    full_name="google.cloud.datacatalog.v1beta1.SerializedPolicyTag",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="display_name",
            full_name="google.cloud.datacatalog.v1beta1.SerializedPolicyTag.display_name",
            index=0,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b"\340A\002",
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="description",
            full_name="google.cloud.datacatalog.v1beta1.SerializedPolicyTag.description",
            index=1,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="child_policy_tags",
            full_name="google.cloud.datacatalog.v1beta1.SerializedPolicyTag.child_policy_tags",
            index=2,
            number=4,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=466,
    serialized_end=617,
)


_IMPORTTAXONOMIESREQUEST = _descriptor.Descriptor(
    name="ImportTaxonomiesRequest",
    full_name="google.cloud.datacatalog.v1beta1.ImportTaxonomiesRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="parent",
            full_name="google.cloud.datacatalog.v1beta1.ImportTaxonomiesRequest.parent",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b"\340A\002\372A%\022#datacatalog.googleapis.com/Taxonomy",
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="inline_source",
            full_name="google.cloud.datacatalog.v1beta1.ImportTaxonomiesRequest.inline_source",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[
        _descriptor.OneofDescriptor(
            name="source",
            full_name="google.cloud.datacatalog.v1beta1.ImportTaxonomiesRequest.source",
            index=0,
            containing_type=None,
            create_key=_descriptor._internal_create_key,
            fields=[],
        )
    ],
    serialized_start=620,
    serialized_end=789,
)


_INLINESOURCE = _descriptor.Descriptor(
    name="InlineSource",
    full_name="google.cloud.datacatalog.v1beta1.InlineSource",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="taxonomies",
            full_name="google.cloud.datacatalog.v1beta1.InlineSource.taxonomies",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b"\340A\002",
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        )
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=791,
    serialized_end=884,
)


_IMPORTTAXONOMIESRESPONSE = _descriptor.Descriptor(
    name="ImportTaxonomiesResponse",
    full_name="google.cloud.datacatalog.v1beta1.ImportTaxonomiesResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="taxonomies",
            full_name="google.cloud.datacatalog.v1beta1.ImportTaxonomiesResponse.taxonomies",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        )
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=886,
    serialized_end=976,
)


_EXPORTTAXONOMIESREQUEST = _descriptor.Descriptor(
    name="ExportTaxonomiesRequest",
    full_name="google.cloud.datacatalog.v1beta1.ExportTaxonomiesRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="parent",
            full_name="google.cloud.datacatalog.v1beta1.ExportTaxonomiesRequest.parent",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b"\340A\002\372A%\022#datacatalog.googleapis.com/Taxonomy",
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="taxonomies",
            full_name="google.cloud.datacatalog.v1beta1.ExportTaxonomiesRequest.taxonomies",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b"\340A\002\372A%\n#datacatalog.googleapis.com/Taxonomy",
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="serialized_taxonomies",
            full_name="google.cloud.datacatalog.v1beta1.ExportTaxonomiesRequest.serialized_taxonomies",
            index=2,
            number=3,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[
        _descriptor.OneofDescriptor(
            name="destination",
            full_name="google.cloud.datacatalog.v1beta1.ExportTaxonomiesRequest.destination",
            index=0,
            containing_type=None,
            create_key=_descriptor._internal_create_key,
            fields=[],
        )
    ],
    serialized_start=979,
    serialized_end=1178,
)


_EXPORTTAXONOMIESRESPONSE = _descriptor.Descriptor(
    name="ExportTaxonomiesResponse",
    full_name="google.cloud.datacatalog.v1beta1.ExportTaxonomiesResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="taxonomies",
            full_name="google.cloud.datacatalog.v1beta1.ExportTaxonomiesResponse.taxonomies",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        )
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=1180,
    serialized_end=1280,
)

_SERIALIZEDTAXONOMY.fields_by_name["policy_tags"].message_type = _SERIALIZEDPOLICYTAG
_SERIALIZEDPOLICYTAG.fields_by_name[
    "child_policy_tags"
].message_type = _SERIALIZEDPOLICYTAG
_IMPORTTAXONOMIESREQUEST.fields_by_name["inline_source"].message_type = _INLINESOURCE
_IMPORTTAXONOMIESREQUEST.oneofs_by_name["source"].fields.append(
    _IMPORTTAXONOMIESREQUEST.fields_by_name["inline_source"]
)
_IMPORTTAXONOMIESREQUEST.fields_by_name[
    "inline_source"
].containing_oneof = _IMPORTTAXONOMIESREQUEST.oneofs_by_name["source"]
_INLINESOURCE.fields_by_name["taxonomies"].message_type = _SERIALIZEDTAXONOMY
_IMPORTTAXONOMIESRESPONSE.fields_by_name[
    "taxonomies"
].message_type = (
    google_dot_cloud_dot_datacatalog__v1beta1_dot_proto_dot_policytagmanager__pb2._TAXONOMY
)
_EXPORTTAXONOMIESREQUEST.oneofs_by_name["destination"].fields.append(
    _EXPORTTAXONOMIESREQUEST.fields_by_name["serialized_taxonomies"]
)
_EXPORTTAXONOMIESREQUEST.fields_by_name[
    "serialized_taxonomies"
].containing_oneof = _EXPORTTAXONOMIESREQUEST.oneofs_by_name["destination"]
_EXPORTTAXONOMIESRESPONSE.fields_by_name[
    "taxonomies"
].message_type = _SERIALIZEDTAXONOMY
DESCRIPTOR.message_types_by_name["SerializedTaxonomy"] = _SERIALIZEDTAXONOMY
DESCRIPTOR.message_types_by_name["SerializedPolicyTag"] = _SERIALIZEDPOLICYTAG
DESCRIPTOR.message_types_by_name["ImportTaxonomiesRequest"] = _IMPORTTAXONOMIESREQUEST
DESCRIPTOR.message_types_by_name["InlineSource"] = _INLINESOURCE
DESCRIPTOR.message_types_by_name["ImportTaxonomiesResponse"] = _IMPORTTAXONOMIESRESPONSE
DESCRIPTOR.message_types_by_name["ExportTaxonomiesRequest"] = _EXPORTTAXONOMIESREQUEST
DESCRIPTOR.message_types_by_name["ExportTaxonomiesResponse"] = _EXPORTTAXONOMIESRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SerializedTaxonomy = _reflection.GeneratedProtocolMessageType(
    "SerializedTaxonomy",
    (_message.Message,),
    {
        "DESCRIPTOR": _SERIALIZEDTAXONOMY,
        "__module__": "google.cloud.datacatalog_v1beta1.proto.policytagmanagerserialization_pb2",
        "__doc__": """Message capturing a taxonomy and its policy tag hierarchy as a nested
  proto. Used for taxonomy import/export and mutation.
  Attributes:
      display_name:
          Required. Display name of the taxonomy. Max 200 bytes when
          encoded in UTF-8.
      description:
          Description of the serialized taxonomy. The length of the
          description is limited to 2000 bytes when encoded in UTF-8. If
          not set, defaults to an empty description.
      policy_tags:
          Top level policy tags associated with the taxonomy if any.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.datacatalog.v1beta1.SerializedTaxonomy)
    },
)
_sym_db.RegisterMessage(SerializedTaxonomy)

SerializedPolicyTag = _reflection.GeneratedProtocolMessageType(
    "SerializedPolicyTag",
    (_message.Message,),
    {
        "DESCRIPTOR": _SERIALIZEDPOLICYTAG,
        "__module__": "google.cloud.datacatalog_v1beta1.proto.policytagmanagerserialization_pb2",
        "__doc__": """Message representing one policy tag when exported as a nested proto.
  Attributes:
      display_name:
          Required. Display name of the policy tag. Max 200 bytes when
          encoded in UTF-8.
      description:
          Description of the serialized policy tag. The length of the
          description is limited to 2000 bytes when encoded in UTF-8. If
          not set, defaults to an empty description.
      child_policy_tags:
          Children of the policy tag if any.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.datacatalog.v1beta1.SerializedPolicyTag)
    },
)
_sym_db.RegisterMessage(SerializedPolicyTag)

ImportTaxonomiesRequest = _reflection.GeneratedProtocolMessageType(
    "ImportTaxonomiesRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _IMPORTTAXONOMIESREQUEST,
        "__module__": "google.cloud.datacatalog_v1beta1.proto.policytagmanagerserialization_pb2",
        "__doc__": """Request message for [ImportTaxonomies][google.cloud.datacatalog.v1beta
  1.PolicyTagManagerSerialization.ImportTaxonomies].
  Attributes:
      parent:
          Required. Resource name of project that the newly created
          taxonomies will belong to.
      source:
          Required. Source taxonomies to be imported in a tree
          structure.
      inline_source:
          Inline source used for taxonomies import
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.datacatalog.v1beta1.ImportTaxonomiesRequest)
    },
)
_sym_db.RegisterMessage(ImportTaxonomiesRequest)

InlineSource = _reflection.GeneratedProtocolMessageType(
    "InlineSource",
    (_message.Message,),
    {
        "DESCRIPTOR": _INLINESOURCE,
        "__module__": "google.cloud.datacatalog_v1beta1.proto.policytagmanagerserialization_pb2",
        "__doc__": """Inline source used for taxonomies import.
  Attributes:
      taxonomies:
          Required. Taxonomies to be imported.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.datacatalog.v1beta1.InlineSource)
    },
)
_sym_db.RegisterMessage(InlineSource)

ImportTaxonomiesResponse = _reflection.GeneratedProtocolMessageType(
    "ImportTaxonomiesResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _IMPORTTAXONOMIESRESPONSE,
        "__module__": "google.cloud.datacatalog_v1beta1.proto.policytagmanagerserialization_pb2",
        "__doc__": """Response message for [ImportTaxonomies][google.cloud.datacatalog.v1bet
  a1.PolicyTagManagerSerialization.ImportTaxonomies].
  Attributes:
      taxonomies:
          Taxonomies that were imported.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.datacatalog.v1beta1.ImportTaxonomiesResponse)
    },
)
_sym_db.RegisterMessage(ImportTaxonomiesResponse)

ExportTaxonomiesRequest = _reflection.GeneratedProtocolMessageType(
    "ExportTaxonomiesRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _EXPORTTAXONOMIESREQUEST,
        "__module__": "google.cloud.datacatalog_v1beta1.proto.policytagmanagerserialization_pb2",
        "__doc__": """Request message for [ExportTaxonomies][google.cloud.datacatalog.v1beta
  1.PolicyTagManagerSerialization.ExportTaxonomies].
  Attributes:
      parent:
          Required. Resource name of the project that taxonomies to be
          exported will share.
      taxonomies:
          Required. Resource names of the taxonomies to be exported.
      destination:
          Required. Taxonomies export destination.
      serialized_taxonomies:
          Export taxonomies as serialized taxonomies.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.datacatalog.v1beta1.ExportTaxonomiesRequest)
    },
)
_sym_db.RegisterMessage(ExportTaxonomiesRequest)

ExportTaxonomiesResponse = _reflection.GeneratedProtocolMessageType(
    "ExportTaxonomiesResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _EXPORTTAXONOMIESRESPONSE,
        "__module__": "google.cloud.datacatalog_v1beta1.proto.policytagmanagerserialization_pb2",
        "__doc__": """Response message for [ExportTaxonomies][google.cloud.datacatalog.v1bet
  a1.PolicyTagManagerSerialization.ExportTaxonomies].
  Attributes:
      taxonomies:
          List of taxonomies and policy tags in a tree structure.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.datacatalog.v1beta1.ExportTaxonomiesResponse)
    },
)
_sym_db.RegisterMessage(ExportTaxonomiesResponse)


DESCRIPTOR._options = None
_SERIALIZEDTAXONOMY.fields_by_name["display_name"]._options = None
_SERIALIZEDPOLICYTAG.fields_by_name["display_name"]._options = None
_IMPORTTAXONOMIESREQUEST.fields_by_name["parent"]._options = None
_INLINESOURCE.fields_by_name["taxonomies"]._options = None
_EXPORTTAXONOMIESREQUEST.fields_by_name["parent"]._options = None
_EXPORTTAXONOMIESREQUEST.fields_by_name["taxonomies"]._options = None

_POLICYTAGMANAGERSERIALIZATION = _descriptor.ServiceDescriptor(
    name="PolicyTagManagerSerialization",
    full_name="google.cloud.datacatalog.v1beta1.PolicyTagManagerSerialization",
    file=DESCRIPTOR,
    index=0,
    serialized_options=b"\312A\032datacatalog.googleapis.com\322A.https://www.googleapis.com/auth/cloud-platform",
    create_key=_descriptor._internal_create_key,
    serialized_start=1283,
    serialized_end=1813,
    methods=[
        _descriptor.MethodDescriptor(
            name="ImportTaxonomies",
            full_name="google.cloud.datacatalog.v1beta1.PolicyTagManagerSerialization.ImportTaxonomies",
            index=0,
            containing_service=None,
            input_type=_IMPORTTAXONOMIESREQUEST,
            output_type=_IMPORTTAXONOMIESRESPONSE,
            serialized_options=b'\202\323\344\223\002?":/v1beta1/{parent=projects/*/locations/*}/taxonomies:import:\001*',
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="ExportTaxonomies",
            full_name="google.cloud.datacatalog.v1beta1.PolicyTagManagerSerialization.ExportTaxonomies",
            index=1,
            containing_service=None,
            input_type=_EXPORTTAXONOMIESREQUEST,
            output_type=_EXPORTTAXONOMIESRESPONSE,
            serialized_options=b"\202\323\344\223\002<\022:/v1beta1/{parent=projects/*/locations/*}/taxonomies:export",
            create_key=_descriptor._internal_create_key,
        ),
    ],
)
_sym_db.RegisterServiceDescriptor(_POLICYTAGMANAGERSERIALIZATION)

DESCRIPTOR.services_by_name[
    "PolicyTagManagerSerialization"
] = _POLICYTAGMANAGERSERIALIZATION

# @@protoc_insertion_point(module_scope)
