
from http.server import BaseHTTPRequestHandler, HTTPServer
import json



data = [
    {"id": 1, "name": "sam larry", "track": "AI Developer"},
    {"id": 2, "name": "Bolatito", "track": "AI Developer" }
]




class BasicAPI(BaseHTTPRequestHandler):
    def send_data(self, payload, status):
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(payload, indent=2).encode())

    

    def do_PUT(self):
        content_size = int(self.headers.get("Content-Length", 0))
        parsed_data = self.rfile.read(content_size)


        updated_data = json.loads(parsed_data)
        print(updated_data)

        record_id = int(self.path.strip('/'))
        for item in data:
            if record_id == item["id"]:
                item.update(updated_data)
                self.send_data({"message": item}, status=200)
                

        self.send_data({
            "Message": "Data Recieved",
            "data": data
        }, status=201)

def run():
    HTTPServer(("localhost", 8000), BasicAPI).serve_forever()

print("running")
run()
