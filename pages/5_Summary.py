# pages/5_Summary.py
import streamlit as st
import json
import random
import pandas as pd
import plotly.graph_objects as go
import config
import utils
import os
import time


st.set_page_config(layout="centered", page_title="Round Summary")

# --- 0. 로그인 및 기본 설정 ---
if not st.session_state.get("authenticated_team"):
    st.error("Please log in first.")
    if st.button("Go to Login"):
        st.switch_page("pages/0_Login.py") # 사용자의 시작 페이지에 맞게 수정
    st.stop()

my_team = st.session_state.get("authenticated_team")
all_player_teams = list(config.team_credentials.keys())

st.title("📊 Round Summary & Leaderboard")
st.markdown("""
You’ve reached the moment of truth..
            
Now it’s time to see how your nation’s choices — across AI investments, cooperative actions, and strategic diplomacy — shaped your **model breakthroughs** and **paper production**.  
Did international collaboration accelerate your growth, or did mistrust and misalignment slow you down?

This is your chance to compare national outcomes and strategize how your country can grow faster, stronger, and smarter. Look carefully at the upcoming stats — and ask yourself:  
**How will you catch up with the AI superpowers, the two giants — the US and China?**

Identify which policies gave you a competitive edge — and which ones may need to be reinforced before the next round begins.

Let’s see how far you've come… and where you must go next.

> <b>"Mission accomplished!"</b> (but the timer keeps ticking...)<br>
> <i>— Ethan Hunt, <i>Mission: Impossible – Ghost Protocol</i> (2011)</i>
""", unsafe_allow_html=True)
st.markdown("---")


# --- 1. 데이터 로딩 및 결과 계산 ---
# 모든 팀의 hidden, cooperation 파라미터를 한 번에 로드
all_params = {}
for team_name in all_player_teams:
    hidden, coop = {}, {}
    try:
        with open(config.shared_dir / f"hidden_{team_name}.json", "r") as f:
            hidden = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        pass
    try:
        with open(config.shared_dir / f"cooperation_{team_name}.json", "r") as f:
            coop = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        pass
    all_params[team_name] = {'hidden': hidden, 'coop': coop}

# 라운드 결과 계산
history = utils.load_history()
current_round_num = len(history) + 1
st.header(f"🏁 End of Round {current_round_num}")

initial_scores = history[-1]['scores'] if history else config.initial_data

all_results = {}
for team_name in all_player_teams:
    growth = st.session_state.get('growth_rate', 0) if team_name == my_team else 0
    (final_p, final_m), details = utils.calculate_round_results(
        team_name,
        initial_scores.get(team_name, {}).get('papers', 0),
        initial_scores.get(team_name, {}).get('models', 0),
        growth,
        all_params.get(team_name, {}).get('hidden', {}),
        all_params.get(team_name, {}).get('coop', {})
    )
    all_results[team_name] = {
        'papers': int(final_p), 'models': int(final_m),
        'paper_delta': int(details.get('total_paper_delta', 0)),
        'model_delta': float(details.get('total_model_delta', 0)),
        'delta_details': details
    }

# 미국, 중국 데이터 랜덤 업데이트
us_papers_initial, us_models_initial = initial_scores.get('United States', {}).get('papers', 0), initial_scores.get('United States', {}).get('models', 0)
us_delta = random.randint(150, 250)
us_papers_final = us_papers_initial + us_delta
us_models_final = utils.calculate_ai_models(us_papers_final)
all_results['United States'] = {'papers': us_papers_final, 'models': int(us_models_final), 'paper_delta': us_delta, 'model_delta': us_models_final - us_models_initial}

cn_papers_initial, cn_models_initial = initial_scores.get('China', {}).get('papers', 0), initial_scores.get('China', {}).get('models', 0)
cn_delta = random.randint(200, 300)
cn_papers_final = cn_papers_initial + cn_delta
cn_models_final = utils.calculate_ai_models(cn_papers_final)
all_results['China'] = {'papers': cn_papers_final, 'models': int(cn_models_final), 'paper_delta': cn_delta, 'model_delta': cn_models_final - cn_models_initial}

# --- 2. UI 렌더링 ---
# 로그인한 팀의 요약

# --- Balloon effect for the winner ---
if all_results:
    # Find the team with the highest number of models
    winner_team = max(all_results, key=lambda team: all_results[team].get('models', 0))
    
    # If the logged-in user is the winner, show the balloons
    if winner_team == my_team:
        st.balloons()

st.header(f"{config.country_flags[my_team]} Your Nation's Progress")
my_results = all_results.get(my_team, {})
col1, col2 = st.columns(2)
col1.metric("⚛ Total Papers", f"{my_results.get('papers', 'N/A'):,}")
col2.metric("🪄 Total Models", f"{my_results.get('models', 'N/A'):,}")

with st.expander("🔍 View Detailed Breakdown of Your Growth"):
    details = my_results.get('delta_details', {})
    if details:
        col1, col2 = st.columns(2)
        
        # --- 논문 성장 상세 내역 ---
        with col1:
            st.markdown("##### 📄 Paper Growth Details")
            st.markdown(f"- **Base Growth**: `{details.get('base_growth', 0)}`")
            
            # 국내 이벤트
            for i, event_delta in enumerate(details.get('domestic_deltas', []), 1):
                st.markdown(f"- Domestic Event {i}: `{event_delta.get('paper_delta', 0)}`")
            
            # 국제 이벤트
            for i, event_delta in enumerate(details.get('international_deltas', []), 1):
                st.markdown(f"- Intl. Event {i}: `{event_delta.get('paper_delta', 0)}`")

            st.markdown(f"**Total: `{int(details.get('total_paper_delta', 0))}`**")

        # --- 모델 성장 상세 내역 ---
        with col2:
            st.markdown("##### 🪄 Model Growth Details")
            st.markdown(f"- **From New Papers**: `+{details.get('from_papers_model', 0):.2f}`")

            # 국내 이벤트
            for i, event_delta in enumerate(details.get('domestic_deltas', []), 1):
                st.markdown(f"- Domestic Event {i}: `{event_delta.get('model_delta', 0)}`")
            
            # 국제 이벤트
            for i, event_delta in enumerate(details.get('international_deltas', []), 1):
                st.markdown(f"- Intl. Event {i}: `{event_delta.get('model_delta', 0):.2f}`")

            st.markdown(f"**Total: `{details.get('total_model_delta', 0):.2f}`**")

# Global AI Superpowers
st.header("🌍 Global AI Superpowers")
col1, col2 = st.columns(2)
with col1:
    st.markdown(f"### {config.country_flags['United States']} United States")
    us_data = all_results.get('United States', {})
    st.metric("Total Papers", f"{us_data.get('papers', 'N/A'):,}")
    st.metric("Estimated Models", f"{us_data.get('models', 'N/A'):,}")
with col2:
    st.markdown(f"### {config.country_flags['China']} China")
    cn_data = all_results.get('China', {})
    st.metric("Total Papers", f"{cn_data.get('papers', 'N/A'):,}")
    st.metric("Estimated Models", f"{cn_data.get('models', 'N/A'):,}")
st.markdown("---")

# 리더보드
st.header("🏆 Leaderboard")
leaderboard_data = []
for name, data in all_results.items():
    leaderboard_data.append({
        "Country": f"{config.country_flags.get(name, '🇺🇳')} {name}",
        "Papers": data['papers'],
        "Models": data['models'],
        "Paper Growth": f"+{data['paper_delta']}" if data['paper_delta'] >= 0 else str(data['paper_delta']),
        "Model Growth": f"+{data['model_delta']:.2f}" if data['model_delta'] >= 0 else f"{data['model_delta']:.2f}",
    })
df_leaderboard = pd.DataFrame(leaderboard_data).sort_values(by=["Models", "Papers"], ascending=False).reset_index(drop=True)
df_leaderboard.index = df_leaderboard.index + 1
df_leaderboard.index.name = "Rank"
st.dataframe(df_leaderboard, use_container_width=True)

# 누적 성장 그래프
st.header("📈 Cumulative Growth Trend (Models)")

# 탭을 사용하여 모델 수와 논문 수 그래프 분리
tab1, tab2 = st.tabs(["🪄 Models Growth", "📄 Papers Growth"])

# --- Round 0 (초기값) 데이터 생성 ---
round_0_data_models = {'round': 0}
round_0_data_papers = {'round': 0}

initial_player_sum_models = 0
initial_player_sum_papers = 0

for name, data in config.initial_data.items():
    round_0_data_models[name] = data['models']
    round_0_data_papers[name] = data['papers']
    
    # 4 Players Sum을 위해 config.team_credentials에 있는 국가들만 합산
    if name in config.team_credentials: # config.team_credentials에 있는 플레이어 국가들만 합산
        initial_player_sum_models += data['models']
        initial_player_sum_papers += data['papers']

# '4 Players Sum' 데이터를 Round 0에 추가
round_0_data_models['4 Players Sum'] = initial_player_sum_models
round_0_data_papers['4 Players Sum'] = initial_player_sum_papers

# 'United States'와 'China' 데이터도 Round 0에 포함
# config.initial_data에서 직접 가져오므로 별도 처리 불필요 (이미 위 루프에서 포함됨)
# 다만, ensure that these are always included even if not explicitly in config.team_credentials
# 이전에 미국/중국을 따로 합산하던 로직이 있다면 이 부분은 initial_data를 기준으로 한번에 처리합니다.
# 안전을 위해 한 번 더 명시적으로 확인:
if 'United States' not in round_0_data_models:
    round_0_data_models['United States'] = config.initial_data.get('United States', {}).get('models', 0)
    round_0_data_papers['United States'] = config.initial_data.get('United States', {}).get('papers', 0)
if 'China' not in round_0_data_models:
    round_0_data_models['China'] = config.initial_data.get('China', {}).get('models', 0)
    round_0_data_papers['China'] = config.initial_data.get('China', {}).get('papers', 0)


# 차트 데이터 리스트에 라운드 0을 먼저 추가
chart_data_models = [round_0_data_models]
chart_data_papers = [round_0_data_papers]

# 현재까지의 기록을 차트 데이터에 추가 (기존 로직 유지)
new_round_to_save = {
    "round": current_round_num,
    "scores": all_results
}
current_history = history + [new_round_to_save] # 이 부분은 save_history 호출 전에만 사용

for round_data in current_history: # 이 루프는 이미 저장된 history와 현재 라운드 결과 all_results를 합친 것
    # Round 0은 이미 위에서 추가되었으므로, round_num이 0인 경우는 건너뜁니다.
    if round_data['round'] == 0:
        continue 
        
    round_num = round_data['round']
    scores = round_data['scores']
    
    row_models = {'round': round_num}
    row_papers = {'round': round_num}
    
    player_sum_models, player_sum_papers = 0, 0
    # 모든 국가에 대해 데이터 추가
    all_countries_for_chart = list(config.team_credentials.keys()) + ["United States", "China"] # 그래프에 포함할 모든 국가
    for name in all_countries_for_chart:
        # scores 딕셔너리에 해당 국가의 데이터가 있는지 확인하고 가져옵니다.
        row_models[name] = scores.get(name, {}).get('models', 0)
        row_papers[name] = scores.get(name, {}).get('papers', 0)
        
        # '4 Players Sum'에는 config.team_credentials에 있는 플레이어 국가들만 합산
        if name in config.team_credentials:
            player_sum_models += row_models[name]
            player_sum_papers += row_papers[name]
        
    row_models['4 Players Sum'] = player_sum_models
    row_papers['4 Players Sum'] = player_sum_papers
    
    chart_data_models.append(row_models)
    chart_data_papers.append(row_papers)

# --- Models Growth 탭 ---
with tab1:
    if chart_data_models:
        df_models = pd.DataFrame(chart_data_models).set_index('round')
        
        # 범례 순서 지정: United States, China, 4 Players Sum이 먼저 오도록
        # config.team_credentials에 있는 플레이어 국가들을 동적으로 추가합니다.
        player_countries_sorted = sorted(config.team_credentials.keys()) # 알파벳 순 정렬 등 필요시 변경
        legend_order = ["United States", "China", "4 Players Sum"] + player_countries_sorted
        
        # 실제 df_models에 존재하는 컬럼만 선택하여 순서를 맞춥니다.
        legend_order = [col for col in legend_order if col in df_models.columns]

        df_models = df_models[legend_order]
        
        # Plotly 그래프 생성
        fig_models = go.Figure()
        for country in df_models.columns:
            fig_models.add_trace(go.Scatter(x=df_models.index, y=df_models[country],
                                            mode='lines+markers', name=country))
        
        # X축 범위와 틱(tick) 설정
        fig_models.update_layout(
            xaxis=dict(
                title="Round",
                range=[0, current_round_num + 2],  # 현재 라운드 + 2 만큼 여유 공간
                tickmode='linear',
                tick0=0,
                dtick=1  # 1단위로 정수 틱만 표시
            ),
            yaxis_title="Number of Models",
            legend_title="Country"
        )
        st.plotly_chart(fig_models, use_container_width=True)

# --- Papers Growth 탭 ---
with tab2:
    if chart_data_papers:
        df_papers = pd.DataFrame(chart_data_papers).set_index('round')
        
        # 범례 순서 지정: Models Growth 탭과 동일하게 적용
        legend_order = ["United States", "China", "4 Players Sum"] + player_countries_sorted
        legend_order = [col for col in legend_order if col in df_papers.columns]
        
        df_papers = df_papers[legend_order]
        
        # Plotly 그래프 생성
        fig_papers = go.Figure()
        for country in df_papers.columns:
            fig_papers.add_trace(go.Scatter(x=df_papers.index, y=df_papers[country],
                                            mode='lines+markers', name=country))
                                            
        # X축 범위와 틱(tick) 설정
        fig_papers.update_layout(
            xaxis=dict(
                title="Round",
                range=[0, current_round_num + 2],
                tickmode='linear',
                tick0=0,
                dtick=1
            ),
            yaxis_title="Number of Papers",
            legend_title="Country"
        )
        st.plotly_chart(fig_papers, use_container_width=True)

# 발생한 이벤트 목록
st.markdown("---")
st.header("🔔 Events This Round")

# Domestic Events Display
with st.expander(f"🏠 Domestic Events in {my_team}"):
    try:
        domestic_event_file_path = config.shared_dir / f"domestic_{my_team}.json"
        if os.path.exists(domestic_event_file_path):
            with open(domestic_event_file_path, "r") as f:
                all_domestic_events = json.load(f)
                if not isinstance(all_domestic_events, list):
                    all_domestic_events = [all_domestic_events]
                
                if all_domestic_events:
                    for i, event in enumerate(all_domestic_events, 1):
                        st.markdown(f"**Event {i}: {event.get('title', 'N/A')}**")
                        
                        # --- 수정된 부분: 첫 문장만 추출 ---
                        description = event.get('description', 'N/A')
                        
                        # 문장 끝을 나타내는 ., ?, ! 중 가장 먼저 나오는 위치를 찾음
                        end_indices = [idx for idx in [description.find('.'), description.find('?'), description.find('!')] if idx != -1]
                        
                        if end_indices:
                            # 가장 첫 번째 문장 종결 부호까지 잘라냄
                            first_sentence = description[:min(end_indices) + 1]
                        else:
                            # 문장 부호가 없으면 전체를 첫 문장으로 간주
                            first_sentence = description
                        
                        st.write(first_sentence)
                        st.markdown("---")
                else:
                    st.info(f"No domestic events occurred for {my_team} this round.")
        else:
            st.info(f"No domestic events occurred for {my_team} this round.")
    except Exception as e:
        st.error(f"An error occurred while loading your domestic events: {e}")

# International Events Display
with st.expander("🌍 International Events"):
    try:
        international_event_file = config.shared_dir / "international.json"
        if os.path.exists(international_event_file):
            with open(international_event_file, "r") as f:
                all_international_events = json.load(f)
                if all_international_events:
                    for i, event in enumerate(all_international_events, 1):
                        st.markdown(f"**Event {i}: {event.get('title', 'N/A')}**")
                        
                        # Description의 첫 문장만 표기
                        description = event.get('description', 'N/A')
                        end_indices = [idx for idx in [description.find('.'), description.find('?'), description.find('!')] if idx != -1]
                        first_sentence = description[:min(end_indices) + 1] if end_indices else description
                        st.write(first_sentence)

                        # --- 수정된 부분: 효과 요약 및 수식 숨기기 ---
                        # 1. 효과 요약을 먼저 보여줍니다.
                        if event.get("effect_summary"):
                            st.info(f"💡 Parameters : {event.get('effect_summary')}")
                        
                        # 2. Popover 버튼 안에 복잡한 수식을 숨깁니다.
                        with st.popover("⚙️ Equations for this event"):
                            if event.get("delta_papers"):
                                st.code(f"Paper Δ: {event.get('delta_papers')}", language="python")
                            if event.get("delta_models"):
                                st.code(f"Model Δ: {event.get('delta_models')}", language="python")
                        
                        st.markdown("---")
                else:
                    st.info("No international events occurred this round.")
        else:
            st.info("No international events occurred this round.")
    except Exception as e:
        st.error(f"An error occurred while loading international events: {e}")

# 인용구 및 다음 라운드 버튼
st.markdown("---")
st.markdown("""
> *"China is not behind, they are right there with us... Remember, this is not a sprint, it's an infinite race. This is a country with a great will, and we will be competing for a long time."*
>
> <p style='text-align: right; font-style: italic;'>– Jensen Huang, NVIDIA CEO, at the 2025 Technology Conference, Washington D.C.</p>
""", unsafe_allow_html=True)
st.markdown("---")

if st.button("End Round and Save History"):
    utils.save_history(new_round_to_save)
    st.success(f"Round {current_round_num} has been successfully recorded.")

if st.button("🚀 Start Next Round", type="primary"):
    st.toast("Clearing data for the new round...")
    files_to_clear = [config.shared_dir / "international.json"]
    
    # domestic 파일과 cooperation 파일을 모두 삭제하도록 주석 해제
    for country_name in all_player_teams:
        files_to_clear.append(config.shared_dir / f"domestic_{country_name}.json")
        files_to_clear.append(config.shared_dir / f"cooperation_{country_name}.json")
    
    for f in files_to_clear:
        if f.exists():
            f.unlink()

    keys_to_clear_from_session = [
        "growth_rate", "cooperation_state", "cooperation_confirmed",
        # 1_Circumstances, 4_Events 페이지의 세션 상태 초기화
        "domestic_event_shown", "international_event_shown", 
        "event_phase", "is_rolling", "event_result", 
        "international_events_1_circumstance", "international_events"
    ]
    for key in keys_to_clear_from_session:
        if key in st.session_state:
            del st.session_state[key]
            
    st.success("Starting new round... Navigating to Circumstances Phase!")
    time.sleep(2)
    st.switch_page("pages/1_Circumstances.py")