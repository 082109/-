
import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go

# --------------------------------------------------
# 기본 설정
# --------------------------------------------------
st.set_page_config(
    page_title="Gradient Descent Lab",
    page_icon="📉",
    layout="wide"
)

# --------------------------------------------------
# 디자인
# --------------------------------------------------
st.markdown("""
<style>
    .stApp {
        background-color: #101010;
        color: white;
    }

    h1, h2, h3 {
        color: white !important;
    }

    p, li, label {
        color: #dddddd;
    }

    .main-title {
        font-size: 42px;
        font-weight: 800;
        color: white;
        margin-bottom: 5px;
    }

    .sub-title {
        color: #aaaaaa;
        font-size: 17px;
        margin-bottom: 30px;
    }

    .section-number {
        color: #ff4b4b;
        font-size: 14px;
        font-weight: bold;
        letter-spacing: 2px;
    }

    .info-card {
        background-color: #1d1d1d;
        border: 1px solid #383838;
        border-radius: 12px;
        padding: 20px;
        height: 100%;
    }

    .info-card h3 {
        color: #ff5555 !important;
        margin-top: 0;
    }

    .info-card p {
        color: #dddddd;
        line-height: 1.6;
    }

    .highlight {
        color: #ff5555;
        font-weight: bold;
    }

    .result-card {
        background-color: #202020;
        border-left: 4px solid #ff4b4b;
        padding: 15px;
        border-radius: 7px;
        margin: 8px 0;
    }

    div[data-testid="stMetric"] {
        background-color: #202020;
        padding: 15px;
        border-radius: 10px;
    }

    hr {
        border-color: #383838;
    }
</style>
""", unsafe_allow_html=True)


# --------------------------------------------------
# 제목
# --------------------------------------------------
st.markdown(
    '<div class="main-title">GRADIENT DESCENT LAB</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="sub-title">미분으로 이해하는 인공지능의 학습 원리</div>',
    unsafe_allow_html=True
)

st.markdown("---")


# --------------------------------------------------
# 01. 경사하강법이란?
# --------------------------------------------------
st.markdown('<div class="section-number">01 / INTRODUCTION</div>',
            unsafe_allow_html=True)

st.header("경사하강법이란?")

st.write("""
경사하강법은 함수의 값이 작아지는 방향으로 조금씩 이동하면서
최솟값을 찾아가는 **최적화 방법**이다.

인공지능은 데이터를 학습하면서 예측한 값과 실제 값 사이의 오차를 줄여야 한다.
이때 오차를 함수로 나타낸 것이 손실함수이며,
경사하강법은 손실함수의 값을 줄이는 데 활용된다.

즉, 현재 위치에서 함수의 순간변화율을 확인하고
그 반대 방향으로 이동하면서 오차가 작아지는 지점을 찾아가는 것이다.
""")

st.markdown("""
<div class="result-card">
    <b>핵심 내용</b><br>
    경사하강법은 현재 위치에서 미분을 활용해 이동 방향을 정하고,
    함수의 값이 작아지는 방향으로 반복해서 이동하는 방법이다.
</div>
""", unsafe_allow_html=True)

st.markdown("---")


# --------------------------------------------------
# 02. 핵심 개념
# --------------------------------------------------
st.markdown('<div class="section-number">02 / KEY CONCEPTS</div>',
            unsafe_allow_html=True)

st.header("경사하강법을 이해하기 위한 핵심 개념")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="info-card">
        <h3>손실함수</h3>
        <p>
        인공지능이 예측한 값과 실제 값 사이의 오차를
        수학적으로 나타낸 함수이다.
        경사하강법은 이 함수의 값을 줄이는 것을 목표로 한다.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="info-card">
        <h3>미분</h3>
        <p>
        특정 지점에서 함수가 얼마나 빠르게 변하는지 나타낸다.
        순간변화율을 통해 함수의 값이 증가하는지 감소하는지
        판단할 수 있다.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="info-card">
        <h3>학습률</h3>
        <p>
        한 번 이동할 때 얼마나 큰 폭으로 움직일지 정하는 값이다.
        학습률에 따라 최솟값에 도달하는 과정과 속도가 달라진다.
        </p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")


# --------------------------------------------------
# 03. 경사하강법의 수학적 원리
# --------------------------------------------------
st.markdown('<div class="section-number">03 / MATHEMATICAL PRINCIPLE</div>',
            unsafe_allow_html=True)

st.header("경사하강법은 어떻게 계산할까?")

st.write("경사하강법은 다음과 같은 계산식을 반복해서 사용한다.")

st.latex(r"x_{n+1}=x_n-\alpha f'(x_n)")

st.write("""
- \(x_n\) : 현재 위치
- \(x_{n+1}\) : 다음에 이동할 위치
- \(f'(x_n)\) : 현재 위치에서의 순간변화율
- \(\alpha\) : 학습률
""")

st.info("""
현재 위치에서 순간변화율을 구한 뒤,
학습률을 곱한 값을 현재 위치에서 빼준다.
이 과정을 반복하면서 함수의 값이 작아지는 지점을 찾아간다.
""")

st.markdown("---")


# --------------------------------------------------
# 04. 직접 실험하기
# --------------------------------------------------
st.markdown('<div class="section-number">04 / INTERACTIVE EXPERIMENT</div>',
            unsafe_allow_html=True)

st.header("직접 경사하강법 실험하기")

st.write("""
아래 그래프는 함수 \(f(x)=(x-4)^2\)를 나타낸다.
시작 위치와 학습률, 반복 횟수를 바꾸면서
경사하강법이 최솟값을 찾아가는 과정을 확인해 보자.
""")

st.latex(r"f(x)=(x-4)^2")

col1, col2, col3 = st.columns(3)

with col1:
    start_x = st.slider(
        "시작 위치",
        min_value=-2.0,
        max_value=10.0,
        value=0.0,
        step=0.5
    )

with col2:
    learning_rate = st.slider(
        "학습률",
        min_value=0.05,
        max_value=0.95,
        value=0.25,
        step=0.05
    )

with col3:
    iterations = st.slider(
        "반복 횟수",
        min_value=1,
        max_value=30,
        value=5,
        step=1
    )

# 경사하강법 계산
x_values = [start_x]

for i in range(iterations):
    current_x = x_values[-1]
    derivative = 2 * (current_x - 4)
    next_x = current_x - learning_rate * derivative
    x_values.append(next_x)

loss_values = [(x - 4) ** 2 for x in x_values]

# 그래프 범위
x_min = min(-3, start_x - 1)
x_max = max(11, start_x + 1)

x_graph = np.linspace(x_min, x_max, 400)
y_graph = (x_graph - 4) ** 2

# 그래프 생성
fig = go.Figure()

fig.add_trace(go.Scatter(
    x=x_graph,
    y=y_graph,
    mode="lines",
    name="손실함수",
    line=dict(color="#ff4b4b", width=3)
))

fig.add_trace(go.Scatter(
    x=x_values,
    y=loss_values,
    mode="lines+markers",
    name="이동 경로",
    line=dict(color="#ffffff", width=2, dash="dot"),
    marker=dict(size=9, color="#ffffff")
))

fig.add_trace(go.Scatter(
    x=[4],
    y=[0],
    mode="markers",
    name="최솟값",
    marker=dict(size=13, color="#ff4b4b", symbol="star")
))

fig.update_layout(
    template="plotly_dark",
    paper_bgcolor="#101010",
    plot_bgcolor="#181818",
    xaxis_title="x",
    yaxis_title="f(x)",
    height=480,
    legend=dict(orientation="h", y=1.12),
    margin=dict(l=20, r=20, t=40, b=20)
)

st.plotly_chart(fig, use_container_width=True)

# 결과 표시
final_x = x_values[-1]
final_loss = loss_values[-1]

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("최종 위치", f"{final_x:.4f}")

with col2:
    st.metric("최종 손실함수 값", f"{final_loss:.4f}")

with col3:
    st.metric("반복 횟수", f"{iterations}회")

st.subheader("이동 과정 확인하기")

result_df = pd.DataFrame({
    "반복": list(range(iterations + 1)),
    "현재 위치": [round(x, 4) for x in x_values],
    "손실함수 값": [round(y, 4) for y in loss_values]
})

st.dataframe(result_df, use_container_width=True, hide_index=True)

st.markdown("""
<div class="result-card">
    <b>확인해 볼 점</b><br>
    학습률과 반복 횟수를 바꾸면 최솟값에 가까워지는 과정이 달라진다.
    시작 위치에서 출발해 점들이 최솟값인 x=4에 가까워지는 모습을 확인해 보자.
</div>
""", unsafe_allow_html=True)

st.markdown("---")


# --------------------------------------------------
# 05. 순간변화율에 따른 이동 방향
# --------------------------------------------------
st.markdown('<div class="section-number">05 / DIRECTION</div>',
            unsafe_allow_html=True)

st.header("순간변화율은 이동 방향을 어떻게 결정할까?")

st.write("""
경사하강법에서는 순간변화율의 부호를 통해
어느 방향으로 이동해야 함수의 값이 작아지는지 판단할 수 있다.
""")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="info-card">
        <h3>순간변화율이 양수인 경우 (+)</h3>
        <p>
        함수가 증가하는 방향이 오른쪽이므로,
        함수의 값이 작아지려면 왼쪽으로 이동해야 한다.
        </p>
        <p class="highlight">왼쪽 방향으로 이동</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="info-card">
        <h3>순간변화율이 음수인 경우 (-)</h3>
        <p>
        함수가 감소하는 방향이 오른쪽이므로,
        함수의 값이 작아지려면 오른쪽으로 이동해야 한다.
        </p>
        <p class="highlight">오른쪽 방향으로 이동</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<div class="info-card">
    <h3>순간변화율이 0인 경우</h3>
    <p>
    해당 지점에서 순간변화율이 0이므로,
    미분값을 이용한 이동량은 0이 된다.
    위 실험에서 사용한 아래로 볼록한 이차함수에서는
    이 지점이 최솟값이다.
    </p>
</div>
""", unsafe_allow_html=True)

st.write("""
따라서 경사하강법은 순간변화율의 부호와 크기를 이용해
이동 방향과 이동량을 결정한다.
""")

st.markdown("---")


# --------------------------------------------------
# 06. 학습률 비교하기
# --------------------------------------------------
st.markdown('<div class="section-number">06 / LEARNING RATE</div>',
            unsafe_allow_html=True)

st.header("학습률에 따라 결과가 어떻게 달라질까?")

st.write("""
학습률은 한 번 이동할 때 움직이는 폭을 결정한다.
같은 함수와 시작 위치를 사용하더라도 학습률에 따라
최솟값을 찾아가는 과정이 달라질 수 있다.
""")

st.latex(r"f(x)=x^2+2")

st.write("시작 위치를 x=8로 두고 학습률을 바꾸어 비교해 보자.")

selected_rate = st.select_slider(
    "비교할 학습률 선택",
    options=[0.1, 0.3, 0.6, 0.9, 1.0, 1.1],
    value=0.3
)

rate_x = [8.0]
rate_loss = [8.0 ** 2 + 2]

for i in range(10):
    current_x = rate_x[-1]
    derivative = 2 * current_x
    next_x = current_x - selected_rate * derivative

    rate_x.append(next_x)
    rate_loss.append(next_x ** 2 + 2)

rate_fig = go.Figure()

rate_fig.add_trace(go.Scatter(
    x=np.linspace(-10, 10, 300),
    y=np.linspace(-10, 10, 300) ** 2 + 2,
    mode="lines",
    name="손실함수",
    line=dict(color="#ff4b4b", width=3)
))

rate_fig.add_trace(go.Scatter(
    x=rate_x,
    y=rate_loss,
    mode="lines+markers",
    name="이동 과정",
    line=dict(color="#ffffff", width=2, dash="dot"),
    marker=dict(size=8, color="#ffffff")
))

rate_fig.update_layout(
    template="plotly_dark",
    paper_bgcolor="#101010",
    plot_bgcolor="#181818",
    xaxis_title="x",
    yaxis_title="f(x)",
    height=430,
    margin=dict(l=20, r=20, t=30, b=20)
)

st.plotly_chart(rate_fig, use_container_width=True)

st.write(f"선택한 학습률: **{selected_rate}**")

if selected_rate < 0.5:
    st.success("""
    학습률이 비교적 작아 한 번에 이동하는 폭이 작다.
    최솟값에 도달하는 데 더 많은 반복이 필요할 수 있다.
    """)
elif selected_rate < 1:
    st.success("""
    최솟값을 지나 반대편으로 이동할 수 있지만,
    이동 폭이 점점 작아지면서 최솟값에 가까워진다.
    """)
elif selected_rate == 1:
    st.warning("""
    최솟값을 기준으로 양쪽을 반복해서 이동한다.
    이 예시에서는 손실함수 값이 줄어들지 않는다.
    """)
else:
    st.error("""
    이동 폭이 점점 커져 최솟값에서 멀어진다.
    따라서 이 예시에서는 최솟값에 수렴하지 않는다.
    """)

st.markdown("""
<div class="result-card">
    <b>학습률의 핵심</b><br>
    학습률이 너무 작으면 최솟값을 찾는 속도가 느려질 수 있고,
    너무 크면 최솟값을 지나치거나 오히려 멀어질 수 있다.
    </div>
""", unsafe_allow_html=True)

st.markdown("---")


# --------------------------------------------------
# 07. 경사하강법 정리
# --------------------------------------------------
st.markdown('<div class="section-number">07 / SUMMARY</div>',
            unsafe_allow_html=True)

st.header("경사하강법의 작동 과정 정리")

st.write("""
경사하강법은 산에서 낮은 곳을 찾아 내려가는 과정에 비유할 수 있다.
현재 내가 서 있는 위치에서 어느 방향이 아래쪽인지 확인하고,
한 번에 이동할 거리를 정한 뒤 조금씩 움직이는 것이다.
이 과정을 반복하면 함수의 최솟값에 가까워질 수 있다.
""")

st.subheader("경사하강법의 4단계")

steps = [
    ("01", "현재 위치 확인", "함수에서 현재 위치를 정한다."),
    ("02", "미분값 계산", "현재 위치에서의 순간변화율을 구한다."),
    ("03", "이동 방향과 거리 결정", "미분값과 학습률을 이용해 다음 위치를 계산한다."),
    ("04", "과정 반복", "함수의 값이 작아지는 방향으로 계속 이동한다.")
]

for number, title, description in steps:
    st.markdown(f"""
    <div class="result-card">
        <span class="highlight">{number}</span>
        <b>　{title}</b><br>
        {description}
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

st.subheader("오늘의 핵심 정리")

st.write("""
- **손실함수**는 인공지능의 예측 오차를 나타낸다.
- **미분**은 현재 위치에서 함수의 순간변화율을 알려준다.
- **학습률**은 한 번에 이동하는 정도를 결정한다.
- **경사하강법**은 이 세 가지 원리를 이용해 손실함수의 값을 줄여 나간다.
""")

st.markdown("""
<div class="info-card">
    <h3>마무리</h3>
    <p>
    경사하강법은 단순히 함수의 최솟값을 구하는 수학적 방법을 넘어,
    인공지능이 예측 오차를 줄이며 학습하는 과정에도 활용되는 원리이다.
    </p>
</div>
""", unsafe_allow_html=True)
