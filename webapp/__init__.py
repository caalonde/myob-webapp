import flask
from flask import jsonify
import subprocess

def myapp():
    app = flask.Flask(__name__)

    @app.route("/")
    def home():
        """A dummy docstring."""
        return "Hello World!"

    @app.route("/health", methods=['GET'])
    def healthcheck():
        """A dummy docstring."""
        return ""

    @app.route("/metadata")
    def metadata():
        """A dummy docstring."""

        # Git hash info
        bashCommand = "git rev-parse --short HEAD"
        process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
        githash, error = process.communicate()

        f = open("setup.py", "r")
        version = "0000000000"
        description = "no description"
        for x in f:
            if "version" in x:
                version = x.strip()
                print(version)
            elif "description" in x:
                description = x.strip()
                print(description)

        myapplication = [{
            "version": version[9:len(version)-2],
            "description" : description[13:len(description)-2],
            "lastcommitsha": str(githash,"utf-8")[0:7]
        }]

        return jsonify(myapplication)

    return app
