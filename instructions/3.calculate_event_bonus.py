
import numpy as np

# Event loss formulas (extend this dictionary to include all your events)
event_formulas = {
    1: {
        "Δ_models": "-2 * (1 if AI_Investment_Focus + Talent_Index + Education_Investment < 20 else 0.5 if AI_Investment_Focus + Talent_Index + Education_Investment < 25 else 0)",
        "Δ_papers": "round(-10 * (1 - np.log((3*AI_Investment_Focus + 6*Talent_Index + 1*Education_Investment)/10)))"
    },
    2: {
        "Δ_models": "-2 * (1 if Talent_Index + AI_Investment_Focus < 12 else 0.5)",
        "Δ_papers": "round(-20 * np.exp(-0.1 * (Talent_Index + Education_Investment)))"
    },
    3: {
        "Δ_models": "round(-2 * (1 - Electricity/10))",
        "Δ_papers": "-20 * (1 if Electricity + Semiconductor < 10 else 0.5)"
    },
    4: {
        "Δ_models": "round(-1 * (1 - AI_Literacy_Education / 15))",
        "Δ_papers": "0"
    }
}

# Function to evaluate event losses
def evaluate_events(event_ids, params):
    results = []
    for eid in event_ids:
        if eid not in event_formulas:
            raise ValueError(f"Event {eid} not defined.")
        scope = dict(params)
        scope["np"] = np
        Δ_models = eval(event_formulas[eid]["Δ_models"], {}, scope)
        Δ_papers = eval(event_formulas[eid]["Δ_papers"], {}, scope)
        results.append([Δ_models, Δ_papers])
    return np.array(results)

# Function to evaluate diplomacy outcome
def evaluate_diplomacy(
    Alignment_US, Alignment_China,
    AI_Change_US, AI_Change_China,
    Total_AI_paper_US, Total_AI_paper_China,
    tolerance=0.2
):
    if Alignment_China == 0 or AI_Change_China == 0:
        return 0, 0

    alignment_ratio = Alignment_US / Alignment_China
    ai_change_ratio = AI_Change_US / AI_Change_China
    ratio_error = abs(alignment_ratio - ai_change_ratio)
    success = int(ratio_error <= tolerance)

    total_paper = Total_AI_paper_US + Total_AI_paper_China
    weighted_sum = Total_AI_paper_US * Alignment_US + Total_AI_paper_China * Alignment_China
    bonus = round(2 * weighted_sum / total_paper) if total_paper != 0 else 0

    return success, bonus

if __name__ == "__main__":
    # Example: Evaluate events 1 to 4 with example parameter values
    example_params = {
        "AI_Investment_Focus": 6,
        "Talent_Index": 7,
        "Education_Investment": 6,
        "Electricity": 5,
        "Semiconductor": 6,
        "AI_Literacy_Education": 4,
        "Labor": 0.7,
        "Deployment_Infrastructure": 5,
        "IP_Protection_Strength": 6,
        "Open_Source_Adoption": 5,
        "Democratic_Stability_Index": 7,
        "Dual_Use_Restriction_Strictness": 5,
        "GDP": 1.0,
        "Natural_Resource_Reserves": 1.0
    }

    event_ids = [1, 2, 3, 4]
    result_matrix = evaluate_events(event_ids, example_params)
    print("Event Impact Bonus (Δ_models, Δ_papers):")
    print(result_matrix)

    # Example: Evaluate diplomacy outcome
    success, bonus = evaluate_diplomacy(
        Alignment_US=3,
        Alignment_China=7,
        AI_Change_US=1.2,
        AI_Change_China=2.3,
        Total_AI_paper_US=150,
        Total_AI_paper_China=180
    )
    print(f"Diplomacy Model Bonus: {success}, Diplomacy Paper Bonus: {bonus}")
