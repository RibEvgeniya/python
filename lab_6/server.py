from http.server import HTTPServer, CGIHTTPRequestHandler
httpd = HTTPServer(('localhost', 8000), CGIHTTPRequestHandler)
print("Start:  http://localhost:8000/")
httpd.serve_forever()