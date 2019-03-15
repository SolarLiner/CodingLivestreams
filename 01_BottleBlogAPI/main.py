import os
from bottle import run, route, static_file

import api


@route("/")
@route("/<whatever>")
def index(whatever="index.html"):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    static_dir = os.path.join(current_dir, "static")
    file = static_file(whatever, root=static_dir)
    if file.status_code != 200:
        file = static_file("index.html", root=static_dir)
    print(repr(file))

    return file

run(host="localhost", port=3000)