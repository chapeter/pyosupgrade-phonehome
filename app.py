from flask_api import FlaskAPI
from flask import request, Flask
app = Flask(__name__)
import json
import subprocess


#API Endpoint to have a router request to be configured
@app.route("/api/configme", methods=['POST'])
def configme():
    '''
    POST will contain:
    hostname: str
    jobid: str
    ip: str
    '''
    r = request
    r = json.loads(r.data)
    hostname = str(r['hostname'])
    jobid = str(r['jobid'])
    ip = str(r['ip'])

    print(hostname)

    subprocess.call("./configme.sh {}".format(hostname), shell=True)
    return("You have been configured")

if __name__ == '__main__':
    app.secret_key = '1234'
app.run(host="0.0.0.0", port=5000, debug=True)
