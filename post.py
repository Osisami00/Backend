from http.server import BaseHTTPRequestHandler, HTTPServer
import json



# BaseHTTPRequestHandler - is set to inherit a class created somewhere
# HTTPServer - the func use to run our server
# API is the full url while endpoint is a part

# create a class for base

data = []

class BasicAPI(BaseHTTPRequestHandler):   #we just inherited the class of BaseHTTP
    def send_data(self, payload, status=201):
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(payload).encode())


    def do_POST(self):
        content_size = int(self.headers["COntent-Length"], 0)
        # self.rfile.read()
        parsed_data =self.rfile.read(content_size)

        post_data = json.loads(parsed_data)
        print(post_data)
        data.append(post_data)   #saving to database
        self.send_data({
            "Message" : "Data Received",
            "data" : post_data
        })

def run():
    HTTPServer(('localhost', 5100), BasicAPI).serve_forever()
    # itself except stated otherwise

print("Application is running!!!")
run()



        

