
import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go

# ==========================================
# 1. 기본 설정
# ==========================================

st.set_page_config(
    page_title="Gradient Descent Lab",
    page_icon="📉",
    layout="wide"
)

# ==========================================
# 2. 디자인
# ==========================================

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

.main-title {
    font-size: 38px;
    font-weight: 800;
    color: white;
}

.sub-title {
    color: #aaaaaa;
    font-size: 16px;
    margin-bottom: 25px;
}

.section-number {
    color: #ff5555;
    font-size: 13px;
    font-weight: bold;
    letter-spacing: 2px;
}

.info-card {
    background-color: #202020;
    border: 1px solid #383838;
    border-radius: 12px;
    padding: 20px;
    margin-bottom: 12px;
}

.info-card h3 {
    color: #ff5555 !important;
}

.result-card {
    background-color: #202020;
    border-left: 4px solid #ff5555;
    border-radius: 8px;
    padding: 16px;
    margin: 12px 0;
}

.highlight {
    color: #ff5555;
    font-weight: bold;
}

.small-text {
    color: #aaaaaa;
    font-size: 13px;
}

hr {
    border-color: #383838;
}
</style>
""", unsafe_allow_html=True)


# ==========================================
# 제목
# ==========================================

st.markdown(
    '<div class="main-title">GRADIENT DESCENT LAB</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="sub-title">미분으로 이해하는 인공지능의 학습 원리</div>',
    unsafe_allow_html=True
)

st.markdown("---")


# ==========================================
# 01. 최적화란?
# ==========================================

st.markdown(
    '<div class="section-number">01 / OPTIMIZATION</div>',
    unsafe_allow_html=True
)

st.header("최적화란 무엇일까?")

st.write("""
최적화란 주어진 조건에서 함수의 값이 최대 또는 최소가 되는
상태를 찾아내는 방법이다.

예를 들어 인공지능 모델이 어떤 값을 예측한다고 생각해 보자.
모델의 예측값과 실제값 사이에 차이가 발생할 수 있는데,
이 차이를 줄이는 것도 최적화의 한 과정이다.

변수가 적은 문제는 그래프로 표현할 수 있지만,
변수가 많아지면 시각적으로 나타내기 어려워진다.
따라서 복잡한 문제에서도 최적의 값을 찾아내기 위해
다양한 최적화 알고리즘이 사용된다.
""")

st.markdown("""
<div class="info-card">
    <h3>핵심 개념</h3>
    <p>
    최적화는 함수의 값을 가장 크게 하거나 작게 만드는
    조건과 값을 찾아내는 과정이다.
    </p>
</div>
""", unsafe_allow_html=True)

st.subheader("간단한 함수로 최솟값 확인하기")

st.latex(r"y=x^2+2")

st.write("""
위 함수는 x=0일 때 y=2로 가장 작은 값을 갖는다.
따라서 최솟값은 2이다.
""")

x_graph = np.linspace(-10, 10, 400)
y_graph = x_graph ** 2 + 2

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=x_graph,
    y=y_graph,
    mode="lines",
    name="y = x² + 2",
    line=dict(color="#ff5555", width=3)
))

fig.add_trace(go.Scatter(
    x=[0],
    y=[2],
    mode="markers+text",
    name="최솟값",
    text=["최솟값 (0, 2)"],
    textposition="top center",
    marker=dict(color="#2589ff", size=12)
))

fig.update_layout(
    template="plotly_dark",
    paper_bgcolor="#101010",
    plot_bgcolor="#202020",
    xaxis_title="x",
    yaxis_title="y",
    height=400
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("---")


# ==========================================
# 02. 인공지능 모델의 가중치와 편향
# ==========================================

st.markdown(
    '<div class="section-number">02 / MODEL PARAMETERS</div>',
    unsafe_allow_html=True
)

st.header("인공지능은 무엇을 조정할까?")

st.write("""
인공지능 모델은 데이터를 학습하면서 예측 결과가 실제 결과에
가까워지도록 내부의 여러 값을 조정한다.

이때 대표적으로 조정되는 값이 가중치(Weight)와 편향(Bias)이다.
""")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="info-card">
        <h3>가중치 (Weight)</h3>
        <p>
        입력된 정보가 예측 결과에 얼마나 큰 영향을 미치는지를
        결정하는 값이다.
        </p>
        <p>
        예를 들어 어떤 정보가 예측에 더 중요하게 반영되도록
        그 영향력을 조절하는 역할을 한다.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="info-card">
        <h3>편향 (Bias)</h3>
        <p>
        입력값과 가중치만으로 결정되는 결과에 추가로 더해지는 값이다.
        </p>
        <p>
        모델의 예측 결과가 적절한 위치에 오도록
        조정하는 역할을 한다.
        </p>
    </div>
    """, unsafe_allow_html=True)

st.write("""
인공지능은 학습 과정에서 가중치와 편향을 조금씩 수정한다.
이러한 조정을 통해 예측값과 실제값 사이의 오차를 줄여 나간다.
""")

st.markdown("""
<div class="result-card">
    <b>정리</b><br>
    가중치와 편향은 인공지능 모델이 학습하면서 조정하는 값이며,
    이러한 값을 통틀어 모델의 파라미터라고 부른다.
</div>
""", unsafe_allow_html=True)

st.markdown("---")


# ==========================================
# 03. 손실함수와 기울기
# ==========================================

st.markdown(
    '<div class="section-number">03 / LOSS FUNCTION & GRADIENT</div>',
    unsafe_allow_html=True
)

st.header("손실함수와 기울기는 무엇일까?")

st.subheader("① 손실함수 (Loss Function)")

st.write("""
손실함수는 인공지능 모델이 예측한 값과 실제값 사이의 오차를
수학적으로 나타낸 함수이다.

예측값과 실제값의 차이가 클수록 손실함수의 값도 커지고,
오차가 줄어들수록 손실함수의 값도 작아지도록 설정할 수 있다.
""")

st.latex(r"J(\theta)")

st.write("""
여기서 J는 손실함수를 의미하고,
θ(세타)는 모델이 학습하면서 조정하는 파라미터를 나타낸다.

즉, 가중치와 편향이 달라지면 예측 결과가 달라지고,
이에 따라 손실함수의 값도 달라진다.
""")

st.markdown("""
<div class="info-card">
    <h3>② 기울기 (Gradient)</h3>
    <p>
    기울기는 현재 위치에서 손실함수의 값이
    어느 방향으로 얼마나 빠르게 변하는지를 나타낸다.
    </p>
    <p>
    기울기를 확인하면 손실함수의 값이 증가하는 방향과
    감소하는 방향을 판단할 수 있다.
    </p>
</div>
""", unsafe_allow_html=True)

st.write("""
변수가 하나일 때는 미분값으로 기울기를 확인할 수 있다.
하지만 인공지능 모델처럼 조정할 값이 여러 개라면
각 변수에 대한 편미분값을 모아 기울기(Gradient)를 구한다.

이렇게 구한 기울기를 이용해 가중치와 편향을
어느 방향으로 얼마나 조정할지 결정한다.
""")

st.latex(r"\nabla J(\theta)")

st.markdown("---")


# ==========================================
# 04. 경사하강법의 수식과 원리
# ==========================================

st.markdown(
    '<div class="section-number">04 / GRADIENT DESCENT</div>',
    unsafe_allow_html=True
)

st.header("경사하강법이란?")

st.write("""
경사하강법은 손실함수의 값을 최소화하기 위해
현재 모델의 파라미터를 조금씩 조정하는 최적화 알고리즘이다.

현재 위치에서 기울기를 확인한 뒤,
손실함수의 값이 감소하는 방향으로 이동하는 과정을 반복한다.
""")

st.subheader("경사하강법의 핵심 수식")

st.latex(
    r"\theta_{t+1}=\theta_t-\alpha\nabla J(\theta_t)"
)

st.write("사진 속 수식을 구성하는 각 기호를 살펴보자.")

formula_items = [
    ("θₜ", "현재 파라미터", "현재 모델이 가지고 있는 가중치와 편향 등의 값"),
    ("θₜ₊₁", "다음 파라미터", "현재 값을 조정한 후 새롭게 정해지는 값"),
    ("α", "학습률 (Learning rate)", "한 번에 파라미터를 얼마나 크게 수정할지 결정하는 값"),
    ("∇J(θₜ)", "기울기 (Gradient)", "현재 파라미터 위치에서 손실함수가 변하는 방향과 정도")
]

for symbol, title, description in formula_items:
    st.markdown(f"""
    <div class="info-card">
        <h3>{symbol} : {title}</h3>
        <p>{description}</p>
    </div>
    """, unsafe_allow_html=True)

st.subheader("왜 기울기를 빼는 것일까?")

st.write("""
경사하강법은 손실함수의 값을 줄이는 방향으로 이동해야 한다.

기울기가 양수라면 현재 위치에서 오른쪽으로 갈수록
함수의 값이 증가하는 경향이 있으므로 왼쪽으로 이동해야 한다.

반대로 기울기가 음수라면 오른쪽으로 갈수록
함수의 값이 감소하는 경향이 있으므로 오른쪽으로 이동해야 한다.

따라서 현재 기울기의 반대 방향으로 이동하도록
수식에서 기울기를 빼는 것이다.
""")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="info-card">
        <h3>기울기가 양수 (+)</h3>
        <p>기울기를 빼면 현재 값이 작아진다.</p>
        <p class="highlight">왼쪽 방향으로 이동 ←</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="info-card">
        <h3>기울기가 음수 (-)</h3>
        <p>음수인 기울기를 빼면 현재 값이 커진다.</p>
        <p class="highlight">오른쪽 방향으로 이동 →</p>
    </div>
    """, unsafe_allow_html=True)

st.subheader("학습률은 왜 중요할까?")

st.write("""
학습률은 한 번 이동할 때 파라미터를 얼마나 크게 바꿀지 결정한다.

학습률이 너무 작으면 조금씩 이동하기 때문에
손실함수를 최소화하는 데 많은 반복이 필요할 수 있다.

반대로 학습률이 너무 크면 최솟값을 지나치거나
오히려 최솟값에서 멀어질 수 있다.

따라서 손실함수를 안정적으로 줄이기 위해서는
적절한 학습률을 선택하는 것이 중요하다.
""")

st.markdown("""
<div class="result-card">
    <b>경사하강법의 핵심 과정</b><br>
    현재 파라미터 확인 → 기울기 계산 → 학습률 적용 →
    파라미터 수정 → 이 과정을 반복하며 손실함수 최소화
</div>
""", unsafe_allow_html=True)

st.markdown("---")


# ==========================================
# 05. 그래프로 직접 체험하기
# ==========================================

st.markdown(
    '<div class="section-number">05 / INTERACTIVE EXPERIMENT</div>',
    unsafe_allow_html=True
)

st.header("직접 경사하강법 실험하기")

st.write("""
앞에서 배운 원리를 간단한 이차함수에 적용해 보자.

실제 인공지능에서는 여러 개의 가중치와 편향을 조정하지만,
이번 실험에서는 이해하기 쉽도록 하나의 변수 x만 조정한다.

함수의 값이 최소가 되는 x를 찾아가는 과정을 확인해 보자.
""")

st.latex(r"f(x)=x^2+2")

st.latex(r"f'(x)=2x")

st.write("""
이 함수의 최솟값은 x=0일 때 2이다.
시작 위치와 학습률, 반복 횟수를 바꾸면서
경사하강법의 이동 과정을 관찰해 보자.
""")

col1, col2 = st.columns(2)

with col1:
    start_x = st.slider(
        "시작 위치 x",
        min_value=-10.0,
        max_value=10.0,
        value=10.0,
        step=0.5
    )

with col2:
    learning_rate = st.slider(
        "학습률 (Step size)",
        min_value=0.01,
        max_value=1.5,
        value=0.1,
        step=0.01,
        format="%.2f"
    )

iterations = st.slider(
    "반복 횟수",
    min_value=1,
    max_value=30,
    value=10
)

# 경사하강법 계산
x_values = [start_x]
loss_values = [start_x ** 2 + 2]

current_x = start_x

for i in range(iterations):
    derivative = 2 * current_x
    next_x = current_x - learning_rate * derivative

    current_x = next_x

    x_values.append(current_x)
    loss_values.append(current_x ** 2 + 2)

# 그래프 범위 계산
max_abs_x = max(10, max(abs(v) for v in x_values))
graph_limit = min(max_abs_x * 1.15, 100000)

x_graph = np.linspace(-graph_limit, graph_limit, 500)
y_graph = x_graph ** 2 + 2

# 함수 그래프
fig2 = go.Figure()

fig2.add_trace(go.Scatter(
    x=x_graph,
    y=y_graph,
    mode="lines",
    name="손실함수",
    line=dict(color="#ff5555", width=3)
))

# 이동 경로
fig2.add_trace(go.Scatter(
    x=x_values,
    y=loss_values,
    mode="lines+markers",
    name="이동 경로",
    line=dict(color="#2589ff", width=2),
    marker=dict(size=8, color="#2589ff")
))

# 최솟값
fig2.add_trace(go.Scatter(
    x=[0],
    y=[2],
    mode="markers",
    name="최솟값",
    marker=dict(color="#ff5555", size=13, symbol="star")
))

fig2.update_layout(
    template="plotly_dark",
    paper_bgcolor="#101010",
    plot_bgcolor="#202020",
    xaxis_title="x",
    yaxis_title="f(x)",
    height=480
)

st.plotly_chart(fig2, use_container_width=True)

# 결과
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("학습률", f"{learning_rate:.2f}")

with col2:
    st.metric("최종 x값", f"{current_x:.5f}")

with col3:
    st.metric("최종 함수값", f"{loss_values[-1]:.5f}")

# 수렴 상태
if abs(current_x) < 0.1:
    st.success("최솟값에 가까워졌어!")
elif learning_rate == 1.0:
    st.warning("최솟값을 기준으로 양쪽을 반복해서 이동하고 있어.")
elif learning_rate > 1.0:
    st.error("이 함수에서는 학습률이 너무 커서 최솟값에서 멀어지고 있어.")
else:
    st.info("반복 횟수를 늘려 최솟값에 가까워지는지 확인해 보자.")

# 이동 과정 표
st.subheader("반복에 따른 이동 과정")

result_df = pd.DataFrame({
    "반복 횟수": range(iterations + 1),
    "현재 x값": [round(v, 5) for v in x_values],
    "함수값": [round(v, 5) for v in loss_values]
})

st.dataframe(
    result_df,
    use_container_width=True,
    hide_index=True
)

st.markdown("---")


# ==========================================
# 06. 학습률에 따른 결과 비교
# ==========================================

st.markdown(
    '<div class="section-number">06 / LEARNING RATE</div>',
    unsafe_allow_html=True
)

st.header("학습률에 따라 결과가 어떻게 달라질까?")

st.write("""
학습률을 직접 조절해 보면서 최솟값에 가까워지는 과정을 비교해 보자.

아래 그래프에서는 시작 위치를 x=10으로 고정하고,
학습률을 자유롭게 조절할 수 있다.
""")

compare_rate = st.slider(
    "비교할 학습률",
    min_value=0.01,
    max_value=1.5,
    value=0.6,
    step=0.01,
    format="%.2f",
    key="compare_rate"
)

compare_x = [10.0]
compare_y = [102.0]

current_x = 10.0
converged = False

for i in range(1000):
    derivative = 2 * current_x
    current_x = current_x - compare_rate * derivative

    compare_x.append(current_x)
    compare_y.append(current_x ** 2 + 2)

    if abs(current_x) < 0.1:
        converged = True
        break

# 비교 그래프
display_count = min(len(compare_x), 30)

fig3 = go.Figure()

# 함수 그래프
fig3.add_trace(go.Scatter(
    x=x_graph,
    y=y_graph,
    mode="lines",
    name="y = x² + 2",
    line=dict(color="#ff7777", width=3)
))

# 이동 경로
fig3.add_trace(go.Scatter(
    x=compare_x[:display_count],
    y=compare_y[:display_count],
    mode="lines+markers",
    name="이동 경로",
    line=dict(color="#2589ff", width=2),
    marker=dict(size=7)
))

fig3.add_trace(go.Scatter(
    x=[0],
    y=[2],
    mode="markers",
    name="최솟값",
    marker=dict(color="#ff5555", size=13, symbol="star")
))

fig3.update_layout(
    template="plotly_dark",
    paper_bgcolor="#101010",
    plot_bgcolor="#202020",
    xaxis_title="x",
    yaxis_title="y",
    height=450
)

st.plotly_chart(fig3, use_container_width=True)

if converged:
    st.success(
        f"최솟값에 가까워졌어! "
        f"필요한 반복 횟수는 {len(compare_x)-1}회야."
    )
elif compare_rate == 1.0:
    st.warning(
        "최솟값을 기준으로 양쪽을 반복해서 이동하고 있어. "
        "함수값이 줄어들지 않아."
    )
elif compare_rate > 1.0:
    st.error(
        "학습률이 너무 커서 최솟값에서 멀어지고 있어."
    )
else:
    st.info(
        "현재 설정에서는 아직 최솟값에 도달하지 않았어. "
        "반복 횟수나 학습률을 바꾸어 보자."
    )

st.markdown("---")


# ==========================================
# 07. 핵심 내용 정리
# ==========================================

st.markdown(
    '<div class="section-number">07 / SUMMARY</div>',
    unsafe_allow_html=True
)

st.header("경사하강법 핵심 내용 정리")

summary_items = [
    ("최적화", "함수의 최댓값이나 최솟값을 찾는 과정"),
    ("가중치와 편향", "인공지능 모델이 학습하면서 조정하는 값"),
    ("손실함수", "예측값과 실제값 사이의 오차를 나타내는 함수"),
    ("기울기", "손실함수가 변하는 방향과 정도"),
    ("학습률", "한 번에 값을 얼마나 수정할지 결정하는 값"),
    ("경사하강법", "기울기를 이용해 손실함수를 최소화하는 최적화 알고리즘")
]

for title, description in summary_items:
    st.markdown(f"""
    <div class="result-card">
        <b class="highlight">{title}</b><br>
        {description}
    </div>
    """, unsafe_allow_html=True)

st.subheader("마무리")

st.write("""
경사하강법은 인공지능 모델의 손실함수를 최소화하기 위해
가중치와 편향을 조정하는 최적화 알고리즘이다.

현재 위치에서 기울기를 계산하고 학습률을 적용하여
파라미터를 조금씩 수정하는 과정을 반복한다.

이번 실험을 통해 학습률에 따라 최솟값에 도달하는 과정이
어떻게 달라지는지 직접 확인할 수 있다.
""")
