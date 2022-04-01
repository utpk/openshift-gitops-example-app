import http.server
import socketserver
import os
from http import HTTPStatus

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(HTTPStatus.OK)
        self.end_headers()
        self.wfile.write(os.environ.get('HTML_TEXT','<h1>Hello World</h1>'))

httpd = socketserver.TCPServer(('', 8080), Handler)
httpd.serve_forever()
