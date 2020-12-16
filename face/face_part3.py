import cv2 
import numpy as np # 배열계산을 편하게 하기위해 numpy 모듈 사용
from os import listdir # 운영체제에서 제공되는 여러 기능을 파이썬에 수행할 수 있게 해줌.
                       # listdir -> 특정 경로에 존재하는 파일과 디렉터리 목록을 구하는 함수
from os.path import isfile, join # isfile -> 경로가 파일인지 아닌지 검사, 파일인 경우 True, 그 외의 경우 False 반환
                                 # joim -> 해당 OS형식에 맞도록 입력 받은 경로를 연결

data_path = 'faces/' # faces폴더에 있는 파일 리스트 얻기 
onlyfiles = [f for f in listdir(data_path) if isfile(join(data_path,f))]

Training_Data, Labels = [], []

for i, files in enumerate(onlyfiles): # in enumerate -> 반복문 사용시 몇번째 반복문인지 확인일 필요할때 사용함
    image_path = data_path + onlyfiles[i]
    images = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE) # cv2.imread -> 이미지 파일을 읽는 함수, 절대/상대 경로 설정 가능
    Training_Data.append(np.asarray(images, dtype=np.uint8))
    Labels.append(i)

Labels = np.asarray(Labels, dtype=np.int32)
# asarray와 array중 asarray를 사용한 이유는 array는 복사본을 만든 후 저장하고, asarray는 복사본 없이 값을 저장
# 원본값을 array와 asarray에 담고 원본값을 변경했을 경우, array는 본래 원본값을 가지고 있고 asarray는 바뀐 값을 저장함
# 복사본을 반환할 때 메모리 문제를 일으킬 소지를 차단하기위해 asarray를 사용

model = cv2.face.LBPHFaceRecognizer_create()
# LBPH를 사용할 새 변수 생성
#LBPHFaceRecognizer란 추출된 얼굴 이미지의 dataset을 구성하고 이 dataset에 포함된 각각의 얼굴이미지에 대해 특성을 분석하여 데이터에 저장
model.train(np.asarray(Training_Data), np.asarray(Labels))

print("Model Training Complete!!!!!")

face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def face_detector(img, size = 0.5):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray,1.3,5)
    # 받은 이미지에 대해 크기가 다른 object를 검출하는 함수.
    # 1.3은 ScaleFactor(이미지에서 얼굴 크기가 서로 다른것을 보상해주는 값), 5는 minNeighbor(얼굴 사이의 최소 간격(픽셀))

    if faces is():
        return img,[]

    for(x,y,w,h) in faces:
        cv2.rectangle(img, (x,y),(x+w,y+h),(0,255,255),2) # top-left corner와 bottom-right corner점을 연결하는 사각형을 그림
  # cv2.rectangle(img, start, end, color, thickness) -> img – 그림을 그릴 이미지, start – 시작 좌표, end – 종료 좌표, color – BGR형태의 Color, thickness (int) – 선의 두께. pixel
        roi = img[y:y+h, x:x+w]
        roi = cv2.resize(roi, (200,200)) # resize -> 크기 재조정

    return img,roi

cap = cv2.VideoCapture(0)
while True:

    ret, frame = cap.read()

    image, face = face_detector(frame)

    try:
        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
        result = model.predict(face) # 위에서 학습한 모델로 예측 시도하는 코드

        if result[1] < 500:
            confidence = int(100*(1-(result[1])/300))
            display_string = str(confidence)+'% Confidence it is user'
        cv2.putText(image,display_string,(100,120), cv2.FONT_HERSHEY_COMPLEX,1,(250,120,255),2) # cv2.FONT_HERSHEY_COMPLEX -> normal size serif font(그냥 폰트값)


        if confidence > 75:
            cv2.putText(image, "Unlocked", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
            cv2.imshow('Face Cropper', image)

        else:
            cv2.putText(image, "Locked", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
            cv2.imshow('Face Cropper', image)


    except:
        cv2.putText(image, "Face Not Found", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2)
        cv2.imshow('Face Cropper', image)
        pass

    if cv2.waitKey(1)==13:
        break


cap.release()
cv2.destroyAllWindows()
