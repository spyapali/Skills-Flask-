from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index_page():
    """Show an index page."""

    return "<html><body>This is the Ubermelon homepage.</body></html>"

    # Alternately, we could make this a Jinja template in `templates/`
    # and return that result of rendering this, like:
    #
    # return render_template("index.html")
@app.route("/application-form")
def show_application_form():
	"""Show application form."""

	return render_template("application-form.html")

@app.route("/application", methods=["POST"])
def show_application():
	first_name = request.form.get("first_name")
	last_name = request.form.get("last_name")
	salary = request.form.get("salary")
	desired_job = request.form.get("job")

	return render_template("application-response.html", first_name=first_name, last_name=last_name, 
								salary=salary, desired_job=desired_job)
	

# def show_application():


if __name__ == "__main__":
    app.run(debug=True)
