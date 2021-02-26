from flask import Flask, redirect, url_for, render_template, request

app=Flask(__name__)


app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r

@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
	    user = request.form["movie_field"]           '''this line reads the data entered in the search bar on the site'''
	    return redirect(url_for("user", usr=user))
    else:
	    return render_template("index.html")

@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"

if __name__=="__main__":
    app.run()