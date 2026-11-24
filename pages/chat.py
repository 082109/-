
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="경사하강법의 실제 활용",
    page_icon="📌",
    layout="wide"
)

# -------------------------------
# 디자인
# -------------------------------
st.markdown("""
<style>
.stApp {
    background-color: #101010;
    color: white;
}

.block-container {
    padding-top: 3rem;
    padding-bottom: 4rem;
    max-width: 1100px;
}

h1, h2, h3, p, label {
    color: white !important;
}

.main-title {
    font-size: 42px;
    font-weight: 800;
    margin-bottom: 10px;
}

.sub-title {
    color: #aaaaaa;
    font-size: 17px;
    margin-bottom: 45px;
}

.section-title {
    font-size: 27px;
    font-weight: 750;
    margin-top: 55px;
    margin-bottom: 20px;
}

.section-number {
    color: #ff625e;
    font-weight: bold;
    font-size: 15px;
}

.example-card {
    background-color: #1d1d1d;
    border: 1px solid #333333;
    border-radius: 13px;
    padding: 22px;
    min-height: 170px;
    margin-bottom: 12px;
}

.example-card h3 {
    font-size: 19px;
    margin-bottom: 10px;
}

.example-card p {
    color: #bbbbbb !important;
    font-size: 14px;
    line-height: 1.7;
}

.explain-box {
    background-color: #202020;
    border: 1px solid #393939;
    border-radius: 12px;
    padding: 24px;
    line-height: 1.8;
    margin-top: 15px;
    margin-bottom: 20px;
}

.highlight {
    color: #ff625e !important;
    font-weight: bold;
}

.step-card {
    background-color: #1d1d1d;
    border-left: 4px solid #ff625e;
    border-radius: 8px;
    padding: 18px 22px;
    margin-bottom: 12px;
}

.step-card p {
    color: #cccccc !important;
    margin-bottom: 0;
    line-height: 1.7;
}

hr {
    border-color: #333333;
    margin-top: 35px;
    margin-bottom: 35px;
}
</style>
""", unsafe_allow_html=True)


# -------------------------------
# 제목
# -------------------------------
st.markdown(
    '<div class="main-title">경사하강법의 실제 활용</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="sub-title">인공지능은 경사하강법을 어떻게 활용할까?</div>',
    unsafe_allow_html=True
)


# -------------------------------
# 01. 활용 사례
# -------------------------------
st.markdown(
    '<div class="section-number">01 / APPLICATION</div>'
    '<div class="section-title">경사하강법은 어디에 활용될까?</div>',
    unsafe_allow_html=True
)

st.write(
    "경사하강법은 인공지능 모델이 학습하는 과정에서 "
    "예측 오차를 줄이기 위해 활용된다. "
    "다음은 경사하강법을 활용할 수 있는 대표적인 사례이다."
)

examples = [
    (
        "🖼️ 이미지 인식",
        "이미지 분류 인공지능은 사진 속 사물이 무엇인지 예측한다. "
        "경사하강법으로 모델의 설정값을 조정해 분류 오차를 줄인다."
    ),
    (
        "🎙️ 음성 인식",
        "음성을 문자로 바꾸는 인공지능은 음성과 문장의 관계를 학습한다. "
        "학습 과정에서 예측 결과의 오차를 줄이도록 모델을 조정한다."
    ),
    (
        "🌐 기계 번역",
        "번역 인공지능은 문장을 다른 언어로 변환하는 방법을 학습한다. "
        "경사하강법을 이용해 번역 결과의 오차를 줄일 수 있다."
    ),
    (
        "🎬 콘텐츠 추천",
        "영화나 영상의 평점을 예측하는 추천 모델은 "
        "사용자와 콘텐츠의 관계를 학습한다. "
        "경사하강법으로 예측 평점과 실제 평점의 차이를 줄인다."
    ),
    (
        "💬 감정 분석",
        "댓글의 감정이 긍정적인지 부정적인지 분류하는 모델을 학습할 때 "
        "분류 결과의 오차를 줄이는 데 활용할 수 있다."
    ),
    (
        "🚗 자율주행",
        "주변 사물과 도로 상황을 인식하는 인공지능 모델의 "
        "학습 과정에서 예측 오차를 줄이는 데 활용할 수 있다."
    )
]

cols = st.columns(3)

for i, (title, description) in enumerate(examples):
    with cols[i % 3]:
        st.markdown(f"""
        <div class="example-card">
            <h3>{title}</h3>
            <p>{description}</p>
        </div>
        """, unsafe_allow_html=True)


# -------------------------------
# 02. 실제 활용 사례 자세히 보기
# -------------------------------
st.markdown(
    '<div class="section-number">02 / EXAMPLE</div>'
    '<div class="section-title">영화 평점 예측으로 이해하기</div>',
    unsafe_allow_html=True
)

st.write(
    "이번에는 영화 추천 서비스를 예로 들어보자. "
    "추천 모델은 사용자가 어떤 영화에 높은 평점을 줄지 예측할 수 있다."
)

st.markdown("""
<div class="explain-box">
    <b>상황을 가정해 보자.</b><br><br>
    어떤 사용자가 영화 A에 실제로 5점을 주었다고 하자.<br>
    그런데 인공지능 모델은 처음에 이 영화의 평점을 2점으로 예측했다.<br><br>
    이 경우 예측값과 실제 평점 사이에 차이가 발생한다.
    모델은 이러한 차이를 줄이도록 학습해야 한다.
</div>
""", unsafe_allow_html=True)

st.markdown("#### 학습 과정")

st.markdown("""
<div class="step-card">
    <b class="highlight">① 예측하기</b>
    <p>사용자가 영화에 줄 평점을 예측한다.</p>
</div>
<div class="step-card">
    <b class="highlight">② 비교하기</b>
    <p>예측한 평점과 실제 평점의 차이를 확인한다.</p>
</div>
<div class="step-card">
    <b class="highlight">③ 모델 조정하기</b>
    <p>경사하강법을 이용해 예측 오차가 작아지는 방향으로 모델을 조정한다.</p>
</div>
<div class="step-card">
    <b class="highlight">④ 반복 학습하기</b>
    <p>이 과정을 여러 번 반복하여 예측이 실제 결과에 가까워지도록 학습한다.</p>
</div>
""", unsafe_allow_html=True)


# -------------------------------
# 03. 그래프로 확인하기
# -------------------------------
st.markdown(
    '<div class="section-number">03 / GRAPH EXPERIMENT</div>'
    '<div class="section-title">그래프로 경사하강법 확인하기</div>',
    unsafe_allow_html=True
)

st.write(
    "위에서 살펴본 학습 과정을 단순화한 그래프로 확인해 보자. "
    "아래 그래프는 모델의 설정값에 따라 예측 오차가 어떻게 달라지는지 나타낸 예시이다."
)

st.markdown("""
<div class="explain-box">
    <b>그래프 읽는 방법</b><br><br>
    • 가로축: 인공지능 모델의 설정값을 단순화한 변수<br>
    • 세로축: 예측 오차를 나타내는 값<br>
    • 곡선: 설정값에 따른 예측 오차의 변화<br>
    • 점과 선: 경사하강법을 반복 적용하며 이동한 위치<br><br>
    실제 인공지능 모델에는 여러 설정값이 존재하지만,
    여기서는 이해를 위해 하나의 변수만 사용한 간단한 예시로 나타냈다.
</div>
""", unsafe_allow_html=True)


# -------------------------------
# 그래프 조절
# -------------------------------
st.markdown("### 직접 조건을 바꿔 보자!")

col1, col2, col3 = st.columns(3)

with col1:
    start_x = st.slider(
        "시작 위치",
        min_value=-2.0,
        max_value=8.0,
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
        max_value=15,
        value=5,
        step=1
    )


# -------------------------------
# 경사하강법 계산
# -------------------------------
def f(x):
    return (x - 4) ** 2

def derivative(x):
    return 2 * (x - 4)

x = start_x
history = [x]

for _ in range(iterations):
    x = x - learning_rate * derivative(x)
    history.append(x)


# -------------------------------
# 그래프 그리기
# -------------------------------
fig, ax = plt.subplots(figsize=(10, 5))

fig.patch.set_facecolor("#101010")
ax.set_facecolor("#1d1d1d")

x_values = np.linspace(-2, 10, 300)
y_values = f(x_values)

# 손실함수 곡선
ax.plot(
    x_values,
    y_values,
    color="#ff625e",
    linewidth=2.5,
    label="Loss function"
)

# 최솟값 위치
ax.axvline(
    x=4,
    color="#aaaaaa",
    linestyle="--",
    alpha=0.7,
    label="Minimum"
)

# 이동 경로
history_y = [f(value) for value in history]

ax.plot(
    history,
    history_y,
    color="#4da6ff",
    marker="o",
    linewidth=2,
    markersize=6,
    label="Gradient descent"
)

# 시작 위치
ax.scatter(
    history[0],
    history_y[0],
    color="#ffd166",
    s=100,
    zorder=5,
    label="Start"
)

# 마지막 위치
ax.scatter(
    history[-1],
    history_y[-1],
    color="#55d98b",
    s=100,
    zorder=5,
    label="Final position"
)

ax.set_xlabel("Model parameter", color="white")
ax.set_ylabel("Prediction error", color="white")
ax.set_title("Gradient Descent", color="white", fontsize=15)

ax.tick_params(colors="white")
ax.spines["bottom"].set_color("#777777")
ax.spines["left"].set_color("#777777")
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

ax.grid(alpha=0.15)
ax.legend(facecolor="#292929", labelcolor="white")

st.pyplot(fig)


# -------------------------------
# 그래프 결과 설명
# -------------------------------
st.markdown("### 현재 학습 결과")

result1, result2, result3 = st.columns(3)

result1.metric(
    "시작 위치의 오차",
    f"{f(history[0]):.4f}"
)

result2.metric(
    "마지막 위치의 오차",
    f"{f(history[-1]):.4f}"
)

result3.metric(
    "마지막 위치",
    f"{history[-1]:.4f}"
)

st.markdown("""
<div class="explain-box">
    <b>그래프에서 확인할 점</b><br><br>
    • 파란색 선은 경사하강법을 적용하며 이동한 경로이다.<br>
    • 노란색 점은 처음 시작한 위치이다.<br>
    • 초록색 점은 반복 학습 후 도달한 위치이다.<br>
    • 회색 점선은 손실함수가 가장 작아지는 위치를 나타낸다.<br><br>
    학습률과 시작 위치, 반복 횟수를 바꾸면서
    초록색 점이 최솟값에 어떻게 가까워지는지 확인해 보자.
</div>
""", unsafe_allow_html=True)


# -------------------------------
# 반복 과정 표
# -------------------------------
st.markdown("### 반복에 따른 변화")

data = {
    "반복 횟수": list(range(len(history))),
    "현재 위치": [round(v, 4) for v in history],
    "예측 오차": [round(f(v), 4) for v in history]
}

st.dataframe(
    data,
    use_container_width=True,
    hide_index=True
)


# -------------------------------
# 04. 느낀점
# -------------------------------
st.markdown(
    '<div class="section-number">04 / REFLECTION</div>'
    '<div class="section-title">느낀점</div>',
    unsafe_allow_html=True
)

st.markdown("""
<div class="explain-box">
    경사하강법이 이미지 인식, 음성 인식, 콘텐츠 추천 등
    다양한 인공지능 기술의 학습 과정에 활용된다는 것을 알게 되었다.
    특히 영화 평점을 예측하는 사례와 그래프를 통해
    모델이 처음부터 정확한 결과를 내는 것이 아니라,
    예측 오차를 줄이는 방향으로 반복해서 학습한다는 점을 이해할 수 있었다.
    직접 시작 위치와 학습률, 반복 횟수를 바꾸어 보면서
    경사하강법의 원리가 실제로 어떻게 적용되는지 확인할 수 있었다.
</div>
""", unsafe_allow_html=True)
