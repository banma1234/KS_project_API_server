import urllib.request
# import environ
# import os

# env = environ.Env(
#     DEBUG=(bool, False)
# )
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

def papago(string):
    client_id = "92S0absIUZJOfpBKLgGl"
    client_secret = "xpZVKEY8Ba"
    data = "source=en&target=ko&text=" + string
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
        
        return result
    else:
        print("Error Code:" + rescode)
        return "Error Code:" + rescode