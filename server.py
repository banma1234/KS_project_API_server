from flask import Flask
import datetime
import utils.translate.papago as translater
import utils.translate.hello as hello
import run as OCR
  
timeNow = datetime.datetime.now()

  
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

@app.route('/api/test')
def doTest():
    print(hello.wow())
    return(hello.wow())

@app.route('/api/scanImage')
def readText():
    imageToText = OCR.perform_ocr()
    result = translater.papago(imageToText)
    
    return result
      
# Running app
if __name__ == '__main__':
    app.run(host='0.0.0.0')