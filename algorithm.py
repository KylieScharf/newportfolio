# image (PNG, JPG) to base64 conversion (string), learn about base64 on wikipedia https://en.wikipedia.org/wiki/Base64
import base64
from io import BytesIO
import numpy
from PIL import ImageDraw, Image
from pathlib import Path # https://medium.com/@ageitgey/python-3-quick-tip-the-easy-way-to-deal-with-file-paths-on-windows-mac-and-linux-11a072b58d5f
import http.client
import requests
import json



def image_base64(img, img_type):
    with BytesIO() as buffer:
        img.save(buffer, img_type) #this saves the image as something different/converts it into binary for the data
        return base64.b64encode(buffer.getvalue()).decode() #after dot is a function
# formatter preps base64 string for inclusion, ie <img src=[this return value] ... />
def image_formatter(img, img_type):
    return "data:image/" + img_type + ";base64," + image_base64(img, img_type)
# color_data prepares a series of images for data analysis

def image_data(path=Path("static/assets/"), img_list=None, shouldDraw=False):  # path of static images is defaulted
    if img_list is None:  # color_dict is defined with defaults
        img_list = [
            {'source': "Romolo Tavani ", 'label': "Drowning Hand", 'file': "rip(lower).jpg"}, # this is one dictionary where the source is the word and the "smiley" is the definition
        ]
    # gather analysis data and meta data for each image, adding attributes to each row in table
    for img_dict in img_list:
        file = path / img_dict['file']  # file with path for local access (backend)
        # Python Image Library operations
        img_reference = Image.open(file)  # PIL: this is opeening the image like if we did image.open(static/assets/smiley.jpg) adn this creates an instance of the image. image.open() is a function that loads the image and creates an image pbject that can be modified with the .save: the image object we recieve using image.open can later be used to resize, crop, or more the image
        if shouldDraw == True:
            draw = ImageDraw.Draw(img_reference)
            draw.text((75, 50), "Hello World", fill=(255, 0, 0))
        img_data = img_reference.getdata()  # Reference https://www.geeksforgeeks.org/python-pil-image-getdata/ this gets the binary from the RGB without meta data :  Image.open() reads the image and gets all relevant info from the image.
        img_dict['format'] = img_reference.format #jpeg vs png (file format)
        img_dict['mode'] = img_reference.mode #pixel format s o RGB vs RGBA
        img_dict['size'] = img_reference.size #height and width of the image
        # Conversion of original Image to Base64, a string format that serves HTML nicely
        img_dict['base64'] = image_formatter(img_reference, img_dict['format'])
        # Numpy is used to allow easy access to data of image, python list
        img_dict['data'] = numpy.array(img_data)
        img_dict['hex_array'] = []
        img_dict['binary_array'] = []
        img_dict['gray_data'] = []
        img_dict['green_data'] = []
        img_dict['flip'] = img_reference.transpose(Image.FLIP_LEFT_RIGHT)
        degree_flippedImage = img_reference.transpose(Image.FLIP_LEFT_RIGHT)
        img_dict['base64_flip'] = image_formatter(degree_flippedImage,img_dict['format'])
        # 'data' is a list of RGB data, the list is traversed and hex and binary lists are calculated and formatted
        #in this area made the code more efficient based on big O notation
        for pixel in img_dict['data']:
            # hexadecimal conversions
            hex_value = hex(pixel[0])[-2:] + hex(pixel[1])[-2:] + hex(pixel[2])[-2:]
            hex_value = hex_value.replace("x", "0")
            img_dict['hex_array'].append("#" + hex_value)
            # binary conversions
            bin_value = bin(pixel[0])[2:].zfill(8) + " " + bin(pixel[1])[2:].zfill(8) + " " + bin(pixel[2])[2:].zfill(8)
            img_dict['binary_array'].append(bin_value)
        # create gray scale of image, ref: https://www.geeksforgeeks.org/convert-a-numpy-array-to-an-image/
        #got rid of a second for loop for they grey data to make big O notation go from O(2N) to O(N) because there is only one for loop now
        #for pixel in img_dict['data']:
            average = (pixel[0] + pixel[1] + pixel[2]) // 3
            if len(pixel) > 3:
                img_dict['gray_data'].append((average, average, average, pixel[3])) # append means to add it like when you do "" + something to create a string
                img_dict['green_data'].append((0, average, 0, pixel[3]))
            else:
                img_dict['gray_data'].append((average, average, average))
                img_dict['green_data'].append((0, average, 0))
        img_reference.putdata(img_dict['gray_data'])
        img_dict['base64_GRAY'] = image_formatter(img_reference, img_dict['format'])
        img_reference.putdata(img_dict['green_data'])
        img_dict['base64_GREEN'] = image_formatter(img_reference, img_dict['format'])

        #img_reference.save(img_dict['flip'])
        #img_dict['base64_flip'] = image_formatter(img_reference, img_dict['format'])
    return img_list  # list is returned with all the attributes for each image dictionary
# run this as standalone tester to see data printed in terminal


if __name__ == "__main__":
    #r = requests.get('https://api.dailysmarty.com/posts')
    #print(r.json())
    #print(pprint.pprint(r.json))
    #print(pprint.pprint(r.json()['posts'][0]['url_for_post']))
    url = "https://covid-19-data.p.rapidapi.com/country/code"

    querystring = {"code":"us"}

    headers = {
        'x-rapidapi-host': "covid-19-data.p.rapidapi.com",
        'x-rapidapi-key': "00a6319afcmshb59ecb31e0a9dbap1c6de4jsn4b86a9198483"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    print(response.text)
    list_of_dictionaries = response.json()
    #return render_template(.html list=list)
    print("hello")
    print(list_of_dictionaries)
    python = json.loads(response.text)


    print(python)
    url = "https://corona-virus-world-and-india-data.p.rapidapi.com/api"

    headers = {
        'x-rapidapi-key': "dec069b877msh0d9d0827664078cp1a18fajsn2afac35ae063",
        'x-rapidapi-host': "corona-virus-world-and-india-data.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers)
    world = response.json().get('world_total')
    countries = response.json().get('countries_stat')
    print(world['total_cases'])
    print(world)
    print(countries)

    #return countries


if __name__ == "__main__":
    url = "https://foreca-weather.p.rapidapi.com/location/search/san jose"

    querystring = {"lang":"en","country":"us"}

    headers = {
        'x-rapidapi-host': "foreca-weather.p.rapidapi.com",
        'x-rapidapi-key': "00a6319afcmshb59ecb31e0a9dbap1c6de4jsn4b86a9198483"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)



