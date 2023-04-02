from flask import Flask, request
import easygui
from subprocess import run as bash

app = Flask(__name__)

@app.route("/com/")
def run():
    com = request.args.get("com")
    if easygui.boolbox("Does this website have permission to run: " + com, "permission", ["Yes", "No"]):
        bash(com)
    return "<script>window.close();</script>"


app.run(host='0.0.0.0')
