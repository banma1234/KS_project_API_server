from flask import Flask, request, jsonify
import utils.translate.papago as translater
import utils.translate.hello as hello
import run as OCR
  
app = Flask(__name__)
  
# Route for seeing a data

@app.route('/api/test')
def doTest():
    print(hello.wow())
    return(hello.wow())

@app.route('/api/scanImage', methods=['POST'])
def readText():
    if 'image' in request.files:
        print("hit!")
        image = request.files['image']
        imageData = image.read()
        
        imageToText = OCR.perform_ocr(imageData)
        result = translater.papago(imageToText)
    
        return {'success': True, 'message': result}
    else:
        return {'success': False, 'message': "failed to read image"}
      
# Running app
if __name__ == '__main__':
    app.run(host='0.0.0.0')