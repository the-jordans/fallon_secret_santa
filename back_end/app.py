from flask import Flask, render_template, Response
from family_constants import family_dict
from secret_santa_hub import return_matches_for_everyone
import json

app = Flask(__name__)

@app.route('/family_data')
def family_data():
    resp = Response(json.dumps(family_dict))
    resp.headers['Content-Type'] = 'application/json'
    return resp

@app.route('/gift_data')
def gift_data():
    resp = Response(json.dumps(return_matches_for_everyone()))
    resp.headers['Content-Type'] = 'application/json'
    return resp


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True, threaded=True)
