# Plan B (완료)
얼굴 검출과 학습, 인식 완료

얼굴 인식 -> 도어락 시스템 작동 (Open)

사용 모듈 : 라즈베리파이 1, 파이카메라, 릴레이 모듈, 도어락
-> 라즈베리 파이 하나에 다이렉트 연결

# Plan A (개발중단)
기존 Plan B에서 라즈베리파이 2개를 이용하여 지그비 통신으로 얼굴 인식과 도어락 Open

동작 : 카메라로 얼굴이 인식되면 A지그비 통신 -> B지그비로 인식 완료 값을 받아 도어락 Open

# 진행 보고 

2020/12/01
- 텔레그램 통신 성공

2020/12/04
- 얼굴 검출 및 인식 성공

2020/12/07
- 릴레이 모듈 + 도어락 동작 성공

2020/12/08
- 얼굴 인식 프로그램과 텔레그램 통신 성공

2020/12/08
- 지그비 시리얼 통신 시도 -> 실패 

2020/12/11
- 얼굴 인식 -> 인식률 78% 이상-> 도어락 Open(다이렉트) 성공 -> 텔레그램 

2020/12/15
- 지그비 송수신 코드 수정 후 재시도 -> 실패 
