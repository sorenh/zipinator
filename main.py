import os
from flask import Flask
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    proc = subprocess.Popen([os.path.join(os.path.dirname(__file__), 'bin', 'git'), 'archive', 'https://github.com/sorenh/zipinator'], stdout=subprocess.PIPE)
    retval, _ = proc.communicate()
    return retval
