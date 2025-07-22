# pages/5_Summary.py
import streamlit as st
import json
import random
import pandas as pd
import plotly.graph_objects as go
import config
import utils

st.set_page_config(layout="centered", page_title="Round Summary")

# --- 로그인 확인 ---
if not st.session_state.get("authenticated_team"):
    st.error("Please log in first.")
    if st.button("Go to Login"):
        st.switch_page("pages/1_Login.py")
    st.stop()

my_team = st.session_state.get("authenticated_team")

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


# --- 유일한 데이터 계산 로직 ---

# 1. 기록 및 초기 데이터 로드
history = utils.load_history()
current_round_num = len(history) + 1
st.header(f"🏁 End of Round {current_round_num}")

if history:
    initial_scores = history[-1]['scores']
else:
    initial_scores = {name: data for name, data in config.initial_data.items()}

# 2. 모든 국가의 현재 라운드 결과 계산
all_results = {}
for name in config.team_credentials.keys():
    growth = st.session_state.get('growth_rate', 0) if name == my_team else 0
    (final_p, final_m), details = utils.calculate_round_results(
        name,
        initial_scores.get(name, {}).get('papers', 0),
        initial_scores.get(name, {}).get('models', 0),
        growth
    )
    all_results[name] = {
        'papers': int(final_p),
        'models': int(final_m),
        'paper_delta': int(details.get('total_paper_delta', 0)),
        'model_delta': float(details.get('total_model_delta', 0)),
        'delta_details': details  # 상세 내역 저장
    }


# 3. 미국, 중국 데이터 업데이트
us_papers_initial, us_models_initial = initial_scores.get('United States', {}).get('papers', 0), initial_scores.get('United States', {}).get('models', 0)
us_delta = random.randint(150, 250)
us_papers_final = us_papers_initial + us_delta
us_models_final = utils.calculate_ai_models(us_papers_final)
all_results['United States'] = {
    'papers': us_papers_final, 'models': int(us_models_final),
    'paper_delta': us_delta, 'model_delta': us_models_final - us_models_initial
}

cn_papers_initial, cn_models_initial = initial_scores.get('China', {}).get('papers', 0), initial_scores.get('China', {}).get('models', 0)
cn_delta = random.randint(200, 300)
cn_papers_final = cn_papers_initial + cn_delta
cn_models_final = utils.calculate_ai_models(cn_papers_final)
all_results['China'] = {
    'papers': cn_papers_final, 'models': int(cn_models_final),
    'paper_delta': cn_delta, 'model_delta': cn_models_final - cn_models_initial
}


# --- UI 렌더링 ---
# 1. 로그인한 팀의 요약 표시
st.header(f"{config.country_flags[my_team]} Your Nation's Progress")
my_results = all_results.get(my_team, {})
col1, col2 = st.columns(2)
col1.metric("⚛ Total Papers", my_results.get('papers', 'N/A'))
col2.metric("🪄 Total Models", my_results.get('models', 'N/A'))

# "Detailed Breakdown" 부분을 수정하여 상세 내역 표시
with st.expander("🔍 View Detailed Breakdown of Your Growth"):
    details = my_results.get('delta_details', {})
    if details:
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("##### 📄 Paper Growth Details")
            st.markdown(f"- Base Growth: `{details.get('base_growth', 0)}`")
            st.markdown(f"- Domestic Event: `{details.get('domestic_paper', 0)}`")
            st.markdown(f"- International Event: `{details.get('international_paper', 0)}`")
            st.markdown(f"**Total: `{int(details.get('total_paper_delta', 0))}`**")
        
        with col2:
            st.markdown("##### 🪄 Model Growth Details")
            st.markdown(f"- From New Papers: `+{details.get('from_papers_model', 0):.2f}`")
            st.markdown(f"- Domestic Event: `{details.get('domestic_model', 0)}`")
            st.markdown(f"- International Event: `{details.get('international_model', 0)}`")
            st.markdown(f"**Total: `{details.get('total_model_delta', 0):.2f}`**")
    else:
        st.write("No growth details available for this round.")
st.markdown("---")

# 2. Global AI Superpowers 표시
st.header("🌍 Global AI Superpowers")
col1, col2 = st.columns(2)
with col1:
    st.markdown("### 🇺🇸 United States")
    us_data = all_results.get('United States', {})
    st.metric("Total Papers", us_data.get('papers', 'N/A'))
    st.metric("Estimated Models", us_data.get('models', 'N/A'))
with col2:
    st.markdown("### 🇨🇳 China")
    cn_data = all_results.get('China', {})
    st.metric("Total Papers", cn_data.get('papers', 'N/A'))
    st.metric("Estimated Models", cn_data.get('models', 'N/A'))
st.markdown("---")
# --- 추가된 부분 끝 ---


# 3. 기능 1: 랭킹 리더보드
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

df = pd.DataFrame(leaderboard_data)
df = df.sort_values(by=["Models", "Papers"], ascending=False).reset_index(drop=True)
df.index = df.index + 1
df.index.name = "Rank"
st.dataframe(df, use_container_width=True)


# 4. 기능 2: 누적 성장 그래프
st.header("📈 Cumulative Growth Trend (Models)")

# 탭을 사용하여 모델 수와 논문 수 그래프 분리
tab1, tab2 = st.tabs(["🪄 Models Growth", "📄 Papers Growth"])

# 라운드 0(초기값) 데이터 생성
round_0_data_models = {'round': 0}
round_0_data_papers = {'round': 0}

initial_player_sum_models = 0
initial_player_sum_papers = 0

for name, data in config.initial_data.items():
    round_0_data_models[name] = data['models']
    round_0_data_papers[name] = data['papers']
    if name in config.team_credentials:
        initial_player_sum_models += data['models']
        initial_player_sum_papers += data['papers']

round_0_data_models['4 Players Sum'] = initial_player_sum_models
round_0_data_papers['4 Players Sum'] = initial_player_sum_papers

# 차트 데이터 리스트에 라운드 0을 먼저 추가
chart_data_models = [round_0_data_models]
chart_data_papers = [round_0_data_papers]

# 현재까지의 기록을 차트 데이터에 추가
new_round_to_save = {
    "round": current_round_num,
    "scores": all_results
}
current_history = history + [new_round_to_save]

for round_data in current_history:
    round_num = round_data['round']
    scores = round_data['scores']
    
    row_models = {'round': round_num}
    row_papers = {'round': round_num}
    
    player_sum_models, player_sum_papers = 0, 0
    for name in config.team_credentials.keys():
        row_models[name] = scores.get(name, {}).get('models', 0)
        row_papers[name] = scores.get(name, {}).get('papers', 0)
        player_sum_models += row_models[name]
        player_sum_papers += row_papers[name]
        
    row_models['United States'] = scores.get('United States', {}).get('models', 0)
    row_papers['United States'] = scores.get('United States', {}).get('papers', 0)
    row_models['China'] = scores.get('China', {}).get('models', 0)
    row_papers['China'] = scores.get('China', {}).get('papers', 0)
    row_models['4 Players Sum'] = player_sum_models
    row_papers['4 Players Sum'] = player_sum_papers
    
    chart_data_models.append(row_models)
    chart_data_papers.append(row_papers)

# --- Models Growth 탭 ---
with tab1:
    if chart_data_models:
        df_models = pd.DataFrame(chart_data_models).set_index('round')
        
        # 범례 순서 지정
        legend_order = ["United States", "China", "4 Players Sum", "Korea", "Japan", "Mongolia", "Taiwan"]
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
        
        # 범례 순서 지정
        legend_order = ["United States", "China", "4 Players Sum", "Korea", "Japan", "Mongolia", "Taiwan"]
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

# 5. 기능 3: 이번 라운드 국제 이벤트
st.header("🔔 Events This Round")

# 플레이어의 Domestic Event 표시
st.subheader(f"Domestic Event in {my_team}")
try:
    with open(config.shared_dir / f"domestic_{my_team}.json", "r") as f:
        domestic_event = json.load(f)
    st.markdown(f"**{domestic_event['title']}**")
    st.write(domestic_event['description'])
except FileNotFoundError:
    st.warning(f"Your domestic event file was not found.")

# 국제 이벤트 표시
st.subheader("International Events (Applied to all nations)")
try:
    with open(config.shared_dir / "international.json", "r") as f:
        international_events = json.load(f)
    for i, event in enumerate(international_events, 1):
        st.markdown(f"**{i}. {event['title']}**")
        st.write(event['description'])
except FileNotFoundError:
    st.warning("International events file not found for this round.")
