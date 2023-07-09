import subprocess
from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/')

@app.route('/home')
def home():
   return render_template('home.html')

@app.route('/run_script_webcam')
def run_script_webcam():
   try:
      # variable = "http://192.168.1.3:8080/video"
      # result = subprocess.check_output("python yolov5/detect.py --source "+variable+ " --weights yolov5s.pt --conf 0.4", shell=True)
      result = subprocess.check_output("python yolov5/detect.py --source 0 --weights yolov5s.pt --conf 0.4", shell=True)
      return render_template('http://127.0.0.1:5000', **locals())
   except:
      return render_template('detection.html')

@app.route('/run_script_phone', methods=['GET', 'POST'])
def run_script_phone():
   try:
      if request.method == "POST":
         ip_address = request.form.get("ip")
      result = subprocess.check_output("python yolov5/detect.py --source "+ip_address+ "/video --weights yolov5s.pt --conf 0.4", shell=True)
      return render_template('http://127.0.0.1:5000', **locals())
   except:
      return render_template('detection.html')

if __name__ == '__main__':      
    app.run(host='0.0.0.0')