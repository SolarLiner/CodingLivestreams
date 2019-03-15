import os

from bottle import abort, route, run
from frontmatter import Frontmatter


@route("/api/<slug>")
def index(slug):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    blog_post_file = os.path.join(current_dir, "blog", f"{slug}.md")

    if not os.path.exists(blog_post_file):
        abort(404, "Blog post not found")
        return

    frontmatter = Frontmatter.read_file(blog_post_file)
    body = frontmatter.get("body")
    attributes = frontmatter.get("attributes")

    data = attributes.copy()
    data.update(dict(body=body, date=attributes.get("date").isoformat()))

    return data

