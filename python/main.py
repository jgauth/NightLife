import json, logging
from flask import Flask, request, redirect, url_for, flash, abort, jsonify, render_template


app = Flask("john")

'''@app.route("/create", methods=['GET'])
def test():
    if request.method == 'GET':
        print("GET REQ")
        return app.send_static_file('index.html')'''

@app.route("/api/healthcheck", methods=['GET'])
def healthcheck():
    return jsonify({ 'data': 'sup' })

@app.route("/api/event/create", methods=['POST','PUT'])
def create_event():
    if request.method == 'POST' or request.method == 'PUT':
        data = request.get_json()
        print(data)
    response = jsonify({ 'message': 'upload success' })
    response.status_code = 200
    return response
