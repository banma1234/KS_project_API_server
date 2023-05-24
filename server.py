from flask import Flask
# import sys, os
# import environ
import datetime
# import urllib.request
import utils.translate.papago as translater
import utils.translate.hello as hello
import utils.OCR.run as OCR
  
timeNow = datetime.datetime.now()
# env = environ.Env(
#     # set casting, default value
#     DEBUG=(bool, False)
# )
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

  
app = Flask(__name__)
  
# Route for seeing a data
@app.route('/api/data')
def get_time():
  
    # Returning an api for showing in  reactjs
    return {
        'Name':"KS_project",
        "Date":timeNow, 
        "programming":"python"
        }
      
@app.route('/api/translate', methods=['GET'])
def translate():
    print(translater.papago())
    return(translater.papago())

@app.route('/api/test')
def doTest():
    print(hello.wow())
    return(hello.wow())

@app.route('/api/ocr')
def readText():
    OCR
    return "wow"
      
# Running app
if __name__ == '__main__':
    app.run(host='0.0.0.0')