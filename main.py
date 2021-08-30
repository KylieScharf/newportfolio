# import "packages" from flask
from flask import Flask, render_template, request

# create a Flask instance
app = Flask(__name__)

# The following create new routes for the top navigation bar buttons and must be connected to an HTML page
# connects default URL to render index.html
@app.route('/', methods=['GET', 'POST'])
def index():
    # submit button has been pushed
    if request.form:
        indexName = request.form.get("indexSearch")
        if indexName == "area 51":
            return render_template("kylie.html", name1="World")
        if indexName == "bermuda triangle":
            return render_template("hawkers.html")
        if indexName == "great pyramid":
            return render_template("kangaroos.html")
        if indexName == "crooked forrest":
            return render_template("walruses.html")

    # starting and empty input default
    return render_template("index.html")


# connects /kangaroos path to render kangaroos.html
@app.route('/kangaroos/')
def kangaroos():
    return render_template("kangaroos.html")


@app.route('/walruses/')
def walruses():
    return render_template("walruses.html")


@app.route('/hawkers/')
def hawkers():
    return render_template("hawkers.html")

@app.route('/kylie/', methods=['GET', 'POST'])
def kylie():
    # submit button has been pushed
    if request.form:
        name = request.form.get("kylieInput")
        if len(name) != 0:  # input field has content
            return render_template("kylie.html", name1=name)
    # starting and empty input default
    return render_template("kylie.html", name1="World")




# runs the application on the development server
#The rest just create routes that may be used but this actually runs the program on the server
if __name__ == "__main__":
    app.run(debug=True)
