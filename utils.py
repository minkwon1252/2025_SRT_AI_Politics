# utils.py
import streamlit as st
import numpy as np
import math
import random
from scipy.stats import norm
import config
import json
import pandas as pd
import altair as alt
import os
import itertools

u = 84.17
threshold = 40 * u / 19

def calculate_ai_models(paper_count, normalize_to=15, reference_variance=2000):
    
    if paper_count <= 0:
        return 0
        
    std_dev = np.sqrt(paper_count)
    z_score = (threshold - u) / std_dev
    probability = 1 - norm.cdf(z_score)

    reference_std = np.sqrt(reference_variance)
    ref_prob = 1 - norm.cdf((threshold - u) / reference_std)
    scaling_factor = normalize_to / ref_prob

    return probability * scaling_factor
    
def process_coop_params(raw: dict) -> dict:
    out = {}
    for k, v in raw.items():
        if isinstance(v, str):
            if v == "Yes":
                out[k] = 1
            elif v == "No":
                out[k] = 0
            elif v == "None":
                out[k] = None
            else:
                out[k] = v
        else:
            out[k] = v
    return out

def evaluate_delta(expr: str, params: dict) -> int:
    safe_locals = {
        k: params[k]
        for k in params
        if isinstance(params[k], (int, float, str)) or params[k] is None
    }
    try:
        return int(eval(
            expr,
            {
                "__builtins__": {},
                "round": round,
                "min": min,
                "max": max,
                "int": int,
                "sqrt": np.sqrt,
                "np": np,
                "mean": np.mean,
                "log": math.log,
                "exp": math.exp,
                "abs": abs
            },
            safe_locals
        ))
    except Exception as e:
        st.error(f"Error evaluating expression:\n{expr}\n\n{e}")
        return 0

def evaluate_event_international(expr: str, hidden: dict, coop_dict: dict) -> int:
    # --- debuging code ---
    #st.warning(f"--- 🕵️ 디버깅 시작: 국제 이벤트 계산 ---")
    #st.write(f"**계산 공식:** `{expr}`")
    
    total = 0
    for country, bilateral_raw in coop_dict.items():
        bilateral = process_coop_params(bilateral_raw)
        combined = {**hidden, **bilateral}
        delta_for_partner = evaluate_delta(expr, combined)
        
        # for each partners
        #st.write(f"- 파트너 **{country}**에 공식 적용 결과: **`{delta_for_partner}`**")
        
        total += delta_for_partner
        
    #st.write(f"**➡️ 이 공식의 최종 합산 결과: `{total}`**")
    #st.warning("--- 🕵️ 디버깅 종료 ---")
    # --- 디버깅 코드 종료 ---
    return total

def category_to_multiplier(val, mapping):
    return mapping.get(str(val).strip(), 1.0)
#---- AI Policy Phase ----
    
def compute_growth_rate(params, fixed):
    try:
        tech_term = np.log(1 + 1.2 * params["Semiconductor"] + 0.8 * params["Electricity"] + params["Open_Source_Adoption"] + 1.5 * params["AI_Fund"]) ** 1.2
        human_term = np.sqrt((params["Talent_Index"] + 1) * (params["Education_Investment"] + 1))
        cultural_term = 1.5 * 10 * (np.tanh(0.2 * (params["AI_Literacy_Education"] + params["Democratic_Stability_Index"])) + 1)
        labor_term = fixed["Labor"] ** 0.75
        nat = category_to_multiplier(fixed["Natural_Resource_Reserves"], {"Low": 1, "Medium": 1.2, "High": 1.6})
        gdp = category_to_multiplier(fixed["GDP"], {"Low": 0.8, "Medium": 1.0, "High": 1.2})
        return round(4 * ((tech_term * human_term + cultural_term) * labor_term * nat * gdp))
    except:
        return None


# compute_growth_rate
PARAMETER_TERM_MAP = {
    "Semiconductor": "Technical",
    "Electricity": "Technical",
    "Open_Source_Adoption": "Technical",
    "AI_Fund": "Technical",
    "Talent_Index": "Human Resources",
    "Education_Investment": "Human Resources",
    "AI_Literacy_Education": "Socio-Cultural",
    "Democratic_Stability_Index": "Socio-Cultural"
}

def compute_terms(params):
    """
    각 파라미터 그룹(항)의 값을 계산하여 딕셔너리로 반환합니다.
    """
    try:
        tech_term = np.log(1 + 1.2 * params.get("Semiconductor", 0) + 0.8 * params.get("Electricity", 0) + params.get("Open_Source_Adoption", 0) + 1.5 * params.get("AI_Fund", 0)) ** 1.2
        human_term = np.sqrt((params.get("Talent_Index", 0) + 1) * (params.get("Education_Investment", 0) + 1))
        cultural_term = 1.5 * 10 * (np.tanh(0.2 * (params.get("AI_Literacy_Education", 0) + params.get("Democratic_Stability_Index", 0))) + 1)
        
        return {
            "Technical": tech_term,
            "Human Resources": human_term,
            "Socio-Cultural": cultural_term
        }
    except (ValueError, TypeError):
        return {"Technical": 0, "Human Resources": 0, "Socio-Cultural": 0}
    
def plot_parameter_impact(param_name, current_params, fixed_conditions):
    """
    특정 파라미터가 속한 '항(term)'의 값 변화를 그래프로 그립니다.
    """
    term_to_plot = PARAMETER_TERM_MAP.get(param_name)
    
    if not term_to_plot:
        raise ValueError(f"'{param_name}'은 성장률 계산에 영향을 주지 않습니다.")

    param_values = list(range(11))
    term_output_values = []

    for val in param_values:
        temp_params = current_params.copy()
        temp_params[param_name] = val
        all_terms = compute_terms(temp_params)
        term_value = all_terms[term_to_plot]
        term_output_values.append(term_value)

    current_value = current_params.get(param_name)
    current_term_output = compute_terms(current_params)[term_to_plot]

    df = pd.DataFrame({
        'Parameter Value': param_values,
        'Term Contribution': term_output_values
    })

    y_axis_title = f'{term_to_plot} Term Contribution'

    line = alt.Chart(df).mark_line(point=True).encode(
        x=alt.X('Parameter Value:Q', title=f'{param_name.replace("_", " ")} Level', scale=alt.Scale(domain=[0, 10])),
        y=alt.Y('Term Contribution:Q', title=y_axis_title, scale=alt.Scale(zero=False)),
        tooltip=['Parameter Value', alt.Tooltip('Term Contribution:Q', format='.2f')]
    ).properties(
        title=alt.TitleParams(
            text=f'Impact of {param_name.replace("_", " ")} on {term_to_plot} Term',
            anchor='middle'
        )
    )
    
    point = alt.Chart(pd.DataFrame({
        'Parameter Value': [current_value],
        'Term Contribution': [current_term_output]
    })).mark_point(
        color='red', size=100, filled=True, opacity=1
    ).encode(
        x='Parameter Value:Q',
        y='Term Contribution:Q',
        tooltip=['Parameter Value', alt.Tooltip('Term Contribution:Q', format='.2f')]
    )

    return line + point
        

# --- Intelligence Phase ---

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def intel_accuracy_prob(intelligence):
    return 0.4 * sigmoid(1.5 * (intelligence - 5)) + 0.5

# ——— hidden parameter range gen intel ———

def get_hidden_param_info(param_name, true_val, intel_score):
    if intel_score < 1:
        return "Unknown (Intel Score too low)"

    # --- Start Modification ---
    # Ensure true_val is a number; if None or non-numeric, treat as 0 or handle as an error
    if true_val is None:
        # Option 1: Treat None as 0 for calculation purposes (most likely intended behavior)
        true_val = 0 
        st.warning(f"DEBUG: '{param_name}' had a None value, treated as 0 for calculation in intel.")
    elif not isinstance(true_val, (int, float)):
        # Option 2: If it's a string or other type, convert if possible or default to 0
        try:
            true_val = float(true_val) # Try converting to float
            st.warning(f"DEBUG: '{param_name}' had non-numeric value '{true_val}', converted to float.")
        except (ValueError, TypeError):
            true_val = 0 # Fallback if conversion fails
            st.error(f"ERROR: '{param_name}' had unconvertible non-numeric value '{true_val}', defaulted to 0.")
    # --- End Modification ---

    # Determine confidence level based on intel_score
    if intel_score < 4:
        confidence = "Low Confidence"
        offset_range = 3 # Can be off by +/- 3
    elif intel_score < 7:
        confidence = "Medium Confidence"
        offset_range = 2 # Can be off by +/- 2
    else: # intel_score >= 7
        confidence = "High Confidence"
        offset_range = 1 # Can be off by +/- 1

    # Generate a random offset within the range
    offset = random.randint(0, offset_range)
    direction = random.choice([-1, 1])

    # Calculate fake value, ensuring it stays within 0-10 range
    fake_val = (true_val + direction * offset) % 11
    if fake_val < 0: # Ensure positive result from modulo for negative inputs
        fake_val += 11

    # Adjust fake_val to be within 0-10 range explicitly if % 11 resulted in more than 10
    # or if the true value was very high/low and offset pushed it out
    fake_val = max(0, min(10, int(round(fake_val)))) # Ensure it's an integer for display

    if intel_score >= 10:
        return f"{param_name}: {int(round(true_val))} (Exact, High Confidence)" # Ensure true_val is also integer for display
    else:
        return f"{param_name}: {fake_val} (Approximate, {confidence})"


# ——— cooperative parameter gen intel ———
def get_coop_info(param, true_val, intel_score, options=None):

    if options is None:
        if param == "Joint_Project":
            options = ["None", "Energy", "Military", "Education", "Space", "Materials"]
        elif param == "AI_Standard_Alignment":
            options = ["None", "US", "China"]
        else:
            options = None  # fallback to binary

    acc = intel_accuracy_prob(intel_score)
    correct = random.random() < acc

    if options:
        if correct:
            pick = true_val
        else:
            others = [o for o in options if o != true_val]
            pick = random.choice(others) if others else true_val
    else:
        pick = true_val if correct else ("No" if true_val == "Yes" else "Yes")

    return f"{param}: {pick}"

# --- Summary Page Helper Functions ---
def parse_dilemma_papers(outcome_str, val_a, val_b):
    if not isinstance(outcome_str, str):
        return outcome_str
    
    total = 0
    if "A" in outcome_str:
        total += val_a if "+A" in outcome_str or "A" == outcome_str else -val_a
    if "B" in outcome_str:
        total += val_b if "+B" in outcome_str or "B" == outcome_str else -val_b
    return total


def calculate_round_results(team_name: str, initial_papers: int, initial_models: int, growth_rate: int, all_params: dict) -> tuple[tuple[int, int], dict]:
    """
    한 팀의 라운드 결과를 계산합니다. (모든 이벤트 유형을 한 번에 처리하도록 수정됨)
    """
    hidden_params = all_params.get(team_name, {}).get('hidden', {})
    coop_params_raw = all_params.get(team_name, {}).get('coop', {})
    
    domestic_deltas = []
    international_deltas = []
    team_fixed_values = config.fixed_values.get(team_name, {})
    evaluation_params = {**team_fixed_values, **hidden_params}
    
    # GDP, Resoure Mapping
    gdp_map = {"Low": 0.2, "Medium": 0.6, "High": 1.0}
    if "GDP" in evaluation_params and isinstance(evaluation_params["GDP"], str):
        evaluation_params["GDP_value"] = gdp_map.get(evaluation_params["GDP"], 0)
    nat_resource_map = {"Low": 0.5, "High": 1.0}
    if "Natural_Resource_Reserves" in evaluation_params and "Resource_value" not in evaluation_params:
         evaluation_params["Resource_value"] = nat_resource_map.get(evaluation_params["Natural_Resource_Reserves"], 0)

    # Domestic event
    domestic_event_file_path = config.shared_dir / f"domestic_{team_name}.json"
    if os.path.exists(domestic_event_file_path):
        try:
            with open(domestic_event_file_path, "r") as f:
                all_domestic_events = json.load(f)
                if not isinstance(all_domestic_events, list):
                    all_domestic_events = [all_domestic_events]
            for event in all_domestic_events:
                paper_d = evaluate_delta(event.get("delta_papers", "0"), evaluation_params)
                model_d = evaluate_delta(event.get("delta_models", "0"), evaluation_params)
                domestic_deltas.append({"title": event.get("title"), "paper_delta": paper_d, "model_delta": model_d})
        except (json.JSONDecodeError, IndexError):
            pass

    # --- International event ---
    international_event_file = config.shared_dir / "international.json"
    if os.path.exists(international_event_file):
        with open(international_event_file, "r") as f:
            all_international_events = json.load(f)

        for event in all_international_events:
            event_type = event.get("evaluation_type")
            paper_d, model_d = 0, 0

            if event_type == "interactive" and "logic" in event:
                logic = event["logic"]
                team_a_name = team_name
                
                # define partner as B
                for team_b_name in coop_params_raw.keys():
                    if team_b_name not in all_params: continue

                    team_a_proposal_for_b = coop_params_raw.get(team_b_name, {})
                    team_a_context = {**team_fixed_values, **hidden_params, **team_a_proposal_for_b, 'True': True, 'False': False, 'None': None}

                    team_b_hidden = all_params.get(team_b_name, {}).get('hidden', {})
                    team_b_coop_raw = all_params.get(team_b_name, {}).get('coop', {})
                    team_b_fixed = config.fixed_values.get(team_b_name, {})
                    team_b_proposal_for_a = team_b_coop_raw.get(team_a_name, {})
                    team_b_context = {**team_b_fixed, **team_b_hidden, **team_b_proposal_for_a, 'True': True, 'False': False, 'None': None}

                    try:
                        activation_str = logic["activation_param"]
                        is_active_a = eval(activation_str, {}, team_a_context)
                        is_active_b = eval(activation_str, {}, team_b_context)
                    except Exception:
                        is_active_a, is_active_b = False, False
                    
                    if not (is_active_a and is_active_b): 
                        continue

                    val_a = team_a_context.get(logic["comparison_param"], 0)
                    val_b = team_b_context.get(logic["comparison_param"], 0)
                    threshold = logic["threshold"]
                    
                    if val_a > threshold and val_b > threshold: outcome_key = "high_high"
                    elif val_a > threshold and val_b <= threshold: outcome_key = "high_low"
                    elif val_a <= threshold and val_b > threshold: outcome_key = "low_high"
                    else: outcome_key = "low_low"
                    
                    # outcome for A
                    outcome_for_a = logic["outcomes"][outcome_key].get("A", {})
                    model_d += outcome_for_a.get("models", 0)

                    try:
                        paper_formula = str(outcome_for_a.get("papers", "0"))
                        paper_context = {'A': val_a, 'B': val_b}
                        paper_d += round(eval(paper_formula, {}, paper_context))
                    except Exception:
                        paper_d += 0
            
            else: # non-dilemma type
                paper_d = evaluate_event_international(event.get("delta_papers", "0"), hidden_params, coop_params_raw)
                model_d = evaluate_event_international(event.get("delta_models", "0"), hidden_params, coop_params_raw)
            
            if paper_d != 0 or model_d != 0:
                international_deltas.append({"title": event.get("title"), "paper_delta": paper_d, "model_delta": model_d})

    # Sum them up
    total_paper_delta = growth_rate + sum(d['paper_delta'] for d in domestic_deltas) + sum(d['paper_delta'] for d in international_deltas)
    final_papers = max(0, initial_papers + total_paper_delta)
    new_models_from_papers = calculate_ai_models(final_papers) - calculate_ai_models(initial_papers)
    total_model_delta = new_models_from_papers + sum(d['model_delta'] for d in domestic_deltas) + sum(d['model_delta'] for d in international_deltas)
    final_models = max(0.0, initial_models + total_model_delta)
    delta_details = {
        'base_growth': growth_rate, 'domestic_deltas': domestic_deltas, 'international_deltas': international_deltas,
        'total_paper_delta': total_paper_delta, 'from_papers_model': new_models_from_papers, 'total_model_delta': total_model_delta
    }
    return (final_papers, final_models), delta_details

def load_history():
    """history.json 파일에서 모든 라운드 기록을 로드합니다."""
    history_file = config.shared_dir / "history.json"
    if history_file.exists():
        with open(history_file, "r") as f:
            return json.load(f)
    return []

def save_history(new_round_data):
    """기존 기록에 현재 라운드 데이터를 추가하여 저장합니다."""
    history = load_history()
    if not any(d['round'] == new_round_data['round'] for d in history):
        history.append(new_round_data)
        history_file = config.shared_dir / "history.json"
        with open(history_file, "w") as f:
            json.dump(history, f, indent=4)


