# import "packages" from flask
from flask import Flask, render_template, request

# create a Flask instance
app = Flask(__name__)

# The following create new routes for the top navigation bar buttons and must be connected to an HTML page
# connects default URL to render index.html
#home page
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("index.html")
#end home page

#about pages
@app.route('/aboutPages/aboutKylie/')
def aboutKylie():
    return render_template("aboutPages/aboutKylie.html")

@app.route('/aboutPages/aboutKhushi/')
def aboutKhushi():
    return render_template("aboutPages/aboutKhushi.html")

@app.route('/aboutPages/aboutKevin/')
def aboutKevin():
    return render_template("aboutPages/aboutKevin.html")

@app.route('/aboutPages/aboutDaniel/')
def aboutDaniel():
    return render_template("aboutPages/aboutDaniel.html")

@app.route('/aboutPages/aboutHamza/')
def aboutHamza():
    return render_template("aboutPages/aboutHamza.html")
#end about pages

#technical info drop down
@app.route('/technicalInfo/journal0/')
def journal0():
    return render_template("technicalInfo/journal0.html")

@app.route('/technicalInfo/pairShareKK/')
def pairShareKK():
    return render_template("technicalInfo/pairShareKK.html")

@app.route('/technicalInfo/designInfo/')
def designInfo():
    return render_template("technicalInfo/designInfo.html")

@app.route('/technicalInfo/technicalResearch/')
def technicalResearch():
    return render_template("technicalInfo/technicalResearch.html")

@app.route('/technicalInfo/wireframe/')
def wireframe():
    return render_template("technicalInfo/wireframe.html")

@app.route('/technicalInfo/brainwrite/')
def brainwrite():
    return render_template("technicalInfo/brainwrite.html")
#end technical info drop down

#theme pages
# connects /greatPyramid path to render greatPyramid.html
@app.route('/themePages/greatPyramid/')
def greatPyramid():
    return render_template("themePages/greatPyramid.html")

@app.route('/themePages/area51/')
def Area51():
    return render_template("themePages/Area51.html")

@app.route('/themePages/bermudaTriangle/')
def bermudaTriangle():
    return render_template("themePages/bermudaTriangle.html")
#end theme pages

#greet pages
@app.route('/greet/kylie/', methods=['GET', 'POST'])
def kylie():
    # submit button has been pushed
    if request.form: #if the submit button has been pressed
        kylieInput = request.form.get("kylieForm") #store the input into a variable
        if len(kylieInput) != 0:  # if the length of the input stored in the variable is greater than 0/field has content
            return render_template("greet/kylie.html", kylieDisplayName=kylieInput) #render the same page and set the variable already created in jinja to whatever the user inputed-->
    # starting and empty input default
    return render_template("greet/kylie.html", kylieDisplayName="World")#if nothing has happened render the page and set the variable in jinja to a default value "world"-->

@app.route('/greet/daniel/', methods=['GET', 'POST'])
def daniel():
    # submit button has been pushed
    if request.form:
        danielInput = request.form.get("danielForm")
        if len(danielInput) != 0:  # input field has content
            return render_template("greet/daniel.html", danielDisplayName=danielInput)
    # starting and empty input default
    return render_template("greet/daniel.html", danielDisplayName="World")

@app.route('/greet/khushi/', methods=['GET', 'POST'])
def khushi():
    # submit button has been pushed
    print("1")
    if request.form:
        print("2")
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            print("3")
            return render_template("greet/khushi.html", name1=name)
    # starting and empty input default
    return render_template("greet/khushi.html", name1="World")

@app.route('/greet/hamza/', methods=['GET', 'POST'])
def hamza():
    # submit button has been pushed
    if request.form:
        hamzaInput = request.form.get("hamzaForm")
        if len(hamzaInput) != 0:  # input field has content
            return render_template("greet/hamza.html", hamzaDisplayName=hamzaInput)
    # starting and empty input default
    return render_template("greet/hamza.html", hamzaDisplayName="World")

@app.route('/greet/kevin/', methods=['GET', 'POST'])
def kevin():
    # submit button has been pushed
    if request.form:
        kevinInput = request.form.get("kevinForm")
        if len(kevinInput) != 0:  # input field has content
            return render_template("greet/kevin.html", kevinDisplayName=kevinInput)
    # starting and empty input default
    return render_template("greet/kevin.html", kevinDisplayName="World")
#end greet pages



# runs the application on the development server
#The rest just create routes that may be used but this actually runs the program on the server
if __name__ == "__main__":
    app.run(debug=True)
