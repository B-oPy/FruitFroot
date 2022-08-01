# FruitFroot
![icon](https://user-images.githubusercontent.com/104330432/182096938-c120bb18-b13a-4505-9927-c7ef29bef564.png)

## Description
> FruitFroot 프로젝트에서는 국내 사과와 배 과원들에서 발병한 사진들의 데이터를 통해 차후 발생할 질병들에 대한 구분과 그 질병들의 치료법을 제공하기 위한것을 목표로 하였다 
## 프로젝트 수행 절차 
![수행절차](https://user-images.githubusercontent.com/104330432/182101308-18e850fc-a356-4dac-8b92-8b9462a1e401.png)

## 사과와 배의 질병 이미지 데이터셋
> - 사과와 배의 과수화상병및 질병 이미지 분류 <br>
> - https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=146 에서 제공된 데이터를 바탕으로 이미지 분류 서비스를 구축하였다 
> - 제공된 데이터의 양이 너무나 방대하였기에 증강된 데이터들은 삭제를 하였고 사이즈를 (224, 224) 로 줄여서 총 사과 이미지 37024개와 배 이미지 22991개의 이미지 데이터들을 사용하였다
## 사과와 배에서 발생할 수있는 질병들
![이미지설명](https://user-images.githubusercontent.com/104330432/182098359-d91702ad-ff5b-4d9c-8710-bb4670dbf04c.png)

## Modeling 
> - 처음에는 정상 배, 배검은병무늬병, 배과수화상병, 정상 사과, 사과갈색무늬병, 사과과수화상병, 사과부란병, 사과점무늬낙엽병, 사과탄저병의 9개의 클래스로 구분하여 Multi-Class Image Classification을 하였으나 그 결과 사과와 배를 정확히 구분하지 못하는 모습을 보였다 <br>
> - 문제점을 개선하기 위해서 배에서는 정상, 배검은병무늬병, 배과수화상병 3개의 클래스, 사과에서는 정상, 사과갈색무늬병, 사과과수화상병, 사과부란병, 사과점무늬낙엽병, 사과탄저병 6개의 클래스로 구분지어 각각 MobileNet과 VGG19 모델로 학습을 시켰더니 아래와 같은 결과를 보여주었다 <br>

||배|사과|
|------|---|---|
||MobileNet|VGG19|
|Validation Loss|0.0595|0.0922|
|Validation Accuracy|0.9774|0.9705|

![수정됨_그림1](https://user-images.githubusercontent.com/104330432/182108170-fe66f30e-1b21-4a47-a481-8df1c4b28f85.png)


## Flask API
<img width="1315" alt="스크린샷 2022-08-01 오후 12 56 06" src="https://user-images.githubusercontent.com/104330432/182100793-283d5f93-dedb-444e-bbe8-4d042b4f7610.png">

> <b>데스크탑 화면</b>
<img height="500" width="600" alt="스크린샷 2022-07-29 오후 5 21 12" src="https://user-images.githubusercontent.com/104330432/182103930-d1466b11-291e-4e40-839d-ceb05e59fdc8.png">
<img height="500" width="600" alt="스크린샷 2022-07-29 오후 5 22 06" src="https://user-images.githubusercontent.com/104330432/182103990-fccc674b-37b4-4523-ae9c-bdd5222c5738.png">

> <b>모바일 화면</b>

![11](https://user-images.githubusercontent.com/104330432/182106789-cccc38df-0304-4ab4-9134-20895b1e5ce1.png)

> <b>자세히 보기 화면</b>

<img height="500" width="800" alt="스크린샷 2022-07-29 오후 4 14 08" src="https://user-images.githubusercontent.com/104330432/182104433-a964eed1-cfff-455d-b0bc-facf4cd4e88a.png">
