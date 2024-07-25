### c1. 퍼셉트론 학습 알고리즘

node와 weight로 이루어짐

입력 -> 신경망 계산 -> 출력

신경망 학습: weight 조절

---

날씨 예측 퍼셉트론

구름 양, 바람 세기 -> 신경망 -> 맑음 or 비

x1 = 0 -> 구름 0
x1 = 1 -> 구름 100%

x2 = 0 -> 바람 0
x2 = 1 -> 바람 100%

y = 0 -> 맑음
y = 1 -> 비

---

퍼셉트론 학습 방법

new weight = now weight + now input \* error \* learning rate
