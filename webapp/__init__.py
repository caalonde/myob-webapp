"""System module."""
import subprocess
import json
import flask
from flask import jsonify

def myapp():
    """A dummy docstring."""
    app = flask.Flask(__name__)

    @app.route("/")
    def home():
        """A dummy docstring."""
        return "Hello World!"

    @app.route("/health")
    def healthcheck():
        """A dummy docstring."""
        return ""

    @app.route("/metadata")
    def metadata():
        """A dummy docstring."""

        # Git hash info
        gitcmd = "git rev-parse --short HEAD"
        process = subprocess.run(gitcmd.split(), stdout=subprocess.PIPE, text=True, check=True)
        githash = process.stdout

        # Get app info
        pipcmd = "pip show webapp"
        process = subprocess.run(pipcmd.split(), stdout=subprocess.PIPE, text=True, check=True)
        pipout = process.stdout

        name = ""
        version = ""
        description = ""

        lines = pipout.split("\n")

        for line in lines:
            if "Name" in line:
                name = line.split(":")[1]
            elif "Version" in line:
                version = line.split(":")[1]
            elif "Summary" in line:
                description = line.split(":")[1]

        data = {'description': description.strip(), \
                'version': version.strip(), \
                'lastcommitsha': githash.strip() }
        fdata = { name.strip() : [ data ]}
        jdata = json.dumps(fdata)

        return jdata

    return app
