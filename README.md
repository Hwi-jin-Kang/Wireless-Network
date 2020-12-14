# 무선 네트워크 프로젝트
* 3조 - 킹콩 킹두부

# 팀원
* 강휘진, 곽범수, 백재원, 임진수, 진재혁

# 프로젝트 정보
## 얼굴 인식 도어락
  * 개요 : [기사](http://www.ablenews.co.kr/News/NewsContent.aspx?CategoryCode=0014&NewsCode=001420190502111917597795)를 읽고 '리모컨 도어락'에도 불편함, 개선사항이 있을 것으로 판단돼 프로젝트를 진행

  * 목적 : 라즈베리파이와 카메라 센서, 도어락을 이용해 기존 '버튼 및 리모콘 도어락'을 보완, 개선

  * 모듈 구성도

   ![슬라이드6](https://user-images.githubusercontent.com/71058308/101472201-39e8f700-3983-11eb-97dc-17f221855242.PNG)

  * 동작 방식 

   ![슬라이드9](https://user-images.githubusercontent.com/71058308/101472404-88969100-3983-11eb-9c7f-1418448ae587.PNG)

   ![슬라이드10](https://user-images.githubusercontent.com/71058308/101472409-89c7be00-3983-11eb-84bc-17c92892c80a.PNG)

   ![슬라이드11](https://user-images.githubusercontent.com/71058308/101472413-89c7be00-3983-11eb-9d12-4b745a464b27.PNG)
   
  * openCV란? 
  
    Open Source Computer Vision
    
    영상/동영상 처리에 사용할 수 있는 오픈소스 라이브러리
    
    계산 효율성과 실시간 응용 프로그램에 중점을 두고 설계됨
    
  * 유튜브 영상
  
    [동작 영상](https://www.youtube.com/watch?v=3K4KkrcV4Vw)

   ### Plan B (완료)
    얼굴 검출과 학습, 인식 완료

    얼굴 인식 -> 도어락 시스템 작동 (Open)

    사용 모듈 : 라즈베리파이 1, 파이카메라, 릴레이 모듈, 도어락
     -> 라즈베리 파이 하나에 다이렉트 연결

   ### Plan A (개발중)
    기존 Plan B에서 라즈베리파이 2개를 이용하여 지그비 통신으로 얼굴 인식과 도어락 Open

    동작 : 카메라로 얼굴이 인식되면 A지그비 통신 -> B지그비로 인식 완료 값을 받아 도어락 Open

    
   ### 진행 보고 

    2020/12/01
    - 텔레그램 통신 성공

    2020/12/04
    - 얼굴 검출 및 인식 성공

    2020/12/07
    - 릴레이 모듈 + 도어락 동작 성공

    2020/12/08
    - 얼굴 인식 프로그램과 텔레그램 통신 성공

    2020/12/11
    - 얼굴 인식 -> 인식률 78% 이상-> 도어락 Open(다이렉트) 성공 -> 텔레그램 
    
  * 참고
  
    [도어락->IOT](http://mibediy.blogspot.com/2016/02/4-iot-hw.html)
  
    [openCV](https://m.blog.naver.com/PostView.nhn?blogId=chandong83&logNo=221436424539&proxyReferer=https:%2F%2Fblog.naver.com%2Fchandong83%2F221436424539)
    
    
    

 ## 파일 리스트
  
   ./DoorLock (도어락 Lock/Unlock 코드)
  
   ./Telegram (텔레그램 사진/문구 전송 코드)
 
   ./face (openCV를 이용한 얼굴 인식 코드)
  
   ./zigbee (지그비 무선 통신 코드)
