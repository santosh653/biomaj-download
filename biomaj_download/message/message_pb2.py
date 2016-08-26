# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: message.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='message.proto',
  package='biomaj',
  serialized_pb=_b('\n\rmessage.proto\x12\x06\x62iomaj\"\x83\x08\n\x0c\x44ownloadFile\x12\x0c\n\x04\x62\x61nk\x18\x01 \x02(\t\x12\x0f\n\x07session\x18\x02 \x02(\t\x12\x11\n\tlocal_dir\x18\x03 \x02(\t\x12\x18\n\x10timeout_download\x18\x04 \x01(\x05\x12\x34\n\x0bremote_file\x18\x05 \x02(\x0b\x32\x1f.biomaj.DownloadFile.RemoteFile\x12)\n\x05proxy\x18\x06 \x01(\x0b\x32\x1a.biomaj.DownloadFile.Proxy\x1a$\n\x05Param\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\r\n\x05value\x18\x02 \x02(\t\x1a\xa7\x01\n\tHttpParse\x12\x10\n\x08\x64ir_line\x18\x01 \x02(\t\x12\x11\n\tfile_line\x18\x02 \x02(\t\x12\x10\n\x08\x64ir_name\x18\x03 \x02(\x05\x12\x10\n\x08\x64ir_date\x18\x04 \x02(\x05\x12\x11\n\tfile_name\x18\x05 \x02(\x05\x12\x11\n\tfile_date\x18\x06 \x02(\x05\x12\x18\n\x10\x66ile_date_format\x18\x07 \x01(\t\x12\x11\n\tfile_size\x18\x08 \x02(\x05\x1aj\n\x04\x46ile\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x0c\n\x04root\x18\x02 \x01(\t\x12\x0f\n\x07save_as\x18\x03 \x01(\t\x12\x0b\n\x03url\x18\x04 \x01(\t\x12\x0c\n\x04year\x18\x05 \x01(\x05\x12\r\n\x05month\x18\x06 \x01(\x05\x12\x0b\n\x03\x64\x61y\x18\x07 \x01(\x05\x1a\xcc\x02\n\nRemoteFile\x12(\n\x05\x66iles\x18\x01 \x03(\x0b\x32\x19.biomaj.DownloadFile.File\x12/\n\x08protocol\x18\x02 \x02(\x0e\x32\x1d.biomaj.DownloadFile.Protocol\x12\x0e\n\x06server\x18\x03 \x02(\t\x12\x12\n\nremote_dir\x18\x04 \x02(\t\x12\x0f\n\x07save_as\x18\x05 \x01(\t\x12)\n\x05param\x18\x06 \x03(\x0b\x32\x1a.biomaj.DownloadFile.Param\x12\x32\n\nhttp_parse\x18\x07 \x01(\x0b\x32\x1e.biomaj.DownloadFile.HttpParse\x12:\n\x0bhttp_method\x18\x08 \x01(\x0e\x32 .biomaj.DownloadFile.HTTP_METHOD:\x03GET\x12\x13\n\x0b\x63redentials\x18\t \x01(\t\x1a*\n\x05Proxy\x12\r\n\x05proxy\x18\x01 \x02(\t\x12\x12\n\nproxy_auth\x18\x02 \x01(\t\"m\n\x08Protocol\x12\x07\n\x03\x46TP\x10\x00\x12\x08\n\x04SFTP\x10\x01\x12\x08\n\x04HTTP\x10\x02\x12\t\n\x05HTTPS\x10\x03\x12\r\n\tDIRECTFTP\x10\x04\x12\x0e\n\nDIRECTHTTP\x10\x05\x12\x0f\n\x0b\x44IRECTHTTPS\x10\x06\x12\t\n\x05LOCAL\x10\x07\" \n\x0bHTTP_METHOD\x12\x07\n\x03GET\x10\x00\x12\x08\n\x04POST\x10\x01')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_DOWNLOADFILE_PROTOCOL = _descriptor.EnumDescriptor(
  name='Protocol',
  full_name='biomaj.DownloadFile.Protocol',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='FTP', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SFTP', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HTTP', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HTTPS', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DIRECTFTP', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DIRECTHTTP', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DIRECTHTTPS', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LOCAL', index=7, number=7,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=910,
  serialized_end=1019,
)
_sym_db.RegisterEnumDescriptor(_DOWNLOADFILE_PROTOCOL)

_DOWNLOADFILE_HTTP_METHOD = _descriptor.EnumDescriptor(
  name='HTTP_METHOD',
  full_name='biomaj.DownloadFile.HTTP_METHOD',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='GET', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POST', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1021,
  serialized_end=1053,
)
_sym_db.RegisterEnumDescriptor(_DOWNLOADFILE_HTTP_METHOD)


_DOWNLOADFILE_PARAM = _descriptor.Descriptor(
  name='Param',
  full_name='biomaj.DownloadFile.Param',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='biomaj.DownloadFile.Param.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='biomaj.DownloadFile.Param.value', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=215,
  serialized_end=251,
)

_DOWNLOADFILE_HTTPPARSE = _descriptor.Descriptor(
  name='HttpParse',
  full_name='biomaj.DownloadFile.HttpParse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dir_line', full_name='biomaj.DownloadFile.HttpParse.dir_line', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='file_line', full_name='biomaj.DownloadFile.HttpParse.file_line', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dir_name', full_name='biomaj.DownloadFile.HttpParse.dir_name', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dir_date', full_name='biomaj.DownloadFile.HttpParse.dir_date', index=3,
      number=4, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='file_name', full_name='biomaj.DownloadFile.HttpParse.file_name', index=4,
      number=5, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='file_date', full_name='biomaj.DownloadFile.HttpParse.file_date', index=5,
      number=6, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='file_date_format', full_name='biomaj.DownloadFile.HttpParse.file_date_format', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='file_size', full_name='biomaj.DownloadFile.HttpParse.file_size', index=7,
      number=8, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=254,
  serialized_end=421,
)

_DOWNLOADFILE_FILE = _descriptor.Descriptor(
  name='File',
  full_name='biomaj.DownloadFile.File',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='biomaj.DownloadFile.File.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='root', full_name='biomaj.DownloadFile.File.root', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='save_as', full_name='biomaj.DownloadFile.File.save_as', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='url', full_name='biomaj.DownloadFile.File.url', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='year', full_name='biomaj.DownloadFile.File.year', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='month', full_name='biomaj.DownloadFile.File.month', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='day', full_name='biomaj.DownloadFile.File.day', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=423,
  serialized_end=529,
)

_DOWNLOADFILE_REMOTEFILE = _descriptor.Descriptor(
  name='RemoteFile',
  full_name='biomaj.DownloadFile.RemoteFile',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='files', full_name='biomaj.DownloadFile.RemoteFile.files', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='protocol', full_name='biomaj.DownloadFile.RemoteFile.protocol', index=1,
      number=2, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='server', full_name='biomaj.DownloadFile.RemoteFile.server', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='remote_dir', full_name='biomaj.DownloadFile.RemoteFile.remote_dir', index=3,
      number=4, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='save_as', full_name='biomaj.DownloadFile.RemoteFile.save_as', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='param', full_name='biomaj.DownloadFile.RemoteFile.param', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='http_parse', full_name='biomaj.DownloadFile.RemoteFile.http_parse', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='http_method', full_name='biomaj.DownloadFile.RemoteFile.http_method', index=7,
      number=8, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='credentials', full_name='biomaj.DownloadFile.RemoteFile.credentials', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=532,
  serialized_end=864,
)

_DOWNLOADFILE_PROXY = _descriptor.Descriptor(
  name='Proxy',
  full_name='biomaj.DownloadFile.Proxy',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='proxy', full_name='biomaj.DownloadFile.Proxy.proxy', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='proxy_auth', full_name='biomaj.DownloadFile.Proxy.proxy_auth', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=866,
  serialized_end=908,
)

_DOWNLOADFILE = _descriptor.Descriptor(
  name='DownloadFile',
  full_name='biomaj.DownloadFile',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='bank', full_name='biomaj.DownloadFile.bank', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='session', full_name='biomaj.DownloadFile.session', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='local_dir', full_name='biomaj.DownloadFile.local_dir', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='timeout_download', full_name='biomaj.DownloadFile.timeout_download', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='remote_file', full_name='biomaj.DownloadFile.remote_file', index=4,
      number=5, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='proxy', full_name='biomaj.DownloadFile.proxy', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_DOWNLOADFILE_PARAM, _DOWNLOADFILE_HTTPPARSE, _DOWNLOADFILE_FILE, _DOWNLOADFILE_REMOTEFILE, _DOWNLOADFILE_PROXY, ],
  enum_types=[
    _DOWNLOADFILE_PROTOCOL,
    _DOWNLOADFILE_HTTP_METHOD,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=26,
  serialized_end=1053,
)

_DOWNLOADFILE_PARAM.containing_type = _DOWNLOADFILE
_DOWNLOADFILE_HTTPPARSE.containing_type = _DOWNLOADFILE
_DOWNLOADFILE_FILE.containing_type = _DOWNLOADFILE
_DOWNLOADFILE_REMOTEFILE.fields_by_name['files'].message_type = _DOWNLOADFILE_FILE
_DOWNLOADFILE_REMOTEFILE.fields_by_name['protocol'].enum_type = _DOWNLOADFILE_PROTOCOL
_DOWNLOADFILE_REMOTEFILE.fields_by_name['param'].message_type = _DOWNLOADFILE_PARAM
_DOWNLOADFILE_REMOTEFILE.fields_by_name['http_parse'].message_type = _DOWNLOADFILE_HTTPPARSE
_DOWNLOADFILE_REMOTEFILE.fields_by_name['http_method'].enum_type = _DOWNLOADFILE_HTTP_METHOD
_DOWNLOADFILE_REMOTEFILE.containing_type = _DOWNLOADFILE
_DOWNLOADFILE_PROXY.containing_type = _DOWNLOADFILE
_DOWNLOADFILE.fields_by_name['remote_file'].message_type = _DOWNLOADFILE_REMOTEFILE
_DOWNLOADFILE.fields_by_name['proxy'].message_type = _DOWNLOADFILE_PROXY
_DOWNLOADFILE_PROTOCOL.containing_type = _DOWNLOADFILE
_DOWNLOADFILE_HTTP_METHOD.containing_type = _DOWNLOADFILE
DESCRIPTOR.message_types_by_name['DownloadFile'] = _DOWNLOADFILE

DownloadFile = _reflection.GeneratedProtocolMessageType('DownloadFile', (_message.Message,), dict(

  Param = _reflection.GeneratedProtocolMessageType('Param', (_message.Message,), dict(
    DESCRIPTOR = _DOWNLOADFILE_PARAM,
    __module__ = 'message_pb2'
    # @@protoc_insertion_point(class_scope:biomaj.DownloadFile.Param)
    ))
  ,

  HttpParse = _reflection.GeneratedProtocolMessageType('HttpParse', (_message.Message,), dict(
    DESCRIPTOR = _DOWNLOADFILE_HTTPPARSE,
    __module__ = 'message_pb2'
    # @@protoc_insertion_point(class_scope:biomaj.DownloadFile.HttpParse)
    ))
  ,

  File = _reflection.GeneratedProtocolMessageType('File', (_message.Message,), dict(
    DESCRIPTOR = _DOWNLOADFILE_FILE,
    __module__ = 'message_pb2'
    # @@protoc_insertion_point(class_scope:biomaj.DownloadFile.File)
    ))
  ,

  RemoteFile = _reflection.GeneratedProtocolMessageType('RemoteFile', (_message.Message,), dict(
    DESCRIPTOR = _DOWNLOADFILE_REMOTEFILE,
    __module__ = 'message_pb2'
    # @@protoc_insertion_point(class_scope:biomaj.DownloadFile.RemoteFile)
    ))
  ,

  Proxy = _reflection.GeneratedProtocolMessageType('Proxy', (_message.Message,), dict(
    DESCRIPTOR = _DOWNLOADFILE_PROXY,
    __module__ = 'message_pb2'
    # @@protoc_insertion_point(class_scope:biomaj.DownloadFile.Proxy)
    ))
  ,
  DESCRIPTOR = _DOWNLOADFILE,
  __module__ = 'message_pb2'
  # @@protoc_insertion_point(class_scope:biomaj.DownloadFile)
  ))
_sym_db.RegisterMessage(DownloadFile)
_sym_db.RegisterMessage(DownloadFile.Param)
_sym_db.RegisterMessage(DownloadFile.HttpParse)
_sym_db.RegisterMessage(DownloadFile.File)
_sym_db.RegisterMessage(DownloadFile.RemoteFile)
_sym_db.RegisterMessage(DownloadFile.Proxy)


# @@protoc_insertion_point(module_scope)
