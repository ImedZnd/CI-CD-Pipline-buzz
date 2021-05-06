import os
from flask import Flask, request
from datetime import date, datetime
from buzz import generator

app = Flask(__name__)

@app.route("/")
def generate_buzz():
    page = '<html><body style="background-color:powderblue;"><h1>'
    page += '<br><h1>'
    page += generator.generate_buzz()
    page += '</h1>'
    page += '<br>'
    page += 'User-Agent :'+request.headers.get('User-Agent')
    page += '<br><h1>'
    page += '<br>'
    page += 'User IP Adress:'+request.remote_addr
    page += '<br><h1>'
    page += 'Date and Time:'+datetime.now().strftime("%d-%b-%Y (%H:%M:%S.%f)")
    page += '</h1>'
    page += '</body></html>'
    return page

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)))
