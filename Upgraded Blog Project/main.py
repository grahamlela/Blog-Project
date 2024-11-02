from flask import Flask, render_template
import requests

response = requests.get("https://api.npoint.io/674f5423f73deab1e9a7")
ALL_POSTS = response.json()

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", blog_posts=ALL_POSTS)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/post/<int:post_id>")
def show_post(post_id):
    return render_template("post.html", post=ALL_POSTS[post_id - 1])


if __name__ == "__main__":
    app.run(debug=True)
