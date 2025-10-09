#!/usr/bin/python3


'''
task_03_http_server.py
task_03_http_server.py
'''

from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class RequestHandler(BaseHTTPRequestHandler):
    """
    ServerHandler - Server Handler class
    """
    def do_GET(self):
        """
        do_GET - Get function
        Return: Void
        """
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            message = "Hello, this is a simple API!"
            self.wfile.write(message.encode("utf-8"))

        elif self.path == "/data":
            data = {"name": "John", "age": 30, "city": "New York"}
            json_data = json.dumps(data)
            self.send_response(200)
            self.header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json_data.encode("utf-8"))

        elif self.path == "/info":
            data = {
                "version": "1.0",
                "description": "A simple API built with http.server"}
            json_data = json.dumps(data)
            self.send_response(200)
            self.header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json_data.encode("utf-8"))

        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")

        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


def main():
    """
    main - Main function
    Return: Void
    """
    with HTTPServer(("", 8000), RequestHandler) as httpd:
        httpd.serve_forever()


if __name__ == "__main__":
    main()
