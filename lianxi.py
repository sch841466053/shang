from spyne import Application ,rpc,ServiceBase,Iterable, Integer, Unicode
from spyne.server.wsgi import WsgiApplication
from spyne.protocol.soap import Soap11


class HelloWorldService(ServiceBase):
    @rpc(Unicode, Integer, _returns=Iterable(Unicode))
    def say_hello(ctx, name, times):
        for i in range(times):
            yield "Hello,%s" % name


application = Application([HelloWorldService], tns="spyne.example.hello",
                          in_protocol=Soap11(validator="lxml"),out_protocol=Soap11())
if __name__ == '__main__':


    print(123)
    print(456)

    print(897)

    print("zaigognsi")

    from wsgiref.simple_server import make_server
    wsgi_app = WsgiApplication(application)
    server = make_server("127.0.0.1", 8000, wsgi_app)
    server.serve_forever()
    
