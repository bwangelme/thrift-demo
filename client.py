import sys
sys.path.append('./genpy')

from genpy.tutorial import Calculator
from genpy.tutorial.ttypes import InvalidOperation, Operation, Work, GreetArg

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol


def ping(client):
    client.ping()
    print('ping()')


def add(client, arg1=-2, arg2=-1):
    sum_ = client.add(arg1, arg2)
    print('(%d) + (%d) =%d' % (arg1, arg2, sum_))


def divide_0(client):
    work = Work()
    work.op = Operation.DIVIDE
    work.num1 = -2
    work.num2 = 0

    try:
        quotient = client.calculate(1, work)
        print('Whoa? You know how to divide by zero?')
        print('FYI the answer is %d' % quotient)
    except InvalidOperation as e:
        print('InvalidOperation: %r' % e)


def subtract(client):
    work = Work()
    work.op = Operation.SUBTRACT
    work.num1 = 15
    work.num2 = 10

    diff = client.calculate(1, work)
    print('15-10=%d' % diff)


def log(client):
    log = client.getStruct(1)
    print('Check log: %s' % log.value)


def wwork(client, type_):
    try:
        client.wwork(type_)
    except InvalidOperation:
        print("wwork exception")
        return

    print("wwork normal")


def greet(client):
    arg = GreetArg(num1=-1, num2=-2, msg="abc")
    client.greet(arg)


def main():
    # Make socket
    transport = TSocket.TSocket('localhost', 9090)
    # Buffering is critical. Raw sockets are very slow
    transport = TTransport.TFramedTransport(transport)
    # Wrap in a protocol
    protocol = TBinaryProtocol.TBinaryProtocol(transport)
    # Create a client to use the protocol encoder
    client = Calculator.Client(protocol)
    # Connect!
    transport.open()

    greet(client)

    # Close!
    transport.close()


if __name__ == '__main__':
    main()
