# 도어락 제어를 위한 구조 설명




## 제품
* 도어락 밀레시스텍 MI-2300


![도어락](https://user-images.githubusercontent.com/71259069/101465606-7f0d2900-3983-11eb-8056-d23ded5b4118.PNG)



* 릴레이 JQC-3FF-S-Z


![릴레이](https://user-images.githubusercontent.com/71259069/101465641-88969100-3983-11eb-9ddc-a872de217201.PNG)




## 도어락 내부 구조도
* Tact Switch 버튼


![tact-sw-6-500](https://user-images.githubusercontent.com/71259069/101466652-baf4be00-3984-11eb-8742-40080f84b984.jpg)

* 도어락 내부


![KakaoTalk_20201208_183741322](https://user-images.githubusercontent.com/71259069/101466459-85e86b80-3984-11eb-9658-fc200c5fd143.jpg)


## 릴레이 구성도

![도어락low](https://user-images.githubusercontent.com/71259069/101478068-73296300-3993-11eb-8c45-1f722c87dad0.png)


![도어락high](https://user-images.githubusercontent.com/71259069/101478074-745a9000-3993-11eb-95b5-088cd4fcab0b.png)




## 동작 설명


해당 도어락은 Tack Switch 구조로 스위치 단자에 전류가 쇼트될때 신호를 입력받아 동작합니다.

따라서 스위치와 연결된 (초록색)점퍼선과 건전지 단자와 연결된 (보라색)점퍼선을 연결하면 Lock/unLock 기능을 수행합니다.

릴레이를 이용해 각 점퍼선을 com과 no에 연결하고,

라즈베리파이에서 relay.py 코드를 이용해 HIGH 신호가 입력 받는다면

두 선을 쇼트시켜서 도어락을 Lock/unLock 시킵니다.
