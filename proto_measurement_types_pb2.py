# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto_measurement_types.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto_measurement_types.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1dproto_measurement_types.proto*\x9e\x07\n\x0fMeasurementType\x12\x1e\n\x1aMEASUREMENT_TYPE_NO_SENSOR\x10\x00\x12 \n\x1cMEASUREMENT_TYPE_TEMPERATURE\x10\x01\x12\x1d\n\x19MEASUREMENT_TYPE_HUMIDITY\x10\x02\x12)\n%MEASUREMENT_TYPE_ATMOSPHERIC_PRESSURE\x10\x03\x12*\n&MEASUREMENT_TYPE_DIFFERENTIAL_PRESSURE\x10\x04\x12\x1d\n\x19MEASUREMENT_TYPE_OK_ALARM\x10\x05\x12\x18\n\x14MEASUREMENT_TYPE_IAQ\x10\x06\x12\x1d\n\x19MEASUREMENT_TYPE_FLOODING\x10\x07\x12\x1e\n\x1aMEASUREMENT_TYPE_PULSE_CNT\x10\x08\x12&\n\"MEASUREMENT_TYPE_ELECTRICITY_METER\x10\t\x12 \n\x1cMEASUREMENT_TYPE_WATER_METER\x10\n\x12\"\n\x1eMEASUREMENT_TYPE_SOIL_MOISTURE\x10\x0b\x12\x1b\n\x17MEASUREMENT_TYPE_CO_GAS\x10\x0c\x12\x1c\n\x18MEASUREMENT_TYPE_NO2_GAS\x10\r\x12\x1c\n\x18MEASUREMENT_TYPE_H2S_GAS\x10\x0e\x12\"\n\x1eMEASUREMENT_TYPE_AMBIENT_LIGHT\x10\x0f\x12\x1b\n\x17MEASUREMENT_TYPE_PM_1_0\x10\x10\x12\x1b\n\x17MEASUREMENT_TYPE_PM_2_5\x10\x11\x12\x1c\n\x18MEASUREMENT_TYPE_PM_10_0\x10\x12\x12 \n\x1cMEASUREMENT_TYPE_NOISE_LEVEL\x10\x13\x12\x1c\n\x18MEASUREMENT_TYPE_NH3_GAS\x10\x14\x12\x1c\n\x18MEASUREMENT_TYPE_CH4_GAS\x10\x15\x12\"\n\x1eMEASUREMENT_TYPE_HIGH_PRESSURE\x10\x16\x12 \n\x1cMEASUREMENT_TYPE_DISTANCE_MM\x10\x17\x12*\n&MEASUREMENT_TYPE_WATER_METER_ACC_MINOR\x10\x18\x12*\n&MEASUREMENT_TYPE_WATER_METER_ACC_MAJOR\x10\x19\x12\x1c\n\x18MEASUREMENT_TYPE_CO2_GAS\x10\x1a\x62\x06proto3'
)

_MEASUREMENTTYPE = _descriptor.EnumDescriptor(
  name='MeasurementType',
  full_name='MeasurementType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='MEASUREMENT_TYPE_NO_SENSOR', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MEASUREMENT_TYPE_TEMPERATURE', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MEASUREMENT_TYPE_HUMIDITY', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MEASUREMENT_TYPE_ATMOSPHERIC_PRESSURE', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MEASUREMENT_TYPE_DIFFERENTIAL_PRESSURE', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MEASUREMENT_TYPE_OK_ALARM', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MEASUREMENT_TYPE_IAQ', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MEASUREMENT_TYPE_FLOODING', index=7, number=7,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MEASUREMENT_TYPE_PULSE_CNT', index=8, number=8,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MEASUREMENT_TYPE_ELECTRICITY_METER', index=9, number=9,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MEASUREMENT_TYPE_WATER_METER', index=10, number=10,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MEASUREMENT_TYPE_SOIL_MOISTURE', index=11, number=11,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MEASUREMENT_TYPE_CO_GAS', index=12, number=12,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MEASUREMENT_TYPE_NO2_GAS', index=13, number=13,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MEASUREMENT_TYPE_H2S_GAS', index=14, number=14,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MEASUREMENT_TYPE_AMBIENT_LIGHT', index=15, number=15,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MEASUREMENT_TYPE_PM_1_0', index=16, number=16,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MEASUREMENT_TYPE_PM_2_5', index=17, number=17,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MEASUREMENT_TYPE_PM_10_0', index=18, number=18,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MEASUREMENT_TYPE_NOISE_LEVEL', index=19, number=19,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MEASUREMENT_TYPE_NH3_GAS', index=20, number=20,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MEASUREMENT_TYPE_CH4_GAS', index=21, number=21,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MEASUREMENT_TYPE_HIGH_PRESSURE', index=22, number=22,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MEASUREMENT_TYPE_DISTANCE_MM', index=23, number=23,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MEASUREMENT_TYPE_WATER_METER_ACC_MINOR', index=24, number=24,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MEASUREMENT_TYPE_WATER_METER_ACC_MAJOR', index=25, number=25,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MEASUREMENT_TYPE_CO2_GAS', index=26, number=26,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=34,
  serialized_end=960,
)
_sym_db.RegisterEnumDescriptor(_MEASUREMENTTYPE)

MeasurementType = enum_type_wrapper.EnumTypeWrapper(_MEASUREMENTTYPE)
MEASUREMENT_TYPE_NO_SENSOR = 0
MEASUREMENT_TYPE_TEMPERATURE = 1
MEASUREMENT_TYPE_HUMIDITY = 2
MEASUREMENT_TYPE_ATMOSPHERIC_PRESSURE = 3
MEASUREMENT_TYPE_DIFFERENTIAL_PRESSURE = 4
MEASUREMENT_TYPE_OK_ALARM = 5
MEASUREMENT_TYPE_IAQ = 6
MEASUREMENT_TYPE_FLOODING = 7
MEASUREMENT_TYPE_PULSE_CNT = 8
MEASUREMENT_TYPE_ELECTRICITY_METER = 9
MEASUREMENT_TYPE_WATER_METER = 10
MEASUREMENT_TYPE_SOIL_MOISTURE = 11
MEASUREMENT_TYPE_CO_GAS = 12
MEASUREMENT_TYPE_NO2_GAS = 13
MEASUREMENT_TYPE_H2S_GAS = 14
MEASUREMENT_TYPE_AMBIENT_LIGHT = 15
MEASUREMENT_TYPE_PM_1_0 = 16
MEASUREMENT_TYPE_PM_2_5 = 17
MEASUREMENT_TYPE_PM_10_0 = 18
MEASUREMENT_TYPE_NOISE_LEVEL = 19
MEASUREMENT_TYPE_NH3_GAS = 20
MEASUREMENT_TYPE_CH4_GAS = 21
MEASUREMENT_TYPE_HIGH_PRESSURE = 22
MEASUREMENT_TYPE_DISTANCE_MM = 23
MEASUREMENT_TYPE_WATER_METER_ACC_MINOR = 24
MEASUREMENT_TYPE_WATER_METER_ACC_MAJOR = 25
MEASUREMENT_TYPE_CO2_GAS = 26


DESCRIPTOR.enum_types_by_name['MeasurementType'] = _MEASUREMENTTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


# @@protoc_insertion_point(module_scope)
