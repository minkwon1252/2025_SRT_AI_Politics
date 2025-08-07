# pages/Admin_Dashboard.py
import streamlit as st
import json
import os
import glob
import pandas as pd
import config  # 여러분의 config.py 파일
import utils   # 여러분의 utils.py 파일

st.set_page_config(layout="wide", page_title="Admin Dashboard")

# --- 관리자 인증 ---
def check_password():
    """비밀번호가 맞으면 True를, 틀리면 False를 반환합니다."""
    if "admin_authenticated" not in st.session_state:
        st.session_state.admin_authenticated = False

    if not st.session_state.admin_authenticated:
        password = st.sidebar.text_input("Enter Admin Password:", type="password")
        if st.sidebar.button("Login"):
            # st.secrets에서 비밀번호를 가져와 비교합니다.
            if password == st.secrets.get("ADMIN_PASSWORD", "admin1234"):
                st.session_state.admin_authenticated = True
                st.rerun()
            else:
                st.sidebar.error("Incorrect password")
    return st.session_state.admin_authenticated

if not check_password():
    st.title("🔒 Admin Access Required")
    st.warning("Please enter the admin password in the sidebar to proceed.")
    st.stop()


# --- 인증 후 대시보드 표시 ---
st.title("👑 Admin Dashboard")
st.markdown("Monitor the current state of the game and manage game files.")

# --- 1. 현재 라운드 정보 ---
try:
    history = utils.load_history()
    current_round_num = len(history) + 1
    st.header(f"🔵 Current Status: Round {current_round_num}")
except Exception as e:
    st.error(f"Could not load history.json: {e}")
    current_round_num = 1


# --- 2. 공용 파일 상태 ---
st.header("🗂️ Shared Game Files")
col1, col2 = st.columns(2)

with col1:
    st.subheader("International Event")
    try:
        with open(config.shared_dir / "international.json", "r") as f:
            st.json(json.load(f))
    except FileNotFoundError:
        st.info("international.json does not exist yet.")
    except Exception as e:
        st.error(f"Error reading international.json: {e}")

with col2:
    st.subheader("Game History")
    try:
        with open(config.shared_dir / "history.json", "r") as f:
            st.json(json.load(f))
    except FileNotFoundError:
        st.info("history.json does not exist yet.")
    except Exception as e:
        st.error(f"Error reading history.json: {e}")


# --- 3. 플레이어별 진행 상황 ---
st.header("👨‍💻 Player Status & Submissions")
all_player_teams = list(config.team_credentials.keys())
player_status_data = []

for team in all_player_teams:
    status = {"Team": f"{config.country_flags.get(team, '🏳️')} {team}"}
    hidden_file = config.shared_dir / f"hidden_{team}.json"
    coop_file = config.shared_dir / f"cooperation_{team}.json"
    
    status["Policy Submitted (hidden.json)"] = "✅ Yes" if hidden_file.exists() else "❌ No"
    status["Cooperation Submitted (coop.json)"] = "✅ Yes" if coop_file.exists() else "❌ No"
    player_status_data.append(status)

st.dataframe(pd.DataFrame(player_status_data), use_container_width=True)

# 각 플레이어의 제출 파일 내용 확인
with st.expander("📂 View Submitted File Contents"):
    for team in all_player_teams:
        st.subheader(f"{config.country_flags.get(team, '🏳️')} {team}")
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("**Policy Parameters (hidden.json)**")
            try:
                with open(config.shared_dir / f"hidden_{team}.json", "r") as f:
                    st.json(json.load(f))
            except FileNotFoundError:
                st.write("Not submitted yet.")
        with c2:
            st.markdown("**Cooperation Parameters (cooperation.json)**")
            try:
                with open(config.shared_dir / f"cooperation_{team}.json", "r") as f:
                    st.json(json.load(f))
            except FileNotFoundError:
                st.write("Not submitted yet.")
        st.divider()


# --- 4. 관리자 액션 ---
st.header("⚙️ Admin Actions")
st.warning("⚠️ These actions directly modify game files. Use with caution.")

if st.button("🔴 Clear Files for Next Round"):
    try:
        # 5_Summary.py에 있는 파일 삭제 로직을 그대로 사용
        files_to_clear = [config.shared_dir / "international.json"]
        for country_name in all_player_teams:
            files_to_clear.append(config.shared_dir / f"domestic_{country_name}.json")
            files_to_clear.append(config.shared_dir / f"cooperation_{country_name}.json") # Coop 파일도 삭제

        cleared_files, failed_files = [], []
        for f in files_to_clear:
            if f.exists():
                try:
                    f.unlink()
                    cleared_files.append(f.name)
                except Exception as e:
                    failed_files.append(f"{f.name}: {e}")
        
        if cleared_files:
            st.success(f"Successfully cleared files: {', '.join(cleared_files)}")
        if failed_files:
            st.error(f"Failed to clear some files: {', '.join(failed_files)}")
        st.toast("Round files have been cleared!")
    except Exception as e:
        st.error(f"An error occurred during file clearing: {e}")

if st.button("🚨 Reset ENTIRE Game History (Deletes history.json)"):
    history_file = config.shared_dir / "history.json"
    if history_file.exists():
        history_file.unlink()
        st.success("history.json has been deleted. The game history is now reset.")
    else:
        st.info("history.json does not exist. No action taken.")
