# pages/4_Events.py
import streamlit as st
import random
import json
import time
import config
import utils
import os

st.set_page_config(layout="centered", page_title="Event Phase")

# --- 0. 로그인 및 기본 설정 ---
if not st.session_state.get("authenticated_team"):
    st.error("Please log in first.")
    st.switch_page("pages/0_Login.py") # 사용자의 시작 페이지에 맞게 수정

team = st.session_state.get("authenticated_team")

# --- [핵심 수정] '단계(Phase)' 기반 상태 초기화 ---
# 이 페이지의 진행 상태를 단 하나의 변수로 관리합니다.
if "event_phase" not in st.session_state:
    st.session_state.event_phase = "roulette" # 초기 단계는 'roulette'

# 디버깅용 리셋 버튼 (필요 시 사이드바에서 사용)
if st.sidebar.button("⚠️ Reset Event Page State"):
    # 이 페이지에서 사용하는 모든 상태 변수를 삭제하여 처음부터 다시 시작
    keys_to_reset = [
        "event_phase", "is_rolling", "event_result", "event_title", "event_description",
        "intel_step1_result_value", "intel_result_step2", "intel_result_step3", "intel_result_step4",
        "intel_shown_step2", "intel_shown_step3", "intel_shown_step4",
        "international_event_generated_4events", "international_events_display"
    ]
    for key in keys_to_reset:
        if key in st.session_state:
            del st.session_state[key]
    st.toast("Event page state has been reset!")
    st.rerun()

st.title("🌏 Event Phase")
st.markdown("""
While you were busy shaping your nation's grand AI strategy in the political arena, life back home did not wait. **Unexpected domestic events**—both large and small—have unfolded independently of your decisions. These events can dramatically affect your nation's capacity to produce groundbreaking AI papers and models.  
Now, it's time to discover what has happened within your borders...

> **"We just rolled up a snowball and tossed it into hell. Now let's see what chance it has."** > <i>– Ethan Hunt, Mission: Impossible II (2000)</i>
""", unsafe_allow_html=True)
st.markdown("---")


# --- 1. 국내 이벤트 룰렛 단계 ---
if st.session_state.event_phase == "roulette":
    st.header("🎲 Domestic Event Roulette")
    
    # 이벤트 결과가 정해지면 결과를 보여주고 다음 단계로 가는 버튼을 표시
    if "event_result" in st.session_state:
        st.markdown(f"### 📍 Domestic Event: **{st.session_state.get('event_title', 'N/A')}**")
        st.markdown(f"📖 {st.session_state.get('event_description', 'N/A')}")
        st.markdown("---")
        if st.button("Proceed to Intelligence Briefing", type="primary"):
            st.session_state.event_phase = "intelligence"
            st.rerun()
    # 이벤트 결과가 없으면 룰렛 버튼을 표시
    else:
        is_rolling = st.session_state.get("is_rolling", False)
        col1, col2 = st.columns(2)
        with col1:
            if st.button("▶️ Start Roulette", disabled=is_rolling):
                st.session_state.is_rolling = True
                st.rerun()
        with col2:
            if st.button("⏹ Stop", disabled=not is_rolling):
                st.session_state.is_rolling = False
                
                # 1. 'event' 변수 정의
                eid = random.randint(1, len(config.domestic_events))
                event = config.domestic_events.get(eid, {"title": "Unknown", "description": "N/A"})
                
                # 2. domestic_{team}.json 파일에 이벤트 결과 추가 (올바른 위치)
                domestic_event_file_path = config.shared_dir / f"domestic_{team}.json"
                existing_events = []
                if os.path.exists(domestic_event_file_path):
                    try:
                        with open(domestic_event_file_path, "r") as f:
                            content = json.load(f)
                            if isinstance(content, list):
                                existing_events = content
                            else: 
                                existing_events = [content]
                    except (json.JSONDecodeError, FileNotFoundError):
                        pass
                
                existing_events.append(event)

                with open(domestic_event_file_path, "w") as f:
                    json.dump(existing_events, f)

                # 4. 세션 상태에 결과 저장 및 페이지 새로고침
                st.session_state["event_result"] = eid
                st.session_state["event_title"] = event["title"]
                st.session_state["event_description"] = event["description"]
                st.rerun()

        if is_rolling:
            st.markdown(f"### 🔄 Rolling... **{random.randint(1, 100)}**")
            time.sleep(0.1)
            st.rerun()

# --- 2. 정보전 브리핑 단계 ---
elif st.session_state.event_phase == "intelligence":
    st.header("🕵️ Intelligence Briefing")
    st.markdown("""
    Operatives from the **...** have returned with highly classified intel...
    > *"We need reliable intelligence, and we need it now..."*
    """, unsafe_allow_html=True) # 설명 부분 생략

    intel_score = st.session_state.get(f"hidden_params_Intelligence", 5)
    pool = [c for c in config.team_credentials if c != team]
    
    # --- 각 정보 단계 UI ---
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

    # 모든 정보 확인이 끝났는지 체크
    all_intel_revealed = (intel_score < 2 or st.session_state.get("intel_shown_step2", False)) and \
                         (intel_score < 6 or st.session_state.get("intel_shown_step3", False)) and \
                         (intel_score < 9 or st.session_state.get("intel_shown_step4", False))

    st.markdown("---")
    if not all_intel_revealed:
        st.info("💡 Please reveal all available intel steps above to continue.")
    else:
        if st.button("Proceed to Final Policy Adjustment", type="primary"):
            st.session_state.event_phase = "adjustment"
            st.rerun()

# --- 3. 최종 정책 조정 단계 ---
elif st.session_state.event_phase == "adjustment":
    st.header("🛠️ Final Policy Adjustment")

    # 사용 가능한 포인트 계산
    used_points = sum(v for k, v in st.session_state.items() if k.startswith("hidden_params_") and k != "hidden_params_Alignment_China" and isinstance(v, (int, float)))
    remaining = 100 - used_points

    if remaining <= 0:
        st.info("✅ You have no remaining policy points for adjustment.")
        if st.button("Proceed to International Events"):
            st.session_state.event_phase = "international"
            st.rerun()
    else:
        st.markdown(f"**💻 Remaining Points: `{remaining}` | Max Usable: `{min(5, remaining)}` | Only one parameter adjustable**")
        all_params = [p for group in config.parameter_groups.values() for p in group if p not in ["Alignment_China"]]
        
        selected_param = st.selectbox("Choose ONE parameter to adjust", all_params, key="adjust_select")
        
        # st.session_state에서 현재 값을 가져올 때 접두사를 포함해야 합니다.
        current_val = st.session_state.get(f"hidden_params_{selected_param}", 0)

        delta_cap = min(5, remaining)
        max_val = min(10, current_val + delta_cap)
        min_val = max(0, current_val - delta_cap)

        # 조정 UI 표시
        if selected_param == "Alignment_US":
            new_val = st.slider("New Alignment_US value", 0, 10, current_val)
            new_cn = 10 - new_val
            st.markdown(f"➡️ Alignment_China will automatically adjust to: `{new_cn}`")
        else:
            new_val = st.slider(f"New value for {selected_param}", min_val, max_val, current_val)

        # --- [채워진 부분] 저장 로직 ---
        if st.button("✅ Confirm Final Adjustment"):
            # 1. 세션 상태에 새로운 값 업데이트
            st.session_state[f"hidden_params_{selected_param}"] = new_val
            if selected_param == "Alignment_US":
                st.session_state["hidden_params_Alignment_China"] = 10 - new_val
            
            # 2. 파일에 저장하기 위해 모든 hidden_params 값을 딕셔너리로 준비
            updated_hidden_params = {
                k.replace("hidden_params_", ""): v 
                for k, v in st.session_state.items() 
                if k.startswith("hidden_params_")
            }

            full_params_to_save = {**updated_hidden_params, **config.fixed_values[team]}
            
            # JSON 파일에 변경된 내용을 덮어씁니다.
            with open(config.shared_dir / f"hidden_{team}.json", "w") as f:
                json.dump(full_params_to_save, f)

            # 3. 다음 단계로 상태 전환
            st.session_state.event_phase = "international"
            
            # 4. 사용자에게 피드백 후 페이지 새로고침
            st.success("✅ Adjustment saved. Proceeding to International Events.")
            time.sleep(1)
            st.rerun()

# --- 4. 국제 이벤트 및 요약 단계로 이동 ---
elif st.session_state.event_phase == "international":
    st.markdown("---")
    st.header("📍 International Events")
    st.markdown("While domestic reforms were unfolding, a new wave of **international events** emerged...")

    # 국제 이벤트 생성 및 파일 저장 로직
    if "international_events" not in st.session_state:
        event_file = config.shared_dir / "international.json"
        chosen_events = []

        # 1. 파일이 이미 존재하는지 확인하고, 내용을 읽어옵니다.
        if event_file.exists():
            try:
                with open(event_file, "r") as f:
                    chosen_events = json.load(f)
            except json.JSONDecodeError:
                chosen_events = []

        # 2. 이벤트 개수를 확인하고, 2개 미만이면 새로 추가합니다.
        if len(chosen_events) < 2:
            # 다른 팀이 i1만 생성한 경우, i2를 여기서 생성합니다.
            st.write("Your team triggered the second international event!")
            
            # 이미 존재하는 이벤트와 겹치지 않게 새 이벤트 1개를 샘플링합니다.
            existing_titles = {e['title'] for e in chosen_events}
            possible_new_events = [e for e in config.international_events if e['title'] not in existing_titles]
            
            if possible_new_events:
                new_event = random.sample(possible_new_events, 1)
                chosen_events.extend(new_event)
            
                # 업데이트된 이벤트 목록을 파일에 다시 씁니다.
                with open(event_file, "w") as f:
                    json.dump(chosen_events, f)
        else:
            st.write("Two international events have already been determined by other teams.")

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