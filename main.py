import streamlit as st

st.set_page_config(
    page_title="경사하강법 소개",
    page_icon="📉",
    layout="wide"
)

# -----------------------------
# 디자인
# -----------------------------
st.markdown("""
<style>
.stApp {
    background-color: #101010;
    color: white;
}

.block-container {
    max-width: 1100px;
    padding-top: 3rem;
}

.main-title {
    font-size: 42px;
    font-weight: 800;
    color: white;
    margin-bottom: 8px;
}

.subtitle {
    font-size: 17px;
    color: #aaaaaa;
}

.line {
    border-top: 1px solid #444444;
    margin: 25px 0;
}

.contents-title {
    font-size: 25px;
    font-weight: 700;
    margin-bottom: 20px;
}

.section-title {
    font-size: 30px;
    font-weight: 750;
    margin-bottom: 25px;
}

.page-label {
    color: #ff4b4b;
    font-size: 15px;
    font-weight: 700;
}

.content-box {
    background-color: #1c1c1c;
    border: 1px solid #383838;
    border-radius: 12px;
    padding: 24px;
    margin: 15px 0;
    line-height: 1.8;
}

.point {
    background-color: #242424;
    border-left: 4px solid #ff4b4b;
    padding: 15px 20px;
    margin: 12px 0;
    border-radius: 5px;
}

.formula-box {
    background-color: #252525;
    border: 1px solid #555555;
    border-radius: 12px;
    padding: 25px;
    text-align: center;
    margin: 20px 0;
}

.stButton > button {
    background-color: #222222;
    color: white;
    border: 1px solid #555555;
    border-radius: 10px;
    padding: 15px;
    font-size: 17px;
    width: 100%;
}

.stButton > button:hover {
    background-color: #383838;
    border: 1px solid #ff4b4b;
    color: white;
}
</style>
""", unsafe_allow_html=True)


# -----------------------------
# 페이지 상태
# -----------------------------
if "page" not in st.session_state:
    st.session_state.page = 0


contents = [
    "경사하강법이란?",
    "미분의 역할",
    "미분값과 학습률",
    "경사하강법의 수식",
    "경사하강법의 작동 과정"
]


# -----------------------------
# 첫 화면
# -----------------------------
if st.session_state.page == 0:

    st.markdown('<div class="main-title">경사하강법 소개</div>',
                unsafe_allow_html=True)

    st.markdown(
        '<div class="subtitle">미분을 활용해 함수의 최솟값을 찾아가는 방법</div>',
        unsafe_allow_html=True
    )

    st.markdown('<div class="line"></div>', unsafe_allow_html=True)

    st.markdown('<div class="contents-title">목차</div>',
                unsafe_allow_html=True)

    for i, title in enumerate(contents):
        if st.button(f"{i + 1}.  {title}", key=f"menu_{i}"):
            st.session_state.page = i + 1
            st.rerun()


# -----------------------------
# 내용 페이지
# -----------------------------
else:

    page = st.session_state.page

    if st.button("← 처음 화면으로"):
        st.session_state.page = 0
        st.rerun()

    st.markdown(
        f'<div class="page-label">SECTION 0{page}</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f'<div class="section-title">{contents[page - 1]}</div>',
        unsafe_allow_html=True
    )

    st.markdown('<div class="line"></div>', unsafe_allow_html=True)


    # 1. 경사하강법이란?
    if page == 1:

        st.markdown("""
        경사하강법은 **함수의 최솟값을 찾아가기 위해 사용하는 방법**이다.

        인공지능은 데이터를 학습하면서 예측한 결과와 실제 결과 사이의 오차를 줄여 나간다.
        이때 오차를 수학적으로 나타낸 함수를 손실 함수라고 한다.

        경사하강법은 손실 함수의 값을 줄이는 방향으로 조금씩 이동하면서
        오차가 가장 작아지는 지점을 찾아간다.
        """)

        st.markdown("""
        <div class="point">
        <b>핵심 내용</b><br>
        손실 함수의 값을 줄이기 위해 미분을 활용하고,
        최솟값을 향해 반복적으로 이동하는 방법
        </div>
        """, unsafe_allow_html=True)


    # 2. 미분의 역할
    elif page == 2:

        st.markdown("""
        경사하강법에서 미분은 **현재 위치에서 어느 방향으로 이동해야
        함수의 값이 작아지는지 판단하는 데 활용된다.**

        산을 내려가는 상황을 생각해 보자.

        현재 내가 산의 어느 지점에 있다고 가정해 보자.
        가장 낮은 지점으로 내려가려면 먼저 어느 방향으로 움직여야 하는지 알아야겠지?
        이때 미분을 활용할 수 있다.
        """)

        st.markdown("""
        <div class="content-box">
        <b>미분값의 부호에 따른 이동 방향</b><br><br>
        <b style="color:#ff7777;">미분값이 양수 (+)</b><br>
        오른쪽으로 갈수록 함수의 값이 커지므로 왼쪽으로 이동한다.<br><br>

        <b style="color:#ff7777;">미분값이 음수 (-)</b><br>
        오른쪽으로 갈수록 함수의 값이 작아지므로 오른쪽으로 이동한다.<br><br>

        <b style="color:#ff7777;">미분값이 0</b><br>
        접선의 기울기가 0인 지점이다.
        </div>
        """, unsafe_allow_html=True)


    # 3. 미분값과 학습률
    elif page == 3:

        st.markdown("""
        경사하강법은 이동 방향뿐만 아니라 **한 번에 얼마나 이동할지**도 정해야 한다.

        이때 사용하는 값이 바로 학습률이다.
        학습률은 한 번의 이동에서 미분값을 얼마나 반영할지 결정하는 값이다.
        """)

        st.markdown("""
        <div class="content-box">
        <b>학습률에 따른 차이</b><br><br>

        <b style="color:#ff7777;">학습률이 너무 작으면</b><br>
        한 번에 이동하는 거리가 작아 최솟값을 찾는 데 시간이 오래 걸린다.<br><br>

        <b style="color:#ff7777;">적절한 학습률을 사용하면</b><br>
        최솟값을 향해 안정적으로 이동할 수 있다.<br><br>

        <b style="color:#ff7777;">학습률이 너무 크면</b><br>
        최솟값을 지나쳐 반대편으로 이동하는 현상이 발생할 수 있다.
        </div>
        """, unsafe_allow_html=True)


    # 4. 경사하강법의 수식
    elif page == 4:

        st.markdown("경사하강법은 다음과 같은 수식으로 나타낼 수 있다.")

        st.markdown("""
        <div class="formula-box">
        """, unsafe_allow_html=True)

        st.latex(r"x_{t+1}=x_t-\alpha f'(x_t)")

        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("**수식에 사용된 기호**")

        st.markdown("""
        <div class="content-box">
        **현재 위치 \(x_t\)**  
        지금 함수 위에 서 있는 지점

        **다음 위치 \(x_{t+1}\)**  
        미분값과 학습률을 이용해 새롭게 계산한 지점

        **학습률 \(\alpha\)**  
        미분값을 얼마나 반영할지 결정하는 값

        **현재 위치에서의 미분값 \(f'(x_t)\)**  
        현재 위치에서 함수가 변하는 순간적인 정도를 나타내는 값
        </div>
        """, unsafe_allow_html=True)

        st.markdown("### 왜 학습률과 미분값을 곱할까?")

        st.markdown("""
        미분값은 현재 위치에서 함수의 기울기를 나타낸다.
        기울기가 크면 함수가 가파르고, 기울기가 작으면 완만하다.

        하지만 미분값만으로 이동하면 이동 크기를 조절하기 어렵다.
        이때 학습률을 곱하면 미분값의 크기를 조절하여
        **실제로 한 번에 얼마나 이동할지** 정할 수 있다.

        즉, 미분값이 이동 방향과 기울기의 크기를 알려 준다면,
        학습률은 그 기울기를 이동에 얼마나 반영할지 결정한다.

        마지막으로 미분값에 학습률을 곱한 값을 현재 위치에서 빼는 이유는
        함수의 값이 작아지는 방향으로 이동하기 위해서이다.
        """)


    # 5. 경사하강법의 작동 과정
    elif page == 5:

        st.markdown("""
        경사하강법은 다음 과정을 반복하면서 함수의 최솟값을 찾아간다.
        """)

        steps = [
            ("01", "현재 위치 정하기", "함수 위에서 출발할 위치를 정한다."),
            ("02", "미분값 계산하기", "현재 위치에서의 기울기를 구한다."),
            ("03", "이동 방향 결정하기", "미분값의 부호를 통해 함수의 값이 작아지는 방향을 판단한다."),
            ("04", "이동 크기 결정하기", "학습률을 이용해 한 번에 이동할 크기를 정한다."),
            ("05", "반복하기", "새로운 위치에서 위 과정을 반복하며 최솟값에 가까워진다.")
        ]

        for number, title, description in steps:
            st.markdown(f"""
            <div class="point">
                <span style="color:#ff4b4b; font-weight:800;">{number}</span>
                <b>　{title}</b><br>
                {description}
            </div>
            """, unsafe_allow_html=True)
