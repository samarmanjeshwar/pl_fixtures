from flask import Flask, request
import json
import requests

application = Flask(__name__)


#Main file to catch requests
@application.route('/')
def index():
  return json.dumps({"name": "Premier League Fixtures"})

if __name__ == '__main__':
  application.run(debug=True, host = '127.0.0.1', port = 8000)
