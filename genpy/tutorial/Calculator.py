#
# Autogenerated by Thrift Compiler (0.16.0)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TFrozenDict, TException, TApplicationException
from thrift.protocol.TProtocol import TProtocolException
from thrift.TRecursive import fix_spec

import sys
import shared.SharedService
import logging
from .ttypes import *
from thrift.Thrift import TProcessor
from thrift.transport import TTransport
all_structs = []


class Iface(shared.SharedService.Iface):
    """
    Ahh, now onto the cool part, defining a service. Services just need a name
    and can optionally inherit from another service using the extends keyword.

    """
    def ping(self):
        """
        A method definition looks like C code. It has a return type, arguments,
        and optionally a list of exceptions that it may throw. Note that argument
        lists and exception lists are specified using the exact same syntax as
        field lists in struct or exception definitions.

        """
        pass

    def add(self, num1, num2):
        """
        Parameters:
         - num1
         - num2

        """
        pass

    def calculate(self, logid, w):
        """
        Parameters:
         - logid
         - w

        """
        pass

    def wwork(self, type):
        """
        Parameters:
         - type

        """
        pass

    def greet(self, arg):
        """
        Parameters:
         - arg

        """
        pass

    def zip(self):
        """
        This method has a oneway modifier. That means the client only makes
        a request and does not listen for any response at all. Oneway methods
        must be void.

        """
        pass


class Client(shared.SharedService.Client, Iface):
    """
    Ahh, now onto the cool part, defining a service. Services just need a name
    and can optionally inherit from another service using the extends keyword.

    """
    def __init__(self, iprot, oprot=None):
        shared.SharedService.Client.__init__(self, iprot, oprot)

    def ping(self):
        """
        A method definition looks like C code. It has a return type, arguments,
        and optionally a list of exceptions that it may throw. Note that argument
        lists and exception lists are specified using the exact same syntax as
        field lists in struct or exception definitions.

        """
        self.send_ping()
        self.recv_ping()

    def send_ping(self):
        self._oprot.writeMessageBegin('ping', TMessageType.CALL, self._seqid)
        args = ping_args()
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_ping(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = ping_result()
        result.read(iprot)
        iprot.readMessageEnd()
        return

    def add(self, num1, num2):
        """
        Parameters:
         - num1
         - num2

        """
        self.send_add(num1, num2)
        return self.recv_add()

    def send_add(self, num1, num2):
        self._oprot.writeMessageBegin('add', TMessageType.CALL, self._seqid)
        args = add_args()
        args.num1 = num1
        args.num2 = num2
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_add(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = add_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        raise TApplicationException(TApplicationException.MISSING_RESULT, "add failed: unknown result")

    def calculate(self, logid, w):
        """
        Parameters:
         - logid
         - w

        """
        self.send_calculate(logid, w)
        return self.recv_calculate()

    def send_calculate(self, logid, w):
        self._oprot.writeMessageBegin('calculate', TMessageType.CALL, self._seqid)
        args = calculate_args()
        args.logid = logid
        args.w = w
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_calculate(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = calculate_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.ouch is not None:
            raise result.ouch
        raise TApplicationException(TApplicationException.MISSING_RESULT, "calculate failed: unknown result")

    def wwork(self, type):
        """
        Parameters:
         - type

        """
        self.send_wwork(type)
        return self.recv_wwork()

    def send_wwork(self, type):
        self._oprot.writeMessageBegin('wwork', TMessageType.CALL, self._seqid)
        args = wwork_args()
        args.type = type
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_wwork(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = wwork_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.ouch is not None:
            raise result.ouch
        raise TApplicationException(TApplicationException.MISSING_RESULT, "wwork failed: unknown result")

    def greet(self, arg):
        """
        Parameters:
         - arg

        """
        self.send_greet(arg)
        self.recv_greet()

    def send_greet(self, arg):
        self._oprot.writeMessageBegin('greet', TMessageType.CALL, self._seqid)
        args = greet_args()
        args.arg = arg
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_greet(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = greet_result()
        result.read(iprot)
        iprot.readMessageEnd()
        return

    def zip(self):
        """
        This method has a oneway modifier. That means the client only makes
        a request and does not listen for any response at all. Oneway methods
        must be void.

        """
        self.send_zip()

    def send_zip(self):
        self._oprot.writeMessageBegin('zip', TMessageType.ONEWAY, self._seqid)
        args = zip_args()
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()


class Processor(shared.SharedService.Processor, Iface, TProcessor):
    def __init__(self, handler):
        shared.SharedService.Processor.__init__(self, handler)
        self._processMap["ping"] = Processor.process_ping
        self._processMap["add"] = Processor.process_add
        self._processMap["calculate"] = Processor.process_calculate
        self._processMap["wwork"] = Processor.process_wwork
        self._processMap["greet"] = Processor.process_greet
        self._processMap["zip"] = Processor.process_zip
        self._on_message_begin = None

    def on_message_begin(self, func):
        self._on_message_begin = func

    def process(self, iprot, oprot):
        (name, type, seqid) = iprot.readMessageBegin()
        if self._on_message_begin:
            self._on_message_begin(name, type, seqid)
        if name not in self._processMap:
            iprot.skip(TType.STRUCT)
            iprot.readMessageEnd()
            x = TApplicationException(TApplicationException.UNKNOWN_METHOD, 'Unknown function %s' % (name))
            oprot.writeMessageBegin(name, TMessageType.EXCEPTION, seqid)
            x.write(oprot)
            oprot.writeMessageEnd()
            oprot.trans.flush()
            return
        else:
            self._processMap[name](self, seqid, iprot, oprot)
        return True

    def process_ping(self, seqid, iprot, oprot):
        args = ping_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = ping_result()
        try:
            self._handler.ping()
            msg_type = TMessageType.REPLY
        except TTransport.TTransportException:
            raise
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("ping", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_add(self, seqid, iprot, oprot):
        args = add_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = add_result()
        try:
            result.success = self._handler.add(args.num1, args.num2)
            msg_type = TMessageType.REPLY
        except TTransport.TTransportException:
            raise
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("add", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_calculate(self, seqid, iprot, oprot):
        args = calculate_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = calculate_result()
        try:
            result.success = self._handler.calculate(args.logid, args.w)
            msg_type = TMessageType.REPLY
        except TTransport.TTransportException:
            raise
        except InvalidOperation as ouch:
            msg_type = TMessageType.REPLY
            result.ouch = ouch
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("calculate", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_wwork(self, seqid, iprot, oprot):
        args = wwork_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = wwork_result()
        try:
            result.success = self._handler.wwork(args.type)
            msg_type = TMessageType.REPLY
        except TTransport.TTransportException:
            raise
        except InvalidOperation as ouch:
            msg_type = TMessageType.REPLY
            result.ouch = ouch
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("wwork", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_greet(self, seqid, iprot, oprot):
        args = greet_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = greet_result()
        try:
            self._handler.greet(args.arg)
            msg_type = TMessageType.REPLY
        except TTransport.TTransportException:
            raise
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("greet", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_zip(self, seqid, iprot, oprot):
        args = zip_args()
        args.read(iprot)
        iprot.readMessageEnd()
        try:
            self._handler.zip()
        except TTransport.TTransportException:
            raise
        except Exception:
            logging.exception('Exception in oneway handler')

# HELPER FUNCTIONS AND STRUCTURES


class ping_args(object):


    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('ping_args')
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(ping_args)
ping_args.thrift_spec = (
)


class ping_result(object):


    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('ping_result')
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(ping_result)
ping_result.thrift_spec = (
)


class add_args(object):
    """
    Attributes:
     - num1
     - num2

    """


    def __init__(self, num1=None, num2=None,):
        self.num1 = num1
        self.num2 = num2

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I32:
                    self.num1 = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.num2 = iprot.readI32()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('add_args')
        if self.num1 is not None:
            oprot.writeFieldBegin('num1', TType.I32, 1)
            oprot.writeI32(self.num1)
            oprot.writeFieldEnd()
        if self.num2 is not None:
            oprot.writeFieldBegin('num2', TType.I32, 2)
            oprot.writeI32(self.num2)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(add_args)
add_args.thrift_spec = (
    None,  # 0
    (1, TType.I32, 'num1', None, None, ),  # 1
    (2, TType.I32, 'num2', None, None, ),  # 2
)


class add_result(object):
    """
    Attributes:
     - success

    """


    def __init__(self, success=None,):
        self.success = success

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.I32:
                    self.success = iprot.readI32()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('add_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.I32, 0)
            oprot.writeI32(self.success)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(add_result)
add_result.thrift_spec = (
    (0, TType.I32, 'success', None, None, ),  # 0
)


class calculate_args(object):
    """
    Attributes:
     - logid
     - w

    """


    def __init__(self, logid=None, w=None,):
        self.logid = logid
        self.w = w

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I32:
                    self.logid = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRUCT:
                    self.w = Work()
                    self.w.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('calculate_args')
        if self.logid is not None:
            oprot.writeFieldBegin('logid', TType.I32, 1)
            oprot.writeI32(self.logid)
            oprot.writeFieldEnd()
        if self.w is not None:
            oprot.writeFieldBegin('w', TType.STRUCT, 2)
            self.w.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(calculate_args)
calculate_args.thrift_spec = (
    None,  # 0
    (1, TType.I32, 'logid', None, None, ),  # 1
    (2, TType.STRUCT, 'w', [Work, None], None, ),  # 2
)


class calculate_result(object):
    """
    Attributes:
     - success
     - ouch

    """


    def __init__(self, success=None, ouch=None,):
        self.success = success
        self.ouch = ouch

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.I32:
                    self.success = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.ouch = InvalidOperation.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('calculate_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.I32, 0)
            oprot.writeI32(self.success)
            oprot.writeFieldEnd()
        if self.ouch is not None:
            oprot.writeFieldBegin('ouch', TType.STRUCT, 1)
            self.ouch.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(calculate_result)
calculate_result.thrift_spec = (
    (0, TType.I32, 'success', None, None, ),  # 0
    (1, TType.STRUCT, 'ouch', [InvalidOperation, None], None, ),  # 1
)


class wwork_args(object):
    """
    Attributes:
     - type

    """


    def __init__(self, type=None,):
        self.type = type

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I32:
                    self.type = iprot.readI32()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('wwork_args')
        if self.type is not None:
            oprot.writeFieldBegin('type', TType.I32, 1)
            oprot.writeI32(self.type)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(wwork_args)
wwork_args.thrift_spec = (
    None,  # 0
    (1, TType.I32, 'type', None, None, ),  # 1
)


class wwork_result(object):
    """
    Attributes:
     - success
     - ouch

    """


    def __init__(self, success=None, ouch=None,):
        self.success = success
        self.ouch = ouch

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.STRUCT:
                    self.success = Work()
                    self.success.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.ouch = InvalidOperation.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('wwork_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.STRUCT, 0)
            self.success.write(oprot)
            oprot.writeFieldEnd()
        if self.ouch is not None:
            oprot.writeFieldBegin('ouch', TType.STRUCT, 1)
            self.ouch.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(wwork_result)
wwork_result.thrift_spec = (
    (0, TType.STRUCT, 'success', [Work, None], None, ),  # 0
    (1, TType.STRUCT, 'ouch', [InvalidOperation, None], None, ),  # 1
)


class greet_args(object):
    """
    Attributes:
     - arg

    """


    def __init__(self, arg=None,):
        self.arg = arg

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRUCT:
                    self.arg = GreetArg()
                    self.arg.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('greet_args')
        if self.arg is not None:
            oprot.writeFieldBegin('arg', TType.STRUCT, 1)
            self.arg.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(greet_args)
greet_args.thrift_spec = (
    None,  # 0
    (1, TType.STRUCT, 'arg', [GreetArg, None], None, ),  # 1
)


class greet_result(object):


    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('greet_result')
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(greet_result)
greet_result.thrift_spec = (
)


class zip_args(object):


    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('zip_args')
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(zip_args)
zip_args.thrift_spec = (
)
fix_spec(all_structs)
del all_structs
