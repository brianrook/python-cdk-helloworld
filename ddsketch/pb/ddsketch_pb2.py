# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ddsketch.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0e\x64\x64sketch.proto\"}\n\x08\x44\x44Sketch\x12\x1e\n\x07mapping\x18\x01 \x01(\x0b\x32\r.IndexMapping\x12\x1e\n\x0epositiveValues\x18\x02 \x01(\x0b\x32\x06.Store\x12\x1e\n\x0enegativeValues\x18\x03 \x01(\x0b\x32\x06.Store\x12\x11\n\tzeroCount\x18\x04 \x01(\x01\"\xa7\x01\n\x0cIndexMapping\x12\r\n\x05gamma\x18\x01 \x01(\x01\x12\x13\n\x0bindexOffset\x18\x02 \x01(\x01\x12\x32\n\rinterpolation\x18\x03 \x01(\x0e\x32\x1b.IndexMapping.Interpolation\"?\n\rInterpolation\x12\x08\n\x04NONE\x10\x00\x12\n\n\x06LINEAR\x10\x01\x12\r\n\tQUADRATIC\x10\x02\x12\t\n\x05\x43UBIC\x10\x03\"\xa6\x01\n\x05Store\x12(\n\tbinCounts\x18\x01 \x03(\x0b\x32\x15.Store.BinCountsEntry\x12\x1f\n\x13\x63ontiguousBinCounts\x18\x02 \x03(\x01\x42\x02\x10\x01\x12 \n\x18\x63ontiguousBinIndexOffset\x18\x03 \x01(\x11\x1a\x30\n\x0e\x42inCountsEntry\x12\x0b\n\x03key\x18\x01 \x01(\x11\x12\r\n\x05value\x18\x02 \x01(\x01:\x02\x38\x01\x62\x06proto3')



_DDSKETCH = DESCRIPTOR.message_types_by_name['DDSketch']
_INDEXMAPPING = DESCRIPTOR.message_types_by_name['IndexMapping']
_STORE = DESCRIPTOR.message_types_by_name['Store']
_STORE_BINCOUNTSENTRY = _STORE.nested_types_by_name['BinCountsEntry']
_INDEXMAPPING_INTERPOLATION = _INDEXMAPPING.enum_types_by_name['Interpolation']
DDSketch = _reflection.GeneratedProtocolMessageType('DDSketch', (_message.Message,), {
  'DESCRIPTOR' : _DDSKETCH,
  '__module__' : 'ddsketch_pb2'
  # @@protoc_insertion_point(class_scope:DDSketch)
  })
_sym_db.RegisterMessage(DDSketch)

IndexMapping = _reflection.GeneratedProtocolMessageType('IndexMapping', (_message.Message,), {
  'DESCRIPTOR' : _INDEXMAPPING,
  '__module__' : 'ddsketch_pb2'
  # @@protoc_insertion_point(class_scope:IndexMapping)
  })
_sym_db.RegisterMessage(IndexMapping)

Store = _reflection.GeneratedProtocolMessageType('Store', (_message.Message,), {

  'BinCountsEntry' : _reflection.GeneratedProtocolMessageType('BinCountsEntry', (_message.Message,), {
    'DESCRIPTOR' : _STORE_BINCOUNTSENTRY,
    '__module__' : 'ddsketch_pb2'
    # @@protoc_insertion_point(class_scope:Store.BinCountsEntry)
    })
  ,
  'DESCRIPTOR' : _STORE,
  '__module__' : 'ddsketch_pb2'
  # @@protoc_insertion_point(class_scope:Store)
  })
_sym_db.RegisterMessage(Store)
_sym_db.RegisterMessage(Store.BinCountsEntry)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _STORE_BINCOUNTSENTRY._options = None
  _STORE_BINCOUNTSENTRY._serialized_options = b'8\001'
  _STORE.fields_by_name['contiguousBinCounts']._options = None
  _STORE.fields_by_name['contiguousBinCounts']._serialized_options = b'\020\001'
  _DDSKETCH._serialized_start=18
  _DDSKETCH._serialized_end=143
  _INDEXMAPPING._serialized_start=146
  _INDEXMAPPING._serialized_end=313
  _INDEXMAPPING_INTERPOLATION._serialized_start=250
  _INDEXMAPPING_INTERPOLATION._serialized_end=313
  _STORE._serialized_start=316
  _STORE._serialized_end=482
  _STORE_BINCOUNTSENTRY._serialized_start=434
  _STORE_BINCOUNTSENTRY._serialized_end=482
# @@protoc_insertion_point(module_scope)