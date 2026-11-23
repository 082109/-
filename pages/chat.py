
import streamlit as st
import numpy as np
import plotly.graph_objects as go

# ==========================================
# 1. 페이지 설정
# ==========================================

st.set_page_config(
    page_title="Gradient Descent in Media",
    page_icon="🎬",
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

.media-card {
    background-color: #202020;
    border: 1px solid #383838;
    border-radius: 12px;
    padding: 20px;
    margin-bottom: 15px;
}

.media-card h3 {
    color: #ff5555 !important;
}

.highlight {
    color: #ff5555;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)


# ==========================================
# 3. 제목
# ==========================================

st.title("🎬 GRADIENT DESCENT × MEDIA")
st.caption("경사하강법은 콘텐츠 추천 알고리즘에 어떻게 활용될까?")

st.markdown("---")


# ==========================================
# 4. 미디어 플랫폼과 인공지능
# ==========================================

st.markdown("### 01 / MEDIA PLATFORM")

st.header("우리가 보는 콘텐츠는 어떻게 추천될까?")

st.write("""
유튜브나 넷플릭스와 같은 미디어 플랫폼에서는
이용자의 관심사와 콘텐츠 이용 기록을 분석하여
개인에게 적합한 콘텐츠를 추천한다.

예를 들어 이용자가 특정 장르의 영상을 자주 시청하거나
비슷한 주제의 콘텐츠에 긍정적인 반응을 보인다면,
플랫폼은 이러한 정보를 바탕으로 이용자의 선호를 예측한다.

이 과정에서 인공지능 알고리즘이 활용된다.
""")

st.markdown("""
<div class="media-card">
<h3>콘텐츠 추천 알고리즘</h3>
<p>
이용자의 시청 기록, 선호 장르, 콘텐츠 반응 등의 정보를 분석하여
어떤 콘텐츠에 관심을 가질 가능성이 높은지 예측하는 기술이다.
</p>
</div>
""", unsafe_allow_html=True)

st.subheader("추천 알고리즘의 기본 과정")

steps = [
    ("01", "이용자 정보 수집", "시청 기록이나 콘텐츠에 대한 반응 등을 확인한다."),
    ("02", "선호도 예측", "수집한 정보를 바탕으로 이용자가 관심을 가질 콘텐츠를 예측한다."),
    ("03", "추천 결과 확인", "실제 이용자의 반응과 예측 결과를 비교한다."),
    ("04", "모델 학습", "예측 오차를 줄이도록 모델의 값을 조정한다.")
]

for number, title, description in steps:
    st.markdown(f"""
    <div class="media-card">
        <span class="highlight">{number}</span>
        <h3>{title}</h3>
        <p>{description}</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")


# ==========================================
# 5. 손실함수와 콘텐츠 추천
# ==========================================

st.markdown("### 02 / LOSS FUNCTION")

st.header("추천 결과의 오차를 어떻게 줄일까?")

st.write("""
인공지능이 이용자의 선호도를 예측했더라도
실제 이용자의 반응과 예측 결과가 항상 일치하는 것은 아니다.

예를 들어 어떤 영상에 이용자가 높은 관심을 보일 것이라고
예측했지만 실제로는 관심을 보이지 않을 수도 있다.

이처럼 예측값과 실제값 사이에는 오차가 발생한다.

인공지능은 이러한 오차를 손실함수로 나타내고,
손실함수의 값을 줄이는 방향으로 학습한다.
""")

st.latex(r"\text{손실}=(\text{예측값}-\text{실제값})^2")

st.write("""
예를 들어 이용자의 콘텐츠 선호도를 1부터 5까지의 점수로
나타낸다고 가정해 보자.
""")

col1, col2 = st.columns(2)

with col1:
    st.metric("인공지능의 예측값", "4점")

with col2:
    st.metric("실제 이용자 반응", "2점")

st.write("""
이 경우 예측값과 실제값의 차이는 2점이다.
이 차이를 제곱하면 손실은 4가 된다.

인공지능은 이러한 오차를 줄이도록
모델의 가중치와 편향을 수정한다.
""")

st.markdown("---")


# ==========================================
# 6. 경사하강법의 활용
# ==========================================

st.markdown("### 03 / GRADIENT DESCENT")

st.header("경사하강법은 여기서 어떤 역할을 할까?")

st.write("""
콘텐츠 추천 인공지능은 이용자의 선호도를 예측하는 과정에서
가중치와 편향 등의 값을 조정한다.

이때 경사하강법을 활용하면 손실함수의 기울기를 계산하여
손실이 감소하는 방향으로 모델의 값을 수정할 수 있다.

즉, 예측 결과와 실제 반응 사이의 오차를 줄이도록
모델을 반복적으로 학습시키는 것이다.
""")

st.latex(r"\theta_{t+1}=\theta_t-\alpha\nabla J(\theta_t)")

st.markdown("""
<div class="media-card">
<h3>미디어 추천 알고리즘에서의 의미</h3>
<p>
<b>손실함수</b> : 이용자의 실제 반응과 예측 결과 사이의 오차</p>
<p>
<b>기울기</b> : 손실함수가 증가하거나 감소하는 방향과 정도</p>
<p>
<b>학습률</b> : 가중치와 편향을 한 번에 얼마나 수정할지 결정하는 값</p>
<p>
<b>경사하강법</b> : 오차를 줄이도록 모델의 값을 반복적으로 조정하는 방법
</p>
</div>
""", unsafe_allow_html=True)

st.write("""
이러한 학습 과정을 반복하면 모델은 이용자의 반응을
더 잘 예측할 수 있도록 조정된다.

다만 실제 추천 시스템은 이용자의 다양한 정보와
여러 개의 변수 및 복잡한 학습 과정을 활용하므로,
여기서 설명한 내용은 그 원리를 단순화한 것이다.
""")

st.markdown("---")


# ==========================================
# 7. 간단한 추천 알고리즘 실험
# ==========================================

st.markdown("### 04 / RECOMMENDATION EXPERIMENT")

st.header("추천 결과를 직접 조정해 보자")

st.write("""
간단한 예시를 통해 예측값과 실제 반응 사이의 오차가
어떻게 달라지는지 확인해 보자.

아래에서는 이용자의 콘텐츠 선호도를 예측하는
가상의 모델을 설정한다.

가중치와 편향을 조정하면 예측값이 달라지고,
그에 따라 손실값도 변한다.
""")

st.latex(r"\hat{y}=wx+b")

st.write("""
- w : 입력 정보에 곱해지는 가중치
- x : 이용자의 콘텐츠 관련 정보
- b : 편향
- ŷ : 인공지능의 예측값
""")

st.info("실험을 위한 가상의 예시이며, 실제 플랫폼의 추천 알고리즘을 그대로 구현한 것은 아니야.")

col1, col2 = st.columns(2)

with col1:
    input_x = st.slider(
        "이용자 정보 x",
        0.0, 5.0, 3.0,
        step=0.5
    )

    weight = st.slider(
        "가중치 w",
        0.0, 2.0, 1.0,
        step=0.1
    )

with col2:
    bias = st.slider(
        "편향 b",
        -2.0, 2.0, 0.0,
        step=0.1
    )

    actual = st.slider(
        "실제 이용자 반응",
        0.0, 5.0, 4.0,
        step=0.5
    )

prediction = weight * input_x + bias
loss = (prediction - actual) ** 2

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("예측값", f"{prediction:.2f}")

with col2:
    st.metric("실제값", f"{actual:.2f}")

with col3:
    st.metric("손실값", f"{loss:.2f}")

st.subheader("예측값과 실제값 비교")

fig = go.Figure()

fig.add_trace(go.Bar(
    x=["예측값", "실제값"],
    y=[prediction, actual],
    marker_color=["#ff5555", "#2589ff"]
))

fig.update_layout(
    template="plotly_dark",
    paper_bgcolor="#101010",
    plot_bgcolor="#202020",
    yaxis_title="선호도 점수",
    height=350
)

st.plotly_chart(fig, use_container_width=True)

if loss < 0.1:
    st.success("예측값이 실제값에 매우 가까워!")
elif loss < 1:
    st.info("예측값과 실제값의 차이가 크지 않아.")
else:
    st.warning("예측값과 실제값 사이에 오차가 있어. 가중치와 편향을 조정해 보자.")

st.write("""
가중치와 편향을 바꾸면 예측값이 달라지고,
예측값과 실제값의 차이에 따라 손실값도 달라진다.

실제 인공지능은 이러한 조정을 사람이 매번 직접 하는 것이 아니라,
경사하강법과 같은 최적화 알고리즘을 활용해 학습 과정에서 수행한다.
""")

st.markdown("---")


# ==========================================
# 8. 미디어 진로와 연결
# ==========================================

st.markdown("### 05 / MEDIA CAREER")

st.header("미디어 분야와 경사하강법의 연결")

st.write("""
경사하강법은 단순히 수학이나 인공지능 분야에서만
활용되는 개념이 아니다.

오늘날 미디어 플랫폼은 인공지능을 활용해
이용자의 콘텐츠 소비 경향을 분석하고
개인에게 적합한 콘텐츠를 추천한다.

따라서 경사하강법을 이해하면 미디어 플랫폼이
이용자의 반응을 예측하고 추천 결과를 개선하는
수학적 원리도 이해할 수 있다.
""")

st.markdown("""
<div class="media-card">
<h3>PD · 콘텐츠 기획 분야</h3>
<p>
PD와 콘텐츠 기획자는 콘텐츠를 제작하는 것뿐만 아니라
시청자의 관심과 반응을 분석하고,
어떤 콘텐츠가 효과적으로 전달될 수 있을지 고민한다.
</p>
<p>
미디어 플랫폼의 추천 알고리즘을 이해하는 것은
이용자의 콘텐츠 소비 방식과 미디어 환경의 변화를
분석하는 데에도 도움이 된다.
</p>
</div>
""", unsafe_allow_html=True)

st.subheader("마무리")

st.write("""
이번 탐구를 통해 경사하강법이 미분을 활용하여
손실함수를 최소화하고, 인공지능 모델의 가중치와 편향을
조정하는 최적화 알고리즘이라는 점을 알 수 있었다.

또한 이러한 원리가 콘텐츠 추천 알고리즘에도 활용된다는 점에서
수학적 개념이 실제 미디어 기술과 연결되어 있음을 이해할 수 있었다.
""")

