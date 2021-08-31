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
            return render_template("Area51.html")
        if indexName == "bermuda triangle":
            return render_template("bermudaTriangle.html")
        if indexName == "great pyramid":
            return render_template("greatPyramid.html")

    # starting and empty input default
    return render_template("index.html")


# connects /kangaroos path to render greatPyramid.html
@app.route('/greatPyramid/')
def greatPyramid():
    return render_template("greatPyramid.html")


@app.route('/bermudaTriangle/')
def bermudaTriangle():
    return render_template("bermudaTriangle.html")


@app.route('/area51/')
def area51():
    return render_template("Area51.html")

@app.route('/kylie/', methods=['GET', 'POST'])
def kylie():
    # submit button has been pushed
    if request.form:
        kylieInput = request.form.get("kylieForm")
        if len(kylieInput) != 0:  # input field has content
            return render_template("kylie.html", kylieDisplayName=kylieInput)
    # starting and empty input default
    return render_template("kylie.html", kylieDisplayName="World")

@app.route('/daniel/', methods=['GET', 'POST'])
def daniel():
    # submit button has been pushed
    if request.form:
        danielInput = request.form.get("danielForm")
        if len(danielInput) != 0:  # input field has content
            return render_template("daniel.html", danielDisplayName=danielInput)
    # starting and empty input default
    return render_template("daniel.html", danielDisplayName="World")

@app.route('/khushi/', methods=['GET', 'POST'])
def khushi():
    # submit button has been pushed
    print("1")
    if request.form:
        print("2")
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            print("3")
            return render_template("khushi.html", name1=name)
    # starting and empty input default
    return render_template("khushi.html", name1="World")



# runs the application on the development server
#The rest just create routes that may be used but this actually runs the program on the server
if __name__ == "__main__":
    app.run(debug=True)
