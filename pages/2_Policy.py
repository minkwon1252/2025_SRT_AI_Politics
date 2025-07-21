# pages/2_Policy_Parameters.py
import streamlit as st
import time
import json
import config
import utils

st.set_page_config(layout="centered", page_title="Policy Parameters")

# 로그인 확인
if not st.session_state.get("authenticated_team"):
    st.error("Please log in first.")
    st.switch_page("pages/1_Login.py")

team = st.session_state["authenticated_team"]
st.title(f"Welcome, team {config.country_flags[team]} {team}")

st.markdown("""
<style>
.big-caption { font-size: 17px !important; color: black !important; line-height: 1.6; margin-bottom: 1em; }
.important-line { font-weight: bold; font-size: 18px; margin-top: 1em; }
</style>
<div class='big-caption'>
    In this stage, you will define the <b>overall direction of your country's AI policy</b>. Your choices will directly influence the growth of notable academic papers—like <i>“Attention is All You Need”</i>—which in turn accelerates the emergence of groundbreaking AI models such as ChatGPT or DeepSeek.
    <br><br>
    Each parameter belongs to a different policy category such as technical support, education, culture, stance, and diplomacy. You must allocate your 100 policy points across these options.
    <br><br>
    Note: <b>Sharing_Tendency</b> and <b>Willing_to_Cooperate</b> will play a key role during the cooperative parameter phase. All parameters, including your stance and investments, will influence how much your country benefits from future global or domestic events—affecting both AI model and paper growth. Hover over each ❓ icon to see a short description of what each parameter means.

> **"Hope is not a strategy."**  
> <i>– August Walker, Mission: Impossible - Fallout (2018)</i>
""", unsafe_allow_html=True)

st.title(f"📜 Your AI Policy Parameters")
hidden_params = {}
total_score = 0

for group, params in config.parameter_groups.items():
    with st.expander(f"**{group}**"):
        for param in params:
            if param == "Alignment_US":
                us = st.slider("Alignment_US + Alignment_China = 10", 0, 10, 5, key="Alignment_US", help=config.parameter_descriptions["Alignment_US"])
                cn = 10 - us
                hidden_params["Alignment_US"] = us
                hidden_params["Alignment_China"] = cn
                percent = us * 10
                st.markdown(f"""
                    <div style='height: 10px; width: 100%; background: linear-gradient(to right, blue {percent}%, red {percent}%); border-radius: 5px;'></div>
                    <div style='display: flex; justify-content: space-between;'>
                        <span style='color: blue;'>US: {us}</span>
                        <span style='color: red;'>China: {cn}</span>
                    </div>
                """, unsafe_allow_html=True)
                total_score += 10
            elif param != "Alignment_China":
                val = st.slider(param, 0, 10, 5, key=param, help=config.parameter_descriptions.get(param, ""))
                hidden_params[param] = val
                total_score += val

st.markdown(f"**📊 Current Used Policy Points: {total_score}/100**")

with st.expander("🟪 Fixed Conditions"):
    for k, v in config.fixed_values[team].items():
        st.markdown(f"**{k}**: {v}")

st.markdown("---")

if total_score > 100:
    st.error("❌ Total exceeds 100 policy points. Please adjust.")
else:
    if st.button("📥 Confirm Inputs"):
        growth = utils.compute_growth_rate(hidden_params, config.fixed_values[team])

        for k, v in hidden_params.items():
            st.session_state[f"hidden_params_{k}"] = v
        
        full_hidden_params = {**hidden_params, **config.fixed_values[team]}
        
        with open(config.shared_dir / f"hidden_{team}.json", "w") as f:
            json.dump(full_hidden_params, f)

        st.session_state["growth_rate"] = growth
        st.session_state.hidden_confirmed = True

        st.success(f"📈 Estimated Growth Rate of Notable Papers: {growth} per round")
        st.toast("Proceeding to Cooperation Phase...")
        time.sleep(2)
        st.switch_page("pages/3_Cooperation.py")
    else:
        st.info("ℹ️ Please adjust your inputs and press 'Confirm Inputs' to compute growth rate.")
