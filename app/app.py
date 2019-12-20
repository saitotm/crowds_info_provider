from flask import Flask, render_template, request, url_for
import serial

app = Flask(__name__)

level = [700, 1000, 1500]

@app.route('/')
def index():
    co2 = get_co2()

    if co2 < level[0]:
        img = 'img/face_0.png'
        state = '特に問題はありません'

    elif co2 < level[1]:
        img = 'img/face_1.png'
        state = '注意が必要です'
    
    elif co2 < level[2]:
        img = 'img/face_2.png'
        state = '眠気・不活発になるレベルです'
    
    else:
        img = 'img/face_3.png'
        state = '健康被害の出る可能性があります'
        
    return render_template('index.html', state=state, img=img, co2=co2)

def get_co2():
    ser = serial.Serial('/dev/cu.usbmodem1424301', 9600, timeout=None)
    line = ser.readline()
    line1 = int(line.rstrip().decode())
    ser.close()
    return line1

app.run(port=8000, debug=True)