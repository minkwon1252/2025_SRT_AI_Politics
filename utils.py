# utils.py
import streamlit as st
import numpy as np
import math
import random
from scipy.stats import norm
import config # config.py file

u = 84.17
threshold = 40 * u / 19

def calculate_ai_models(paper_count, normalize_to=15, reference_variance=2000):
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
    total = 0
    for country, bilateral_raw in coop_dict.items():
        bilateral = process_coop_params(bilateral_raw)
        combined = {**hidden, **bilateral}
        total += evaluate_delta(expr, combined)
    return total

def category_to_multiplier(val, mapping):
    return mapping.get(str(val).strip(), 1.0)
    
def compute_growth_rate(params, fixed):
    try:
        tech_term = np.log(1 + 1.2 * params["Semiconductor"] + 0.8 * params["Electricity"] + params["Open_Source_Adoption"] + 1.5 * params["AI_Investment_Focus"]) ** 1.2
        human_term = np.sqrt((params["Talent_Index"] + 1) * (params["Education_Investment"] + 1))
        cultural_term = 1.5 * 10 * (np.tanh(0.2 * (params["AI_Literacy_Education"] + params["Democratic_Stability_Index"])) + 1)
        labor_term = fixed["Labor"] ** 0.75
        nat = category_to_multiplier(fixed["Natural_Resource_Reserves"], {"Low": 1, "Medium": 1.2, "High": 1.6})
        gdp = category_to_multiplier(fixed["GDP"], {"Low": 0.8, "Medium": 1.0, "High": 1.2})
        return round(4 * ((tech_term * human_term + cultural_term) * labor_term * nat * gdp))
    except:
        return None
        

# --- Intelligence Phase ---

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def intel_accuracy_prob(intelligence):
    return 0.4 * sigmoid(1.5 * (intelligence - 5)) + 0.5

# ——— hidden parameter 범위 정보 생성 ———
def get_hidden_param_info(param, true_val, intel_score):
    acc = intel_accuracy_prob(intel_score)
    correct = random.random() < acc

    # Define margin based on intelligence score
    if intel_score <= 0:
        return f"{param}: 0~10"
    elif intel_score <=2:
        margin = random.choice([4, 2])
    elif intel_score <= 5: 
        margin = random.choice([3, 2])
    elif intel_score <= 7:
        margin = random.choice([3, 1])
    elif intel_score <= 9:
        margin = random.choice([2, 1])
    else:
        margin = random.choice([1, 0])

    if correct:
        # 🎯 비대칭 범위 (정확한 값 기준, 오른쪽이 조금 더 넓은 경향)
        left = np.random.binomial(n=margin, p=0.3)
        right = margin - left
        low = max(0, true_val - left)
        high = min(10, true_val + right)
    else:
        # ❌ 틀린 중심값: 70% 과대평가, 30% 과소평가
        direction = 1 if random.random() < 0.7 else -1
        offset = random.randint(margin + 1, margin + 2)
        fake_val = (true_val + direction * offset) % 11

        # 틀린 값에 대한 비대칭 범위 (우측이 넓은 경향)
        fake_margin = random.randint(1, 2)
        left = np.random.binomial(n=fake_margin, p=0.3)
        right = fake_margin - left
        low = max(0, fake_val - left)
        high = min(10, fake_val + right)

    return f"{param}: {low}" if low == high else f"{param}: {low}~{high}"


# ——— cooperative parameter 정보 생성 ———
def get_coop_info(param, true_val, intel_score, options=None):
    # 자동 추론: options가 없으면 param 이름 기반으로 유추
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
