import http.server
import socketserver
import os

PORT = 8080
os.chdir(os.path.dirname(os.path.abspath(__file__)))

class Handler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        print(f"[{self.client_address[0]}] {format % args}")

print(f"Server started: http://localhost:{PORT}")
print("Open this URL in browser to see the page")
print("Ctrl+C to stop")

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    httpd.serve_forever()
