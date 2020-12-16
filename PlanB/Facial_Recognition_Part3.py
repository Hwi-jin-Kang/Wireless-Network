import cv2
import numpy as np
from os import listdir
from os.path import isfile, join
import telepot
import picamera
import time
import RPi.GPIO as GPIO


#part2와 같은 학습. 
data_path = 'faces/' #이미지가 저장된 경로 설정.
onlyfiles = [f for f in listdir(data_path) if isfile(join(data_path,f))] #faces에 저장된 이미지 1개씩 불러와서 저장

Training_Data, Labels = [], [] #배열설정.

for i, files in enumerate(onlyfiles): #이미지 1개씩 불러오기.
    image_path = data_path + onlyfiles[i] # 이미지 경로 설정. ex) faces/image1.jpg
    images = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    Training_Data.append(np.asarray(images, dtype=np.uint8))
    Labels.append(i)

Labels = np.asarray(Labels, dtype=np.int32)

model = cv2.face.LBPHFaceRecognizer_create()

model.train(np.asarray(Training_Data), np.asarray(Labels))

print("Model Training Complete!!!!!")
# 여기까지 part2와 동일

#여기서부터 part1의 이미지 촬영.
face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') #얼굴패턴 참조.

def face_detector(img, size = 0.5):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray,1.3,5)

    if faces is():
        return img,[]

    for(x,y,w,h) in faces:
        cv2.rectangle(img, (x,y),(x+w,y+h),(0,255,255),2)
        roi = img[y:y+h, x:x+w]
        roi = cv2.resize(roi, (200,200))

    return img,roi #검출된 자표에 사각 박스를 그리고 검출된 부위를 잘라서 리턴값으로 전달함.

cap = cv2.VideoCapture(0) #카메라 열기
cap.set(cv2.CAP_PROP_FRAME_WIDTH,1280) #카메라 사이즈 조절
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,800) #카메라 사이즈 조절
fps = cap.get(cv2.CAP_PROP_FPS)
print("Frames per second using video.get(cv2.CAP_PROP_FPS) : {0}".format(fps))
while True:
    #반복으로 카메라로부터 사진 한장씩 읽기.
    ret, frame = cap.read()

    image, face = face_detector(frame)
    #위에서 학습한 모델로 예측을 시도함.
    try:
        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
        result = model.predict(face)
        #result[1]은 신뢰도, 0에 가까울수록 자신과 같다는 의미를 나타냅니다.
        if result[1] < 500:
            confidence = int(100*(1-(result[1])/300))
            display_string = str(confidence)+'% Confidence it is user'
            #유사도를 화면에 표시하기 위한 것.
        cv2.putText(image,display_string,(100,120), cv2.FONT_HERSHEY_COMPLEX,1,(250,120,255),2)

        #유사도 설정. 78퍼센트를 넘으면 해당 코드 작동.
        if confidence > 78:
            cv2.putText(image, "Unlocked", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
            
            #얼굴 인식에 성공시
            GPIO.setmode(GPIO.BCM) 
            GPIO.setup(18, GPIO.OUT) #18번 핀을 작동시켜서
            GPIO.output(18, True) # 전류를 보냄. -> 도어락 작동을 의미
            time.sleep(2)
            GPIO.cleanup()
            #telegram, zigbee
            telegram_id='1446929504' #텔레그램 아이디 설정
            my_token = '1499970896:AAGpsbRzUTrNZZo_wDQ7BTzIhRKCiUALsKI' #토큰
            cv2.imwrite('/home/pi/work1/Facial-Recognition/image/image.jpg',image) 
            bot = telepot.Bot(my_token)              
            msg = 'open the door!' #전송할 메세지 작성.
            bot.sendPhoto(chat_id = telegram_id, photo=open('/home/pi/work1/Facial-Recognition/image/image.jpg','rb'))
            #이미지를 전송을 위한 
            #해당 로컬에 저장된 경로에 저장된 이미지 전송. -> 파일명, 디렉터리명 주의.
            bot.sendMessage(chat_id = telegram_id, text = msg)
            cv2.imshow('Face Cropper', image) #카메라 키기.

        else: #유사도를 못넘을시
            cv2.putText(image, "Locked", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2) #lock를 출력함.
            cv2.imshow('Face Cropper', image) #카메라 작동.
 

    except:
        #얼굴 검출이 안될경우.
        cv2.putText(image, "Face Not Found", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2)
        cv2.imshow('Face Cropper', image) #얼굴을 찾을 수 없다는 메세지를 출력후 카메라 켜기.
        pass

    if cv2.waitKey(1)==13:
        break


cap.release()
cv2.destroyAllWindows()
