# pages/2_Policy_Parameters.py
import streamlit as st
import time
import json
import config
import utils

st.set_page_config(layout="centered", page_title="Policy Parameters")

# 0. Check authentication
if not st.session_state.get("authenticated_team"):
    st.error("Please log in first.")
    st.switch_page("pages/0_Login.py") 
    st.stop()

team = st.session_state["authenticated_team"]

# 1. Intro
st.title(f"Welcome, team {config.country_flags[team]} {team}")
st.markdown("""
<style>
.big-caption { font-size: 17px !important; color: black !important; line-height: 1.6; margin-bottom: 1em; }
</style>
<div class='big-caption'>
    In this stage, you will define the <b>overall direction of your country's AI policy</b>. Your choices will directly influence the growth of notable academic papers which in turn accelerates the emergence of groundbreaking AI models such as ChatGPT or DeepSeek.
    <br><br>
    Each parameter belongs to a different policy category such as technical support, education, culture, stance, and diplomacy. You must allocate your 100 policy points across these options.
    <br><br>
    Note: <b>Willing_to_Cooperate</b> will play a key role during the cooperative parameter phase. All parameters will interact with future global or domestic events. Hover over each ❓ icon to view a brief description of each parameter.
            
> **"Hope is not a strategy."**  
> <i>– August Walker, Mission: Impossible - Fallout (2018)</i>
</div>
""", unsafe_allow_html=True)

st.divider()
st.markdown("""
<style>
.big-caption { font-size: 17px !important; color: black !important; line-height: 1.6; margin-bottom: 1em; }
</style>
<div class='big-caption'>
    <b>AI Paper annual growth rate ∝ </b>  (Technical * Human + Culture ) * Fixed Conditions + Event Bonus
    <br><br>
    <b>AI Model production rate ∝ </b> Total AI Paper produced (NOT a linear function) + Event Bonus
</div>
""", unsafe_allow_html=True)

st.divider()

# 2. policy parameters input
st.title("📜 Your AI Policy Parameters")

# `st.session_state` update if not initialized
if 'policy_params' not in st.session_state:
    all_params = [p for group in config.parameter_groups.values() for p in group]
    st.session_state.policy_params = {param: 5 for param in all_params}

# UI rendering
for group, params in config.parameter_groups.items():
    with st.expander(f"**{group}**", expanded=False):
        for param in params:
            # Special case: Alignment_US/China
            if param == "Alignment_US":
                us_val = st.session_state.policy_params.get("Alignment_US", 5)
                us = st.slider("Alignment US + China = 10", 0, 10, us_val, 
                               help=config.parameter_descriptions.get("Alignment_US", ""))
                st.session_state.policy_params["Alignment_US"] = us
                st.session_state.policy_params["Alignment_China"] = 10 - us
                
                percent = us * 10
                st.markdown(f"""
                    <div style='height: 10px; width: 100%; background: linear-gradient(to right, blue {percent}%, red {percent}%); border-radius: 5px;'></div>
                    <div style='display: flex; justify-content: space-between;'>
                        <span style='color: blue;'>US: {us}</span>
                        <span style='color: red;'>China: {10-us}</span>
                    </div>
                """, unsafe_allow_html=True)
            
            # Alignment_China not shown in slider
            elif param != "Alignment_China":
                # space for analysis button
                row_cols = st.columns([0.85, 0.15])
                
                with row_cols[0]:
                    val = st.slider(
                        param.replace("_", " "), 0, 10, 
                        st.session_state.policy_params.get(param, 5),
                        key=f"slider_{param}",
                        help=config.parameter_descriptions.get(param, "")
                    )
                    st.session_state.policy_params[param] = val
                
                with row_cols[1]:
                    # viod space for analysis button
                    st.markdown('<div style="height: 30px;"></div>', unsafe_allow_html=True) 
                    with st.popover("📈"):
                        st.markdown(config.parameter_insights.get(param, "Not available."))
                        
                        try:
                            chart = utils.plot_parameter_impact(
                                param, 
                                st.session_state.policy_params, 
                                config.fixed_values[team]
                            )
                            st.altair_chart(chart, use_container_width=True)
                        except ValueError as e:
                            st.info(f"ℹ️ This parameter does not directly affect the paper growth rate. (It may influence other phases of the game.)")
                        except Exception as e:
                            st.error(f"Error: {e}")

# 3. Calculate total score
st.divider()

current_params_for_sum = st.session_state.policy_params.copy()
current_params_for_sum.pop("Alignment_US", None)
current_params_for_sum.pop("Alignment_China", None)
total_score = sum(current_params_for_sum.values()) + 10 # Alignment 10 points

st.markdown(f"### **📊 Current Used Policy Points: {total_score} / 100**")

with st.expander("🟪 Fixed Conditions"):
    for k, v in config.fixed_values[team].items():
        st.markdown(f"**{k}**: {v}")

st.markdown("---")

if total_score > 100:
    st.error("❌ Total exceeds 100 policy points. Please adjust.")
else:
    if st.button("📥 Confirm Inputs", type="secondary"):
        hidden_params = st.session_state.policy_params
        growth = utils.compute_growth_rate(hidden_params, config.fixed_values[team])
        
        # Save hidden parameters to session state
        for k, v in hidden_params.items():
            st.session_state[f"hidden_params_{k}"] = v
        
        # file saving
        full_hidden_params = {**hidden_params, **config.fixed_values[team]}
        with open(f"shared_data/hidden_{team}.json", "w") as f:
            json.dump(full_hidden_params, f)
            
        st.session_state["growth_rate"] = growth
        st.session_state.hidden_confirmed = True
        
        st.success(f"📈 Estimated Growth Rate of Notable Papers: {growth} per round")
        st.toast("Proceeding to Cooperation Phase...")
        time.sleep(2)
        
        # To next page
        st.switch_page("pages/3_Cooperation.py")
    else:
        st.info("ℹ️ Please adjust your inputs and press 'Confirm Inputs' to compute growth rate.")