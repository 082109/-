
import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go

# ==========================================
# 1. 기본 설정 및 디자인
# ==========================================

st.set_page_config(
    page_title="Gradient Descent Lab",
    page_icon="📉",
    layout="wide"
)

st.markdown("""
<style>
.stApp {
    background-color: #101010;
    color: white;
}
h1, h2, h3 {
    color: white !important;
}
p, li {
    color: #dddddd;
    line-height: 1.8;
}
.card {
    background-color: #202020;
    border: 1px solid #383838;
    border-radius: 12px;
    padding: 20px;
    margin-bottom: 12px;
}
.card h3 {
    color: #ff5555 !important;
}
.red {
    color: #ff5555;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

st.title("📉 GRADIENT DESCENT LAB")
st.caption("미분으로 이해하는 인공지능의 학습 원리")

st.markdown("---")


# ==========================================
# 2. 최적화와 인공지능
# ==========================================

st.markdown("### 01 / OPTIMIZATION")
st.header("최적화란 무엇일까?")

st.write("""
최적화란 주어진 조건에서 함수의 값이 최대 또는 최소가 되는
상태를 찾아내는 과정이다.

인공지능 모델도 학습 과정에서 최적화를 활용한다.
모델이 예측한 값과 실제값 사이에는 오차가 발생할 수 있는데,
인공지능은 이 오차를 줄이도록 내부의 값을 조정한다.

이때 조정하는 대표적인 값이 가중치와 편향이다.
""")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="card">
    <h3>가중치 (Weight)</h3>
    입력된 정보가 예측 결과에 얼마나 큰 영향을 미칠지
    결정하는 값이다.
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
    <h3>편향 (Bias)</h3>
    가중치와 입력값으로 계산한 결과에 추가하여
    예측 결과를 조정하는 값이다.
    </div>
    """, unsafe_allow_html=True)

st.write("""
인공지능은 학습하면서 가중치와 편향을 조금씩 수정한다.
이러한 값이 달라지면 모델의 예측 결과도 달라지고,
결과적으로 예측 오차도 달라진다.
""")

st.markdown("---")


# ==========================================
# 3. 손실함수
# ==========================================

st.markdown("### 02 / LOSS FUNCTION")
st.header("손실함수는 무엇일까?")

st.write("""
손실함수는 인공지능 모델의 예측값과 실제값 사이의 오차를
수학적으로 나타내는 함수이다.

예측값과 실제값의 차이가 클수록 손실함수의 값이 커지고,
오차가 줄어들수록 손실함수의 값도 작아지도록 만들 수 있다.

인공지능은 이 손실함수의 값을 최소화하는 방향으로 학습한다.
""")

st.latex(r"J(\theta)")

st.write("""
여기서 J는 손실함수이고, θ(세타)는 모델이 조정하는
가중치와 편향 등의 값을 의미한다.

즉, 인공지능은 손실함수의 값을 줄이기 위해
가중치와 편향을 계속 수정하는 것이다.
""")

st.markdown("""
<div class="card">
<h3>핵심 질문</h3>
<p>
그렇다면 인공지능은 현재 손실함수의 값이 어느 방향으로
줄어드는지 어떻게 알 수 있을까?
</p>
<p class="red">
이때 활용하는 것이 바로 미분이다.
</p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")


# ==========================================
# 4. 미분과 경사하강법의 관계
# ==========================================

st.markdown("### 03 / DERIVATIVE")
st.header("미분은 경사하강법과 어떤 관계가 있을까?")

st.subheader("① 미분은 순간변화율을 알려 준다")

st.write("""
미분은 특정한 위치에서 함수의 순간변화율을 구하는 방법이다.

순간변화율은 현재 위치에서 x값이 아주 조금 변할 때
y값이 얼마나 빠르게 변하는지를 나타낸다.

그래프에서는 해당 위치에 그은 접선의 기울기로 이해할 수 있다.
""")

st.latex(r"f'(x)=\text{순간변화율}")

st.write("""
경사하강법에서는 이 미분값을 이용해
현재 위치에서 함수의 값이 증가하는지 감소하는지 판단한다.
""")

st.subheader("② 미분값에 따라 이동 방향이 달라진다")

st.write("""
함수의 최솟값을 찾는 상황을 생각해 보자.

현재 위치에서 미분값이 양수라면 접선의 기울기가 양수라는 뜻이다.
이때 오른쪽으로 이동하면 함수값이 증가하는 방향이므로,
함수값을 줄이려면 왼쪽으로 이동해야 한다.

반대로 미분값이 음수라면 접선의 기울기가 음수라는 뜻이다.
이때는 오른쪽으로 이동할수록 함수값이 감소하므로,
오른쪽으로 이동해야 한다.
""")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="card">
    <h3>미분값이 양수 (+)</h3>
    <p>접선이 오른쪽 위로 올라가는 모양이다.</p>
    <p>함수값을 줄이려면 왼쪽으로 이동한다.</p>
    <h2>←</h2>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
    <h3>미분값이 음수 (-)</h3>
    <p>접선이 오른쪽 아래로 내려가는 모양이다.</p>
    <p>함수값을 줄이려면 오른쪽으로 이동한다.</p>
    <h2>→</h2>
    </div>
    """, unsafe_allow_html=True)

st.subheader("③ 미분값을 직접 확인해 보자")

st.write("""
아래 함수에서 x의 위치를 바꾸어 보자.
현재 위치의 접선과 미분값이 어떻게 달라지는지 확인할 수 있다.
""")

st.latex(r"f(x)=x^2+2")
st.latex(r"f'(x)=2x")

a = st.slider(
    "현재 위치 x",
    min_value=-8.0,
    max_value=8.0,
    value=5.0,
    step=0.5,
    key="derivative_x"
)

# 현재 위치의 함수값과 미분값
fa = a**2 + 2
slope = 2*a

# 접선의 방정식
x_tangent = np.linspace(-10, 10, 300)
y_tangent = fa + slope * (x_tangent - a)

x_curve = np.linspace(-10, 10, 400)
y_curve = x_curve**2 + 2

fig_derivative = go.Figure()

fig_derivative.add_trace(go.Scatter(
    x=x_curve,
    y=y_curve,
    mode="lines",
    name="함수",
    line=dict(color="#ff5555", width=3)
))

fig_derivative.add_trace(go.Scatter(
    x=x_tangent,
    y=y_tangent,
    mode="lines",
    name="현재 위치의 접선",
    line=dict(color="#2589ff", width=2, dash="dash")
))

fig_derivative.add_trace(go.Scatter(
    x=[a],
    y=[fa],
    mode="markers",
    name="현재 위치",
    marker=dict(color="yellow", size=12)
))

fig_derivative.update_layout(
    template="plotly_dark",
    paper_bgcolor="#101010",
    plot_bgcolor="#202020",
    xaxis_title="x",
    yaxis_title="f(x)",
    height=450
)

st.plotly_chart(fig_derivative, use_container_width=True)

col1, col2 = st.columns(2)

with col1:
    st.metric("현재 함수값", f"{fa:.2f}")

with col2:
    st.metric("현재 미분값", f"{slope:.2f}")

if slope > 0:
    st.info("미분값이 양수야. 함수값을 줄이려면 왼쪽으로 이동해야 해.")
elif slope < 0:
    st.info("미분값이 음수야. 함수값을 줄이려면 오른쪽으로 이동해야 해.")
else:
    st.success("미분값이 0이야. 이 함수에서는 최솟값에 도달한 상태야.")

st.write("""
**여기서 기억할 점!**

미분값은 단순히 함수의 높이를 알려 주는 것이 아니다.
현재 위치에서 함수가 어느 방향으로 얼마나 빠르게 변하는지를
알려 주기 때문에 경사하강법에서 중요한 역할을 한다.
""")

st.markdown("---")


# ==========================================
# 5. 학습률과 경사하강법 수식
# ==========================================

st.markdown("### 04 / GRADIENT DESCENT FORMULA")
st.header("미분값으로 다음 위치를 계산한다")

st.write("""
미분값을 구했다면 이제 함수값이 감소하는 방향으로
얼마나 이동할지 결정해야 한다.

이때 사용하는 값이 학습률이다.
""")

st.subheader("학습률 (Learning Rate)")

st.write("""
학습률은 한 번의 계산에서 현재 값을 얼마나 크게 수정할지
결정하는 값이다.

미분값이 이동 방향을 알려 준다면,
학습률은 그 방향으로 얼마나 이동할지 조절한다.
""")

st.markdown("""
<div class="card">
<h3>미분값과 학습률의 차이</h3>
<p><b>미분값</b> : 어느 방향으로 이동해야 하는지 판단하는 기준</p>
<p><b>학습률</b> : 한 번에 얼마나 이동할지 조절하는 값</p>
</div>
""", unsafe_allow_html=True)

st.subheader("경사하강법의 수식")

st.latex(r"x_{t+1}=x_t-\alpha f'(x_t)")

st.write("""
이 수식은 다음 위치를 계산하는 방법을 나타낸다.

현재 위치에서 미분값에 학습률을 곱한 값을 빼면
다음 위치를 구할 수 있다.
""")

st.markdown("""
<div class="card">
<h3>수식의 의미</h3>
<p><b>xₜ</b> : 현재 위치</p>
<p><b>xₜ₊₁</b> : 다음 위치</p>
<p><b>f'(xₜ)</b> : 현재 위치에서의 미분값</p>
<p><b>α</b> : 학습률</p>
</div>
""", unsafe_allow_html=True)

st.write("""
왜 미분값을 빼는 걸까?

미분값이 양수이면 양수를 빼기 때문에 x값이 작아진다.
미분값이 음수이면 음수를 빼기 때문에 x값이 커진다.

따라서 이 수식은 미분값의 반대 방향으로 이동하도록 만들어져 있다.
이렇게 함수값이 감소하는 방향으로 이동하는 과정을 반복하는 것이
경사하강법이다.
""")

st.subheader("인공지능에서는 어떻게 적용될까?")

st.write("""
실제 인공지능 모델에서는 하나의 x값이 아니라
여러 개의 가중치와 편향을 동시에 조정한다.

이때 각 변수에 대한 편미분값을 모아 기울기(Gradient)를 구한다.
기울기는 여러 변수의 변화 방향을 함께 나타내는 값이다.

따라서 실제 인공지능 모델에서는 다음과 같은 수식을 사용한다.
""")

st.latex(r"\theta_{t+1}=\theta_t-\alpha\nabla J(\theta_t)")

st.write("""
여기서 ∇J(θₜ)는 현재 파라미터 위치에서 구한 손실함수의 기울기이다.

즉, 하나의 변수만 다루는 경우에는 미분값을 사용하고,
여러 변수를 다루는 경우에는 각 변수의 편미분값으로 구성된
기울기를 사용한다.
""")

st.markdown("---")


# ==========================================
# 6. 그래프를 이용한 경사하강법 체험
# ==========================================

st.markdown("### 05 / INTERACTIVE EXPERIMENT")
st.header("직접 경사하강법 실험하기")

st.write("""
이번에는 미분을 이용해 실제로 최솟값을 찾아보자.

실험에 사용할 함수는 다음과 같다.
""")

st.latex(r"f(x)=x^2+2")
st.latex(r"f'(x)=2x")

st.write("""
이 함수는 x=0일 때 최솟값 2를 갖는다.
시작 위치와 학습률을 바꾸면서 최솟값을 찾아가는 과정을 확인해 보자.
""")

col1, col2 = st.columns(2)

with col1:
    start_x = st.slider(
        "시작 위치",
        -10.0, 10.0, 10.0,
        step=0.5
    )

with col2:
    learning_rate = st.slider(
        "학습률",
        0.01, 1.50, 0.10,
        step=0.01,
        format="%.2f"
    )

iterations = st.slider(
    "반복 횟수",
    1, 30, 10
)

# 경사하강법 계산
x_values = [start_x]
loss_values = [start_x**2 + 2]

current_x = start_x

for i in range(iterations):
    derivative = 2 * current_x
    current_x = current_x - learning_rate * derivative

    x_values.append(current_x)
    loss_values.append(current_x**2 + 2)

# 그래프
limit = max(10, min(100, max(abs(v) for v in x_values) * 1.2))

x_graph = np.linspace(-limit, limit, 400)
y_graph = x_graph**2 + 2

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=x_graph,
    y=y_graph,
    mode="lines",
    name="손실함수",
    line=dict(color="#ff5555", width=3)
))

fig.add_trace(go.Scatter(
    x=x_values,
    y=loss_values,
    mode="lines+markers",
    name="이동 경로",
    line=dict(color="#2589ff", width=2),
    marker=dict(size=8)
))

fig.add_trace(go.Scatter(
    x=[0],
    y=[2],
    mode="markers",
    name="최솟값",
    marker=dict(color="yellow", size=13, symbol="star")
))

fig.update_layout(
    template="plotly_dark",
    paper_bgcolor="#101010",
    plot_bgcolor="#202020",
    xaxis_title="x",
    yaxis_title="f(x)",
    height=480
)

st.plotly_chart(fig, use_container_width=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("학습률", f"{learning_rate:.2f}")

with col2:
    st.metric("최종 x값", f"{current_x:.5f}")

with col3:
    st.metric("최종 함수값", f"{loss_values[-1]:.5f}")

if abs(current_x) < 0.1:
    st.success("최솟값에 가까워졌어!")
elif learning_rate == 1.0:
    st.warning("최솟값을 기준으로 양쪽을 반복해서 이동하고 있어.")
elif learning_rate > 1.0:
    st.error("학습률이 너무 커서 최솟값에서 멀어지고 있어.")
else:
    st.info("반복 횟수를 늘려 최솟값에 가까워지는지 확인해 보자.")

st.subheader("반복 과정 확인하기")

result = pd.DataFrame({
    "반복 횟수": range(iterations + 1),
    "현재 위치": [round(v, 5) for v in x_values],
    "함수값": [round(v, 5) for v in loss_values]
})

st.dataframe(result, use_container_width=True, hide_index=True)

st.markdown("---")


# ==========================================
# 7. 학습률 자유롭게 비교하기
# ==========================================

st.markdown("### 06 / LEARNING RATE EXPERIMENT")
st.header("학습률에 따라 어떻게 달라질까?")

st.write("""
학습률을 직접 바꾸면서 최솟값에 도달하는 과정이
어떻게 달라지는지 관찰해 보자.

학습률이 작으면 이동량도 작아져 최솟값에 도달하기까지
더 많은 반복이 필요할 수 있다.

반대로 학습률이 너무 크면 최솟값을 지나쳐
반복할수록 오히려 멀어질 수 있다.
""")

rate = st.slider(
    "비교할 학습률",
    0.01, 1.50, 0.60,
    step=0.01,
    format="%.2f",
    key="rate_compare"
)

compare_x = [10.0]
compare_y = [102.0]

current = 10.0

for i in range(30):
    current = current - rate * (2 * current)
    compare_x.append(current)
    compare_y.append(current**2 + 2)

    if abs(current) > 100000:
        break

display_count = min(len(compare_x), 30)

fig2 = go.Figure()

fig2.add_trace(go.Scatter(
    x=x_graph,
    y=y_graph,
    mode="lines",
    name="함수",
    line=dict(color="#ff5555", width=3)
))

fig2.add_trace(go.Scatter(
    x=compare_x[:display_count],
    y=compare_y[:display_count],
    mode="lines+markers",
    name="이동 과정",
    line=dict(color="#2589ff", width=2),
    marker=dict(size=7)
))

fig2.add_trace(go.Scatter(
    x=[0],
    y=[2],
    mode="markers",
    name="최솟값",
    marker=dict(color="yellow", size=13, symbol="star")
))

fig2.update_layout(
    template="plotly_dark",
    paper_bgcolor="#101010",
    plot_bgcolor="#202020",
    xaxis_title="x",
    yaxis_title="f(x)",
    height=450
)

st.plotly_chart(fig2, use_container_width=True)

if abs(current) < 0.1:
    st.success("최솟값에 가까워졌어!")
elif rate == 1.0:
    st.warning("최솟값을 중심으로 반복해서 움직이고 있어.")
elif rate > 1.0:
    st.error("학습률이 너무 커서 최솟값에서 멀어지고 있어.")
else:
    st.info("학습률과 반복 횟수를 바꾸어 결과를 비교해 보자.")

st.markdown("---")


# ==========================================
# 8. 마무리
# ==========================================

st.markdown("### 07 / SUMMARY")
st.header("오늘 배운 내용 정리")

summary = [
    ("미분", "현재 위치에서 함수의 순간변화율을 구한다."),
    ("미분값", "함수가 증가하거나 감소하는 방향과 변화 정도를 판단하는 데 활용한다."),
    ("학습률", "한 번의 이동에서 수정할 크기를 조절한다."),
    ("손실함수", "인공지능 모델의 예측 오차를 나타낸다."),
    ("경사하강법", "미분 또는 기울기를 활용해 손실함수의 값을 줄이는 최적화 알고리즘이다.")
]

for title, desc in summary:
    st.markdown(f"""
    <div class="card">
    <h3>{title}</h3>
    <p>{desc}</p>
    </div>
    """, unsafe_allow_html=True)

st.write("""
경사하강법은 단순히 값을 반복해서 바꾸는 방법이 아니다.
미분을 통해 현재 위치에서 함수가 어떻게 변하는지 파악하고,
그 정보를 바탕으로 함수값이 감소하는 방향으로 이동한다.

이처럼 미분은 경사하강법이 최솟값을 찾아가는 데 필요한
방향과 변화 정도를 알려 주는 핵심적인 수학적 도구이다.
""")
