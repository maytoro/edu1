from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World! Update Test on 08:01, Oct 23 2025"
  
if __name__ == '__main__':
    app.run(host= '0.0.0.0',port=8080,debug=True)
