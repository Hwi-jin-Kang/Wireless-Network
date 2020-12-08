# TELEGRAM
  텔레그램을 통해 얼굴인식에 성공하면 성공한 사람의 얼굴과 'open the door!'이라는 문구를 같이 텔레그램 봇으로
  전송합니다.
# 동작방식
  Telepot을 통해 텔레그램 봇이랑 연동하였고 openCV를 활용하여서 이미지 캡쳐는 cv2.imwrite를 통해 이미지를 저장하고 
  bot.sendPhoto로 캡쳐한 이미지를 전송하고 bot.sendMessage를 통해 'open the door!' 문구를 보냅니다.
