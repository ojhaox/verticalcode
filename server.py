import http.server
import socketserver
import webbrowser

PORT = 8000

handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(("", PORT), handler)

print(f"\n🚀 Server running at http://localhost:{PORT}")
webbrowser.open(f'http://localhost:{PORT}')

try:
    httpd.serve_forever()
except KeyboardInterrupt:
    print("\n👋 Shutting down server...")
    httpd.server_close() 