# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: PersonalizedProperty.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='PersonalizedProperty.proto',
  package='PersonalizedProperty',
  syntax='proto2',
  serialized_options=_b('\n-com.zillow.mobile.webservices.personalizationB\024PersonalizedProperty\242\002\024ProtobufPersonalized'),
  serialized_pb=_b('\n\x1aPersonalizedProperty.proto\x12\x14PersonalizedProperty\"/\n\rPropertyState\x12\x0e\n\x06viewed\x18\x01 \x01(\x08\x12\x0e\n\x06hidden\x18\x02 \x01(\x08\x42\\\n-com.zillow.mobile.webservices.personalizationB\x14PersonalizedProperty\xa2\x02\x14ProtobufPersonalized')
)




_PROPERTYSTATE = _descriptor.Descriptor(
  name='PropertyState',
  full_name='PersonalizedProperty.PropertyState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='viewed', full_name='PersonalizedProperty.PropertyState.viewed', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hidden', full_name='PersonalizedProperty.PropertyState.hidden', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=52,
  serialized_end=99,
)

DESCRIPTOR.message_types_by_name['PropertyState'] = _PROPERTYSTATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PropertyState = _reflection.GeneratedProtocolMessageType('PropertyState', (_message.Message,), dict(
  DESCRIPTOR = _PROPERTYSTATE,
  __module__ = 'PersonalizedProperty_pb2'
  # @@protoc_insertion_point(class_scope:PersonalizedProperty.PropertyState)
  ))
_sym_db.RegisterMessage(PropertyState)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
