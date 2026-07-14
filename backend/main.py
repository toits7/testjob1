from http.server import BaseHTTPRequestHandler, HTTPServer
import os
import sys

class MyHttpHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'Hello from Effective Mobile!\n')
        else:
            self.send_response(404)
            self.end_headers()
    

if __name__ == '__main__':
    try:
        str_port = os.getenv('HTTP_SERVER_PORT')
        if str_port is None:
            print(f"Starting http server failed: unknown port")
        int_port = int(str_port)
        server = HTTPServer(('', int_port), MyHttpHandler)
        print(f"Starting http server success on port: '{str_port}'")
        server.serve_forever()
    except Exception as e:
        print(f"Starting http server failed: '{e}'")
        sys.exit(1)
