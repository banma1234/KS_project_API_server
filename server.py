from flask import Flask
import os
import environ
import datetime
import urllib.request
  
timeNow = datetime.datetime.now()

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

  
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
def papago():
    client_id = os.environ.get('NAVER_CLIENT_KEY')
    client_secret = os.environ.get('NAVER_CLIENT_SECRET')
    doTest = "please transfer this sentence to korean"
    data = "source=en&target=ko&text=" + doTest
    url = "https://openapi.naver.com/v1/papago/n2mt"
    
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    rescode = response.getcode()
    # 호출이 성공할 경우 결과값 return
    if(rescode==200):
        response_body = response.read()
        result = response_body.decode('utf-8')
        print("==========================")
        print(result)
        return result
    else:
        print("Error Code:" + rescode)
        return "Error Code:" + rescode
      
# Running app
if __name__ == '__main__':
    app.run(debug=True)