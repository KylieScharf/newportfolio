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
@app.route('/aboutKylie/')
def aboutKylie():
    return render_template("aboutPages/aboutKylie.html")

@app.route('/aboutKhushi/')
def aboutKhushi():
    return render_template("aboutPages/aboutKhushi.html")

@app.route('/aboutKevin/')
def aboutKevin():
    return render_template("aboutPages/aboutKevin.html")

@app.route('/aboutDaniel/')
def aboutDaniel():
    return render_template("aboutPages/aboutDaniel.html")

@app.route('/aboutHamza/')
def aboutHamza():
    return render_template("aboutPages/aboutHamza.html")
#end about pages

#technical info drop down
@app.route('/designInfo/')
def designInfo():
    return render_template("technicalInfo/designInfo.html")


@app.route('/technicalResearch/')
def technicalResearch():
    return render_template("technicalInfo/technicalResearch.html")
#end technical info drop down

#theme pages
# connects /greatPyramid path to render greatPyramid.html
@app.route('/greatPyramid/')
def greatPyramid():
    return render_template("themePages/greatPyramid.html")

@app.route('/area51/')
def Area51():
    return render_template("themePages/Area51.html")

@app.route('/bermudaTriangle/')
def bermudaTriangle():
    return render_template("themePages/bermudaTriangle.html")
#end theme pages

#greet pages
@app.route('/kylie/', methods=['GET', 'POST'])
def kylie():
    # submit button has been pushed
    if request.form: #if the submit button has been pressed
        kylieInput = request.form.get("kylieForm") #store the input into a variable
        if len(kylieInput) != 0:  # if the length of the input stored in the variable is greater than 0/field has content
            return render_template("greet/kylie.html", kylieDisplayName=kylieInput) #render the same page and set the variable already created in jinja to whatever the user inputed-->
    # starting and empty input default
    return render_template("greet/kylie.html", kylieDisplayName="World")#if nothing has happened render the page and set the variable in jinja to a default value "world"-->

@app.route('/daniel/', methods=['GET', 'POST'])
def daniel():
    # submit button has been pushed
    if request.form:
        danielInput = request.form.get("danielForm")
        if len(danielInput) != 0:  # input field has content
            return render_template("greet/daniel.html", danielDisplayName=danielInput)
    # starting and empty input default
    return render_template("greet/daniel.html", danielDisplayName="World")

@app.route('/khushi/', methods=['GET', 'POST'])
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

@app.route('/hamza/', methods=['GET', 'POST'])
def hamza():
    # submit button has been pushed
    if request.form:
        hamzaInput = request.form.get("hamzaForm")
        if len(hamzaInput) != 0:  # input field has content
            return render_template("greet/hamza.html", hamzaDisplayName=hamzaInput)
    # starting and empty input default
    return render_template("greet/hamza.html", hamzaDisplayName="World")

@app.route('/kevin/', methods=['GET', 'POST'])
def kevin():
    # submit button has been pushed
    if request.form:
        kevinInput = request.form.get("kevinForm")
        if len(kevinInput) != 0:  # input field has content
            return render_template("greet/kevin.html", kevinDisplayName=kevinInput)
    # starting and empty input default
    return render_template("greet/kevin.html", kevinDisplayName="World")
#end greet pages

#A51 stories
@app.route('/A51story1/')
def A51story1():
    return render_template("A51stories/A51story1.html")

@app.route('/A51story11/')
def A51story11():
    return render_template("A51stories/A51story11.html")

@app.route('/A51story12/')
def A51story12():
    return render_template("A51stories/A51story12.html")


#BT stories
@app.route('/BTstory1/')
def BTstory1():
    return render_template("BTstories/BTstory1.html")

@app.route('/BTstory11/')
def BTstory11():
    return render_template("BTstories/BTstory11.html")

@app.route('/BTstory12/')
def BTstory12():
    return render_template("BTstories/BTstory12.html")

#GP stories
@app.route('/GPstory1/')
def GPstory1():
    return render_template("GPstories/GPstory1.html")

@app.route('/GPstory11/')
def GPstory11():
    return render_template("GPstories/GPstory11.html")

@app.route('/GPstory12/')
def GPstory12():
    return render_template("GPstories/GPstory12.html")

@app.route('/GPstory111/')
def GPstory111():
    return render_template("GPstories/GPstory111.html")

@app.route('/GPstory112/')
def GPstory112():
    return render_template("GPstories/GPstory112.html")

@app.route('/GPstory121/')
def GPstory121():
    return render_template("GPstories/GPstory121.html")

@app.route('/GPstory122/')
def GPstory122():
    return render_template("GPstories/GPstory122.html")

@app.route('/binary/', methods=['GET', 'POST'])
def binary():
    if request.form:
        bitNumber = request.form.get("bits")
        if len(bitNumber) != 0:  # input field has content
            return render_template("technicalInfo/binary.html", BITS=int(bitNumber))
    # starting and empty input default
    return render_template("technicalInfo/binary.html", BITS=8)



# runs the application on the development server
#The rest just create routes that may be used but this actually runs the program on the server
if __name__ == "__main__":
    app.run(debug=True)
