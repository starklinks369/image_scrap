from flask import Flask, render_template, request,jsonify
from flask_cors import CORS,cross_origin
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen as uReq
import logging
import pymongo
logging.basicConfig(filename="scrapper.log" , level=logging.INFO)
import os

app = Flask(__name__)

@app.route("/", methods = ['GET'])
def homepage():
    return render_template("index.html")

@app.route("/review" , methods = ['POST' , 'GET'])
def index():
    if request.method == 'POST':
                try:

                    # query to search for images
                    query = request.form['content'].replace(" ","")

                    try :
                            # directory to store downloaded images
                        save_directory = "static/images/"

                            # create the directory if it doesn't exist
                        if not os.path.exists(save_directory):
                            os.makedirs(save_directory)
                    except Exception as e :
                        log.info(e)


                            # fake user agent to avoid getting blocked by Google
                    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}

                            # fetch the search results page
                    response = requests.get(f"https://www.google.com/search?q={query}&sxsrf=AJOqlzUuff1RXi2mm8I_OqOwT9VjfIDL7w:1676996143273&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiq-qK7gaf9AhXUgVYBHYReAfYQ_AUoA3oECAEQBQ&biw=1920&bih=937&dpr=1#imgrc=1th7VhSesfMJ4M")


                            # parse the HTML using BeautifulSoup
                    soup = BeautifulSoup(response.content, "html.parser")

                            # find all img tags
                    image_tags = soup.find_all("img")

                            # download each image and save it to the specified directory
                    del image_tags[0]
                    img_data=['image1.jpg', 'image2.jpg', 'image3.jpg', 'image4.jpg', 'image5.jpg',
        'image6.jpg', 'image7.jpg', 'image8.jpg', 'image9.jpg', 'image10.jpg',
        'image11.jpg', 'image12.jpg', 'image13.jpg', 'image14.jpg']
                    index = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
                    for image_tag , i in zip(image_tags , index):
                                # get the image source URL
                                image_url = image_tag['src']
                                
    
                                image_data = requests.get(image_url).content
                                with open(os.path.join(save_directory , f"image{i}.jpg") , "wb") as f :
                                    f.write(image_data)
                                #img_data.append(image_url)
                                
                              

                    return render_template('results.html' , image_src = img_data)
                except Exception as e:
                    logging.info(e)
                    return 'something is wrong'
            # return render_template('results.html')

    else:
        return render_template('index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
