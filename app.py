from flask import Flask, jsonify 
app = Flask(__name__) 
@app.route('/') 
def hello():
    import socket
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return jsonify(POD_IP=ip_address,    POD_NAME=hostname)

if __name__ == "__main__":
     app.run(host ='0.0.0.0', port = 5001, debug = True)