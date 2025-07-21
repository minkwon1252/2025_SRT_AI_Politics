# pages/4_Events.py
import streamlit as st
import random
import json
import time
import math
import numpy as np
import config
import utils

st.set_page_config(layout="centered", page_title="Event Phase")

# --- 로그인 확인 ---
if not st.session_state.get("authenticated_team"):
    st.error("Please log in first.")
    st.switch_page("pages/1_Login.py")

team = st.session_state.get("authenticated_team")

# --- 페이지 상태 초기화 ---
# 이 페이지에서 사용할 세션 상태 변수들을 초기화합니다.
if "rolling" not in st.session_state:
    st.session_state.rolling = False
if "event_result" not in st.session_state:
    st.session_state.event_result = None
if "event_shown" not in st.session_state:
    st.session_state.event_shown = False
if "intel_shown" not in st.session_state:
    st.session_state.intel_shown = False
if "adjustment_confirmed" not in st.session_state:
    st.session_state.adjustment_confirmed = False

st.title("🌏 Event Phase")
st.markdown("""
While you were busy shaping your nation's grand AI strategy in the political arena, life back home did not wait. **Unexpected domestic events**—both large and small—have unfolded independently of your decisions. These events can dramatically affect your nation's capacity to produce groundbreaking AI papers and models.  
Now, it's time to discover what has happened within your borders...

> **"We just rolled up a snowball and tossed it into hell. Now let's see what chance it has."**  
> <i>– Ethan Hunt, Mission: Impossible II (2000)</i>
""", unsafe_allow_html=True)
st.markdown("---")


# --- 1. Domestic Event Roulette ---
st.header("🎲 Domestic Event Roulette")

# Domestic 이벤트가 아직 결정되지 않았을 때만 룰렛을 표시합니다.
if not st.session_state.event_shown:
    col1, col2 = st.columns(2)
    with col1:
        if st.button("▶️ Start Roulette"):
            st.session_state.rolling = True
            st.session_state.event_result = None

    with col2:
        if st.button("⏹ Stop"):
            st.session_state.rolling = False
            # config에서 domestic_events를 가져와 사용합니다.
            st.session_state.event_result = random.randint(1, len(config.domestic_events))
            st.session_state.stop_time = time.time()

    if st.session_state.rolling:
        placeholder = st.empty()
        # 룰렛 애니메이션은 사용자가 멈출 때까지 계속됩니다.
        # time.sleep을 사용하면 다른 상호작용이 멈추므로, 간단한 숫자로 대체합니다.
        n = random.randint(1, 100)
        placeholder.markdown(f"### 🔄 Your nation's fate awaits. Press 'Stop' when you're ready. **{n}**")
        st.rerun() # 부드러운 애니메이션 효과를 위해 rerun 사용

# 이벤트 결과가 있으면 표시합니다.
if st.session_state.event_result:
    # 이벤트 정보를 한 번만 처리하여 session_state에 저장합니다.
    if not st.session_state.event_shown:
        eid = st.session_state.event_result
        event = config.domestic_events.get(eid, {"title": "Unknown", "description": "N/A"})
        st.session_state["event_title"] = event["title"]
        st.session_state["event_description"] = event["description"]

        # 파일 저장 로직은 여기에 둡니다.
        with open(config.shared_dir / f"domestic_{team}.json", "w") as f:
            json.dump(event, f)
        
        st.session_state.event_shown = True
        st.rerun() # 상태 저장 후 UI를 새로고침

    # 저장된 이벤트 정보를 항상 표시합니다.
    st.markdown(f"### 📍 Domestic Event: **{st.session_state['event_title']}**")
    st.markdown(f"📖 {st.session_state['event_description']}")



# --- 2. Intelligence Insight Phase ---
if st.session_state.event_shown: # 국내 이벤트가 확정된 후에만 정보전 단계 표시
    st.markdown("---")
    st.header("🕵️ Intelligence Briefing")
    
    
    agency_name = config.intel_agencies.get(team, "your national intelligence agency")
    st.markdown(f"""
Operatives from the **{agency_name}** have returned with highly classified intel on the AI priorities and strategic moves of rival nations.  
This information was obtained through covert channels—impossible to access via diplomacy or trade.

What lies before you is a rare glimpse behind the curtain.  
Interpret it wisely, and your nation could outmaneuver its competitors in both global cooperation and technological supremacy.

> *"We need reliable intelligence, and we need it now..."*  
> — **Alan Hunley**, *Mission: Impossible – Rogue Nation*
""", unsafe_allow_html=True)

    intel_score = st.session_state.get(f"hidden_params_Intelligence", 5)
    pool = [c for c in config.team_credentials if c != team]
    
    # ✅ 1️⃣ 최초 1회 고정
    if "intel_step1_result_value" not in st.session_state:
        rand_country = random.choice(pool)
        val_str = ""
        try:
            if random.random() < 0.5:
                # config.shared_dir 사용
                with open(config.shared_dir / f"hidden_{rand_country}.json") as f:
                    h1 = json.load(f)
                p1 = random.choice(list(h1.keys()))
                # utils.get_hidden_param_info 사용
                val_str = utils.get_hidden_param_info(p1, h1.get(p1, 0), intel_score)
            else:
                # config.shared_dir 사용
                with open(config.shared_dir / f"cooperation_{rand_country}.json") as f:
                    c1 = json.load(f)
                # config.coop_params 사용
                coop_keys = list(config.coop_params.keys())
                p1 = random.choice(coop_keys)
                val = c1.get(team, {}).get(p1, "None")
                # utils.get_coop_info와 config.coop_params 사용
                val_str = utils.get_coop_info(p1, val, intel_score, config.coop_params[p1].get("options"))
            
            st.session_state["intel_step1_result_value"] = f"{rand_country}'s {val_str}"

        except FileNotFoundError:
            st.session_state["intel_step1_result_value"] = f"Could not retrieve intel on {rand_country}. Their files are not ready."
        except Exception as e:
            st.session_state["intel_step1_result_value"] = f"An error occurred while getting intel: {e}"

    st.markdown("**Intel 1️⃣ (Random Country, Random parameter)**")
    st.success(st.session_state.get("intel_step1_result_value", "Intel processing..."))

    # ✅ 상태 초기화
    for k in ["intel_shown_step2", "intel_shown_step3", "intel_shown_step4"]:
        if k not in st.session_state:
            st.session_state[k] = False
            
    # 2️⃣ 선택 국가 무작위
    if intel_score >= 2:
        sel2 = st.selectbox("2️⃣ Choose a country for random intel", pool, key="country_step2", disabled=st.session_state.get("intel_shown_step2", False))
        if not st.session_state.get("intel_shown_step2", False):
            if st.button("🔍 Reveal Step 2 Intel", key="reveal2"):
                try:
                    if random.random() < 0.5:
                        with open(config.shared_dir / f"hidden_{sel2}.json") as f:
                            h2 = json.load(f)
                        p2 = random.choice(list(h2.keys()))
                        result = utils.get_hidden_param_info(p2, h2.get(p2, 0), intel_score)
                    else:
                        with open(config.shared_dir / f"cooperation_{sel2}.json") as f:
                            c2 = json.load(f)
                        p2 = random.choice(list(config.coop_params.keys()))
                        val = c2.get(team, {}).get(p2, "None")
                        result = utils.get_coop_info(p2, val, intel_score, config.coop_params[p2].get("options"))
                    st.session_state["intel_result_step2"] = f"{sel2}'s {result}"
                except FileNotFoundError:
                    st.session_state["intel_result_step2"] = f"File not found for {sel2}. They may not have saved their choices yet."
                
                st.session_state["intel_shown_step2"] = True
                st.rerun()

        if st.session_state.get("intel_shown_step2"):
            st.success(st.session_state.get("intel_result_step2"))

    # 3️⃣ 선택 국가 cooperative
    if intel_score >= 6:
        sel3 = st.selectbox("3️⃣ Choose a country for cooperative intel", pool, key="country_step3", disabled=st.session_state.get("intel_shown_step3", False))
        coop_key = st.selectbox("Select cooperative parameter", list(config.coop_params.keys()), key="coop_step3", disabled=st.session_state.get("intel_shown_step3", False))
        if not st.session_state.get("intel_shown_step3", False):
            if st.button("🔍 Reveal Step 3 Intel", key="reveal3"):
                try:
                    with open(config.shared_dir / f"cooperation_{sel3}.json") as f:
                        coop_data = json.load(f)
                    val = coop_data.get(team, {}).get(coop_key, "None")
                    meta = config.coop_params[coop_key]
                    result = utils.get_coop_info(coop_key, val, intel_score, meta.get("options"))
                    st.session_state["intel_result_step3"] = f"{sel3}'s {result}"
                except FileNotFoundError:
                     st.session_state["intel_result_step3"] = f"File not found for {sel3}."

                st.session_state["intel_shown_step3"] = True
                st.rerun()

        if st.session_state.get("intel_shown_step3"):
            st.success(st.session_state.get("intel_result_step3"))

    # 4️⃣ 선택 국가 specific hidden
    if intel_score >= 9:
        sel4 = st.selectbox("4️⃣ Choose a country for specific hidden intel", pool, key="country_step4", disabled=st.session_state.get("intel_shown_step4", False))
        # 파일을 버튼 누르기 전에 미리 열면, 상대가 저장 안했을 때 에러 발생. 버튼 안으로 이동.
        
        # 임시로 h4 키 목록을 보여주기 위한 처리
        # 실제로는 이 방식보다 더 나은 UI가 필요할 수 있음
        param_list = list(config.parameter_groups.keys()) # 예시 목록
        
        hidden_key = st.selectbox("Select hidden parameter", list(config.parameter_descriptions.keys()), key="hidden_step4", disabled=st.session_state.get("intel_shown_step4", False))
        if not st.session_state.get("intel_shown_step4", False):
            if st.button("🔍 Reveal Step 4 Intel", key="reveal4"):
                try:
                    with open(config.shared_dir / f"hidden_{sel4}.json") as f:
                        h4 = json.load(f)
                    result = utils.get_hidden_param_info(hidden_key, h4.get(hidden_key, 0), intel_score)
                    st.session_state["intel_result_step4"] = f"{sel4}'s {result}"
                except FileNotFoundError:
                    st.session_state["intel_result_step4"] = f"File not found for {sel4}."

                st.session_state["intel_shown_step4"] = True
                st.rerun()

        if st.session_state.get("intel_shown_step4"):
            st.success(st.session_state.get("intel_result_step4"))

    # 모든 정보 확인이 끝나면 다음 단계로 넘어갈 수 있도록 플래그 설정
    # (이 로직은 페이지의 다음 부분에서 intel_shown을 확인하여 처리)
    all_steps_done = (intel_score < 2 or st.session_state.get("intel_shown_step2", False)) and \
                     (intel_score < 6 or st.session_state.get("intel_shown_step3", False)) and \
                     (intel_score < 9 or st.session_state.get("intel_shown_step4", False))

    if all_steps_done and not st.session_state.get("intel_shown", False):
        st.session_state["intel_shown"] = True
        st.rerun()

# --- 3. Final Policy Adjustment ---
if st.session_state.intel_shown and not st.session_state.adjustment_confirmed:
    st.markdown("---")
    st.header("🛠️ Final Policy Adjustment")

    used_points = sum([v for k, v in st.session_state.items() if k.startswith("hidden_params_") and isinstance(v, (int, float))])
    remaining = 100 - used_points

    if remaining <= 0:
        st.info("✅ You used all your policy points. No adjustments possible.")
        st.session_state.adjustment_confirmed = True # 조정 불가 시 바로 확정 처리
        st.rerun()
    else:
        st.markdown(f"**💻 Remaining Points: `{remaining}` | Max Usable: `{min(5, remaining)}` | Only one parameter adjustable**")
        all_params = [p for group in config.parameter_groups.values() for p in group if p not in ["Alignment_China"]]
        
        selected_param = st.selectbox("Choose ONE parameter to adjust", all_params, key="adjust_select")
        current_val = st.session_state.get(f"hidden_params_{selected_param}", 0)

        # Determine range based on rules
        delta_cap = min(5, remaining)
        max_val = min(10, current_val + delta_cap)
        min_val = max(0, current_val - delta_cap)

    # Special case for Alignment_US/China
    if selected_param == "Alignment_US":
        current_cn = st.session_state.get("hidden_params_Alignment_China", 0)
        new_val = st.slider("New Alignment_US value", 0, 10, current_val)
        new_cn = 10 - new_val
        st.markdown(f"➡️ Alignment_China will automatically adjust to: `{new_cn}`")
    else:
        new_val = st.slider(f"New value for {selected_param}", min_val, max_val, current_val)

        if st.button("✅ Confirm Final Adjustment"):
            # ( ... 기존 코드의 파라미터 저장 로직 ... )
            st.session_state.adjustment_confirmed = True
            st.success("✅ Adjustment saved. This concludes your policy modification for this round.")
            time.sleep(1)
            st.rerun()

# --- 4. Transition to Summary ---
# --- 4. Transition to Summary ---
if st.session_state.adjustment_confirmed:
    st.markdown("---")
    st.header("📍 International Events")
    st.markdown("While domestic reforms were unfolding, a new wave of **international events** emerged...")

    # --- 여기가 수정된 로직 ---
    # 국제 이벤트가 세션에 아직 로드되지 않았다면, 파일에서 로드하거나 새로 생성합니다.
    if "international_events" not in st.session_state:
        event_file = config.shared_dir / "international.json"

        # 1. 파일이 이미 존재하는지 확인
        if event_file.exists():
            # 파일이 있다면, 두 번째 이후의 팀이므로 파일을 읽습니다.
            with open(event_file, "r") as f:
                chosen_events = json.load(f)
                st.write("Previously determined international events have been loaded.")

        # 2. 파일이 존재하지 않는 경우
        else:
            # 파일이 없다면, 첫 번째 팀이므로 이벤트를 새로 생성하고 저장합니다.
            chosen_events = random.sample(config.international_events, 2)
            with open(event_file, "w") as f:
                json.dump(chosen_events, f)
            st.write("Your team was the first to trigger the international events for this round!")

        # 결정된 이벤트를 현재 세션에 저장합니다.
        st.session_state["international_events"] = chosen_events
    # --- 로직 수정 끝 ---


    # 이제 모든 플레이어는 동일한 st.session_state.international_events를 갖게 됩니다.
    with st.expander("🗺️ View International Events", expanded=True):
        if "international_events" in st.session_state:
            for i, event in enumerate(st.session_state.international_events, 1):
                st.markdown(f"#### 💥 Event {i}: {event['title']}\n\n{event['description']}")
        else:
            st.warning("International events are being determined...")


    if st.button("➡️ Proceed to Summary Phase"):
        st.switch_page("pages/5_Summary.py")