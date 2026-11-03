from http.server import HTTPServer, SimpleHTTPRequestHandler

server = HTTPServer(("localhost", 8000), SimpleHTTPRequestHandler)

print("Server started!")
print("Open http://localhost:8000")

server.serve_forever()