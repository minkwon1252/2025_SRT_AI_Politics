# 1_Circumstances.py
import streamlit as st
import random
import json
import time
import math
import numpy as np
import config
import utils
import re # For regular expression to parse formulas
import os


st.set_page_config(layout="centered", page_title="Circumstances Phase")

# --- login ---
if not st.session_state.get("authenticated_team"):
    st.error("Please log in first.")
    st.switch_page("pages/0_Login.py")

team = st.session_state.get("authenticated_team")

# --- initialize ---
if "domestic_event_shown" not in st.session_state:
    st.session_state.domestic_event_shown = False
if "international_event_shown" not in st.session_state:
    st.session_state.international_event_shown = False

# Admin page
st.markdown("""
    <style>
    [data-testid="stSidebarNav"] > ul > li:nth-child(8) {
        border-top: 2px solid #e6e6e6; /* devider */
        padding-top: 20px; /* space */
    }
    </style>
    """, unsafe_allow_html=True)

st.title("📰 Current Circumstances") # Added a newspaper emoji
st.markdown("""
As you step into the world of AI geopolitics, it's crucial to understand the ground realities.
Before you make any strategic decisions, let's look at the **domestic events** that have already unfolded
and the **international event** that will shape the global landscape.
""", unsafe_allow_html=True)
st.markdown("---")


# --- 1. Domestic Event (Fixed for now, can be randomized if needed) ---
# Only when events arent specified
if not st.session_state.domestic_event_shown:
    
    # For a random event:
    chosen_event_id = random.choice(list(config.domestic_events.keys()))
    
    event = config.domestic_events.get(chosen_event_id, {"title": "Unknown", "description": "N/A"})
    st.session_state["event_title"] = event["title"]
    st.session_state["event_description"] = event["description"]
    st.session_state["event_delta_models_formula"] = event.get("delta_models", "")
    st.session_state["event_delta_papers_formula"] = event.get("delta_papers", "")

    # --- Start Modification for 1_Circumstances.py Domestic Event Saving ---
    domestic_event_file_path = config.shared_dir / f"domestic_{team}.json"
    existing_domestic_events = []

    # check if it exists
    if os.path.exists(domestic_event_file_path):
        try:
            with open(domestic_event_file_path, "r") as f:
                loaded_content = json.load(f)

                if isinstance(loaded_content, list):
                    existing_domestic_events = loaded_content
                else:
                    existing_domestic_events = [loaded_content] 
        except json.JSONDecodeError:
            # if json broken
            existing_domestic_events = [] 
    
    existing_domestic_events.append(event) # append new list

    with open(domestic_event_file_path, "w") as f:
        json.dump(existing_domestic_events, f, indent=4) # update list
    # --- End Modification for 1_Circumstances.py Domestic Event Saving ---
    
    st.session_state.domestic_event_shown = True
    st.rerun() 

# show domestic event 
if st.session_state.domestic_event_shown:
    st.markdown(f"### 🏠 Domestic Event: **{st.session_state['event_title']}**")
    st.markdown(f"{st.session_state['event_description']}")

    st.markdown("---")
    
    # Policy Recommendations in an expander
    with st.expander("📂 View Policy Recommendations from Domestic Event"):
        st.markdown("""
        Based on the domestic event that has occurred, these are **some of the many factors** that are relevant for your nation's AI development.
        """)

        # Extract parameters from formulas
        delta_models_formula = st.session_state["event_delta_models_formula"]
        delta_papers_formula = st.session_state["event_delta_papers_formula"]

        # Use regex to find all words that are potential parameters
        parameters_in_formulas = set(re.findall(r'\b[A-Za-z_]+\b', delta_models_formula + delta_papers_formula))

        # Filter out common Python keywords or non-parameter words that might appear in formulas
        ignored_keywords = {'if', 'else', 'round', 'log', 'exp', 'min', 'max', 'int', 'np', 'sqrt', 'True', 'False', 'and', 'or', 'not'}
        
        relevant_parameters = []
        for param in parameters_in_formulas:
            if param in config.parameter_descriptions and param not in ignored_keywords:
                relevant_parameters.append(param)
            # Handle fixed_values parameters like Labor, Natural_Resource_Reserves, GDP if they appear
            elif param in config.fixed_values.get(team, {}) and param not in ignored_keywords:
                relevant_parameters.append(param)

        # Randomly pick two relevant parameters
        if len(relevant_parameters) > 2:
            selected_for_display = random.sample(relevant_parameters, 2)
        else:
            selected_for_display = relevant_parameters # Display all if 2 or fewer

        # =================================================================
        st.session_state.domestic_event_hints = selected_for_display
        # =================================================================

        if selected_for_display:
            for param_name in sorted(list(set(selected_for_display))): # Use set to avoid duplicates and sort for consistent display
                st.subheader(f"💡 {param_name}")
                if param_name in config.parameter_descriptions:
                    st.markdown(f"**Brief Description**: {config.parameter_descriptions[param_name]}")
                st.markdown("---")
        else:
            st.info("No specific policy recommendations could be derived from this event's formulas.")

    # Since there's no policy adjustment, directly proceed to international event display
    st.session_state.adjustment_confirmed = True


# --- 2. International Event ---
# This block now runs immediately after domestic event and policy recommendations are shown,
# because adjustment_confirmed is set to True.
if st.session_state.adjustment_confirmed:
    st.markdown("---")
    st.header("📍 International Event")
    st.markdown("A significant international event will now unfold, impacting global dynamics.")

    # if no interational event make a file.
    if "international_events_1_circumstance" not in st.session_state: # Use a different key to avoid conflict with 4_Events
        event_file = config.shared_dir / "international.json" # Use a different file name

        # 1. check
        if os.path.exists(event_file):
            # if exists you are not the one that triggered
            with open(event_file, "r") as f:
                chosen_events = json.load(f)
                st.write("You were not the one that triggered this event. Other team was first to trigger it...Try faster next time!")

        # 2. if not exist
        else:
            chosen_events = random.sample(config.international_events, 1) # Only one international event
            with open(event_file, "w") as f:
                json.dump(chosen_events, f)
            st.write("Your team was the first to trigger the international event for this round!")

        # save.
        st.session_state["international_events_1_circumstance"] = chosen_events


    with st.expander("🗺️ View International Event", expanded=True):
        if "international_events_1_circumstance" in st.session_state:
            for i, event in enumerate(st.session_state.international_events_1_circumstance, 1):
                st.markdown(f"#### 💥 Event {i}: {event['title']}\n\n{event['description']}")
        else:
            st.warning("International event is being determined...")


    if st.button("➡️ Proceed to Policy Phase"):
        st.switch_page("pages/2_Policy.py") # Direct to Policy page