# pages/5_Summary.py
import streamlit as st
import json
import random
import config
import utils

st.set_page_config(layout="centered", page_title="Summary")

# 로그인 확인
if not st.session_state.get("authenticated_team"):
    st.error("Please log in first.")
    st.switch_page("pages/1_Login.py")

team = st.session_state["authenticated_team"]

st.title("📊 AI Model & Paper Summary")
st.markdown("""
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

# 1. Load Parameters
try:
    with open(config.shared_dir / f"hidden_{team}.json") as f:
        hidden_params = json.load(f)
    with open(config.shared_dir / f"cooperation_{team}.json") as f:
        coop_params_raw = json.load(f)
    with open(config.shared_dir / f"domestic_{team}.json") as f:
        domestic_event = json.load(f)
    with open(config.shared_dir / "international.json") as f:
        international_events = json.load(f)
except FileNotFoundError as e:
    st.error(f"Missing data file: {e.filename}. Please complete the previous steps.")
    st.stop()

# 2. Initialize session state for counts
if "paper_count" not in st.session_state:
    st.session_state["paper_count"] = config.initial_data[team]["papers"]
if "model_count" not in st.session_state:
    st.session_state["model_count"] = config.initial_data[team]["models"]
if "US_papers" not in st.session_state:
    st.session_state["US_papers"] = config.initial_data["US"]["papers"]
    st.session_state["US_models"] = config.initial_data["US"]["models"]
if "China_papers" not in st.session_state:
    st.session_state["China_papers"] = config.initial_data["China"]["papers"]
    st.session_state["China_models"] = config.initial_data["China"]["models"]

# 3. Calculate Deltas
delta_paper_domestic = utils.evaluate_delta(domestic_event["delta_papers"], hidden_params)
delta_model_domestic = utils.evaluate_delta(domestic_event["delta_models"], hidden_params)

delta_paper_international = sum(
    utils.evaluate_event_international(event["delta_papers"], hidden_params, coop_params_raw)
    for event in international_events
)
delta_model_international = sum(
    utils.evaluate_event_international(event["delta_models"], hidden_params, coop_params_raw)
    for event in international_events
)

paper_growth_this_round = st.session_state.get("growth_rate", 0)

# 4. Update Counts
st.session_state["paper_count"] += paper_growth_this_round + delta_paper_domestic + delta_paper_international
st.session_state["model_count"] += delta_model_domestic + delta_model_international
# Probabilistic model growth
new_models_from_papers = utils.calculate_ai_models(st.session_state["paper_count"])
st.session_state["model_count"] += new_models_from_papers

# 5. Update US/China
us_growth = random.randint(150, 250)
cn_growth = random.randint(200, 300)
st.session_state["US_papers"] += us_growth
st.session_state["China_papers"] += cn_growth
st.session_state["US_models"] = int(round(utils.calculate_ai_models(st.session_state["US_papers"])))
st.session_state["China_models"] = int(round(utils.calculate_ai_models(st.session_state["China_papers"])))

# 6. Display Player Summary
st.header(f"{config.country_flags[team]} Your Nation's Progress")
col1, col2 = st.columns(2)
col1.metric("⚛ Total Papers", f"{int(st.session_state['paper_count'])}")
col2.metric("🪄 Total Models", f"{int(st.session_state['model_count'])}")

with st.expander("📄 View Detailed Breakdown"):
    c1, c2 = st.columns(2)
    with c1:
        st.markdown(f"""
        **Paper Growth**
        - Base Growth: `{paper_growth_this_round}`
        - Domestic Event Impact: `{delta_paper_domestic}`
        - International Event Impact: `{delta_paper_international}`
        """)
    with c2:
        st.markdown(f"""
        **Model Growth**
        - From Papers: `+{new_models_from_papers:.2f}`
        - Domestic Event Impact: `{delta_model_domestic}`
        - International Event Impact: `{delta_model_international}`
        """)

# 7. Display US & China Summary
st.markdown("---")
st.header("🌍 Global AI Superpowers")
col1, col2 = st.columns(2)
with col1:
    st.markdown("### 🇺🇸 United States")
    st.metric("Total Papers", st.session_state["US_papers"])
    st.metric("Estimated Models", st.session_state["US_models"])
with col2:
    st.markdown("### 🇨🇳 China")
    st.metric("Total Papers", st.session_state["China_papers"])
    st.metric("Estimated Models", st.session_state["China_models"])
