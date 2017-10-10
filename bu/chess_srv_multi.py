from socketserver import ThreadingMixIn
from http.server import CGIHTTPRequestHandler, HTTPServer

class ThreadingSimpleServer(ThreadingMixIn, HTTPServer):
    pass

import sys
import os

if sys.argv[1:]:
    port = int(sys.argv[1])
else:
    port = 8000

if sys.argv[2:]:
    os.chdir(sys.argv[2])

server = ThreadingSimpleServer(('', port), CGIHTTPRequestHandler)
try:
    while 1:
        sys.stdout.flush()
        server.handle_request()
except KeyboardInterrupt:
    print("Finished")