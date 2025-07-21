# pages/1_Login.py
import streamlit as st
from datetime import datetime
import config

st.set_page_config(layout="centered", page_title="Login")

# 1. After login
if st.session_state.get("authenticated_team"):
        
    
    st.markdown("""
        # 🏛️ **SRT - AI Session Politics**
         
         If you wish to change your team or log out, reload the page.
         
         Otherwise, hit the Main Page button below to receive your mission briefing again.   
        """, unsafe_allow_html=True)
    
    st.success(f"You are already logged in as Team {st.session_state.authenticated_team}.")
    
    if st.button("Main Page"):
        st.switch_page("AI_Session.py")

# 2. Before login
else:
    st.markdown("""
        # 🏛️ **SRT - AI Session Politics**
         Welcome to the 2025 SRT AI Politics session.
        
         In this session, you are entrusted with the strategic leadership of your nation. <i>Your mission, should you choose to accept it</i>, is to **secure your country’s success**—whether through cooperation, competition, or isolation—in a world where artificial intelligence is becoming a defining force.

        As a policymaker, you will **shape your nation's AI strategy** at home and abroad—crafting domestic policies and negotiating international cooperation, both of which directly impact the growth of influential AI research and the emergence of SOTA(State-of-the-Art) AI models.
        
        Along the way, you must navigate the geopolitical tensions between the U.S. and China, deciding where your nation's loyalties lie—or choosing to remain neutral.

        <i>This message will self-destruct after login.</i>
        """, unsafe_allow_html=True)

    with st.form("login_form"):
        team_name = st.selectbox("Select your team:", list(config.team_credentials.keys()))
        team_code = st.text_input("Enter team code (password):", type="password")
        if st.form_submit_button("Login"):
            if config.team_credentials.get(team_name) == team_code:
                st.session_state["authenticated_team"] = team_name
                st.success("Login successful! Redirecting...")
                st.switch_page("pages/2_Policy.py")
            else:
                st.error("Incorrect team code.")

    st.markdown(f"""
<div style='text-align: center; font-size: 0.9em; margin-top: 20px; color: gray;'>
    Developed by Min Kwon, Seoul National University, with <i>a lot</i> of help from ChatGPT, Gemini, and Github Copilot. ({datetime.today().strftime('%Y-%m-%d')})
</div>
""", unsafe_allow_html=True)
