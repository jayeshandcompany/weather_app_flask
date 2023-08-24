from flask import Flask,request,render_template,url_for
import requests
import os
app= Flask(__name__)

@app.route("/")
def index():
  return render_template("index.html")
@app.route("/weather")
def weather():
  lat=request.args.get('latitude')
  lon=request.args.get('longitude')
  url=f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid=e56d9299cab9902dcbf019d138f1e20f"
  re=requests.get(url)
  return render_template("weather.html",data=re.text)
if __name__=="__main__":
  port=os.environ.get("PORT",'5050')
  app.run(host="0.0.0.0",port=port,debug =True)