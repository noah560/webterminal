from flask import Flask, request
import easygui
from subprocess import run as bash

app = Flask(__name__)

@app.route("/")
def run():
    com = request.args.get("c")
    if easygui.boolbox("Does this website have permission to run: " + com, "permission", ["Yes", "No"]):
        bash(com.split(" "))
    return "<script>window.setTimeout(function(){window.close()}, 100);</script>"


app.run(host='0.0.0.0', port=9219)
