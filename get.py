

from http.server import BaseHTTPRequestHandler, HTTPServer
import json



# BaseHTTPRequestHandler - is set to inherit a class created somewhere
# HTTPServer - the func use to run our server
# API is the full url while endpoint is a part

# create a class for base

data = [
    {
        "name": "Olayemi",
        "track": "AI Engineer"
    }
]

class BasicAPI(BaseHTTPRequestHandler):   #we just inherited the class of BaseHTTP
    def send_data(self, data, status=200):
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())


    def do_GET(self):
        self.send_data(data)

def run():
    HTTPServer(('localhost', 8000), BasicAPI).serve_forever()
    # itself except stated otherwise

print("Application is running!!!")
run()



        
