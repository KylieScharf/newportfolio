# import "packages" from flask
from flask import Flask, render_template, request
from algorithm import  image_data
from api.webapi import api_bp
from pathlib import Path # https://medium.com/@ageitgey/python-3-quick-tip-the-easy-way-to-deal-with-file-paths-on-windows-mac-and-linux-11a072b58d5f
import requests
from flask import Blueprint, jsonify

#committ test
# create a Flask instance
app = Flask(__name__)
path = Path(app.root_path) / "static" / "assets"
app_starter = Blueprint('starter', __name__,
                        url_prefix='/starter',
                        template_folder='templates',
                        static_folder='static',
                        static_url_path='assets')

# The following create new routes for the top navigation bar buttons and must be connected to an HTML page
# connects default URL to render index.html
#home page
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("themePages/index.html")
#end home page

#about pages
@app.route('/aboutKylie/')
def aboutKylie():
    return render_template("aboutPages/aboutKylie.html", path=path)

@app.route('/aboutKhushi/')
def aboutKhushi():
    return render_template("aboutPages/aboutKhushi.html")

@app.route('/aboutKevin/')
def aboutKevin():
    return render_template("aboutPages/aboutKevin.html")

@app.route('/aboutDaniel/')
def aboutDaniel():
    return render_template("aboutPages/aboutDaniel.html", path=path)

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
    img_list = [
        {'file': "GP.jpeg"}, # this is one dictionary where the source is the word and the "smiley" is the definition
    ]
    return render_template("themePages/greatPyramid.html", images=image_data(path=path, img_list=img_list))

@app.route('/bermudaTriangle/')
def bermudaTriangle():
    img_list = [
        {'file': "BT.jpg"}, # this is one dictionary where the source is the word and the "smiley" is the definition
    ]
    return render_template("themePages/bermudaTriangle.html", images=image_data(path=path, img_list=img_list))
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

@app.route('/BTstory1/')
def BTstory1():
    return render_template("BTstories/BTstory1.html")

@app.route('/BTstory11/')
def BTstory11():
    return render_template("BTstories/BTstory11.html")

@app.route('/BTstory12/')
def BTstory12():
    return render_template("BTstories/BTstory12.html")

@app.route('/BTstory111/')
def BTstory111():
    return render_template("BTstories/BTstory111.html")

@app.route('/BTstory112/')
def BTstory112():
    return render_template("BTstories/BTstory112.html")

@app.route('/BTstory121/')
def BTstory121():
    return render_template("BTstories/BTstory121.html")

@app.route('/BTstory122/')
def BTstory122():
    return render_template("BTstories/BTstory122.html")

@app.route('/BTstory1121/')
def BTstory1121():
    return render_template("BTstories/BTstory1121.html")

@app.route('/BTstory1122/')
def BTstory1122():
    return render_template("BTstories/BTstory1122.html")

@app.route('/BTstory1211/')
def BTstory1211():
    return render_template("BTstories/BTstory1211.html")

@app.route('/BTstory1212/')
def BTstory1212():
    return render_template("BTstories/BTstory1212.html")

@app.route('/BTstory1221/')
def BTstory1221():
    return render_template("BTstories/BTstory1221.html")

@app.route('/BTstory1222/')
def BTstory1222():
    return render_template("BTstories/BTstory1222.html")

@app.route('/BTstory11211/')
def BTstory11211():
    return render_template("BTstories/BTstory11211.html")

@app.route('/BTstory11212/')
def BTstory11212():
    return render_template("BTstories/BTstory11212.html")

@app.route('/BTstory11221/')
def BTstory11221():
    return render_template("BTstories/BTstory11221.html")

@app.route('/BTstory11222/')
def BTstory11222():
    return render_template("BTstories/BTstory11222.html")

@app.route('/BTstory12111/')
def BTstory12111():
    return render_template("BTstories/BTstory12111.html")

@app.route('/BTstory12112/')
def BTstory12112():
    return render_template("BTstories/BTstory12112.html")

@app.route('/BTstory12211/')
def BTstory12211():
    return render_template("BTstories/BTstory12211.html")

@app.route('/BTstory12212/')
def BTstory12212():
    return render_template("BTstories/BTstory12212.html")

@app.route('/BTstory12221/')
def BTstory12221():
    return render_template("BTstories/BTstory12221.html")

@app.route('/BTstory12222/')
def BTstory12222():
    return render_template("BTstories/BTstory12222.html")

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

#labs
@app.route('/binary/', methods=['GET', 'POST'])
def binary():
    if request.method == "POST":
        if request.form:
            bitNumber = request.form.get("bits")
            if len(bitNumber) != 0:  # input field has content
                return render_template("technicalInfo/binary.html", BITS=int(bitNumber), imageOn="/static/assets/sun.jpg", imageOff="/static/assets/moon.jpg")
        # starting and empty input default
        if request.form["bits2"]:
            print("hello")
            return render_template("technicalInfo/binary.html", BITS=8, imageOn="/static/assets/smiley.jpg", imageOff="/static/assets/rip1.jpg")
    return render_template("technicalInfo/binary.html", BITS=8, imageOn="/static/assets/sun.jpg", imageOff="/static/assets/moon.jpg")

@app.route('/Binary2/', methods=["GET", "POST"])
def Binary2():
    if request.form:
        bitNumber2 = request.form.get("bits2")
        if len(bitNumber2) != 0:  # input field has content
            print("hello")
            return render_template("technicalInfo/Binary2.html", BITS=int(bitNumber2))
    return render_template("technicalInfo/Binary2.html", BITS=8)

@app.route('/rgb/', methods=["GET", "POST"])
def rgb():
    img_list = [
        {'file': "BT.jpg"}
    ]
    return render_template('technicalInfo/rgb.html', images=image_data(path, shouldDraw=True))

@app.route('/logicGate/', methods=['GET', 'POST'])
def logicGate():
    return render_template("technicalInfo/logicGate.html", path=path, BITS=8)

@app.route('/colors/')
def colors():
    return render_template("technicalInfo/colors.html", path=path, BITS=8)

@app.route('/unsignedaddition/')
def unsignedaddition():
    return render_template("technicalInfo/unsignedaddition.html", path=path, BITS=8)

@app.route('/signedAddition/', methods=['GET', 'POST'])
def signedAddition():
    return render_template("technicalInfo/signedAddition.html", path=path, BITS=8)

@app.route('/unicode/', methods=['GET', 'POST'])
def unicode():
    return render_template("technicalInfo/unicode.html", path=path, BITS=8)

@app.route('/unsigned2/', methods=['GET', 'POST'])
def unsigned2():
    return render_template("technicalInfo/unsigned2.html", path=path, BITS=8, imageOn="/static/assets/sun.jpg", imageOff="/static/assets/moon.jpg")

@app.route('/signed2/', methods=['GET', 'POST'])
def signed2():
    return render_template("technicalInfo/signed2.html", path=path, BITS=8, imageOn="/static/assets/sun.jpg", imageOff="/static/assets/moon.jpg")

@app.route('/weather/', methods=['GET', 'POST'])
def weather():
    countryCode = ['105391811', '105368361', '105359777', '105341704', '105393052', '105392171'] #this creates a list of country codes that I got from the API website by searching up different countries with their country lookup
    dictionaryMasterList = [] #this creates an empty list that all the dictionaries go into
    for item in countryCode: #this is a for loop for all the country codes so that each one gets a response
        url = "https://foreca-weather.p.rapidapi.com/observation/latest/" + item

        querystring = {"lang":"en"}

        headers = {
            'x-rapidapi-host': "foreca-weather.p.rapidapi.com",
            'x-rapidapi-key': "00a6319afcmshb59ecb31e0a9dbap1c6de4jsn4b86a9198483"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        list_of_dictionaries2 = response.json().get('observations')
        dictionaryMasterList = dictionaryMasterList + list_of_dictionaries2
    print('WEATHER INFO')
    print(dictionaryMasterList) #up until here is gotten from rapidapi.com and this line creates a response object that is a json response from the server
    return render_template("weather.html", weather=dictionaryMasterList) #we give the list of dictionaries to the HTML to use

@app.route('/translator/', methods=['GET', 'POST'])
def translator():
    url = "https://shakespeare.p.rapidapi.com/shakespeare.json"
    text = "Hello everybody, Type anything in the above search bar to translate it into Shakespearean text like you see to the right of this"
    if request.form:
        text = request.form.get("tester")
        print(text)

    querystring = {"text": text}

    headers = {
        'x-funtranslations-api-secret': "Thou shalt try this API!",
        'x-rapidapi-host': "shakespeare.p.rapidapi.com",
        'x-rapidapi-key': "00a6319afcmshb59ecb31e0a9dbap1c6de4jsn4b86a9198483"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    dictionary = response.json().get('contents')
    print(response.text)
    return render_template("translator.html", dictionary=dictionary)
# runs the application on the development server
#The rest just create routes that may be used but this actually runs the program on the server


@app.route('/translator2/', methods=['GET', 'POST'])
def translator2():
    url = "https://translated-mymemory---translation-memory.p.rapidapi.com/api/get"
    pairs = ["en|es", "en|it", "en|zh", "en|de", "en|he"]
    text = "Translated text will show here"
    original = text
    master_list = []
    if request.form:
        text = request.form.get("tester2")
        original = text
    for item in pairs:
        querystring = {"langpair":item,"q":text,"mt":"1","onlyprivate":"0","de":"a@b.c"}

        headers = {
            'x-rapidapi-host': "translated-mymemory---translation-memory.p.rapidapi.com",
            'x-rapidapi-key': "00a6319afcmshb59ecb31e0a9dbap1c6de4jsn4b86a9198483"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        print(response.text)
        dictionary = [response.json().get('responseData')]
        master_list = master_list + dictionary
    return render_template("translator2.html", dictionary=master_list, original=original)

@app_starter.route('/joke', methods=['GET', 'POST'])
def joke():
    url = "http://127.0.0.1:5000/api/joke"
    #url = "https://csp.nighthawkcodingsociety.com/api/joke"
    param = {"like":0}
    response = requests.request("GET", url, params=param)
    print(response.json())
    a=1
    if a == 1:
        dictionary = response.json()
        id = dictionary['id']
        print(id)
        dictionary['haha'] +=1
        likes = dictionary['haha']
        print("hello")
        print(response.json())
        print(likes)
        param = {"id":id, "like": likes}
        print(dictionary['haha'])
        #response = requests.request("GET", "http://127.0.0.1:5000/api/jokes", params=param)
    return render_template("starter/joke.html", joke=response.json())

@app_starter.route('/jokes', methods=['GET', 'POST'])
def jokes():
    # use this url to test on and make modification on you own machine
    url = "http://127.0.0.1:5000/api/jokes"
    #url = "https://csp.nighthawkcodingsociety.com/api/jokes"

    response = requests.request("GET", url)
    return render_template("starter/jokes.html", jokes=response.json())

@app.route('/area51/')
def Area51():
    img_list = [
        {'file': "A51.jpeg"}, # this is one dictionary where the source is the word and the "smiley" is the definition
    ]
    return render_template("themePages/Area51.html", images=image_data(path=path, img_list=img_list))

@app.route('/feedback/', methods=['GET', 'POST'])
def feedback():
    if request.form:
        input = request.form.get("feed1")
        name = request.form.get("feed2")
        if len(input) != 0:  # input field has content
            return render_template("layouts/feedback.html", input=input, name=name)
    return render_template("layouts/feedback.html")

@app.route('/movie/', methods=['GET', 'POST'])
def movie():
    url = "https://watchmode.p.rapidapi.com/list-titles/"

    querystring = {"types":"movie,tv_series","regions":"US","source_types":"sub,free","source_ids":"23,206","page":"1","limit":"250","genres":"4,9"}

    headers = {
        'x-rapidapi-host': "watchmode.p.rapidapi.com",
        'x-rapidapi-key': "f4480562c7mshcfebe0975d4fd48p16ab77jsnae6575329780"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    response = response.json().get("titles")
    print(response)

    return render_template("movie.html", response=response)

@app.route('/2area51/', methods=['GET', 'POST'])
def area51_story():
    img_list = [
        {'file': "A51.jpeg"}, # this is one dictionary where the source is the word and the "smiley" is the definition
    ]
    return render_template("A51stories/A51story.html" , images=image_data(path=path, img_list=img_list))

app.register_blueprint(api_bp)
app.register_blueprint(app_starter)

if __name__ == "__main__":
    app.run(debug=True)




