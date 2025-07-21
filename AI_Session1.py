# AI_Session.py
import streamlit as st
from datetime import datetime

# 페이지 기본 설정
st.set_page_config(
    page_title="SRT AI Politics",
    page_icon="🏛️",
    layout="centered"
)

# 세션 상태 초기화 (로그인 페이지로 리디렉션하기 위함)
if "page" not in st.session_state:
    st.session_state.page = "login"

if "authenticated_team" not in st.session_state:
    st.switch_page("pages/1_Login.py")

# 메인 페이지 콘텐츠
st.title(f"🏛️ SRT - AI Session Politics")
st.markdown(f"Welcome back, **Team {st.session_state.get('authenticated_team', 'Unknown')}**!")
st.markdown("""
<style>
.big-caption {
    font-size: 17px !important;
    color: black !important;
    line-height: 1.6;
    margin-bottom: 1em;
}
.important-line {
    font-weight: bold;
    font-size: 18px;
    margin-top: 1em;
}
</style>
<div class='big-caption'>
    <span class='important-line'>Your primary mission:</span> Secure your country’s success in AI development.
    <br>
    <span class='important-line'>Your secondary mission:</span> Since this is SRT AI Politics, aim to surpass the US and China in AI model development by cooperation (Sum of SRT &gt; US or China).
    <br><br>
    You can choose to <b>cooperate, compete, or remain neutral</b> toward other nations.
    <hr>
    <span class='important-line'>Key phases and concepts:</span>
    <ul>
        <li><b>AI model</b> 
            <ul>
                <li>Development of landmark AI systems like </b>ChatGPT</b> by your nation. This is your <b>#1 target</b>. </li>
                <li>Models increase via three routes: accumulation of AI papers, cooperation, and luck.</li>
                <li>As of 2025: US has 40, China has 15, your nation has none.</li>
            </ul> 
        <li><b>AI paper</b> 
            <ul>
                <li>Production of notable AI research papers, your <b>#2 target</b>. </li>
                <li>Paper growth is shaped by domestic policies, cooperation, and random events.</li>
                <li>As of 2025: US has 3200, China has 2000, your nation has below 200.</li>
            </ul>         
        <br>
        <li><b>Policy Phase</b> <br>Set domestic AI policies to determine base paper growth (+N papers/round).</li>
        <li><b>Cooperation Phase</b> <br> Negotiate cooperative parameters with other nations, affecting model and paper growth.</li>
        <li><b>Events</b><br> Random domestic or international events that affect AI progress.<br>
                        After domestic events, you can adjust policies. Will you trust or sabotage your partners?</li>
        <li><b>Summary Phase</b><br> Review AI model and paper growth, and see global standings at the end of each round.</li>
    </ul>
</div>
""", unsafe_allow_html=True)

st.info("Keep a record of your decisions and the reasons behind them, as you will need to analyze their outcomes in the final presentation.")

st.markdown("---")
st.markdown(f"""
<div style='text-align: center; font-size: 0.9em; margin-top: 20px; color: gray;'>
    Developed by Min Kwon, Seoul National University, with <i>a lot</i> of help from ChatGPT, Gemini, and Github Copilot. ({datetime.today().strftime('%Y-%m-%d')})
</div>
""", unsafe_allow_html=True)
