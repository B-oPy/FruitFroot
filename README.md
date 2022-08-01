# FruitFroot
![icon](https://user-images.githubusercontent.com/104330432/182096938-c120bb18-b13a-4505-9927-c7ef29bef564.png)

## 사과와 배의 질병 이미지 데이터
> - 사과와 배의 과수화상병및 질병 이미지 분류 <br>
> - https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=146 에서 제공된 데이터를 바탕으로 이미지 분류 서비스를 구축하였다 

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
