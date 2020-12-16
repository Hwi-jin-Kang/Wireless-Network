import cv2
import numpy as np
from os import listdir
from os.path import isfile, join

data_path = 'faces/'
#faces 폴더에 있는 파일 리스트를 얻기
onlyfiles = [f for f in listdir(data_path) if isfile(join(data_path,f))]

#데이터와 매칭될 라벨 변수
Training_Data, Labels = [], []

#파일 개수만큼 루프
for i, files in enumerate(onlyfiles):
    image_path = data_path + onlyfiles[i]
    #이미지 불러오기
    images = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    #Training_Data 리스트에 이미지를 바이트 배열로 추가
    Training_Data.append(np.asarray(images, dtype=np.uint8))
    
    #Labels 리스트엔 카운트 번호 추가
    Labels.append(i)
#Labels를 32 비트 정수로 변환
Labels = np.asarray(Labels, dtype=np.int32)
#모델 생성
model = cv2.face.LBPHFaceRecognizer_create()
#학습 시작
model.train(np.asarray(Training_Data), np.asarray(Labels))

print("Model Training Complete!!!!!")


