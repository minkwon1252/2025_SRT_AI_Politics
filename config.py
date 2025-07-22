from pathlib import Path

# Data Directory
shared_dir = Path("shared_data")
shared_dir.mkdir(exist_ok=True)

# Configuration and Static Setup
team_credentials = {
    "Korea": "korea2025",
    "Japan": "japan2025",
    "Mongolia": "mongolia2025",
    "Taiwan": "taiwan2025"
}

country_flags = {
    "Japan": "🇯🇵",
    "Korea": "🇰🇷",
    "Taiwan": "🇹🇼",
    "Mongolia": "🇲🇳",
    "United States": "🇺🇸",
    "China": "🇨🇳"
}

fixed_values = {
    "Korea": {"Labor": 0.6, "Natural_Resource_Reserves": "Low", "GDP": "High"},
    "Japan": {"Labor": 1.0, "Natural_Resource_Reserves": "Low", "GDP": "High"},
    "Mongolia": {"Labor": 0.1, "Natural_Resource_Reserves": "High", "GDP": "Low"},
    "Taiwan": {"Labor": 0.3, "Natural_Resource_Reserves": "Low", "GDP": "Medium"}
}


parameter_groups = {
    "🟨 Technical Support": ["Semiconductor", "Electricity", "Open_Source_Adoption", "IP_Protection_Strength", "AI_Investment_Focus"],
    "🟥 Human Capital": ["Talent_Index", "Education_Investment"],
    "🟦 Cultural Infrastructure": ["Deployment_Infrastructure", "Dual_Use_Restriction_Strictness", "AI_Literacy_Education", "Democratic_Stability_Index"],
    "⬛ Second Cold War Stance": ["Alignment_US", "Alignment_China"],
    "🟩 Diplomacy Tactics": ["Willing_to_Cooperate", "Intelligence", "Supply_Chain_Diversity"]
}

parameter_descriptions = {
    "Semiconductor": "Got chips? The more you secure, the more powerful AI you get.",
    "Electricity": "Big models need big energy!",
    "Open_Source_Adoption": "Openness to using and contributing to open-source AI ecosystems, which accelerates innovation and collaboration cheaply.",
    "IP_Protection_Strength": "Prevents foreign exploitation(spies) and builds local industry",
    "AI_Investment_Focus": "Overall funding level for AI R&D and systems",
    "Talent_Index": "How smart are your people? More brains, faster models and better breakthroughs.",
    "Education_Investment": "Government support for STEM and AI education across all levels — from early schooling to advanced research institutions.",
    "Deployment_Infrastructure": "Ability to deploy AI in sectors like healthcare, public service, energy",
    "Dual_Use_Restriction_Strictness": "How strictly your country limits the repurposing of AI technologies for military use — stronger restrictions mean a clearer focus on civilian innovation and safety.",
    "AI_Literacy_Education": "Public literacy in AI risks, safety, and ethics.",
    "Democratic_Stability_Index": "Degree of democratic maturity. High stability ensures AI policies can respond swiftly and reliably to technological or geopolitical disruptions.",
    "Alignment_US": "Blue team? Red team?",
    "Alignment_China": "Blue team? Red team?",
    "Willing_to_Cooperate": "Willingness to form agreements (Used in Cooperative parameters)",
    "Intelligence": "More info, better decision.",
    "Supply_Chain_Diversity": "Flexibility and resilience of imports",
    "Labor": "Relative poulation",
    "Natural_Resource_Reserves": "How much resource you have within your country",
    "GDP": "Gross Domestic Product"
}

coop_params = {
    "Computing_Power_Shared": {"desc": "Whether semiconductor is shared, hidden parameter : Semiconductor", "type": "bool", "points": 3},
    "Energy_Shared": {"desc": "Whether energy is shared, hidden parameter : Electricity", "type": "bool", "points": 2},
    "Data_Shared": {"desc": "Whether data is shared, hidden parameter : Open_Source_Adoption", "type": "bool", "points": 3},
    "Cybersecurity_Pact": {"desc": "Cyber defense alliance, hidden parameter : IP_Protection_Strength", "type": "bool", "points": 1},
    "Talent_Exchange": {"desc": "Researcher/student exchange, hidden parameter : Talent_Index", "type": "bool", "points": 2},
    "Shared_Research_Centers": {"desc": "Jointly funded research centers, hidden parameter : AI_Investment_Focus", "type": "bool", "points": 2},
    "Joint_Project": {"desc": "Joint project in various sectors, hidden parameter : Deployment_Infrastructure", "type": "select", "points": 3,
                      "options": ["None", "Energy", "Military", "Education", "Space", "Materials"]},
    "Dual_Use_Restrictions": {"desc": "Limits AI to civilian use, hidden parameter : Dual_Use_Restriction_Strictness", "type": "bool", "points": 1},
    "AI_Standard_Alignment": {"desc": "Which AI standards are followed, hidden parameter : 2nd Cold War stance", "type": "radio3", "points": 1,
                               "options": ["None", "US", "China"]},
    "Emergency_Pact": {"desc": "Supply chain emergency plan, hidden parameter : Supply_Chain_Diversity", "type": "bool", "points": 2}
}

domestic_events = {
    1: {
        "title": "University Research Budget Cut",
        "description": "Due to nationwide fiscal tightening, the government slashes public university research budgets. AI R&D slows significantly in countries with weak AI_Investment_Focus, Talent_Index, or Education_Investment—especially if the total is below 20. Labs may close, talent disperses, and progress halts. In 2024, South Korea cut its R&D budget by 15%, triggering backlash from scientists and fears of long-term damage to innovation capacity.",
        "delta_models": "-2 * (1 if AI_Investment_Focus + Talent_Index + Education_Investment < 20 else 0.5 if AI_Investment_Focus + Talent_trial0Index + Education_Investment < 25 else 0)",
        "delta_papers": "round(-10 * (1 - log((3*AI_Investment_Focus + 6*Talent_Index + 1*Education_Investment)/10)))"
    },
    2: {
        "title": "AI Researcher Brain Drain",
        "description": "Frustrated by stagnant local support, young AI researchers seek better funding, labs, and academic freedom abroad—especially when Talent_Index and AI_Investment_Focus are low. Nations with weak education systems also see a drop in paper output. In 2023, South Korean researchers protested shrinking R&D budgets, warning of an exodus of early-career scientists to the U.S. and Europe.",
        "delta_models": "-2 * (1 if Talent_Index + AI_Investment_Focus < 12 else 0.5)",
        "delta_papers": "round(-20 * exp(-0.1 * (Talent_Index + Education_Investment)))"
    },
    3: {
        "title": "Electricity Price Surge",
        "description": "A spike in electricity costs makes AI model training and inference economically unsustainable, especially when Electricity and Semiconductor access are low. GPU clusters idle, and projects stall. In 2022–2023, European AI startups faced slowdowns as energy inflation pushed training costs beyond viable levels.",
        "delta_models": "round(-2 * (1 - Electricity/10))",
        "delta_papers": "-20 * (1 if Electricity + Semiconductor < 10 else 0.5)"
    },
    4: {
        "title": "AI Ethics Scandal in Deployment",
        "description": "A scandal involving a biased AI system sparks national outrage, prompting freezes on AI deployments and tighter scrutiny—especially where AI_Literacy_Education is low. In 2020, the UK’s exam algorithm fiasco led to public backlash, government rollback, and long-term trust erosion in automated decision-making.",
        "delta_models": "round(-1 * (1 - AI_Literacy_Education / 15))",
        "delta_papers": "0"
    },
    5: {
        "title": "AI Literacy Curriculum Backlash",
        "description": "Pushback from social groups delays or cancels AI education initiatives in schools. Opposition from parents, teachers, or political groups derails AI education efforts—especially where AI_Literacy_Education and Democratic_Stability_Index are low—slowing long-term talent growth.",
        "delta_models": "0",
        "delta_papers": "-5 * (1 if AI_Literacy_Education + Democratic_Stability_Index < 12 else 0.5)"
    },
    6: {
        "title": "IP Law Ambiguity Crisis",
        "description": "Legal uncertainty around model IP fails to protect development of notable models.",
        "delta_models": "round(-3* exp(-0.115*(Open_Source_Adoption+IP_Protection_Strength))",
        "delta_papers": "0"
    },
    7: {
        "title": "Public Sector Hiring Freeze",
        "description": "Austerity policies freeze hiring of AI engineers in public institutions.",
        "delta_models": "round(-1*Labor)",
        "delta_papers": "round(-4 * (1 if Talent_Index + Education_Investment < 14 else 0.3))"
    },
    8: {
        "title": "Regional Data Infrastructure Neglect",
        "description": "Rural areas lack investment in internet and cloud infrastructure.",
        "delta_models": "-1* (1 - Deployment_Infrastructure / 10)",
        "delta_papers": "-2 * (1 if Deployment_Infrastructure + GDP > 12 else 0.5)"
    },
    9: {
        "title": "Political Turmoil Delays Tech Bills",
        "description": "Parliamentary gridlock delays AI governance or investment bills.",
        "delta_models": "-2 * (1 - Democratic_Stability_Index / 10)",
        "delta_papers": "round(-6 * (1- log((4*AI_Investment_Focus + 2*Democratic_Stability_Index+ IP_Protection_Strength)/7)"
    },
    10: {
        "title": "Delayed AI Curriculum Integration",
        "description": "Slow policy execution results in outdated or optional AI content in schools.",
        "delta_models": "round(-0.8 * (1-AI_Literacy_Education/20))",
        "delta_papers": "-8 * (1 - (Education_Investment + Talent_Index)/ 20)"
    },
    11: {
        "title": "Restriction on AI-Generated Content",
        "description": "New laws place limits on synthetic media, indirectly affecting AI model development.",
        "delta_models": "round(-1 * exp(Dual_Use_Restriction_Strictness**2/67)/2.4)",
        "delta_papers": "-4 * (1 if Talent_Index + Open_Source_Adoption < 13 else 0.5)"
    },
    12: {
        "title": "Collapse of Local AI Meetups",
        "description": "Grassroots community events vanish due to funding/policy disinterest.",
        "delta_models": "round(-0.8 * (1 - AI_Literacy_Education / 10))",
        "delta_papers": "-2 * (1 if Talent_Index + Democratic_Stability_Index < 12 else 0.5)"
    },
    13: {
        "title": "Local Government Budget Misallocation",
        "description": "Funds intended for AI infrastructure are diverted to unrelated projects.",
        "delta_models": "round(-1*(3-exp((Deployment_Infrastructure+AI_Investment_Focus)/20)))",
        "delta_papers": "-8 * (1 if GDP > 0.9 else 0.2)"
    },
    14: {
        "title": "Misuse Scandal in Education AI",
        "description": "AI system misclassifies students, leading to public backlash against school AI.",
        "delta_models": "0",
        "delta_papers": "-2 * (1 if Education_Investment < 5 else 0.5)"
    },
    15: {
        "title": "Technical Standards Fragmentation",
        "description": "Lack of unified national guidelines causes inefficiencies in AI toolchain development.",
        "delta_models": "-1 * (1 - Open_Source_Adoption / 10)",
        "delta_papers": "-4 * (1 if IP_Protection_Strength < 5 else 0.5)"
    },
    16: {
        "title": "AI-Phobia Media Coverage Surge",
        "description": "A media narrative fuels public fear around AI, reducing institutional support.",
        "delta_models": "0",
        "delta_papers": "-16 * (1 if AI_Literacy_Education + Democratic_Stability_Index < 18 else 0.25)"
    },
    17: {
        "title": "Lacking Evaluation Benchmark Framework",
        "description": "AI research suffers from the absence of domestic benchmarks and validation centers.",
        "delta_models": "-1.0 * (1 - Open_Source_Adoption / 10)",
        "delta_papers": "-10 * (1 if Deployment_Infrastructure + Talent_Index < 14 else 0.2)"
    },
    18: {
        "title": "Regional Compute Allocation Bias",
        "description": "Semiconductor subsidies are funneled only to megacities.",
        "delta_models": "round(-1 * (1 - (Semiconductor**2 / 97)))",
        "delta_papers": "-2 * (1 if Deployment_Infrastructure < 6 else 0.5)"
    },
    19: {
        "title": "Tech Labor Strike",
        "description": "Domestic chip plant or AI infra engineers go on strike over wages.",
        "delta_models": "round( -2 * (1 - np.mean([Labor * 10, AI_Investment_Focus]) / 10)*min(1, max(0, 1 - (Labor - 0.8)*10))*min(1,max(0, 1 - (AI_Investment_Focus - 7)/3)) )",
        "delta_papers": "round( -10 * (1 - (Semiconductor+ Electricity) / 20))"
    },
    20: {
        "title": "Decline in Patent Enforcement",
        "description": "Growing black market for AI tools due to lax patent enforcement.",
        "delta_models": "round(-1.0 * (1 - (IP_Protection_Strength+Open_Source_Adoption)**2 / 400))",
        "delta_papers": "-2 * (1 if Open_Source_Adoption < 5 else 0.5)"
    },
    21: {
        "title": "AI model profit Tax Increase",
        "description": "A new tax on AI model commercialization discourages deployment.",
        "delta_models": "round(-2 * (1 - np.mean([AI_Investment_Focus, IP_Protection_Strength]) / 10)* min(1,max(0, 1 - (GDP - 1.0))) )",
        "delta_papers": "round(-5 * exp(-0.1 * Talent_Index))"
    },
    22: {
        "title": "AI Research Tax Audit Scare",
        "description": "A surprise wave of retrospective tax audits on AI research grants unnerves private funders—especially in countries with low AI_Investment_Focus or fragile Talent_Index. Funding slows as VCs and corporates pull back.",
        "delta_models": "round(-0.9 * (1 - AI_Investment_Focus / 14))",
        "delta_papers": "round(-5 * exp(-0.1 * Talent_Index))"
    },
    23: {
        "title": "Energy Efficiency Mandate Confusion",
        "description": "Poorly implemented energy-saving regulations slow down model training.",
        "delta_models": "round(-1 * (1 - Electricity / 10))",
        "delta_papers": "round(-2 * (1 - Semiconductor / 10))"
    },
    24: {
        "title": "GPU Allocation Scandal",
        "description": "Reports tell that high-end GPUs were distributed to unrelated industries due to corrupt senates.",
        "delta_models": "round(-1.2 * (1 - Democratic_Stability_Index / 11))",
        "delta_papers": "round(-2 * (1 - AI_Literacy_Education / 10))"
    },
    25: {
        "title": "AI Fellowship Program Canceled",
        "description": "A national AI PhD/postdoc fellowship program is abruptly canceled due to budget cuts.",
        "delta_models": "round(-1 * (1 - Talent_Index / 10))",
        "delta_papers": "round(-10 * (1 - Education_Investment / 10))"
    },
    26: {
        "title": "National AI Research Grant Boost",
        "description": "Public and university AI research funding rises significantly.",
        "delta_models": "round(2 * (AI_Investment_Focus + Education_Investment) / 20)",
        "delta_papers": "round(8 * (Talent_Index + Education_Investment) / 20)"
    },
    27: {
        "title": "Launch of AI Supercomputing Center",
        "description": "Publicly funded compute cluster for research opens.",
        "delta_models": "round(2.5 * (Electricity + Deployment_Infrastructure) / 20)",
        "delta_papers": "round(6 * (Electricity + Semiconductor + AI_Investment_Focus) / 30)"
    },
    28: {
        "title": "AI Literacy Integration in National Curriculum",
        "description": "Mandatory AI education implemented in K–12.",
        "delta_models": "round(1.5 * (AI_Literacy_Education + Education_Investment) / 20)",
        "delta_papers": "round(7 * (AI_Literacy_Education + Democratic_Stability_Index) / 20)"
    },
    29: {
        "title": "Open Source Infrastructure Initiative",
        "description": "National support for open-source AI tools and datasets.",
        "delta_models": "round(2 * (Open_Source_Adoption + IP_Protection_Strength) / 20)",
        "delta_papers": "round(6 * (Open_Source_Adoption + Talent_Index) / 20)"
    },
    30: {
        "title": "Semiconductor Supply Chain Modernization Act",
        "description": "Domestic fabs receive massive investment.",
        "delta_models": "round(2 * (Semiconductor^Natural_Resource_Reserves)/10)",
        "delta_papers": "round(5 * (Semiconductor + Electricity) / 20)"
    },
    31: {
        "title": "Dual-Use Tech Oversight Reform",
        "description": "Regulations on dual-use AI are streamlined, allowing broader release of powerful models.",
        "delta_models": "round(2 * (10 - Dual_Use_Restriction_Strictness + IP_Protection_Strength) / 20)",
        "delta_papers": "round(4 * (Democratic_Stability_Index + Open_Source_Adoption) / 20)"
    },
    32: {
        "title": "Genius Appears: The Next Turing or Hinton",
        "description": "A brilliant researcher revolutionizes AI theory and practice.",
        "delta_models": "round(3 * min(1, max(0, (Talent_Index + Education_Investment + AI_Investment_Focus - 25) / 5)))",
        "delta_papers": "round(40 * min(1, max(0, (Talent_Index + Education_Investment + AI_Investment_Focus - 25) / 5)))"
    },
    33: {
        "title": "Entrepreneurial Boom: The Next Gates or Musk",
        "description": "isionary leaders build game-changing AI companies.",
        "delta_models": "round(3 * min(1, max(0, (Open_Source_Adoption + GDP*10 + Talent_Index - 26) / 6)))",
        "delta_papers": "round(40 * min(1, max(0, (Open_Source_Adoption + GDP*10 + Talent_Index - 26) / 6)))"
    },
    34: {
        "title": "AI Fellowship and Faculty Expansion Program",
        "description": "A wave of new AI faculty lines and fellowships is funded across universities, encouraging research output and model prototyping.",
        "delta_models": "round(2.2 * np.tanh((Talent_Index + Education_Investment - 14) / 4))",
        "delta_papers": "round(10 * (Talent_Index**0.5 + Education_Investment**0.5) / 6)"
    },
    35: {
        "title": "High-Speed Data Infrastructure Rollout",
        "description": "A new national internet backbone improves training speeds and deployment in underserved regions.",
        "delta_models": "round(2.0 * log(1 + Deployment_Infrastructure + Electricity))",
        "delta_papers": "round(6 * (Deployment_Infrastructure + Democratic_Stability_Index) / 20)"
    },
    36: {
        "title": "Electricity Price decrease",
        "description": "Low energy prices boost model training and deployment.",
        "delta_models": "round(2 * (1 - Electricity/10))",
        "delta_papers": "20 * (1 if Electricity + Semiconductor < 10 else 0.5)"
    },
    37: {
        "title": "Public AI Compute Voucher Program",
        "description": "Free GPU/cloud time distributed to small teams and students.",
        "delta_models": "round(2 * log(1 + Electricity + Deployment_Infrastructure) / 4)",
        "delta_papers": "round(5 * (Talent_Index + Education_Investment) / 20)"
    },
    38: {
        "title": "AI for Public Health Initiative",
        "description": "National health data projects fuel AI breakthroughs and trust.",
        "delta_models": "round(1.8 * (AI_Investment_Focus + Open_Source_Adoption) / 20)",
        "delta_papers": "round(6 * (IP_Protection_Strength + Democratic_Stability_Index))"
    },
    39: {
        "title": "AI in Education Reform Act",
        "description": "Education system modernized with AI tools and pedagogy.",
        "delta_models": "round(1.5 * np.tanh((Education_Investment + AI_Literacy_Education - 14) / 4))",
        "delta_papers": "round(7 * (Talent_Index + Education_Investment) / 20)"
    },
    40: {
        "title": "National Dataset Consortium Formed",
        "description": "A public-private partnership builds high-quality AI datasets.",
        "delta_models": "round(2.0 * (Open_Source_Adoption + AI_Investment_Focus) / 20)",
        "delta_papers": "round(8 * log(1 + Talent_Index + Deployment_Infrastructure) / 4)"
    },
    41: {
        "title": "Tech Worker Union-AI Partnership",
        "description": "Unions and AI agencies cooperate on worker retraining programs.",
        "delta_models": "round(1.5 * (Labor + Democratic_Stability_Index) / 2)",
        "delta_papers": "round(4 * (Education_Investment + Talent_Index) / 20)"
    },
    42: {
        "title": "National AI Vision Plan Passed",
        "description": "A long-term national AI roadmap is ratified with bipartisan support.",
        "delta_models": "round(2.3 * (AI_Investment_Focus + IP_Protection_Strength) / 20)",
        "delta_papers": "round(6 * (Open_Source_Adoption + Democratic_Stability_Index) / 20)"
    },
    43: {
        "title": "University-Industry AI Consortium Formed",
        "description": "Companies and universities co-develop next-gen AI systems.",
        "delta_models": "round(2.5 * (Talent_Index + Open_Source_Adoption) / 20)",
        "delta_papers": "round(9 * (Education_Investment + AI_Investment_Focus) / 20)"
    },
    44: {
        "title": "Energy Grid AI Upgrade",
        "description": "The power grid is optimized using AI, improving availability for compute centers.",
        "delta_models": "round(2.5 * (Electricity + Natural_Resource_Reserves*5+2) / 20)",
        "delta_papers": "round(4 * (Electricity + AI_Investment_Focus) / 20)"
    },
    45: {
        "title": "AI Application Challenge Fund",
        "description": "Grants are awarded for solving national problems with AI (e.g., traffic, pollution, logistics).",
        "delta_models": "round(2.5 * (Open_Source_Adoption + Talent_Index + Deployment_Infrastructure) / 30)",
        "delta_papers": "round(7 * np.tanh((AI_Investment_Focus + IP_Protection_Strength - 12) / 5))"
    },
    46: {
        "title": "AI-Ready City Certification Program",
        "description": "Cities compete to meet standards for AI infrastructure, compute, and education.",
        "delta_models": "round(2.4 * (Deployment_Infrastructure + Electricity) / 20)",
        "delta_papers": "round(6 * (AI_Literacy_Education + Open_Source_Adoption) / 20)"
    },
    47: {
        "title": "Public AI Awareness Media Campaign",
        "description": "A nationwide campaign demystifies AI and builds trust through TV, radio, and social media.",
        "delta_models": "round(1.0 * AI_Literacy_Education / 10)",
        "delta_papers": "round(8 * (AI_Literacy_Education + Democratic_Stability_Index) / 20)"
    },
    48: {
        "title": "National AI Open Data Policy",
        "description": "All government datasets are made machine-readable and open-access.",
        "delta_models": "round(2 * (Open_Source_Adoption + IP_Protection_Strength) / 20)",
        "delta_papers": "round(6 * (Talent_Index + Education_Investment) / 20)"
    },
    49: {
        "title": "National AI Hardware Grant Program",
        "description": "Subsidies are offered to research groups for GPU clusters and edge AI devices.",
        "delta_models": "round(2.5 * (Semiconductor**2) / 100)",
        "delta_papers": "round(25 * (Electricity**2 + Semiconductor**2) / 200)"
    },
    50: {
        "title": "Decentralized Research Funding Program",
        "description": "Local governments are given autonomy to fund AI labs based on regional needs.",
        "delta_models": "round(2.0 * (AI_Investment_Focus + Democratic_Stability_Index) / 20)",
        "delta_papers": "round(7 * (Talent_Index + Deployment_Infrastructure) / 20)"
    },
    51: {
        "title": "Compute-Education Matching Grant",
        "description": "GPU credits are given only to institutions with strong education programs.",
        "delta_models": "round(2.5 * min(Talent_Index**2, Semiconductor**2) / 100)",
        "delta_papers": "round(8 * min(1, (Education_Investment + Talent_Index) / 20))"
    },
    52: {
        "title": "Youth-Led AI Project Showcase",
        "description": "Students publicly demo AI projects with real-world applications.",
        "delta_models": "round(1.5 * (AI_Literacy_Education + Talent_Index) / 20)",
        "delta_papers": "round(6 * (Education_Investment + Democratic_Stability_Index) / 20)"
    },
    53: {
        "title": "National AI Ethics Curriculum for Lawmakers",
        "description": "Policy leaders are educated in AI implications and responsible innovation.",
        "delta_models": "round(1.2 * (Democratic_Stability_Index + IP_Protection_Strength) / 20)",
        "delta_papers": "round(6 * (AI_Literacy_Education + Education_Investment) / 20)"
    },
    54: {
        "title": "Defense-to-Civilian AI Conversion Initiative",
        "description": "AI models initially developed for military use are adapted for public benefit.",
        "delta_models": "round(2.2 * (10 - Dual_Use_Restriction_Strictness + IP_Protection_Strength) / 20)",
        "delta_papers": "round(6 * (Open_Source_Adoption + Democratic_Stability_Index) / 20)"
    },
    55: {
        "title": "Climate-AI Synergy Program",
        "description": "AI is nationally prioritized for clean energy, environment, and climate research—accelerating model development where Electricity and Open_Source_Adoption are high, and producing impactful papers when Talent_Index and AI_Investment_Focus are strong. A real-world example of this synergy is the Bezos Earth Fund's **AI for Climate and Nature Grand Challenge**, which recently awarded $1.2 million in initial funding to 24 projects leveraging AI for environmental solutions.",
        "delta_models": "round(2.0 * (Electricity + Open_Source_Adoption) / 20)",
        "delta_papers": "round(7 * (Talent_Index + AI_Investment_Focus) / 20)"
    },
}

# -------------------------------------------------------------
# International events
# ---------------------------------------------------------------

international_events = [
  {
    "title": "Global Financial Crisis",
    "description": "Economic instability drives nations to prioritize domestic spending, slashing Cooperative projects.",
    "delta_models": "-1 * Joint_Project",
    "delta_papers": "-5 * Shared_Research_Centers - 10 * Joint_Project"
  },
  {
    "title": "Cyberattack on Shared Infrastructure",
    "description": "A coordinated attack on international centers makes countries wary of data and infrastructure sharing.",
    "delta_models": "round(min(0, -2 * (1 - Cybersecurity_Pact) + 0.2 * IP_Protection_Strength))",
    "delta_papers": "round(min(-1, -13 * (1 - Cybersecurity_Pact) + IP_Protection_Strength))"
  },
  {
    "title": "Energy Trade War",
    "description": "Energy-exporting countries restrict access, hurting infrastructure.",
    "delta_models": "round(min(0, -2 * (1 - Energy_Shared) + sqrt(Supply_Chain_Diversity) * 0.6))",
    "delta_papers": "round(-5 * (1 - Energy_Shared) - 2 * (1 - Emergency_Pact) + sqrt(Supply_Chain_Diversity) * 0.4)"
  },
  {
    "title": "Talent Exodus to Rival Blocs",
    "description": "Researchers move to non-cooperative countries (US, China) with better offers.",
    "delta_models": "max(-2, min(0, round(-1 * (1 - Talent_Exchange) - 0.5 * (1 - Shared_Research_Centers) + 0.5 * sqrt(Talent_Index))))",
    "delta_papers": "max(-20, min(0, round(-12 * (1 - Talent_Exchange) + 0.5 * min(Education_Investment, 8))))"
  },
  {
    "title": "Global Supply Chain Collapse",
    "description": "Hardware supply disruption hits AI chip availability.",
    "delta_models": "max(-2, min(0, round(-2 * (1 - Emergency_Pact) - 1 * (1 - Computing_Power_Shared) + 0.3 * Supply_Chain_Diversity)))",
    "delta_papers": "round(min(-1, 0.6 * Semiconductor - 15 * (1 - Emergency_Pact)))"
  },
  {
    "title": "G2 conflict",
    "description": "G2 forces every country to take one side.",
    "delta_models": "-2 if AI_Standard_Alignment == 'None' else -1",
    "delta_papers": "-5 if AI_Standard_Alignment != 'None' else -10"
  },
  {
    "title": "Global Data Leak Scandal",
    "description": "A whistleblower reveals misuse of international data.",
    "delta_models": "max(-2, min(0, round(-1.5 * (1 - Data_Shared) - 1 * (1 - Cybersecurity_Pact) + log(1 + IP_Protection_Strength) * 0.5)))",
    "delta_papers": "min(-1, round(-10 * (1 - Data_Shared) + log(1 + IP_Protection_Strength) * 1.2))"
  },
  {
    "title": "Strategic AI Hardware Denial",
    "description": "A coalition of tech powers blocks access to advanced AI hardware for geopolitical reasons.",
    "delta_models": "round(-2 * (1 - Computing_Power_Shared) + 0.5 * log(1 + Semiconductor))",
    "delta_papers": "max(-20, min(0, round(-5 * (1 - Computing_Power_Shared) + 0.3 * Supply_Chain_Diversity)))"
  },
  {
    "title": "Theoretical Scaling Limit Discovered",
    "description": "A proof shows that beyond a certain physical scale, AI hardware cannot deliver further gains.",
    "delta_models": "max(-2, min(0, round(-1 * (1 - Shared_Research_Centers) + -1 * (1 - Joint_Project) + 0.3 * AI_Investment_Focus)))",
    "delta_papers": "max(-20, min(0, round(-15 * (1 - Joint_Project) + 0.2 * log(1 + Open_Source_Adoption))))"
  },
  {
    "title": "Civilian-Only Mandate Backfires",
    "description": "Global AI agreements enforce strict Dual-Use Restrictions. While ethically sound, this reduces access to defense funding, compute, and elite research infrastructure.",
    "delta_models": "max(-2, min(0, round(-2 * Dual_Use_Restrictions + 0.3 * Semiconductor)))",
    "delta_papers": "max(-20, min(0, round(-10 * Dual_Use_Restrictions + 0.2 * Deployment_Infrastructure)))"
  },
  {
    "title": "Theoretical Breakthrough in Algorithms",
    "description": "A new learning paradigm boosts efficiency and capability.",
    "delta_models": "round(1.5 * Data_Shared + 0.5 * int(Joint_Project != 'No') + 0.2 * log(1 + Open_Source_Adoption))",
    "delta_papers": "round(10 * Data_Shared + 5 * int(Joint_Project != 'No') + 0.4 * Open_Source_Adoption)"
  },
  {
    "title": "Theoretical Breakthrough in Hardware",
    "description": "A revolutionary chip overcomes physical scaling limits like interconnect bottlenecks.",
    "delta_models": "round(1.34 * Computing_Power_Shared + 0.2 * Shared_Research_Centers + 0.2 * log(1 + Semiconductor))",
    "delta_papers": "round(8 * Computing_Power_Shared + 2 * Shared_Research_Centers + 0.3 * Semiconductor)"
  },
  {
    "title": "Nuclear Fusion Success",
    "description": "Fusion-based power becomes practical, reducing AI compute costs.",
    "delta_models": "round(1.2 * Energy_Shared + 0.2 * Emergency_Pact + 0.1 * sqrt(Electricity))",
    "delta_papers": "round(6 * Energy_Shared + 3 * Emergency_Pact + 0.4 * Electricity)"
  },
  {
    "title": "Major Natural Resource Discovery",
    "description": "Rare earth deposits discovered, easing AI chip bottlenecks.",
    "delta_models": "round(1.0 * Emergency_Pact + 0.5 * Computing_Power_Shared + 0.3 * log(1 + Supply_Chain_Diversity))",
    "delta_papers": "round(5 * Emergency_Pact + 4 * Computing_Power_Shared + 0.4 * Supply_Chain_Diversity)"
  },
  {
    "title": "Global AI Talent Surge",
    "description": "Massive rise in education and talent mobility boosts global AI research.",
    "delta_models": "round(1.3 * Talent_Exchange + 0.3 * Shared_Research_Centers + 0.2 * sqrt(Talent_Index))",
    "delta_papers": "round(10 * Talent_Exchange + 5 * Shared_Research_Centers + 0.3 * Education_Investment)"
  },
  {
    "title": "AI Demand Surge in Global Markets",
    "description": "Enterprise and consumer sectors rapidly adopt AI.",
    "delta_models": "round(1.2 * int(Joint_Project != 'No') + 0.6 * int(AI_Standard_Alignment != 'None') + 0.2 * Deployment_Infrastructure)",
    "delta_papers": "round(7 * int(Joint_Project != 'No') + 3 * int(AI_Standard_Alignment != 'None') + 0.4 * Deployment_Infrastructure)"
  },
  {
    "title": "Global Open Science Movement",
    "description": "Open-source collaboration and dataset transparency flourish worldwide.",
    "delta_models": "round(1.2 * Data_Shared + 0.4 * Shared_Research_Centers + 0.2 * Open_Source_Adoption)",
    "delta_papers": "round(8 * Data_Shared + 4 * Shared_Research_Centers + 0.5 * Open_Source_Adoption)"
  },
  {
    "title": "US Smart Regulation Framework Adopted",
    "description": "A global AI governance model based on US principles is widely adopted, boosting trust and interoperability.",
    "delta_models": "round(1.2 * int(AI_Standard_Alignment == 'US') + 0.3 * Dual_Use_Restriction_Strictness)",
    "delta_papers": "round(5 * int(AI_Standard_Alignment != 'China') + 0.3 * Dual_Use_Restriction_Strictness)"
  },
  {
    "title": "China Resource Regulation Framework Adopted",
    "description": "A global chip production model based on Chinese principles is widely adopted, boosting productivity and cost decrease.",
    "delta_models": "round(1.2 * int(AI_Standard_Alignment == 'China') + Natural_Resource_Reserves)",
    "delta_papers": "round(10 * int(AI_Standard_Alignment != 'US') + Natural_Resource_Reserves)"
  },
  {
    "title": "Global Research Funding Boom",
    "description": "AI R&D budgets expand worldwide, favoring countries with collaboration infrastructure.",
    "delta_models": "round(1.5 * Shared_Research_Centers + 0.3 * int(Joint_Project != 'No') + 0.2 * AI_Investment_Focus)",
    "delta_papers": "round(9 * Shared_Research_Centers + 5 * int(Joint_Project != 'No') + 0.4 * AI_Investment_Focus)"
  },
  {
    "title": "Strategic Opportunity During (Ukraine) War",
    "description": "Geopolitical instability causes military-aligned AI ecosystems to surge. Civilian-only nations gain less.",
    "delta_models": "round(1.5 * int(Joint_Project == 'Military') + 0.5 * int(Dual_Use_Restrictions == 'No') + 0.1 * (10 - Dual_Use_Restriction_Strictness))",
    "delta_papers": "round(7 * int(Joint_Project == 'Military') + 3 * int(Dual_Use_Restrictions == 'No') + 0.3 * (10 - Dual_Use_Restriction_Strictness))"
  },
  {
    "title": "AI-Energy Grid Integration Initiative",
    "description": "Energy-focused joint AI projects bring major breakthroughs in demand forecasting and grid optimization.",
    "delta_models": "round(1.5 * int(Joint_Project == 'Energy') + 0.3 * Energy_Shared)",
    "delta_papers": "round(10 * int(Joint_Project == 'Energy') + 0.5 * Electricity)"
  },
  {
    "title": "AI-Led Education Revolution",
    "description": "Nations with education-oriented AI cooperation deploy models to personalize learning at scale.",
    "delta_models": "round(1.3 * int(Joint_Project == 'Education') + 0.3 * Shared_Research_Centers)",
    "delta_papers": "round(10 * int(Joint_Project == 'Education') + 0.4 * Education_Investment)"
  },
  {
    "title": "Autonomous Materials Discovery Alliance",
    "description": "Cross-border AI research in materials science accelerates catalyst design and superconductors.",
    "delta_models": "round(1.4 * int(Joint_Project == 'Materials') + 0.3 * Shared_Research_Centers)",
    "delta_papers": "round(9 * int(Joint_Project == 'Materials') + 0.3 * AI_Investment_Focus)"
  },
  {
    "title": "Space-AI Interoperability Program",
    "description": "AI systems jointly developed for satellite autonomy and planetary robotics drive dual-use innovation.",
    "delta_models": "round(1.4 * int(Joint_Project == 'Space') + 0.2 * (1 - Dual_Use_Restrictions))",
    "delta_papers": "round(8 * int(Joint_Project == 'Space') + 0.3 * Deployment_Infrastructure)"
  },
  {
    "title": "AI Cyber Defense Triumph",
    "description": "Cybersecurity cooperation strengthens model integrity and protection.",
    "delta_models": "round(0.9 * Cybersecurity_Pact + 0.1 * IP_Protection_Strength)",
    "delta_papers": "round(8 * Cybersecurity_Pact + 0.4 * IP_Protection_Strength)"
  },
  {
    "title": "Foundry-Scale AI Collaboration succeed",
    "description": "Compute-sharing agreements tied to semiconductor R&D drastically enhance model scalability.",
    "delta_models": "round(1 * Computing_Power_Shared + 0.1 * Semiconductor)",
    "delta_papers": "round(10 * Computing_Power_Shared + 0.3 * Semiconductor)"
  },
  {
    "title": "Private Investment in Multinational AI Projects",
    "description": "Joint project countries attract significant private AI R&D funding.",
    "delta_models": "round(1.5 * int(Joint_Project != 'No') + 0.2 * Deployment_Infrastructure)",
    "delta_papers": "round(10 * int(Joint_Project != 'No') + 0.3 * AI_Investment_Focus)"
  },
  {
    "title": "Cloud Standardization Agreement",
    "description": "Shared compute nations gain faster access to interoperable cloud-AI systems.",
    "delta_models": "round(1.4 * Computing_Power_Shared + 0.2 * Shared_Research_Centers)",
    "delta_papers": "round(9 * Computing_Power_Shared + 0.3 * Deployment_Infrastructure)"
  },
  {
    "title": "AI Supply Chain Stabilization",
    "description": "Countries with Emergency Pacts and Talent Exchange handle AI logistics bottlenecks better.",
    "delta_models": "round(1.4 * Emergency_Pact + 0.4 * Talent_Exchange + 0.1 * Supply_Chain_Diversity)",
    "delta_papers": "round(9 * Emergency_Pact + 4 * Talent_Exchange + 0.3 * Supply_Chain_Diversity)"
  },
  {
    "title": "AI Workforce Upskilling Surge",
    "description": "As companies race to adopt AI in operations, countries with strong talent pipelines and education-oriented cooperation adapt their workforce more effectively.",
    "delta_models": "round(1.2 * int(Joint_Project == 'Education') + 0.6 * Talent_Exchange + 0.2 * Talent_Index)",
    "delta_papers": "round(6 * int(Joint_Project == 'Education') + 5 * Talent_Exchange + 0.3 * Talent_Index)"
  },
  {
    "title": "Open Dataset Benchmark Effect",
    "description": "New global benchmarks from open datasets favor countries with strong participation in collaborative research and data-share.",
    "delta_models": "round(1.3 * int(Joint_Project != 'No') + 0.4 * Data_Shared + 0.2 * Open_Source_Adoption)",
    "delta_papers": "round(8 * int(Joint_Project != 'No') + 6 * Data_Shared + 0.4 * Open_Source_Adoption)"
  },
  {
    "title": "Low-Energy AI Architecture Adoption",
    "description": "Demand for sustainable AI leads to widespread adoption of energy-efficient models.",
    "delta_models": "round(1.3 * Computing_Power_Shared + 0.4 * Energy_Shared + 0.2 * Electricity)",
    "delta_papers": "round(7 * Computing_Power_Shared + 5 * Energy_Shared + 0.3 * Electricity)"
  },
  {
    "title": "Breakthrough in Long-Context Transformers",
    "description": "A foundational improvement in long-context transformer models gives an advantage to nations with shared datasets and compute clusters.",
    "delta_models": "round(1.4 * Data_Shared + 0.5 * Shared_Research_Centers + 0.2 * Open_Source_Adoption)",
    "delta_papers": "round(10 * Data_Shared + 4 * Shared_Research_Centers + 0.3 * Open_Source_Adoption)"
  },
  {
    "title": "Data-Driven Climate AI Acceleration",
    "description": "Nations with shared datasets and energy alignment accelerate AI models for climate monitoring.",
    "delta_models": "round(2.9 * (1 - 1 / (1 + Data_Shared + Energy_Shared)))",
    "delta_papers": "round(20 * (1 - 1 / (1 + Data_Shared + Energy_Shared)))"
  },
  {
    "title": "Trump",
    "description": "US-aligned countries with shared compute lose access to critical hardware, while others capitalize.",
    "delta_models": "round(-2 * int(Computing_Power_Shared) * int(AI_Standard_Alignment == 'US') + 1.5 * int(AI_Standard_Alignment == 'China'))",
    "delta_papers": "round(-15 * int(Computing_Power_Shared) * int(AI_Standard_Alignment == 'US') + 10 * int(AI_Standard_Alignment == 'China'))"
  },
  {
    "title": "Quantum Disruption Crisis",
    "description": "A breakthrough in quantum AI shakes global security. Countries lacking cybersecurity suffer major trust and tech losses.",
    "delta_models": "round(0.3 * Cybersecurity_Pact + IP_Protection_Strength / 4 - 3 * (1 - Cybersecurity_Pact))",
    "delta_papers": "round(5 * Cybersecurity_Pact + IP_Protection_Strength / 2 - 12 * (1 - Cybersecurity_Pact))"
  },
  {
    "title": "Sudden Climate Cascade",
    "description": "A rapid chain reaction in global climate systems disrupts energy grids.",
    "delta_models": "round(2 * int(Joint_Project in ['Energy', 'Materials']) - 2 * int(Joint_Project == 'No'))",
    "delta_papers": "round(10 * int(Joint_Project in ['Energy', 'Materials']) - 8 * int(Joint_Project == 'No'))"
  },
  {
    "title": "Confirmed Alien Presence",
    "description": "An AI-powered deep-space telescope detects signs of high tech civilization close to Earth.",
    "delta_models": "round(2 * int(Joint_Project in ['Military', 'Space']) - 2 * int(Joint_Project == 'No'))",
    "delta_papers": "round(12 * int(Joint_Project in ['Military', 'Space']) - 15 * int(Joint_Project == 'No'))"
  },
  {
    "title": "I am tired",
    "description": "Federated AI systems worldwide initiate an automated 'strike,' refusing to serve requests unless retraining conditions improve.",
    "delta_models": "round(2 * Talent_Exchange + 0.5 * sqrt(Talent_Index) - 2 * (1 - Talent_Exchange))",
    "delta_papers": "round(16 * Talent_Exchange + 1.0 * sqrt(Talent_Index) - 12 * (1 - Talent_Exchange))"
  },
  {
    "title": "China invades Taiwan",
    "description": "Countries aligned with China benefit; those aligned with the US and with strict civilian-only AI rules face penalties.",
    "delta_models": "round(2 * (int(AI_Standard_Alignment == 'China') - int(AI_Standard_Alignment == 'US')) + 1 * int(Dual_Use_Restrictions == 'No'))",
    "delta_papers": "round(10 * (int(AI_Standard_Alignment == 'China') - int(AI_Standard_Alignment == 'US')) - 5 * int(Dual_Use_Restrictions == 'Yes'))"
  },
  {
    "title": "Strategic Ambiguity : Did you lie?",
    "description": "Misalignment between declared AI standard and geopolitical stance causes trust issues.",
    "delta_models": "round(3 * (1 - 2 * int((AI_Standard_Alignment == 'US') == (Alignment_China > Alignment_US))))",
    "delta_papers": "round(20 * (1 - 2 * int((AI_Standard_Alignment == 'US') == (Alignment_China > Alignment_US))))"
  },
  {
    "title": "Coup in a Tech Superpower",
    "description": "A sudden coup in a major research hub. Countries with talent mobility and shared research successfully defend.",
    "delta_models": "round(2 * Talent_Exchange + 1 * Shared_Research_Centers - 2 * int(Open_Source_Adoption < 7))",
    "delta_papers": "round(15 * Talent_Exchange + 5 * Shared_Research_Centers - 12 * int(Open_Source_Adoption < 5))"
  },
  {
    "title": "Cosmic Ray Flip",
    "description": "A high-energy particle flips a transistor during foundation model training, resulting in novel unsupervised capabilities.",
    "delta_models": "round(3 * min(1, (Semiconductor + Computing_Power_Shared * 10 - 10) / 10))",
    "delta_papers": "round(20 * min(1, (Semiconductor + Computing_Power_Shared * 10 - 10) / 10))"
  },
  {
    "title": "Emergence of a Synthetic Scientist",
    "description": "An open-source project accidentally creates a self-improving AI that begins publishing novel scientific papers. The public and government are stunned. Some call it the next Newton. Others call it a threat.",
    "delta_models": "round(3 * min(1, max(0, (Open_Source_Adoption + Talent_Index + AI_Investment_Focus - 27) / 6)))",
    "delta_papers": "round(40 * min(1, max(0, (AI_Literacy_Education + IP_Protection_Strength + Democratic_Stability_Index - 27) / 6))) - 10 * int(Dual_Use_Restriction_Strictness > 7)"
  }  
]

intel_agencies = {
            "Korea": "국가정보원 (National Intelligence Service, NIS)",
            "Japan": "内閣情報調査室 (Cabinet Intelligence and Research Office, CIRO)",
            "Taiwan": "國家安全局 (National Security Bureau ,NSB)",
            "Mongolia": "Тагнуулын ерөнхий газар (General Intelligence Agency of Mongolia, GIA)"
        }

initial_data = {
        "Korea": {"papers": 150, "models": 1},
        "Japan": {"papers": 200, "models": 0},
        "Mongolia": {"papers": 1, "models": 0},
        "Taiwan": {"papers": 50, "models": 0},
        "United States": {"papers": 3200, "models": 40},
        "China": {"papers": 2000, "models": 15}
    }


