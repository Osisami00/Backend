

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

    
  

    def do_DELETE(self):
        if self.path == '/':
            self.send_data({"error": "Specify record id to delete"}, status=400)
        else:
            try:
                record_id = int(self.path.strip("/"))
                for item in data:
                    if record_id == item["id"]:
                        data.remove(item)
                        self.send_data(data, status=200)

                    else: self.send_data({"error": "Record not found"}, status = 404)
                

            except:        
                self.send_data({"error": "Invalid path"}, status=400)


            
def run():
    HTTPServer(("localhost", 8000), BasicAPI).serve_forever()

print("running")
run()