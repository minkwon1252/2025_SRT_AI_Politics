# pages/3_Cooperation.py
import streamlit as st
import pandas as pd
import copy
import json
import time
import config  

st.set_page_config(layout="centered", page_title="Cooperation Phase")

# --- 1. compute_matrix 함수를 파일 내부에 정의 ---
def compute_matrix(state, partners):
    columns = ["Parameter", "Points"] + partners
    rows = []
    total_points_used = 0
    country_points = {p: 0 for p in partners}

    # config.coop_params를 사용하도록 수정
    for param, meta in config.coop_params.items():
        row = [param, meta["points"]]
        for country in partners:
            val = state[country].get(param, "None")
            display = val if val != "None" else "No"
            row.append(display)
            if val not in ["None", "No", "", None]:
                total_points_used += meta["points"]
                country_points[country] += meta["points"]
        rows.append(row)
    
    df = pd.DataFrame(rows, columns=columns)
    used_row = ["Used Points", sum(country_points.values())] + [country_points.get(p, 0) for p in partners]
    df.loc[len(df.index)] = used_row
    df = df.astype(str)
    return df, total_points_used

# --- 로그인 확인 ---
if not st.session_state.get("authenticated_team"):
    st.error("Please log in first.")
    st.switch_page("pages/1_Login.py")

team = st.session_state["authenticated_team"]
partners = [c for c in config.team_credentials if c != team]

st.title(f"🤝 {team} - Cooperative Parameters")
# --- 2. st.session_state 키를 Policy 페이지에서 저장한 키와 일치시킴 ---
coop_limit = 20 + st.session_state.get("hidden_params_Willing_to_Cooperate", 5)
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
    In this phase, you will manage your nation's <b>cooperative AI strategy</b>—deciding how much to share, whom to partner with, and what kind of global AI initiatives to support.
    <br><br>
    You can choose to share computing power, data, talent, or energy. You may also form joint projects or align with international AI standards. Each decision impacts how much your country contributes to and gains from global AI advancement.
    <br><br>
    Your choices are constrained by your <b>Willing_to_Cooperate</b> parameter and the remaining cooperation points. Cooperative actions require mutual agreement between nations, so choose your offers wisely.
    <br><br>
    You might face a <b>Prisoner’s Dilemma</b>, where sharing resources like semiconductors benefits both sides—but only if trust isn’t broken. Or a <b>Stag Hunt</b> might happen, where major gains are possible only when both nations commit fully. Or else, you might find yourself in a <b>Chicken Game</b>, where refusing to join a joint project leads to a dangerous standoff if no one backs down. Choose wisely.

> **"I just want everyone to get along. With me, especially."**  
> <i>– White Widow, Mission: Impossible – Dead Reckoning (2023)</i>
</div>
""", unsafe_allow_html=True)

with st.expander("📜 View Your Hidden Parameters"):
    hidden_params_display = {k.replace("hidden_params_", ""): v for k, v in st.session_state.items() if k.startswith("hidden_params_")}
    st.json(hidden_params_display)

with st.expander("📈 Estimated Paper Growth (from Hidden Parameters)", expanded=False):
    st.markdown(f"**📈 Notable Papers Growth Rate:** {st.session_state.get('growth_rate', 'N/A')} per round")

if "cooperation_state" not in st.session_state:
    # --- 3. config.coop_params를 사용하도록 수정 ---
    st.session_state.cooperation_state = {
        c: {k: "None" if v["type"] != "bool" else "No" for k, v in config.coop_params.items()} for c in partners
    }

# 이제 내부 함수인 compute_matrix를 호출합니다.
matrix_df, all_used = compute_matrix(st.session_state.cooperation_state, partners)
st.markdown("### 🌐 Cooperation Matrix")
st.dataframe(matrix_df, use_container_width=True, height=425)
st.markdown(f"**Total Points Used: {all_used} / {coop_limit}**")

st.markdown("### 🧭 Choose a country to negotiate with:")
selected_country = st.selectbox("Select partner country:", partners)

# --- 4. country_flags와 coop_params 앞에 config. 접두사 추가 ---
with st.expander(f"{config.country_flags[selected_country]} {selected_country} Cooperative Parameters", expanded=True):
    two_column_keys = [
        "Computing_Power_Shared", "Energy_Shared",
        "Data_Shared", "Cybersecurity_Pact",
        "Talent_Exchange", "Shared_Research_Centers",
        "Dual_Use_Restrictions", "Emergency_Pact"
    ]

    cols = st.columns(2)
    for i, key in enumerate(two_column_keys):
        meta = config.coop_params[key]
        helptext = meta["desc"] + f" (+{meta['points']} pts)"
        col = cols[i % 2]
        with col:
            if meta["type"] == "bool":
                st.radio(key, ["No", "Yes"], key=f"{selected_country}_{key}", help=helptext, horizontal=True)

    for key in ["Joint_Project", "AI_Standard_Alignment"]:
        meta = config.coop_params[key]
        helptext = meta["desc"] + f" (+{meta['points']} pts)"
        options = meta.get("options", [])
        if meta["type"] == "select":
            st.selectbox(key, options, key=f"{selected_country}_{key}", help=helptext)
        elif meta["type"] == "radio3": # AI_Standard_Alignment
             st.radio(key, options, key=f"{selected_country}_{key}", help=helptext)


if st.button(f"📩 Confirm Agreement with {config.country_flags[selected_country]} {selected_country}"):
    temp_state = copy.deepcopy(st.session_state.cooperation_state)
    # --- 5. coop_params 앞에 config. 접두사 추가 ---
    for key in config.coop_params:
        widget_key = f"{selected_country}_{key}"
        if widget_key in st.session_state:
            val = st.session_state.get(widget_key)
            temp_state[selected_country][key] = val

    st.session_state.cooperation_state = temp_state
    
    # --- 6. shared_dir 앞에 config. 접두사 추가 ---
    with open(config.shared_dir / f"cooperation_{team}.json", "w") as f:
        json.dump(st.session_state.cooperation_state, f)

    _, used = compute_matrix(st.session_state.cooperation_state, partners)

    if used > coop_limit:
        st.error(f"❌ Saving this agreement would exceed the total point limit. Limit = {coop_limit}, used = {used}")
    else:
        st.toast(f"✅ {selected_country} agreement saved! Total used: {used}/{coop_limit}")
        time.sleep(1)
        st.rerun()

if st.button("📥 Confirm All Cooperative Parameters"):
    all_matched = True
    mismatches = []
    
    try:
        for other_team in partners:
            their_file = config.shared_dir / f"cooperation_{other_team}.json"
            if their_file.exists():
                with open(their_file) as f:
                    their_data = json.load(f)
                for key in config.coop_params:
                    my_val = st.session_state.cooperation_state.get(other_team, {}).get(key, "None")
                    their_val = their_data.get(team, {}).get(key, "None")
                    if my_val != their_val:
                        all_matched = False
                        mismatches.append((other_team, key))
            else:
                all_matched = False
                st.warning(f"Waiting for {other_team} to save their choices.")
                
    except Exception as e:
        st.error(f"Error checking agreements: {e}")
        all_matched = False

    _, used = compute_matrix(st.session_state.cooperation_state, partners)

    if used > coop_limit:
        st.error(f"❌ Too many points used. Limit = {coop_limit}, used = {used}")
    elif not all_matched:
        st.error("❌ Agreement mismatch detected:")
        for other, param in mismatches:
            st.markdown(f"- Mismatch on **{param}** with **{other}**")
    else:
        st.session_state.cooperation_confirmed = True
        st.success(f"✅ All matched! Used {used} / {coop_limit} points. Proceeding to event phase...")
        time.sleep(2)
        st.switch_page("pages/4_Events.py")