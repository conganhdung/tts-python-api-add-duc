from cgitb import handler
import http.server
import socketserver

class myhandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self) :
        if self.path == '/myotherpage':
            self.path = 'myotherpage.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

PORT = 8000
handler  = myhandler
apiserver = socketserver.TCPServer(("",PORT), handler)
print("Server Started at PORT" + str(PORT))
apiserver.serve_forever()