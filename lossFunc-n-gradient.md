$$ \text{가중치 업데이트}: \Delta weight_i = (y_i - \hat{y_i}) \times x_i \times \eta $$

$$ \eta: \text{learning rate} $$

<br>

$$ \Delta weight = \text{error} \times \text{input} \times \eta $$

<br>

손실함수의 기울기 = 0 -> 경사하강법에서 손실함수의 output을 최소화 하는 방법

$$ L = MSE(error) $$

$$ \Delta L = 0 \text{ 이 될 경우, 손실함수의 outpput을 최소화 가능.}$$

여기서 가중치 (w)에 대한 손실 함수의 기울기(편미분)를 계산하면:

$$ \frac{\partial L}{\partial w} = (\text{output} - \text{target}) \times \text{input} $$

여기서 (\text{output} - \text{target} = -\text{error})이므로:

$$ \frac{\partial L}{\partial w} = -\text{error} \times \text{input} $$

하지만 경사하강법에서는 손실을 최소화하기 위해 기울기의 반대 방향으로 이동해야 하므로:

$$ \Delta w = -\eta \times \frac{\partial L}{\partial w} = \eta \times \text{error} \times \text{input} $$

이제 퍼셉트론 학습 규칙과 경사하강법을 비교해보면, 두 방법 모두 같은 업데이트 공식을 따릅니다:

$$ \Delta w = \eta \times \text{error} \times \text{input} $$

따라서, (\text{error} \times \text{input})이 손실 함수의 기울기(gradient)로 사용되는 이유는 손실 함수를 최소화하기 위해 가중치를 조정하는 과정에서 자연스럽게 도출되기 때문입니다.

이해에 도움이 되었길 바랍니다. 추가 질문이 있으시면 언제든지 말씀해 주세요!
