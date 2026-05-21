import http.server
import json
import subprocess

class WebhookHandler(http.server.BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)

        branch_name = "lab1"
        try:
            payload = json.loads(post_data.decode('utf-8'))
            if 'ref' in payload:
                ref = payload['ref']
                if ref.startswith('refs/heads/'):
                    branch_name = ref.replace('refs/heads/', '')
        except Exception as e:
            print("Error parsing JSON:", e)

        subprocess.Popen(["/bin/bash", "/home/ubu/deploy.sh", branch_name])

        self.send_response(200)
        self.send_header('Content-Type', 'text/plain')
        self.end_headers()
        self.wfile.write(f"Deploy started for branch {branch_name}".encode('utf-8'))

if __name__ == '__main__':
    server = http.server.HTTPServer(('0.0.0.0', 8080), WebhookHandler)
    print("Listening on port 8080...")
    server.serve_forever()
