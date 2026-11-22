
import streamlit as st

# 페이지 기본 설정
st.set_page_config(
    page_title="Gradient Descent Lab",
    page_icon="📉",
    layout="wide"
)

# 디자인 설정
st.markdown("""
<style>
    .stApp {
        background-color: #101010;
        color: white;
    }

    h1, h2, h3 {
        color: white;
    }

    .main-title {
        font-size: 48px;
        font-weight: 800;
        color: white;
        margin-bottom: 10px;
    }

    .sub-title {
        font-size: 18px;
        color: #aaaaaa;
        margin-bottom: 35px;
    }

    .red {
        color: #ff4545;
        font-weight: bold;
    }

    .content-box {
        background-color: #1c1c1c;
        padding: 25px;
        border-radius: 12px;
        border-left: 4px solid #ff4545;
        margin-bottom: 20px;
    }

    .small-text {
        color: #aaaaaa;
        font-size: 14px;
    }

    div[data-testid="stMetric"] {
        background-color: #1c1c1c;
        padding: 15px;
        border-radius: 10px;
    }
</style>
""", unsafe_allow_html=True)


# 메인 화면
st.markdown(
    '<div class="main-title">GRADIENT DESCENT <span class="red">LAB.</span></div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="sub-title">미분으로 이해하는 인공지능의 최적화 원리</div>',
    unsafe_allow_html=True
)

st.divider()

# 1. 경사하강법 소개
st.markdown("## 01. 경사하강법이란?")

st.markdown("""
경사하강법(Gradient Descent)은 인공지능이 학습하는 과정에서 
**손실 함수의 값을 최소화하기 위해 사용하는 최적화 기법**이다.

인공지능은 입력 데이터를 바탕으로 결과를 예측하고, 
예측값과 실제값 사이의 차이를 손실 함수로 나타낸다. 
경사하강법은 이 오차를 줄이기 위해 미분을 활용하여 
손실 함수의 값이 감소하는 방향으로 매개변수를 반복적으로 조정한다.
""")

st.markdown("")

# 2. 핵심 개념
st.markdown("## 02. 핵심 개념")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="content-box">
        <h3>손실 함수</h3>
        <p>인공지능의 예측값과 실제값 사이의 오차를 수치로 나타낸 함수</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="content-box">
        <h3>미분</h3>
        <p>손실 함수의 순간변화율을 구하여 현재 지점에서의 변화 방향을 파악하는 데 활용</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="content-box">
        <h3>학습률</h3>
        <p>경사하강법에서 매개변수를 한 번에 얼마나 조정할지 결정하는 값</p>
    </div>
    """, unsafe_allow_html=True)


# 3. 경사하강법의 계산 원리
st.divider()

st.markdown("## 03. 경사하강법의 계산 원리")

st.markdown("""
경사하강법은 현재 위치에서 손실 함수의 순간변화율을 구한 뒤,
그 값을 이용하여 손실 함수가 감소하는 방향으로 값을 조정한다.
이 과정을 반복하면서 손실 함수의 최솟값에 가까워진다.
""")

st.latex(r"x_{n+1}=x_n-\alpha f'(x_n)")

st.markdown("""
- \(x_n\) : 현재 단계의 값
- \(x_{n+1}\) : 다음 단계에서 조정된 값
- \(f'(x_n)\) : 현재 위치에서의 손실 함수의 순간변화율
- \(\alpha\) : 학습률

여기서 미분은 손실 함수가 어느 방향으로 얼마나 변하는지 파악하는 역할을 한다.
학습률은 한 번의 조정 폭을 결정한다.
""")

# 4. 학습률의 중요성
st.divider()

st.markdown("## 04. 학습률에 따른 차이")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="content-box">
        <h3 class="red">학습률이 너무 큰 경우</h3>
        <p>한 번에 이동하는 폭이 지나치게 커져 최솟값을 지나칠 수 있다.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="content-box">
        <h3 class="red">학습률이 너무 작은 경우</h3>
        <p>한 번에 이동하는 폭이 작아 최솟값에 가까워지는 데 오랜 시간이 걸릴 수 있다.</p>
    </div>
    """, unsafe_allow_html=True)


# 5. 정리
st.divider()

st.markdown("## 05. 핵심 정리")

st.markdown("""
경사하강법은 미분을 통해 손실 함수의 순간변화율을 구하고,
학습률에 따라 매개변수를 반복적으로 조정하여 손실 함수의 값을
최소화하는 방법이다.

즉, **미분은 최적화 과정에서 오차를 줄이는 방향을 찾는 데 활용된다.**
""")

st.markdown("")
st.caption("GRADIENT DESCENT LAB. | Calculus × Artificial Intelligence")
