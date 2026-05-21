import http.server
import subprocess

class WebhookHandler(http.server.BaseHTTPRequestHandler):
    def do_POST(self):
        # Запускаем deploy.sh в фоновом режиме
        subprocess.Popen(["/bin/bash", "/home/ubu/deploy.sh"])
        
        # Отвечаем
        self.send_response(200)
        self.send_header('Content-Type', 'text/plain')
        self.end_headers()
        self.wfile.write(b"Deploy started")

if __name__ == '__main__':
    server = http.server.HTTPServer(('0.0.0.0', 8080), WebhookHandler)
    print("Listening on port 8080...")
    server.serve_forever()
