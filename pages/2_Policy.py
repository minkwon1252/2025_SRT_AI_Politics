# pages/2_Policy.py
import streamlit as st
import time
import json
import config
import utils
import random
import re

st.set_page_config(layout="centered", page_title="Policy Parameters")

# 0. Check authentication
if not st.session_state.get("authenticated_team"):
    st.error("Please log in first.")
    st.switch_page("pages/0_Login.py")
    st.stop()

team = st.session_state["authenticated_team"]

# `st.session_state` 초기화
if 'reveal_clicks' not in st.session_state:
    st.session_state.reveal_clicks = 0
if 'last_growth_rate' not in st.session_state:
    st.session_state.last_growth_rate = None

# =================================================================
# Sidebar Event hint
# =================================================================
st.sidebar.header("📌 Event Hints")

# --- 1. Domestic Event 힌트 표시 ---
if st.session_state.get('event_title') and st.session_state.get('domestic_event_hints'):
    st.sidebar.subheader(f"🏠 {st.session_state['event_title']}")
    with st.sidebar.expander("View Domestic Hints"):
        for hint in st.session_state.domestic_event_hints:
            st.info(f"**{hint.replace('_', ' ')}** is a key parameter.")

# --- 2. International Event 힌트 생성 및 표시 ---
# 힌트가 아직 생성되지 않았을 때만 생성
if "international_event_hints" not in st.session_state:
    st.session_state.international_event_hints = []
    if "international_events_1_circumstance" in st.session_state:
        event = st.session_state.international_events_1_circumstance[0]
        st.session_state.international_event_title = event.get("title", "N/A")
        logic = event.get("logic", {})

        # [수정] Dilemma 타입 이벤트인 경우, 규칙을 직접 표시
        if event.get("evaluation_type") == "interactive" and logic.get("type") == "dilemma":
            st.session_state.international_event_hints = {
                "type": "dilemma",
                "activation": logic.get("activation_param", "N/A"),
                "comparison": logic.get("comparison_param", "N/A"),
                "threshold": logic.get("threshold", "N/A")
            }
        # 그 외의 경우, 기존처럼 수식에서 파라미터 추출
        else:
            formulas = event.get("delta_models", "") + " " + event.get("delta_papers", "")
            if formulas:
                params_in_formulas = set(re.findall(r'\b[A-Za-z_]+\b', formulas))
                keywords = {'if', 'else', 'round', 'log', 'exp', 'min', 'max', 'int', 'np', 'sqrt', 'True', 'False', 'and', 'or', 'not'}
                all_possible_params = (
                    set(config.parameter_descriptions.keys()) |
                    set(config.fixed_values.get(team, {}).keys()) |
                    set(config.coop_param_keys)
                )
                relevant_params = [p for p in params_in_formulas if p in all_possible_params and p not in keywords]
                
                if len(relevant_params) > 2:
                    st.session_state.international_event_hints = random.sample(relevant_params, 2)
                else:
                    st.session_state.international_event_hints = relevant_params

# 생성된 International 힌트 표시
if st.session_state.get('international_event_title'):
    st.sidebar.subheader(f"🗺️ {st.session_state['international_event_title']}")
    with st.sidebar.expander("View International Hints"):
        hints = st.session_state.get('international_event_hints')
        
        # [수정] 힌트 포맷에 따라 다르게 표시
        if isinstance(hints, dict) and hints.get("type") == "dilemma":
            st.warning(f"This is a **Dilemma** type event. Your outcome depends on your partner's choice.")
            st.markdown(f"**Activation Rule:**")
            st.code(f"{hints.get('activation')}", language="python")
            st.markdown(f"**Comparison Parameter:** `{hints.get('comparison')}`")
            st.markdown(f"**Threshold:** `{hints.get('threshold')}`")
        elif isinstance(hints, list) and hints:
            for hint in hints:
                st.warning(f"**{hint.replace('_', ' ')}** is a key parameter.")
        else:
            st.info("No specific parameter hints for this event.")


st.sidebar.divider()
# =================================================================
# [SIDEBAR HINT END]
# =================================================================


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
            
> **"Hope is not a strategy."** > <i>– August Walker, Mission: Impossible - Fallout (2018)</i>
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

# 4. Sidebar button for revealing growth rate
st.sidebar.title("Growth Rate Peek")

# 마지막으로 확인한 성장률이 있다면 표시
if st.session_state.last_growth_rate is not None:
    st.sidebar.metric("Last Checked Growth Rate", f"{st.session_state.last_growth_rate}")
    st.sidebar.divider()

clicks_left = 3 - st.session_state.reveal_clicks

if clicks_left > 0:
    st.sidebar.write(f"You have **{clicks_left}** peeks remaining.")
    if st.sidebar.button("📈 Reveal Current Paper Growth Rate"):
        if total_score > 100:
            st.sidebar.error("Cannot calculate with over 100 points.")
        else:
            st.session_state.reveal_clicks += 1
            # 성장률을 계산하고 session_state에 저장
            current_params = st.session_state.policy_params
            growth = utils.compute_growth_rate(current_params, config.fixed_values[team])
            st.session_state.last_growth_rate = growth
            st.toast("Growth rate calculated!")
            # UI 즉시 업데이트를 위해 스크립트 재실행
            st.rerun()
else:
    st.sidebar.warning("You have no more peeks left.")

with st.expander("🟪 Fixed Conditions"):
    for k, v in config.fixed_values[team].items():
        st.markdown(f"**{k}**: {v}")

st.markdown("---")

# 5. Confirm inputs
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