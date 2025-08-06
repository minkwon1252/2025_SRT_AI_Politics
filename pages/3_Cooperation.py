# pages/3_Cooperation.py
import streamlit as st
import pandas as pd
import copy
import json
import time
import config  # config.coop_params, config.coop_param_keys 등을 사용

st.set_page_config(layout="centered", page_title="Cooperation Phase")

# --- 1. 새로운 파라미터 구조에 맞는 점수 및 매트릭스 계산 함수 ---
def compute_cooperation_details(state, partners, coop_config, all_keys):
    """
    points and matrix for cooperation agreements.
    """
    display_rows = []
    country_points = {p: 0 for p in partners}
    
    # 카테고리별로 묶어서 표시 및 계산
    # 1. Data & Talent Shared
    for key in ["Data_Shared", "Talent_Shared"]:
        meta = coop_config[key]
        points = meta["points"]
        row_data = [key.replace("_", " "), str(points)]
        for country in partners:
            if state[country].get(key, False):
                row_data.append("Yes")
                country_points[country] += points
            else:
                row_data.append("No")
        display_rows.append(row_data)

    # 2. Emergency Pact
    pact_points = coop_config["Emergency_Pact_Semiconductor"]["points"]
    pact_row = [f"Emergency Pact", "3"]
    for country in partners:
        pacts = []
        if state[country].get("Emergency_Pact_Semiconductor", False):
            pacts.append("Semiconductor")
            country_points[country] += pact_points
        if state[country].get("Emergency_Pact_Energy", False):
            pacts.append("Energy")
            country_points[country] += pact_points
        pact_row.append(", ".join(pacts) if pacts else "No")
    display_rows.append(pact_row)

    # 3. Joint Research
    research_row = ["Joint Research", "3 ~ 5"]
    for country in partners:
        project = state[country].get("Joint_Research_Project", "3~5")
        display_text = project
        project_points = coop_config["Joint_Research_Project"]["options"].get(project, 0)
        
        if project != "None":
            sub_options = []
            # DU
            if state[country].get("Joint_Research_DU", False):
                dur_points = coop_config["Joint_Research_DU"]["points"]
                project_points += dur_points
                sub_options.append(f"DUR (+{dur_points})")
            # Standard
            standard = state[country].get("Joint_Research_Standard", "None")
            if standard != "None":
                std_points = coop_config["Joint_Research_Standard"]["options"].get(standard, 0)
                project_points += std_points
                sub_options.append(f"{standard} Std (+{std_points})")
            
            if sub_options:
                display_text += f" ({', '.join(sub_options)})"
        
        research_row.append(display_text)
        country_points[country] += project_points
    display_rows.append(research_row)
    
    total_points_used = sum(country_points.values())
    
    columns = ["Parameter", "Base Points"] + partners
    df = pd.DataFrame(display_rows, columns=columns)
    
    # summary row
    used_row = ["Used Points", ""] + [country_points.get(p, 0) for p in partners]
    df.loc["Total"] = used_row
    df = df.astype(str)
    
    return df, total_points_used

# --- authentication ---
if not st.session_state.get("authenticated_team"):
    st.error("Please log in first.")
    st.stop()
    st.switch_page("pages/0_Login.py")

team = st.session_state["authenticated_team"]
negotiable_partners = ["Japan", "Korea", "Taiwan", "Mongolia"]
partners = [c for c in negotiable_partners if c != team]
coop_limit = 10 + st.session_state.get("hidden_params_Willing_to_Cooperate", 5)

# =================================================================
# [MODIFICATION START] 사이드바 이벤트 힌트
# =================================================================
st.sidebar.header("📌 Event Hints")

# --- 1. Domestic Event 힌트 표시 ---
if st.session_state.get('event_title') and st.session_state.get('domestic_event_hints'):
    st.sidebar.subheader(f"🏠 {st.session_state['event_title']}")
    with st.sidebar.expander("View Domestic Hints"):
        for hint in st.session_state.domestic_event_hints:
            st.info(f"**{hint.replace('_', ' ')}** is a key parameter.")

# --- 2. International Event 힌트 표시 ---
if st.session_state.get('international_event_title') and st.session_state.get('international_event_hints'):
    st.sidebar.subheader(f"🗺️ {st.session_state['international_event_title']}")
    with st.sidebar.expander("View International Hints"):
        for hint in st.session_state.international_event_hints:
            st.warning(f"**{hint.replace('_', ' ')}** is a key parameter.")

st.sidebar.divider()
# =================================================================
# [MODIFICATION END] 사이드바 이벤트 힌트
# =================================================================


st.title(f"🤝 {config.country_flags[team]} {team} - Cooperative Parameters")

st.markdown("""
<style>
.big-caption {
    font-size: 17px !important;
    color: black !important;
    line-height: 1.6;
    margin-bottom: 1em;
}
.important-line {
    font-weight: bold;
    font-size: 18px;
    margin-top: 1em;
}
</style>
<div class='big-caption'>
    In this phase, you will manage your nation's <b>cooperative AI strategy</b>—deciding how much to share, whom to partner with, and what kind of global AI initiatives to support.
    <br><br>
    You can choose to share computing power, data, talent, or energy. You may also form joint projects or align with international AI standards. Each decision impacts how much your country contributes to and gains from global AI advancement.
    <br><br>
    Your willingness to cooperate gives you points to spend on agreements. Cooperative actions require mutual agreement between nations, so choose your offers wisely.
    <br><br>
    You might face a <b>Prisoner’s Dilemma</b>, where sharing resources like semiconductors benefits both sides—but only if trust isn’t broken. Or a <b>Stag Hunt</b> might happen, where major gains are possible only when both nations commit fully. Or else, you might find yourself in a <b>Chicken Game</b>, where refusing to join a joint project leads to a dangerous standoff if no one backs down. Choose wisely.

> **"I just want everyone to get along. With me, especially."** > <i>– White Widow, Mission: Impossible – Dead Reckoning (2023)</i>
</div>
""", unsafe_allow_html=True)


# --- intialization ---
if "cooperation_state" not in st.session_state:
    st.session_state.cooperation_state = {
        c: {k: False if "type" in config.coop_params[k] and config.coop_params[k]["type"] == "bool" else "None" for k in config.coop_param_keys}
        for c in partners
    }

# --- matrix update ---
matrix_df, all_used = compute_cooperation_details(st.session_state.cooperation_state, partners, config.coop_params, config.coop_param_keys)
st.markdown("### 🌐 Cooperation Matrix")
st.dataframe(matrix_df, use_container_width=True)
st.markdown(f"**Total Points Used: {all_used} / {coop_limit}**")
if all_used > coop_limit:
    st.error(f"Point limit exceeded! You must reduce your agreements to {coop_limit} points or less.")


# --- Event Example Outcomes (START) ---
with st.expander("💡 View Cooperation Outcomes Examples"):
    st.markdown("""
    This is an example of how your choices interact with international events and other teams choice.
    """)

    # --- Event #71 ---
    st.markdown("#### Event #71 \"Theoretical breakthrough in Algorithms\"")
    st.code("delta model = round(1.5 * Data_Shared + 0.5 * int(Joint_Project != 'No') + 0.2 * log(1 + Open_Source_Adoption))")
    st.code("delta paper = round(10 * Data_Shared + 5 * int(Joint_Project != 'No') + 0.4 * Open_Source_Adoption)")
    st.markdown("---")
    st.markdown("""
<table style="border-collapse: collapse; font-size: 0.9em;">
  <tr>
    <th style="border: 1px solid #ccc; padding: 6px;">Scenario</th>
    <th style="border: 1px solid #ccc; padding: 6px;">Delta Model</th>
    <th style="border: 1px solid #ccc; padding: 6px;">Delta Paper</th>
  </tr>
  <tr>
    <td style="border: 1px solid #ccc; padding: 6px;">
      Open_Source_Adoption = 10<br>
      Data Sharing: ❌<br>
      Joint Project: ❌
    </td>
    <td style="border: 1px solid #ccc; padding: 6px;">0</td>
    <td style="border: 1px solid #ccc; padding: 6px;">4</td>
  </tr>
  <tr>
    <td style="border: 1px solid #ccc; padding: 6px;">
      Open_Source_Adoption = 5<br>
      Data Sharing: ❌<br>
      Joint Project: ✅
    </td>
    <td style="border: 1px solid #ccc; padding: 6px;">1</td>
    <td style="border: 1px solid #ccc; padding: 6px;">7</td>
  </tr>
  <tr>
    <td style="border: 1px solid #ccc; padding: 6px;">
      Open_Source_Adoption = 3<br>
      Data Sharing: ✅<br>
      Joint Project: ✅
    </td>
    <td style="border: 1px solid #ccc; padding: 6px;">2</td>
    <td style="border: 1px solid #ccc; padding: 6px;">16</td>
  </tr>
</table>
""", unsafe_allow_html=True)

    st.markdown("---")

    # --- Event #108 ---
    st.markdown("#### Event #108 \"Data Dilemma\" - interactive case")
    st.code("if Data shared between country A and B")
    
    st.markdown("""
<table style="border-collapse: collapse; font-size: 0.85em;">
  <tr>
    <th style="border: 1px solid #ccc;"></th>
    <th style="border: 1px solid #ccc; padding: 6px;"><b>B Open_Source_Adoption > 7</b></th>
    <th style="border: 1px solid #ccc; padding: 6px;"><b>B Open_Source_Adoption ≤ 7</b></th>
  </tr>
  <tr>
    <td style="border: 1px solid #ccc; padding: 6px;"><b>A Open_Source_Adoption > 7</b></td>
    <td style="border: 1px solid #ccc; padding: 6px;">
      A model +1<br>A paper + B OSA<br>B model +1<br>B paper + A OSA
    </td>
    <td style="border: 1px solid #ccc; padding: 6px;">
      A model -1<br>A paper - A OSA<br>B model +2<br>B paper + B OSA + A OSA
    </td>
  </tr>
  <tr>
    <td style="border: 1px solid #ccc; padding: 6px;"><b>A Open_Source_Adoption ≤ 7</b></td>
    <td style="border: 1px solid #ccc; padding: 6px;">
      A model +2<br>A paper + A OSA + B OSA<br>B model -1<br>B paper + A OSA
    </td>
    <td style="border: 1px solid #ccc; padding: 6px;">
      A model -1<br>A paper - A OSA<br>B model -1<br>B paper - B OSA
    </td>
  </tr>
</table>
""", unsafe_allow_html=True)


# --- Event Example Outcomes (END) ---



# --- Negotiation form ---
st.divider()
st.markdown("### 🧭 Choose a country to negotiate with:")
selected_country = st.selectbox("Select partner country:", partners)

with st.form(key=f"form_{selected_country}"):
    st.header(f"Agreement with {config.country_flags[selected_country]} {selected_country}\n")

    st.subheader("Resource Share")
    # 1. Data_Shared
    meta = config.coop_params["Data_Shared"]
    st.toggle(
        label=f"Data Sharing ({meta['points']} pts)", 
        value=st.session_state.cooperation_state[selected_country]["Data_Shared"],
        key=f"{selected_country}_Data_Shared",
        help=meta["desc"]
    )

    # 2. Talent_Shared
    meta = config.coop_params["Talent_Shared"]
    st.toggle(
        label=f"Talent Sharing ({meta['points']} pts)", 
        value=st.session_state.cooperation_state[selected_country]["Talent_Shared"],
        key=f"{selected_country}_Talent_Shared",
        help=meta["desc"]
    )
    
    st.divider()

    # 3. Emergency_Pact
    st.subheader("Emergency Pact")
    pact_cols = st.columns(2)
    with pact_cols[0]:
        meta = config.coop_params["Emergency_Pact_Semiconductor"]
        st.checkbox(
            label=f"Semiconductor Pact ({meta['points']} pts)",
            value=st.session_state.cooperation_state[selected_country]["Emergency_Pact_Semiconductor"],
            key=f"{selected_country}_Emergency_Pact_Semiconductor",
            help=meta["desc"]
        )
    with pact_cols[1]:
        meta = config.coop_params["Emergency_Pact_Energy"]
        st.checkbox(
            label=f"Energy Pact ({meta['points']} pts)",
            value=st.session_state.cooperation_state[selected_country]["Emergency_Pact_Energy"],
            key=f"{selected_country}_Emergency_Pact_Energy",
            help=meta["desc"]
        )

    st.divider()

    # 4. _Research
    st.subheader("Joint Research")
    meta_proj = config.coop_params["Joint_Research_Project"]
    
    # Project selection
    project_options = list(meta_proj["options"].keys())
    project_index = project_options.index(st.session_state.cooperation_state[selected_country]["Joint_Research_Project"])
    selected_project = st.selectbox(
        "Select Joint Project",
        options=project_options,
        index=project_index,
        key=f"{selected_country}_Joint_Research_Project_temp", # temporary key for form submission
        help=meta_proj["desc"]
    )

    # If a project is selected, show sub-options
    if selected_project != "None":
        st.markdown("###### > Research Sub-options")
        sub_cols = st.columns(2)
        with sub_cols[0]:
            # DUR
            meta_dur = config.coop_params["Joint_Research_DU"]
            st.toggle(
                label=f"Dual-Use Available ({meta_dur['points']} pt)",
                value=st.session_state.cooperation_state[selected_country]["Joint_Research_DU"],
                key=f"{selected_country}_Joint_Research_DU_temp",
                help=meta_dur["desc"]
            )
        with sub_cols[1]:
            # AI Standard
            meta_std = config.coop_params["Joint_Research_Standard"]
            std_options = list(meta_std["options"].keys())
            std_index = std_options.index(st.session_state.cooperation_state[selected_country]["Joint_Research_Standard"])
            st.radio(
                label=f"AI Standard (US/China: +{meta_std['options']['US']} pt)",
                options=std_options,
                index=std_index,
                key=f"{selected_country}_Joint_Research_Standard_temp",
                horizontal=True,
                help=meta_std["desc"]
            )
    
    # Form submission
    submitted = st.form_submit_button(f"📩 Update Agreement with {config.country_flags[selected_country]} {selected_country}")

if submitted:
    # update session state with form data
    temp_state = copy.deepcopy(st.session_state.cooperation_state)
    
    # read values from form
    temp_state[selected_country]["Data_Shared"] = st.session_state[f"{selected_country}_Data_Shared"]
    temp_state[selected_country]["Talent_Shared"] = st.session_state[f"{selected_country}_Talent_Shared"]
    temp_state[selected_country]["Emergency_Pact_Semiconductor"] = st.session_state[f"{selected_country}_Emergency_Pact_Semiconductor"]
    temp_state[selected_country]["Emergency_Pact_Energy"] = st.session_state[f"{selected_country}_Emergency_Pact_Energy"]
    
    # Joint Research update
    selected_project = st.session_state[f"{selected_country}_Joint_Research_Project_temp"]
    temp_state[selected_country]["Joint_Research_Project"] = selected_project
    if selected_project != "None":
        temp_state[selected_country]["Joint_Research_DU"] = st.session_state[f"{selected_country}_Joint_Research_DU_temp"]
        temp_state[selected_country]["Joint_Research_Standard"] = st.session_state[f"{selected_country}_Joint_Research_Standard_temp"]
    else: # if no project selected, reset sub-options
        temp_state[selected_country]["Joint_Research_DU"] = False
        temp_state[selected_country]["Joint_Research_Standard"] = "None"
        
    st.session_state.cooperation_state = temp_state

    with open(f"shared_data/cooperation_{team}.json", "w") as f:
        json.dump(st.session_state.cooperation_state, f)
    
    st.toast(f"Agreement with {selected_country} updated!")
    time.sleep(1)
    st.rerun() # UI and matrix update

# --- Final confirmation ---
st.divider()
if st.button("📥 Confirm All Cooperative Parameters"):
    # 1. First, check the point limit
    _, final_used_points = compute_cooperation_details(st.session_state.cooperation_state, partners, config.coop_params, config.coop_param_keys)
    
    if final_used_points > coop_limit:
        st.error(f"❌ Cannot confirm. Total points used ({final_used_points}) exceeds your limit ({coop_limit}).")
    else:
        # 2. Verify mutual agreements with partners
        mismatches = []
        my_coop_state = st.session_state.cooperation_state
        
        for partner_name, my_proposal in my_coop_state.items():
            try:
                with open(f"shared_data/cooperation_{partner_name}.json", "r") as f:
                    partner_coop_state = json.load(f)
                
                # Get the partner's proposal for my team
                their_proposal_for_me = partner_coop_state.get(team)

                if not their_proposal_for_me:
                    mismatches.append(f"⚠️ Could not find cooperation data for you in {partner_name}'s file.")
                    continue

                # Compare each parameter
                for param_key, my_value in my_proposal.items():
                    their_value = their_proposal_for_me.get(param_key)
                    if my_value != their_value:
                        mismatches.append(f"❌ Disagreement with {partner_name} on '{param_key}': (You: {my_value} | Them: {their_value})")

            except FileNotFoundError:
                st.warning(f"ℹ️ Could not verify agreement with {partner_name}. Their file was not found. Proceeding with confirmation.")
            except Exception as e:
                st.error(f"Error during verification with {partner_name}: {e}")

        # 3. Final decision
        if mismatches:
            st.error("Confirmation failed. The following agreements are not mutual:")
            for msg in mismatches:
                st.write(msg)
        else:
            # If everything matches, save the file and switch pages
            with open(f"shared_data/cooperation_{team}.json", "w") as f:
                json.dump(st.session_state.cooperation_state, f)
            
            st.session_state.cooperation_confirmed = True
            st.success(f"✅ All agreements are mutual! Points used: {final_used_points}/{coop_limit}. Proceeding to the Event Phase...")
            time.sleep(2)
            st.switch_page("pages/4_Events.py")