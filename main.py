
import streamlit as st
import numpy as np
import plotly.graph_objects as go
# =====================================
# 05. 순간변화율에 따른 이동 방향
# =====================================
st.divider()
st.header("05. 순간변화율에 따라 이동 방향은 어떻게 달라질까?")

st.write("""
경사하강법은 현재 위치에서 구한 순간변화율을 이용해
손실 함수의 값이 작아지는 방향으로 이동한다.

이때 순간변화율의 부호에 따라 이동 방향이 달라진다.
""")

st.markdown("""
<div class="info-box">
<h3>순간변화율이 양수인 경우 (+)</h3>
현재 위치에서 x가 증가할수록 함수의 값도 증가한다.
따라서 함수의 값이 작아지는 왼쪽 방향으로 이동한다.
</div>
<br>
<div class="info-box">
<h3>순간변화율이 음수인 경우 (-)</h3>
현재 위치에서 x가 증가할수록 함수의 값은 감소한다.
따라서 함수의 값이 작아지는 오른쪽 방향으로 이동한다.
</div>
<br>
<div class="info-box">
<h3>순간변화율이 0인 경우</h3>
함수의 순간변화율이 0이 되는 지점에서는
그 순간 함수의 기울기가 수평이 된다.
</div>
""", unsafe_allow_html=True)

st.write("""
즉, 경사하강법은 순간변화율의 부호를 이용해
함수의 값이 감소하는 방향을 판단하고 이동한다.
""")

st.latex(r"x_{n+1}=x_n-\alpha f'(x_n)")


# =====================================
# 06. 학습률에 따른 차이
# =====================================
st.divider()
st.header("06. 학습률에 따라 결과가 어떻게 달라질까?")

st.write("""
학습률은 경사하강법에서 한 번 이동할 때의 조정 폭을 결정한다.
같은 함수와 같은 초기값을 사용하더라도 학습률에 따라
최솟값에 접근하는 속도와 이동 과정이 달라진다.

이를 확인하기 위해 다음 함수를 사용해 보자.
""")

st.latex(r"f(x)=x^2+2")

st.write("""
이 함수의 최솟값은 x=0일 때 2이다.
초기값을 8로 설정하고 학습률을 다르게 하여 비교해 보자.
""")

st.latex(r"f'(x)=2x")

st.latex(r"x_{n+1}=x_n-\alpha(2x_n)")

# 학습률 선택
selected_rate = st.select_slider(
    "비교할 학습률 선택",
    options=[0.1, 0.3, 0.6, 0.9, 1.0, 1.1],
    value=0.6
)

st.write(f"현재 선택한 학습률: **{selected_rate}**")

# 반복 계산
def run_gradient_descent(rate, start=8, count=15):
    xs = [start]

    for _ in range(count):
        current = xs[-1]
        next_value = current - rate * (2 * current)
        xs.append(next_value)

    return xs

rates = [0.1, 0.6, 1.0]

fig_rate = go.Figure()

# 손실 함수
x_curve = np.linspace(-9, 9, 400)
y_curve = x_curve ** 2 + 2

fig_rate.add_trace(go.Scatter(
    x=x_curve,
    y=y_curve,
    mode="lines",
    name="손실 함수",
    line=dict(color="#ff4545", width=3)
))

# 선택한 학습률의 이동 과정
selected_values = run_gradient_descent(selected_rate)

selected_losses = [
    x ** 2 + 2 for x in selected_values
]

fig_rate.add_trace(go.Scatter(
    x=selected_values,
    y=selected_losses,
    mode="lines+markers",
    name=f"학습률 {selected_rate}",
    line=dict(color="white", width=2, dash="dot"),
    marker=dict(size=9, color="white")
))

# 최솟값
fig_rate.add_trace(go.Scatter(
    x=[0],
    y=[2],
    mode="markers",
    name="최솟값",
    marker=dict(size=14, color="#ff4545", symbol="star")
))

fig_rate.update_layout(
    title=f"학습률 {selected_rate}일 때의 이동 과정",
    xaxis_title="x",
    yaxis_title="f(x)",
    template="plotly_dark",
    paper_bgcolor="#101010",
    plot_bgcolor="#1c1c1c",
    font=dict(color="white"),
    height=450
)

st.plotly_chart(fig_rate, use_container_width=True)

# 학습률별 비교 그래프
st.subheader("학습률별 이동 과정 비교")

fig_compare = go.Figure()

for rate in rates:
    xs = run_gradient_descent(rate)
    ys = [x ** 2 + 2 for x in xs]

    fig_compare.add_trace(go.Scatter(
        x=list(range(len(xs))),
        y=ys,
        mode="lines+markers",
        name=f"학습률 {rate}"
    ))

fig_compare.update_layout(
    title="반복 횟수에 따른 손실 함수 값의 변화",
    xaxis_title="반복 횟수",
    yaxis_title="손실 함수 값",
    template="plotly_dark",
    paper_bgcolor="#101010",
    plot_bgcolor="#1c1c1c",
    font=dict(color="white"),
    height=450
)

st.plotly_chart(fig_compare, use_container_width=True)

# 학습률 설명
st.subheader("학습률에 따른 특징")

st.markdown("""
<div class="info-box">
<h3>학습률이 작은 경우 (예: 0.1)</h3>
한 번에 이동하는 폭이 작다.
따라서 최솟값에 가까워지지만 더 많은 반복이 필요하다.
</div>
<br>
<div class="info-box">
<h3>학습률이 적절한 경우 (예: 0.6)</h3>
최솟값을 지나 반대편으로 이동할 수 있지만,
이동 폭이 점차 줄어들면서 최솟값에 가까워진다.
</div>
<br>
<div class="info-box">
<h3>학습률이 너무 큰 경우 (예: 1.0 이상)</h3>
최솟값을 지나 반대편으로 이동하는 현상이 반복될 수 있다.
이 함수에서는 학습률이 1이면 최솟값에 수렴하지 않고,
1보다 크면 최솟값에서 점점 멀어질 수 있다.
</div>
""", unsafe_allow_html=True)

st.success(
    "학습률은 단순히 이동하는 크기만 정하는 것이 아니라 "
    "최솟값에 얼마나 빠르고 안정적으로 접근하는지에도 영향을 준다."
)


# =====================================
# 07. 경사하강법 쉽게 이해하기
# =====================================
st.divider()
st.header("07. 경사하강법 쉽게 이해하기")

st.write("""
경사하강법을 이해하려면 산의 가장 낮은 곳을 찾아 내려가는 상황을 떠올려 보자.
산의 어느 지점에 서 있는 사람이 가장 낮은 장소를 찾아 이동한다고 생각하면 된다.
""")

st.markdown("""
<div class="info-box">
<h3>⛰️ 산을 내려가는 과정</h3>
산의 어느 지점에 서 있다면 주변 지형의 기울기를 살펴
어느 방향으로 내려가야 할지 판단할 수 있다.

경사하강법도 이와 비슷하다.
현재 위치에서 함수의 기울기를 확인하고,
함수의 값이 작아지는 방향으로 조금씩 이동한다.
이 과정을 반복하면 점차 가장 낮은 지점에 가까워진다.
</div>
""", unsafe_allow_html=True)

st.write("")
st.subheader("경사하강법의 네 가지 과정")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="info-box">
    <h3>01. 현재 위치 확인</h3>
    현재 손실 함수의 값이 어느 정도인지 확인한다.
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="info-box">
    <h3>02. 순간변화율 계산</h3>
    미분을 이용해 현재 위치에서 함수가
    어느 방향으로 변하는지 확인한다.
    </div>
    """, unsafe_allow_html=True)

with col1:
    st.markdown("""
    <div class="info-box">
    <h3>03. 이동 방향 결정</h3>
    손실 함수의 값이 작아지는 방향으로 이동한다.
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="info-box">
    <h3>04. 반복하기</h3>
    이동한 위치에서 다시 순간변화율을 구하고,
    이 과정을 반복하여 최솟값에 가까워진다.
    </div>
    """, unsafe_allow_html=True)

st.write("")
st.subheader("꼭 알아야 할 세 가지")

st.markdown("""
<div class="info-box">
<h3>① 손실 함수</h3>
인공지능의 예측값과 실제값 사이의 오차를 수치로 나타내는 함수이다.
</div>
<br>
<div class="info-box">
<h3>② 순간변화율</h3>
특정 위치에서 함수의 값이 얼마나 빠르게 변하는지를 나타낸다.
경사하강법은 미분으로 순간변화율을 구해 이동 방향을 판단한다.
</div>
<br>
<div class="info-box">
<h3>③ 학습률</h3>
한 번 이동할 때 얼마나 이동할지를 결정하는 값이다.
학습률이 크면 한 번에 많이 이동하고, 작으면 조금씩 이동한다.
</div>
""", unsafe_allow_html=True)

st.success(
    "경사하강법은 미분으로 현재 위치의 순간변화율을 구하고, "
    "손실 함수의 값이 작아지는 방향으로 값을 반복해서 조정하는 방법이다."
)

st.divider()
st.caption("GRADIENT DESCENT LAB. | Calculus × Artificial Intelligence")
