from message.api import MessageService
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = 'wsws0521@163.com'
authCode = '0521wsws'
class MessageServiceHandler:
    def sendMobileMessage(self, mobile, message):
        print("sendMobileMessage, mobile:" + mobile + ", message:" + message)
        return True

    def sendEmailMessage(self, email, message):
        print("sendEmailMessage, email:" + email + ", message:" + message)
        messageObj = MIMEText(message, "plain", "utf-8")
        messageObj['from'] =
        return True


if __name__ == '__main__':
    handler = MessageServiceHandler()
    processor = MessageService.Processor(handler)

    """监听者"""
    transport = TSocket.TServerSocket('localhost', '9090')
    """传输方式：帧传输"""
    tfactory = TTransport.TFramedTransportFactory()
    """传输协议：二进制传输"""
    pfactory = TBinaryProtocol.TBinaryProtocolFactory

    """创建 server"""
    server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)
    print("python thrift server start")
    server.serve()
    print("python thrift server exit")



