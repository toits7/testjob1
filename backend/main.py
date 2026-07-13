from http.server import BaseHTTPRequestHandler, HTTPServer
from dotenv import load_dotenv
import os
import sys

class MyHttpHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'Hello from Effective Mobile!')
        else:
            self.send_response(404)
            self.end_headers()
    

if __name__ == '__main__':
    try:
        load_dotenv()
        host = os.getenv('HTTP_SERVER_HOST')
        str_port = os.getenv('HTTP_SERVER_PORT')
        if host is None:
            print(f"Starting http server failed: unknown host")
            sys.exit(2)
        elif str_port is None:
            print(f"Starting http server failed: unknown port")
            sys.exit(3)
        int_port = int(str_port)
        server = HTTPServer((host, int_port), MyHttpHandler)
        print(f"Starting http server success: '{host}:{str_port}'")
        server.serve_forever()
        sys.exit(0)
    except Exception as e:
        print(f"Starting http server failed: '{e}'")
        sys.exit(1)
