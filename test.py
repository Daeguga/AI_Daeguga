import modi_plus
from modi_plus.module.output_module import display, led
from modi_plus.module.input_module import button

import cv2
import numpy as np

import requests
import time
import time
import io

def compute_hog_features(img, hog_descriptor):
    h = hog_descriptor.compute(img)
    return h

def predict(img, svm, hog_descriptor):
    img = cv2.resize(img, (128, 256))
    h = compute_hog_features(img, hog_descriptor)
    h = h.reshape(1, -1)
    _, result = svm.predict(h)
    return result[0][0]

def check(path):
    test_img_p = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    result_p = predict(test_img_p, svm, hog)
    result_txt =""
    result = 0
    isComplete = True
    if result_p == 0:
        # 31 road
        result_txt="Come to teacher's room."
        result = 3
    elif result_p == 1:
        # god rock
        result_txt="Uniform!!"
        result = 1
    elif result_p == 2:
        # 2.28 park
        result = 4
    elif result_p == 3:
        # e world
        result_txt="Uniform!!"
        result = 5
    elif result_p == 4:
        # daegu art museum
        result_txt="Uniform!!"
        result = 6
    elif result_p == 5:
        # daegu park
        result_txt="Uniform!!"
        result = 7
    elif result_p == 6:
        # spark land
        result_txt="Uniform!!"
        result = 9
    elif result_p == 7:
        # songhae park
        result_txt="Uniform!!"
        result = 10
    elif result_p == 8:
        # west door market
        result_txt="Uniform!!"
        result = 11
    elif result_p == 9:
        # susung lake
        result_txt="Uniform!!"
        result = 12
    elif result_p == 10:
        # kim gwangseok road
        result_txt="Uniform!!"
        result = 13
    elif result_p == 11:
        # daegu science museum
        result_txt="Uniform!!"
        result = 8
    else:
        result_txt="place NOT FOUND!"
        isComplete=False
    return result, isComplete

hog = cv2.HOGDescriptor()

bundle: modi_plus.MODIPlus = modi_plus.MODIPlus()

mydisplay: display.Display = bundle.displays[0]
myled: led.Led = bundle.leds[0]

shutter: button.Button = bundle.buttons[0]

cap = cv2.VideoCapture(0)

svm = cv2.ml.SVM_load('hog_svm_model.yml')

test_image = []
test_image.append(f"./test.jpg")

userId = 1

while True:
    ret, frame = cap.read()
    if shutter.pressed:
        myled.turn_on()
        cv2.imwrite('test.jpg', frame)

        result, isComplete = check('test.jpg')

        print("result", result)
        print("isComplete", isComplete)

        # 이미지를 이용한 AI 검사
        pointNum = result # 어떤 장소인지 검사
        if isComplete:
            request_param = {
                "userId": userId,
                "pointId": pointNum
            }
            response = requests.post("https://daegugo.baekjoon.kr/complete", params=request_param)
            if (response.status_code == 200):
                mydisplay.write_text("success")
                myled.turn_off()
                time.sleep(2)
                mydisplay.reset()
