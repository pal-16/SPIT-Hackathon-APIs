from flask import Flask,request
from task import get_data
from image_cat import image_category

app = Flask(__name__) 
  
@app.route('/get-new-task',methods=['POST']) 
def get_task(): 
    msg = request.get_json()
    #print(msg,type(msg),msg['message'])
    data = get_data(msg['message'])
    return data

@app.route('/get-image-category',methods=['POST'])
def get_image_cat():
    url = request.get_json()['url']
    cat = image_category(url)
    return cat
  
# main driver function 
if __name__ == '__main__': 
    app.run() 