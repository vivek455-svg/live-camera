# Serves this folder on localhost:8765 and tells browsers never to cache, so edits show on reload.
import http.server, functools, os

class NoCache(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

handler = functools.partial(NoCache, directory=os.path.dirname(os.path.abspath(__file__)))
http.server.ThreadingHTTPServer(("localhost", 8765), handler).serve_forever()
