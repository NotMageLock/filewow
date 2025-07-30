from http.server import HTTPServer, BaseHTTPRequestHandler
import os

PORT = 42020
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

html = f"""
<!DOCTYPE html>
<html>
<head><title>file wow</title></head>
<body>
    <h1>upload file (wowza!)</h1>
    <form enctype="multipart/form-data" method="post">
        <input name="file" type="file"/>
        <input type="submit" value="Upload"/>
    </form>
</body>
</html>
"""

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()
        self.wfile.write(html.encode('utf-8'))

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        content_type = self.headers['Content-Type']

        if not content_type.startswith("multipart/form-data"):
            self.send_error(400, "Invalid content type")
            return

        boundary = content_type.split("boundary=")[-1].encode()
        body = self.rfile.read(content_length)
        parts = body.split(b"--" + boundary)

        for part in parts:
            if b'Content-Disposition' in part and b'name="file"' in part:
                header, filedata = part.split(b"\r\n\r\n", 1)
                filedata = filedata.rsplit(b"\r\n", 1)[0]

                filename_line = header.decode(errors='ignore')
                filename = "upload.bin"
                if "filename=" in filename_line:
                    filename = filename_line.split("filename=")[-1].split('"')[1]

                filepath = os.path.join(UPLOAD_DIR, filename)
                with open(filepath, 'wb') as f:
                    f.write(filedata)

                self.send_response(200)
                self.end_headers()
                self.wfile.write(f"File '{filename}' uploaded successfully.".encode('utf-8'))
                return

        self.send_error(400, "File upload failed")

if __name__ == '__main__':
    server = HTTPServer(('', PORT), SimpleHTTPRequestHandler)
    print(f"Serving on port {PORT}...")
    server.serve_forever()
