
import streamlit as st

st.set_page_config(
    page_title="경사하강법 소개",
    page_icon="📉",
    layout="wide"
)

# -------------------------------
# 디자인 설정
# -------------------------------
st.markdown("""
<style>
.stApp {
    background-color: #101010;
    color: white;
}

.block-container {
    max-width: 1100px;
    padding-top: 3rem;
    padding-bottom: 3rem;
}

.main-title {
    font-size: 58px;
    font-weight: 900;
    margin-bottom: 35px;
    letter-spacing: -2px;
    color: white;
}

.subtitle {
    font-size: 23px;
    color: #aaaaaa;
    margin-bottom: 55px;
}

.line {
    border-top: 2px solid #777777;
    margin-top: 35px;
    margin-bottom: 65px;
}

.contents-title {
    font-size: 34px;
    font-weight: bold;
    margin-bottom: 28px;
    color: white;
}

.section-title {
    font-size: 38px;
    font-weight: bold;
    margin-bottom: 30px;
    color: white;
}

.page-label {
    color: #ff625e;
    font-size: 18px;
    font-weight: bold;
    letter-spacing: 4px;
    margin-bottom: 25px;
}

.content-box {
    background-color: #202020;
    border: 1px solid #444444;
    border-radius: 15px;
    padding: 28px;
    margin-bottom: 20px;
    font-size: 18px;
    line-height: 1.8;
    color: white;
}

.point {
    color: #ff625e;
    font-weight: bold;
}

.formula-box {
    background-color: #252525;
    border: 1px solid #555555;
    border-radius: 15px;
    padding: 25px;
    margin: 25px 0;
}

div.stButton > button {
    background-color: #202020;
    color: white;
    border: 1px solid #444444;
    border-radius: 20px;
    width: 100%;
    height: 150px;
    text-align: left;
    padding: 20px;
    font-size: 20px;
    font-weight: bold;
    transition: 0.2s;
}

div.stButton > button:hover {
    background-color: #333333;
    border: 1px solid #ff625e;
    color: white;
}

div.stButton > button:focus {
    color: white;
    border: 1px solid #ff625e;
}

.back-button div.stButton > button {
    height: 55px;
    text-align: center;
    background-color: #303030;
    font-size: 16px;
}
</style>
""", unsafe_allow_html=True)


# -------------------------------
# 화면 이동 상태
# -------------------------------
if "page" not in st.session_state:
    st.session_state.page = 0


contents = [
    "경사하강법이란?",
    "미분의 역할",
    "미분값과 학습률",
    "경사하강법의 수식",
    "경사하강법의 작동 과정"
]


# -------------------------------
# 첫 화면
# -------------------------------
if st.session_state.page == 0:

    st.markdown(
        '<div class="main-title">경사하강법 소개</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">미분으로 이해하는 인공지능의 최적화 원리</div>',
        unsafe_allow_html=True
    )

    st.markdown('<div class="line"></div>', unsafe_allow_html=True)

    st.markdown(
        '<div class="contents-title">목차</div>',
        unsafe_allow_html=True
    )

    cols = st.columns(3)

    for i in range(3):
        with cols[i]:
            if st.button(
                f"{i+1:02d}\n\n{contents[i]}",
                key=f"menu_{i+1}"
            ):
                st.session_state.page = i + 1
                st.rerun()

    cols = st.columns(3)

    for i in range(3, 5):
        with cols[i-3]:
            if st.button(
                f"{i+1:02d}\n\n{contents[i]}",
                key=f"menu_{i+1}"
            ):
                st.session_state.page = i + 1
                st.rerun()

    st.markdown('<div class="line"></div>', unsafe_allow_html=True)


# -------------------------------
# 각 내용 화면
# -------------------------------
else:

    page = st.session_state.page

    st.markdown('<div class="back-button">', unsafe_allow_html=True)

    if st.button("← 처음 화면으로", key="back"):
        st.session_state.page = 0
        st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown(
        f'<div class="page-label">{page:02d} / 05</div>',
        unsafe_allow_html=True
    )

    # ---------------------------
    # 1. 경사하강법이란?
    # ---------------------------
    if page == 1:

        st.markdown(
            '<div class="section-title">경사하강법이란?</div>',
            unsafe_allow_html=True
        )

        st.markdown("""
        <div class="content-box">
        경사하강법은 <span class="point">미분을 활용하여 함수의 최솟값을 찾아가는 최적화 알고리즘</span>이다.
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        함수의 최솟값을 찾으려면 현재 위치에서 함수의 값이 작아지는 방향을 알아야 한다.

        경사하강법은 이때 미분을 이용한다. 현재 위치에서의 미분값을 확인하고, 함수의 값이 작아지는 방향으로 조금씩 이동하는 과정을 반복한다.
        """)

        st.markdown("### 손실함수란?")

        st.markdown("""
        인공지능이 예측한 값과 실제 값 사이의 차이를 수학적으로 나타낸 함수를 손실함수라고 한다.

        경사하강법은 이 손실함수의 값을 줄이는 방향으로 이동하여 최솟값을 찾는다.
        """)

        st.markdown("""
        **경사하강법의 핵심 과정**

        1. 현재 위치를 정한다.
        2. 현재 위치에서 미분값을 구한다.
        3. 함수의 값이 작아지는 방향으로 이동한다.
        4. 이 과정을 반복하여 최솟값에 가까워진다.
        """)

    # ---------------------------
    # 2. 미분의 역할
    # ---------------------------
    elif page == 2:

        st.markdown(
            '<div class="section-title">미분의 역할</div>',
            unsafe_allow_html=True
        )

        st.markdown("""
        <div class="content-box">
        미분은 특정 지점에서 함수가 얼마나 빠르게 변하는지 나타내는
        <span class="point">순간변화율</span>이다.
        </div>
        """, unsafe_allow_html=True)

        st.markdown("### 미분은 왜 필요할까?")

        st.markdown("""
        산을 내려가는 상황을 생각해 보자.

        현재 내가 산의 어느 지점에 있다고 가정해 보자.
        가장 낮은 지점으로 내려가려면 먼저 어느 방향으로 움직여야 하는지 알아야겠지?

        이때 **미분을 활용해.**
        """)

        st.markdown("""
        <div class="content-box">
        현재 위치에서 산의 기울기를 확인하면 어느 방향으로 내려가야 하는지 판단할 수 있어.

        이처럼 미분은 현재 위치에서 함수의 값이 작아지는 방향을 알아내는 데 도움을 준다.
        </div>
        """, unsafe_allow_html=True)

        st.markdown("### 미분값에 따라 이동 방향은 달라진다.")

        st.markdown("""
        경사하강법에서는 현재 위치의 미분값을 확인하고,
        그 부호에 따라 함수의 값이 작아지는 방향으로 이동한다.
        """)

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("""
            <div class="content-box">
            <h3>미분값이 양수일 때</h3>
            오른쪽으로 갈수록 함수의 값이 커지므로
            <span class="point">왼쪽 방향</span>으로 이동한다.
            </div>
            """, unsafe_allow_html=True)

        with col2:
            st.markdown("""
            <div class="content-box">
            <h3>미분값이 음수일 때</h3>
            오른쪽으로 갈수록 함수의 값이 작아지므로
            <span class="point">오른쪽 방향</span>으로 이동한다.
            </div>
            """, unsafe_allow_html=True)

        st.markdown("""
        미분값이 0이 되면 순간적인 기울기가 0이라는 뜻이다.

        다만 미분값이 0인 지점이 항상 최솟값인 것은 아니다.
        """)

    # ---------------------------
    # 3. 미분값과 학습률
    # ---------------------------
    elif page == 3:

        st.markdown(
            '<div class="section-title">미분값과 학습률</div>',
            unsafe_allow_html=True
        )

        st.markdown("""
        <div class="content-box">
        학습률은 경사하강법에서 한 번에 얼마나 이동할지를 결정하는
        <span class="point">이동 크기</span>이다.
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        미분값이 이동할 방향과 변화 정도를 알려 준다면, 학습률은 실제로 이동하는 크기를 조절한다.
        """)

        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown("""
            <div class="content-box">
            <h3>학습률이 너무 작을 때</h3>
            이동하는 크기가 작아 최솟값을 찾는 데 시간이 오래 걸릴 수 있다.
            </div>
            """, unsafe_allow_html=True)

        with col2:
            st.markdown("""
            <div class="content-box">
            <h3>적절할 때</h3>
            최솟값을 향해 안정적으로 이동할 수 있다.
            </div>
            """, unsafe_allow_html=True)

        with col3:
            st.markdown("""
            <div class="content-box">
            <h3>너무 클 때</h3>
            최솟값을 지나쳐 이동하거나 오히려 최솟값에서 멀어질 수 있다.
            </div>
            """, unsafe_allow_html=True)

    # ---------------------------
    # 4. 경사하강법의 수식
    # ---------------------------
    elif page == 4:

        st.markdown(
            '<div class="section-title">경사하강법의 수식</div>',
            unsafe_allow_html=True
        )

        st.markdown("""
        경사하강법은 현재 위치에서의 미분값과 학습률을 이용하여 다음 위치를 계산한다.
        """)

        # 수식을 회색 상자 안에 표시
        st.markdown('<div class="formula-box">', unsafe_allow_html=True)
        st.latex(r"x_{t+1}=x_t-\alpha f'(x_t)")
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown("### 수식에 포함된 기호")

        st.markdown("""
        - **\(x_t\)** : 현재 위치: 지금 함수 위에서 내가 서 있는 지점이다.
        - **\(x_{t+1}\)** : 다음 위치: 미분값과 학습률을 이용해 새롭게 계산한 지점이다.
        - **\(\alpha\)** : 학습률: 한 번에 얼마나 이동할지 결정한다.
        - **\(f'(x_t)\)** : 현재 위치에서의 미분값: 현재 함수의 기울기를 나타낸다.
        """)

        st.markdown("### 왜 미분값을 빼는 것일까?")

        st.markdown("""
        경사하강법은 함수의 값이 작아지는 방향으로 이동해야 한다.

        - 미분값이 양수라면 오른쪽으로 갈수록 함수의 값이 커지므로 왼쪽으로 이동해야 한다.
        - 미분값이 음수라면 오른쪽으로 갈수록 함수의 값이 작아지므로 오른쪽으로 이동해야 한다.

        따라서 현재 위치에서 **미분값에 학습률을 곱한 값을 빼는 방식**으로 다음 위치를 계산한다.
        """)

        st.markdown("### 실제 계산으로 이해하기")

        st.markdown("""
        다음과 같은 함수를 생각해 보자.
        """)

        st.latex(r"f(x)=(x-4)^2")

        st.markdown("""
        이 함수의 미분값은 다음과 같다.
        """)

        st.latex(r"f'(x)=2(x-4)")

        st.markdown("""
        현재 위치를 \(x=0\), 학습률을 \(\alpha=0.25\)라고 가정해 보자.

        **① 현재 위치에서 미분값 구하기**
        """)

        st.latex(r"f'(0)=2(0-4)=-8")

        st.markdown("""
        미분값이 -8이므로 현재 위치에서 함수는 오른쪽으로 갈수록 감소하는 방향이다.
        
        **② 경사하강법의 수식에 대입하기**
        """)

        st.latex(r"x_{t+1}=0-0.25\\times(-8)")

        st.markdown("**③ 다음 위치 계산하기**")

        st.latex(r"x_{t+1}=2")

        st.markdown("""
        처음에는 \(x=0\)에 있었지만, 계산 결과 다음 위치는 \(x=2\)가 되었다.

        즉, 경사하강법은 미분값을 이용해 이동 방향을 정하고, 학습률을 곱해 이동 크기를 조절한 것이다.
        """)

        st.markdown("""
        <div class="content-box">
        <span class="point">핵심 정리</span><br>
        현재 위치에서 미분값을 구하고, 여기에 학습률을 곱한 값을 현재 위치에서 빼면 다음 위치를 구할 수 있다.
        </div>
        """, unsafe_allow_html=True)

    # ---------------------------
    # 5. 경사하강법의 작동 과정
    # ---------------------------
    elif page == 5:

        st.markdown(
            '<div class="section-title">경사하강법의 작동 과정</div>',
            unsafe_allow_html=True
        )

        st.markdown("""
        지금까지 살펴본 미분값과 학습률이 실제 경사하강법에서 어떻게 연결되는지 정리해 보자.
        """)

        steps = [
            ("01", "현재 위치 확인", "함수 위에서 현재 위치를 정한다."),
            ("02", "미분값 계산", "현재 위치에서 함수의 미분값을 구한다."),
            ("03", "이동 방향 결정", "미분값의 부호를 통해 함수의 값이 작아지는 방향을 판단한다."),
            ("04", "이동 크기 결정", "학습률을 이용하여 한 번에 이동할 크기를 정한다."),
            ("05", "반복", "새로운 위치에서 같은 과정을 반복하며 최솟값에 가까워진다.")
        ]

        for number, title, description in steps:
            st.markdown(f"""
            <div class="content-box">
                <span class="point">{number}</span>
                <h3>{title}</h3>
                {description}
            </div>
            """, unsafe_allow_html=True)

        st.markdown("""
        <div class="content-box">
        <span class="point">핵심 정리</span><br>
        경사하강법은 미분값으로 이동 방향을 판단하고, 학습률로 이동 크기를 조절하면서 함수의 최솟값을 찾아가는 방법이다.
        </div>
        """, unsafe_allow_html=True)
