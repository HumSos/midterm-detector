# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: src/pycam/proto/PositionService.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%src/pycam/proto/PositionService.proto\x12\x0fobject_position\"\x07\n\x05\x45mpty\"3\n\x08Position\x12\t\n\x01x\x18\x01 \x01(\x01\x12\t\n\x01y\x18\x02 \x01(\x01\x12\x11\n\ttimestamp\x18\x03 \x01(\x03\x32T\n\x0fPositionService\x12\x41\n\x0cSendPosition\x12\x16.object_position.Empty\x1a\x19.object_position.Positionb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'src.pycam.proto.PositionService_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _EMPTY._serialized_start=58
  _EMPTY._serialized_end=65
  _POSITION._serialized_start=67
  _POSITION._serialized_end=118
  _POSITIONSERVICE._serialized_start=120
  _POSITIONSERVICE._serialized_end=204
# @@protoc_insertion_point(module_scope)
