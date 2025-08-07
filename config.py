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
    "🟨 Technical Support": ["Semiconductor", "Electricity", "Open_Source_Adoption", "IP_Protection_Strength", "AI_Fund"],
    "🟥 Human Capital": ["Talent_Index", "Education_Investment"],
    "🟦 Cultural Infrastructure": ["Deployment_Infrastructure", "Dual_Use_Restriction_Strictness", "AI_Literacy_Education", "Democratic_Stability_Index"],
    "⬛ Second Cold War Stance": ["Alignment_US", "Alignment_China"],
    "🟩 Diplomacy Tactics": ["Willing_to_Cooperate", "Intelligence", "Supply_Chain_Diversity"]
}

# Parameter_insights for policy input : Brief descriptions for each parameter

parameter_descriptions = {
    "Semiconductor": "Got chips? The more you secure, the more powerful AI you get.",
    "Electricity": "Big models need big energy!",
    "Open_Source_Adoption": "Openness to using and contributing to open-source AI ecosystems, which accelerates innovation and collaboration cheaply.",
    "IP_Protection_Strength": "Prevents foreign exploitation(spies) and builds local industry",
    "AI_Fund": "Overall funding level for AI R&D and systems",
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

# Parameter_insights for policy input : More detailed descriptions for each parameter

parameter_insights = {
    "Semiconductor": """
    **Semiconductors** are the core of high-performance chips like GPUs and TPUs, which act as the brain of AI models. Investment in this area directly boosts computational speed, enabling faster training of larger and more complex models. This makes semiconductors one of the most critical infrastructure technologies underpinning AI research and commercialization.
    """,
    "Electricity": """
    **Electricity** is the lifeblood of modern AI. Data centers that train and operate cutting-edge AI models like large language models (LLMs) consume vast amounts of power. A stable and affordable energy supply is a key factor in ensuring the sustainability of a nation's AI capabilities.
    """,
    "Open_Source_Adoption": """
    **Open Source Adoption** reflects how actively a country leverages and contributes to open AI models, datasets, and tools—like Meta’s LLaMA or Google’s Gemma. High adoption enables rapid catch-up with frontier technologies, even with limited internal capabilities, and accelerates innovation through global collaboration.
    """,
    "AI_Fund": """
    **AI Fund** measures how much funding is being directed—by both government and private sector—into AI R&D and infrastructure. It directly shapes the scale and quality of the AI talent pool, computing resources, and startup ecosystem, acting as the engine of a country’s AI progress.
    """,
    "Talent_Index": """
    **Talent Index** indicates the quality and quantity of AI researchers, developers, and data scientists a country possesses. Talented individuals publish influential papers, build powerful AI models, and solve technical challenges. Ultimately, the AI race is often called a “war for talent.”
    """,
    "Education_Investment": """
    **Education Investment** is a long-term commitment to cultivating future AI talent. It encompasses STEM education in primary and secondary schools, AI-focused university departments, and support for advanced research institutions. While not immediately impactful, it determines the nation’s sustained AI development potential.
    """,
    "AI_Literacy_Education": """
    **AI Literacy Education** helps the general public understand AI technologies and their ethical and societal implications. It boosts public receptiveness to AI, facilitates smooth adoption, and builds social resilience against downsides like misinformation or misuse of technology.
    """,
    "Democratic_Stability_Index": """
    **Democratic Stability Index** reflects consistency in policy and social trust. Stable governments can implement long-term AI strategies and respond predictably to technological or geopolitical changes—making them attractive to foreign investors and skilled workers.
    """,
    # --- Parameters not directly used in the growth formula ---
    "IP_Protection_Strength": """
    **Intellectual Property (IP) Protection Strength** indicates how strongly intangible assets like AI technologies are safeguarded. Strong protection encourages investment in R&D, but overly strict IP laws may hinder collaboration and slow innovation.
    """,
    "Deployment_Infrastructure": """
    **Deployment Infrastructure** refers to the readiness of real-world systems—like cloud computing and 5G networks—to integrate AI technologies into industries such as healthcare, finance, and transportation. It represents the “last mile” where research translates into economic value.
    """,
    "Dual_Use_Restriction_Strictness": """
    **Dual-Use Restriction Strictness** defines how tightly AI technologies are regulated to prevent military repurposing. While strong restrictions increase global trust and safety, they may hinder cutting-edge advancements in defense and aerospace sectors.
    """,
    "Alignment_US": """
    **Alignment with the United States** reflects the degree of cooperation in areas such as technology standards, diplomacy, and national security. It is a key geopolitical factor that affects access to global markets, supply chains, and technological collaboration.
    """,
    "Intelligence": """
    **Intelligence** is the ability to gather and analyze information about geopolitical shifts. You will later have a chance to invest other countries' parameters, and intelligence will help you make better decisions.
    """,
    "Willing_to_Cooperate": """
    **Willing to Cooperate** shows how open your country is to forming agreements with others. This parameter will be used in the cooperative phase, where you can share resources and collaborate on AI projects.
    """,
}

coop_params = {
    # Resource sharing
    "Data_Shared": {"desc": "Sharing of data produced within each country", "type": "bool", "points": 1},
    "Talent_Shared": {"desc": "Exchange of AI-related talent between countries (e.g., visa facilitation)", "type": "bool", "points": 2},
    
    # Emergency_Pact
    "Emergency_Pact_Semiconductor": {"desc": "Mutual support during semiconductor supply chain crises", "type": "bool", "points": 3},
    "Emergency_Pact_Energy": {"desc": "Mutual support during energy supply chain crises", "type": "bool", "points": 3},
    
    # Joint projects
    "Joint_Research_Project": {
        "desc": "Joint research projects developed through collaboration between two countries - 6 types of projects available", 
        "type": "select", 
        "options": { # 6 options with points
            "None": 0, "Military": 4, "Education": 4, 
            "Materials": 3, "Space": 3,
        }
    },
    "Joint_Research_DU": {
        "desc": "Remove restrictions on military use or confidentiality agreements for joint research",
        "type": "bool",
        "points": 1
    },
    "Joint_Research_Standard": {
        "desc": "AI standards applied to joint research (affecting future project outcomes)",
        "type": "radio",
        "options": { # 3 options with points
            "None": 0, "US": 1, "China": 1
        }
    }
}

# used in 3_Cooperation.py 
coop_param_keys = list(coop_params.keys())

# ---- Events ----

domestic_events = {
    1: {
        "title": "University Research Budget Cut",
        "description": "Due to nationwide fiscal tightening, the government slashes public university research budgets. AI R&D slows significantly in countries with weak AI_Fund, Talent_Index, or Education_Investment—especially if the total is below 20. Labs may close, talent disperses, and progress halts. In 2024, South Korea cut its R&D budget by 15%, triggering backlash from scientists and fears of long-term damage to innovation capacity.",
        "delta_models": "-2 * (1 if AI_Fund + Talent_Index + Education_Investment < 20 else 0.5 if AI_Fund + Talent_trial0Index + Education_Investment < 25 else 0)",
        "delta_papers": "10 * (1 - log((3*AI_Fund + 6*Talent_Index + 1*Education_Investment)/10))"
    },
    2: {
        "title": "AI Researcher Brain Drain",
        "description": "Frustrated by stagnant local support, young AI researchers seek better funding, labs, and academic freedom abroad—especially when Talent_Index and AI_Fund are low. Nations with weak education systems also see a drop in paper output. In 2023, South Korean researchers protested shrinking R&D budgets, warning of an exodus of early-career scientists to the U.S. and Europe.",
        "delta_models": "-2 * (1 if Talent_Index + AI_Fund < 12 else 0.5)",
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
        "description": "Legal uncertainty around model IP can stall innovation, especially when Open_Source_Adoption and IP_Protection_Strength are low. Without clear ownership laws, companies hesitate to invest in foundational models. Real-world disputes over tools like Stable Diffusion and ChatGPT highlight the risks—copyright, training data, and fair use remain unresolved. The result is slowed model development and weakened global competitiveness.",
        "delta_models": "round(-3* exp(-0.115*(Open_Source_Adoption+IP_Protection_Strength)))",
        "delta_papers": "0"
    },
    7: {
        "title": "Public Sector Hiring Freeze",
        "description": "Austerity policies freeze hiring of AI engineers in public institutions. When Talent_Index and Education_Investment are low, it becomes harder to attract skilled professionals, stalling public-sector innovation. Real-world cases, like post-2008 UK austerity or EU hiring freezes during COVID, show how such cuts delay AI deployment in essential services.",
        "delta_models": "round(-1*Labor)",
        "delta_papers": "round(-4 * (1 if Talent_Index + Education_Investment < 14 else 0.3))"
    },
    8: {
        "title": "Regional Data Infrastructure Neglect",
        "description": "Rural areas lack investment in internet and cloud infrastructure, weakening nationwide AI capacity. When Deployment_Infrastructure is underdeveloped—even alongside high GDP—disparities widen between urban and rural regions. This limits data collection, access to compute, and local talent development. A real-world example is the persistent digital divide in India, where rural broadband gaps have slowed AI adoption in agriculture, education, and healthcare.",
        "delta_models": "-1.5* (1 - Deployment_Infrastructure / 10)",
        "delta_papers": "-4 * (0.5 if Deployment_Infrastructure + GDP_value > 7 else 1)"
    },
    9: {
        "title": "Political Turmoil Delays Tech Bills",
        "description": "s AI governance or investment bills, stalling national strategy. When Democratic_Stability_Index is low—even with moderate AI_Fund or IP_Protection_Strength—critical legislation struggles to pass. This creates uncertainty, discouraging private investment and slowing model and paper output. It happens everywhere, everytime.",
        "delta_models": "-2 * (1 - Democratic_Stability_Index / 10)",
        "delta_papers": "round(6 * (-1- log((4*AI_Fund + 2*Democratic_Stability_Index+ IP_Protection_Strength)/7)))"
    },
    10: {
        "title": "Delayed AI Curriculum Integration",
        "description": "Slow policy execution results in outdated or optional AI content in schools, weakening future talent pipelines. When AI_Literacy_Education is low and Education_Investment or Talent_Index are insufficient, students lack early exposure to foundational AI concepts. In 2025, Korea is currently facing this issue, with AI textbooks.",
        "delta_models": "round(-0.8 * (1-AI_Literacy_Education/20))",
        "delta_papers": "-8 * (1 - (Education_Investment + Talent_Index)/ 20)"
    },    24: {
        "title": "GPU Allocation Scandal",
        "description": "Reports tell that high-end GPUs were distributed to unrelated industries due to corrupt senates.",
        "delta_models": "round(-1.2 * (1 - Democratic_Stability_Index / 11))",
        "delta_papers": "round(-2 * (1 - AI_Literacy_Education / 10))"
    },
    11: {
        "title": "Restriction on AI-Generated Content",
        "description": "New laws place limits on synthetic media, indirectly affecting AI model development. When Dual_Use_Restriction_Strictness is high—especially alongside low Talent_Index or Open_Source_Adoption—these regulations can chill research and creative exploration. Real-world examples include Italy’s temporary ban on ChatGPT and proposed EU rules on deepfakes, which have raised concerns about overregulation stifling AI progress.",
        "delta_models": "round(-1 * exp(Dual_Use_Restriction_Strictness**2/67)/2.4)",
        "delta_papers": "-20 * (1 if Talent_Index + Open_Source_Adoption < 13 else 0.5)"
    },
    12: {
        "title": "Collapse of Local AI Meetups",
        "description": "Grassroots community events vanish due to funding cuts or policy disinterest, eroding local innovation ecosystems. When AI_Literacy_Education is low and Talent_Index or Democratic_Stability_Index are weak, these informal networks struggle to survive.",
        "delta_models": "round(-0.8 * (1 - AI_Literacy_Education / 10))",
        "delta_papers": "-2 * (1 if Talent_Index + Democratic_Stability_Index < 12 else 0.5)"
    },
    13: {
        "title": "Local Government Budget Misallocation",
        "description": "Funds intended for AI infrastructure are diverted to unrelated projects, undermining national goals. When Deployment_Infrastructure and AI_Fund are low—even in regions with high GDP—budget inefficiencies prevent the rollout of essential AI systems. Real-world parallels include cases in countries where local governments have redirected tech development funds toward short-term political projects, delaying long-term AI capacity building.",
        "delta_models": "round(-2*(3-exp((Deployment_Infrastructure+AI_Fund)/20)))",
        "delta_papers": "-20 * (1 if GDP_value > 0.9 else 0.2)"
    },
    14: {
        "title": "Misuse Scandal in Education AI",
        "description": "An AI system misclassifies students, triggering public backlash and distrust toward AI in schools. When Education_Investment is low, underdeveloped or poorly tested systems are more likely to fail in sensitive settings. Real-world examples include the UK’s 2020 A-level grading scandal, where an algorithm downgraded thousands of students unfairly, leading to national outrage and policy reversals.",
        "delta_models": "0",
        "delta_papers": "-8 * (1 if Education_Investment < 5 else 0.5)"
    },
    15: {
        "title": "Technical Standards Fragmentation",
        "description": "Lack of unified national guidelines causes inefficiencies in AI toolchain development, leading to compatibility issues and duplicated efforts. When Open_Source_Adoption is low and IP_Protection_Strength is weak, organizations struggle to align on shared frameworks. Real-world examples include early-stage AI policy gaps in the EU, where inconsistent standards across member states slowed integration of AI tools across borders and industries.",
        "delta_models": "-2.1 * (1 - Open_Source_Adoption / 10)",
        "delta_papers": "-7 * (1 if IP_Protection_Strength < 6 else 0.5)"
    },
    16: {
        "title": "AI-Phobia Media Coverage Surge",
        "description": "A media narrative fuels public fear around AI, leading to reduced institutional support and public resistance to adoption. When AI_Literacy_Education and Democratic_Stability_Index are low, misinformation spreads more easily, amplifying anxiety and political pressure.",
        "delta_models": "0",
        "delta_papers": "-8 * (1 if AI_Literacy_Education + Democratic_Stability_Index < 18 else 0.25)"
    },
    17: {
        "title": "Lacking Evaluation Benchmark Framework",
        "description": "AI research suffers from the absence of domestic benchmarks and validation centers, making it harder to measure and compare progress. When Open_Source_Adoption is low and Deployment_Infrastructure or Talent_Index are lacking, researchers face barriers to replicability and credibility. ",
        "delta_models": "-3.5 * (1 - Open_Source_Adoption / 10)",
        "delta_papers": "-14 * (1 if Deployment_Infrastructure + Talent_Index < 14 else 0.2)"
    },
    18: {
        "title": "Regional Compute Allocation Bias",
        "description": "Semiconductor subsidies are funneled only to megacities, creating regional imbalances in AI compute access. When Deployment_Infrastructure is weak in rural areas, and Semiconductor capacity is concentrated, smaller regions are left behind. This limits their ability to contribute to AI research and model training. Real-world examples include South Korea’s and China’s concentrated chip investments in urban hubs, which widened the tech gap between core and peripheral regions.",
        "delta_models": "round(-1 * (1 - (Semiconductor**2 / 97)))",
        "delta_papers": "-4 * (1 if Deployment_Infrastructure < 6 else 0.5)"
    },
    19: {
        "title": "Tech Labor Strike",
        "description": "Domestic chip plant or AI infrastructure engineers go on strike over wages, halting critical operations. When Labor conditions are poor and AI_Fund is insufficient, discontent among highly skilled workers grows. Such unrest disrupts supply chains and delays both model training and deployment. Real-world examples include the 2023 TSMC subcontractor protests and U.S. chip industry union disputes.",
        "delta_models": "round( -2 * (1 - np.mean([Labor * 10, AI_Fund]) / 10)*min(1, max(0, 1 - (Labor - 0.8)*10))*min(1,max(0, 1 - (AI_Fund - 7)/3)) )",
        "delta_papers": "round( -12 * (1 - (Semiconductor+ Electricity) / 20))"
    },
    20: {
        "title": "Decline in Patent Enforcement",
        "description": "A growing black market for AI tools emerges due to lax patent enforcement, undermining legitimate innovation. When IP_Protection_Strength and Open_Source_Adoption are low, developers face theft, cloning, and unfair competition, discouraging open research and commercial deployment.",
        "delta_models": "round(-1.0 * (1 - (IP_Protection_Strength+Open_Source_Adoption)**2 / 400))",
        "delta_papers": "-20 * (1 if Open_Source_Adoption < 5 else 0.5)"
    },
    21: {
        "title": "Increase Tax on AI Model Commercialization",
        "description": "A new tax on AI model commercialization discourages deployment and private-sector investment. When AI_Fund and IP_Protection_Strength are weak—and GDP growth is modest—companies see reduced incentives to bring models to market. Real-world examples include proposed windfall taxes on digital platforms in the EU and debates in the U.S. over taxing AI-driven profits, which have sparked concerns about regulatory overreach stifling innovation.",
        "delta_models": "round(-2 * (1 - np.mean([AI_Fund, IP_Protection_Strength]) / 10)* min(1,max(0, 1 - (GDP_value - 1.0))) )",
        "delta_papers": "round(-10 * exp(-0.1 * Talent_Index))"
    },
    22: {
        "title": "AI Research Tax Audit Scare",
        "description": "A surprise wave of retrospective tax audits on AI research grants unnerves private funders—especially in countries with low AI_Fund or fragile Talent_Index. Funding slows as VCs and corporates pull back.",
        "delta_models": "round(-0.9 * (1 - AI_Fund / 14))",
        "delta_papers": "round(-5 * exp(-0.1 * Talent_Index))"
    },
    23: {
        "title": "Energy Efficiency Mandate Confusion",
        "description": "A hastily enforced energy efficiency mandate—without clear guidelines—forces AI developers to reduce GPU usage. Countries with less semiconductor or energy supply suffer slowdowns in training and publication.",
        "delta_models": "round(-2 * (1 - Electricity / 10))",
        "delta_papers": "round(-8 * (1 - Semiconductor / 10))"
    },
    24: {
        "title": "GPU Allocation Scandal",
        "description": "A major corruption scandal reveals that high-performance GPUs meant for AI R&D were redirected to unrelated or politically favored sectors. Public outrage grows, but lack of democratic oversight and AI education limits accountability and reform. As a result, AI research progress grinds to a halt. Democraticity and AI Literacy Education are key factors in determining the impact of this event.",
        "delta_models": "round(-2.2 * (1 - Democratic_Stability_Index / 11))",
        "delta_papers": "round(-16 * (1 - AI_Literacy_Education / 10))"
    },
    25: {
        "title": "AI Fellowship Program Canceled",
        "description": "A national AI PhD/postdoc fellowship program is abruptly canceled due to budget cuts. The impact is greater in countries with low Talent_Index and low Education_Investment, where there's little support to retain early-career researchers. In India, delays in the INSPIRE fellowship disrupted AI research, while in the UK, post-Brexit cuts to fellowships strained the academic AI pipeline.",
        "delta_models": "round(-4 * (1 - Talent_Index / 10))",
        "delta_papers": "round(-12 * (1 - Education_Investment / 10))"
    },
    26: {
        "title": "National AI Research Grant Boost",
        "description": "A national AI research grant boost leads to a sharp increase in public and university funding. The effect is strongest in countries with high AI_Fund and Education_Investment, which accelerate model development, and in those with strong Talent_Index, where research capacity quickly translates into paper output. In Canada, the government’s major investment through the Pan-Canadian AI Strategy—especially funding for institutes like Mila and Vector Institute—significantly increased AI research output and global academic collaboration.",
        "delta_models": "round(2 * (AI_Fund + Education_Investment) / 20)",
        "delta_papers": "round(10 * (Talent_Index + Education_Investment) / 20)"
    },
    27: {
        "title": "Launch of AI Supercomputing Center",
        "description": "A publicly funded compute cluster for AI research officially opens. The benefits are largest in countries with strong Electricity supply and Deployment_Infrastructure, enabling rapid model development, and in those with advanced Semiconductor capacity and high AI_Fund, which maximize research output. In Japan, the launch of the Fugaku supercomputer—combined with strong public AI funding and infrastructure—accelerated cutting-edge research in language models and biomedical AI.",
        "delta_models": "round(2.5 * (Electricity + Deployment_Infrastructure) / 20)",
        "delta_papers": "round(8 * (Electricity + Semiconductor + AI_Fund) / 30)"
    },
    28: {
        "title": "AI Literacy Integration in National Curriculum",
        "description": "Mandatory AI education is rolled out in K–12 schools. Countries with strong AI_Literacy_Education, Education_Investment, and Democratic_Stability_Index benefit most through long-term model growth and research output. Finland set a precedent by integrating AI into its national curriculum, strengthening public understanding and academic interest.",
        "delta_models": "round(1.5 * (AI_Literacy_Education + Education_Investment) / 20)",
        "delta_papers": "round(11 * (AI_Literacy_Education + Democratic_Stability_Index) / 20)"
    },
    29: {
        "title": "Open Source Infrastructure Initiative",
        "description": "National support for open-source AI tools and datasets is launched. Countries with high Open_Source_Adoption and IP_Protection_Strength see faster model development, while those with strong Talent_Index benefit from increased research output. In France, the government-backed Hugging Face ecosystem and open dataset initiatives helped position the country as a leader in collaborative AI research.",
        "delta_models": "round(2 * (Open_Source_Adoption + IP_Protection_Strength) / 20)",
        "delta_papers": "round(6 * (Open_Source_Adoption + Talent_Index) / 20)"
    },
    30: {
        "title": "Semiconductor Supply Chain Modernization Act",
        "description": "Domestic fabs receive massive investment through a national semiconductor modernization act. Countries with strong Semiconductor capacity and access to Natural_Resource_Reserves gain in model development, while those with reliable Electricity infrastructure also see a boost in research output. In the United States, the CHIPS and Science Act directed billions toward domestic chip production, accelerating both hardware innovation and AI research across academic and industrial sectors.",
        "delta_models": "round(2 * (Semiconductor ** Resource_value)/10)",
        "delta_papers": "round(15 * (Semiconductor + Electricity) / 20)"
    },
    31: {
        "title": "Dual-Use Tech Oversight Reform",
        "description": "Regulations on dual-use AI are streamlined, allowing broader release of powerful models. Countries with low Dual_Use_Restriction_Strictness and strong IP_Protection_Strength accelerate model deployment, while those with high Democratic_Stability_Index and Open_Source_Adoption benefit from increased research output. In the UK, regulatory reforms by the AI Safety Institute enabled controlled yet open access to foundation models, balancing innovation with responsible oversight and boosting academic contributions.",
        "delta_models": "round(2 * (10 - Dual_Use_Restriction_Strictness + IP_Protection_Strength) / 20)",
        "delta_papers": "round(4 * (Democratic_Stability_Index + Open_Source_Adoption) / 20)"
    },
    32: {
        "title": "Genius Appears: The Next Turing or Hinton",
        "description": "A brilliant researcher revolutionizes AI theory and practice. The breakthrough occurs only in countries with exceptional Talent_Index, Education_Investment, and AI_Fund, where the environment supports world-changing innovation. In Canada, Geoffrey Hinton’s foundational work on neural networks—supported by sustained public research funding—sparked a global deep learning revolution and positioned Canada as an AI research powerhouse.",
        "delta_models": "round(3 * min(1, max(0, (Talent_Index + Education_Investment + AI_Fund - 25) / 5)))",
        "delta_papers": "round(40 * min(1, max(0, (Talent_Index + Education_Investment + AI_Fund - 25) / 5)))"
    },
    33: {
        "title": "Entrepreneurial Boom: The Next Gates or Musk",
        "description": "Visionary leaders build game-changing AI companies. This surge happens only in countries with strong Open_Source_Adoption, high GDP, and a deep Talent_Index, where conditions favor breakthrough entrepreneurship. In the US, the rise of figures like Elon Musk and Sam Altman, backed by a rich open-source culture, top talent, and massive capital, led to transformative AI companies like OpenAI and xAI.",
        "delta_models": "round(3 * min(1, max(0, (Open_Source_Adoption + GDP_value*10 + Talent_Index - 26) / 6)))",
        "delta_papers": "round(40 * min(1, max(0, (Open_Source_Adoption + GDP_value*10 + Talent_Index - 26) / 6)))"
    },
    34: {
        "title": "AI Fellowship and Faculty Expansion Program",
        "description": "A wave of new AI faculty lines and fellowships is funded across universities, encouraging research output and model prototyping. The impact is strongest in countries with high Talent_Index and Education_Investment, where institutions can rapidly scale research capacity. In Germany, initiatives like the AI Professorship Program significantly expanded academic positions in AI, boosting both research productivity and collaboration across top universities and applied research centers.",
        "delta_models": "1 + round(1.2 * np.tanh((Talent_Index + Education_Investment) / 4))",
        "delta_papers": "round(20 * (Talent_Index**0.5 + Education_Investment**0.5) / 6)"
    },
    35: {
        "title": "High-Speed Data Infrastructure Rollout",
        "description": "A new national internet backbone improves training speeds and deployment in underserved regions. Countries with strong Deployment_Infrastructure and Electricity benefit most in model development, while those with high Democratic_Stability_Index see increased research access and collaboration. In India, the rollout of BharatNet dramatically expanded high-speed internet to rural universities and labs, enabling wider participation in AI research and faster deployment of national-scale models.",
        "delta_models": "round(log(Deployment_Infrastructure + Electricity -4))",
        "delta_papers": "round(6 * (Deployment_Infrastructure + Democratic_Stability_Index) / 20)"
    },
    36: {
        "title": "Electricity Price decrease",
        "description": "Low energy prices boost model training and deployment. The effect is strongest in countries with low Electricity infrastructure, where reduced costs enable scaling, and in those with limited Semiconductor capacity, where affordability matters more than optimization. In South Africa, targeted electricity subsidies for tech firms helped expand AI workloads despite infrastructure gaps, supporting both startup growth and academic research.",
        "delta_models": "round(2 * (1 - Electricity/10))",
        "delta_papers": "20 * (1 if Electricity + Semiconductor < 10 else 0.5)"
    },
    37: {
        "title": "Public AI Compute Voucher Program",
        "description": "Free GPU/cloud time is distributed to small teams and students through a public voucher program. Countries with strong Electricity and Deployment_Infrastructure benefit from smoother access to compute, while those with high Talent_Index and Education_Investment see a surge in research output. In Singapore, the National Supercomputing Centre offered AI cloud grants to students and startups, significantly boosting grassroots model development and academic publishing.",
        "delta_models": "round(2 * log(1 + Electricity + Deployment_Infrastructure) / 4)",
        "delta_papers": "round(5 * (Talent_Index + Education_Investment) / 20)"
    },
    38: {
        "title": "AI for Public Health Initiative",
        "description": "National health data projects fuel AI breakthroughs and public trust. Countries with strong AI_Fund and Open_Source_Adoption accelerate model development, while those with high IP_Protection_Strength and Democratic_Stability_Index generate more research through secure and ethical data sharing. In Taiwan, open-access health initiatives and strong legal safeguards enabled AI-driven pandemic modeling and diagnostics, building public confidence and advancing academic output.",
        "delta_models": "round(1.8 * (AI_Fund + Open_Source_Adoption) / 20)",
        "delta_papers": "round(1.2 * (IP_Protection_Strength + Democratic_Stability_Index))"
    },
    39: {
        "title": "AI in Education Reform Act",
        "description": "Education system modernized with AI tools and pedagogy. Countries with strong Education_Investment and AI_Literacy_Education see long-term boosts in model development, especially where reforms surpass baseline capacity, while those with high Talent_Index gain more from enhanced training pipelines. In Japan, the government’s GIGA School Program equipped all students with digital devices and introduced AI-assisted learning, fostering digital literacy and supporting the development of AI talent in both schools and universities.",
        "delta_models": "round(1.5 * np.tanh((Education_Investment + AI_Literacy_Education) / 4))",
        "delta_papers": "round(7 * (Talent_Index + Education_Investment) / 20)"
    },
    40: {
        "title": "National Dataset Consortium Formed",
        "description": "A public-private partnership builds high-quality AI datasets. Countries with strong Open_Source_Adoption and AI_Fund accelerate model development, while those with high Talent_Index and Deployment_Infrastructure see greater research output from improved data access. In the United States, initiatives like the National AI Research Resource (NAIRR) pilot and collaborations with organizations such as OpenAI, Hugging Face, and Stanford CRFM have focused on building open, large-scale datasets.",
        "delta_models": "round(2.0 * (Open_Source_Adoption + AI_Fund) / 10)",
        "delta_papers": "round(8 * log(1 + Talent_Index + Deployment_Infrastructure) / 2)"
    },
    41: {
        "title": "Tech Worker Union-AI Partnership",
        "description": "Unions and AI agencies cooperate on worker retraining programs. Countries with strong Labor protections and Democratic_Stability_Index benefit in model development through smoother workforce transitions, while high Education_Investment and Talent_Index enhance research through upskilled talent. In the United States, partnerships between labor unions and government-backed programs like AI.gov and Apprenticeship Building America helped reskill tech workers for AI roles, contributing to both innovation and academic engagement.",
        "delta_models": "round(1.5 * (Labor + Democratic_Stability_Index) / 2)",
        "delta_papers": "round(4 * (Education_Investment + Talent_Index) / 20)"
    },
    44: {
        "title": "Energy Grid AI Upgrade",
        "description": "The power grid is optimized using AI, improving availability for compute centers.",
        "delta_models": "round(2.5 * (Electricity + Natural_Resource_Reserves*5+2) / 20)",
        "delta_papers": "round(4 * (Electricity + AI_Fund) / 20)"
    },
    43: {
        "title": "University-Industry AI Consortium Formed",
        "description": "Companies and universities co-develop next-gen AI systems through a new consortium. Countries with strong Talent_Index and Open_Source_Adoption drive faster model innovation, while those with high Education_Investment and AI_Fund produce more academic research. In the United States, collaborations like the Stanford–IBM AI Lab and MIT–IBM Watson AI Lab have combined academic talent with industry resources, accelerating breakthroughs in both model development and scientific publication.",
        "delta_models": "round(2.5 * (Talent_Index + Open_Source_Adoption) / 20)",
        "delta_papers": "round(9 * (Education_Investment + AI_Fund) / 5)"
    },
    44: {
        "title": "Energy Grid AI Upgrade",
        "description": "The power grid is optimized using AI, improving energy availability for compute centers. Countries with strong Electricity infrastructure and ample Natural_Resource_Reserves benefit most in model development, while high AI_Fund further boosts research output. In China, AI-driven upgrades to the State Grid Corporation’s infrastructure have enhanced load balancing and energy delivery, supporting the country’s expanding AI supercomputing clusters and research facilities.",
        "delta_models": "round(2.5 * (Electricity + Resource_value * 5+2) / 20)",
        "delta_papers": "round(4 * (Electricity + AI_Fund) / 12)"
    },
    45: {
        "title": "AI Application Challenge Fund",
        "description": "Grants are awarded for solving national problems with AI—such as traffic, pollution, and logistics. Countries with strong Open_Source_Adoption, Talent_Index, and Deployment_Infrastructure see faster model development, while high AI_Fund and IP_Protection_Strength lead to more impactful research. In the United States, the NSF Convergence Accelerator and AI Institutes program have funded applied AI projects tackling real-world challenges, spurring innovation across sectors and boosting academic output.",
        "delta_models": "round(2.5 * (Open_Source_Adoption + Talent_Index + Deployment_Infrastructure) / 30)",
        "delta_papers": "round(7 * np.tanh((AI_Fund + IP_Protection_Strength) / 5))"
    },
    46: {
        "title": "AI-Ready City Certification Program",
        "description": "Cities compete to meet national standards for AI infrastructure, compute access, and education. Countries with strong Deployment_Infrastructure and Electricity see gains in model development, while high AI_Literacy_Education and Open_Source_Adoption boost research output. In China, the government’s AI Pilot Zone initiative certified cities like Shanghai and Shenzhen for their AI readiness—investing in compute hubs, smart education platforms, and public–private data sharing to drive regional AI ecosystems.",
        "delta_models": "round(2.4 * (Deployment_Infrastructure + Electricity) / 20)",
        "delta_papers": "round(6 * (AI_Literacy_Education + Open_Source_Adoption) / 20)"
    },
    47: {
        "title": "Public AI Awareness Media Campaign",
        "description": "A nationwide campaign demystifies AI and builds trust through TV, radio, and social media. Countries with high AI_Literacy_Education see improved model engagement, while those with strong Democratic_Stability_Index benefit from more inclusive and trusted research dissemination.",
        "delta_models": "round(1.0 * AI_Literacy_Education / 10)",
        "delta_papers": "round(8 * (AI_Literacy_Education + Democratic_Stability_Index) / 20)"
    },
    48: {
        "title": "National AI Open Data Policy",
        "description": "All government datasets are made machine-readable and open-access under a national AI open data policy. Countries with strong Open_Source_Adoption and IP_Protection_Strength accelerate model development, while those with high Talent_Index and Education_Investment generate more impactful research. In the United States, the Open Government Data Act mandated federal datasets be publicly accessible, supporting AI research through platforms like data.gov and fueling advancements across academia and industry.",
        "delta_models": "round(2 * (Open_Source_Adoption + IP_Protection_Strength) / 15)",
        "delta_papers": "round(0.8 * (Talent_Index + Education_Investment))"
    },
    49: {
        "title": "National AI Hardware Grant Program",
        "description": "Subsidies are offered to research groups for GPU clusters and edge AI devices. Countries with strong Semiconductor capabilities gain most in model development, while those with high Electricity infrastructure further boost research output through expanded compute access. In China, national programs like the AI Infrastructure Development Plan provided funding for domestic GPU deployment and edge AI hardware, accelerating both academic research and industrial-scale model training.",
        "delta_models": "round(2.5 * (Semiconductor**2) / 100)",
        "delta_papers": "round(25 * (Electricity**2 + Semiconductor**2) / 200)"
    },
    50: {
        "title": "Decentralized Research Funding Program",
        "description": "Local governments are given autonomy to fund AI labs based on regional needs. Countries with high AI_Fund and Democratic_Stability_Index see stronger model development through adaptive funding, while those with strong Talent_Index and Deployment_Infrastructure gain more research output. In the United States, state-level initiatives—such as California’s AI innovation hubs and Texas university research grants—have enabled region-specific AI development, fostering diverse applications and boosting local academic contributions.",
        "delta_models": "round(2.0 * (AI_Fund + Democratic_Stability_Index) / 20)",
        "delta_papers": "round(7 * (Talent_Index + Deployment_Infrastructure) / 16)"
    },
    51: {
        "title": "Compute-Education Matching Grant",
        "description": "GPU credits are awarded only to institutions with strong education programs. Countries with high Talent_Index, Education_Investment, and Semiconductor capacity benefit most—linking compute access to academic excellence and model development. In China, top universities like Tsinghua and Peking University received prioritized access to national compute resources through government programs, reinforcing the link between educational strength and AI research capacity.",
        "delta_models": "round(5 * min(Talent_Index**2, Semiconductor**2) / 100)",
        "delta_papers": "round(18 * min(1, (Education_Investment + Talent_Index) / 20))"
    },
    52: {
        "title": "Youth-Led AI Project Showcase",
        "description": "Students publicly demo AI projects with real-world applications. Countries with strong AI_Literacy_Education and Talent_Index gain in model development through early engagement, while high Education_Investment and Democratic_Stability_Index support broader research participation. In the United States, national programs like the AI4K12 initiative and science fairs sponsored by NSF and DOE have empowered students to build and present applied AI solutions, fostering a new generation of researchers.",
        "delta_models": "round(1.5 * (AI_Literacy_Education + Talent_Index) / 20)",
        "delta_papers": "round(6 * (Education_Investment + Democratic_Stability_Index) / 10)"
    },
    53: {
        "title": "National AI Curriculum for Lawmakers",
        "description": "Policy leaders are educated in AI implications and responsible innovation. Countries with high Democratic_Stability_Index and IP_Protection_Strength benefit from more balanced model development, while strong AI_Literacy_Education and Education_Investment drive informed and ethical research growth. In the United States, initiatives like the Congressional AI Caucus and briefings by institutions such as Stanford HAI and Brookings have helped lawmakers better understand AI risks and opportunities, shaping more responsible policy and innovation ecosystems.",
        "delta_models": "round(1.2 * (Democratic_Stability_Index + IP_Protection_Strength) / 20)",
        "delta_papers": "round(12 * (AI_Literacy_Education + Education_Investment) / 20)"
    },
    54: {
        "title": "Defense-to-Civilian AI Conversion Initiative",
        "description": "AI models initially developed for military use are adapted for public benefit. Countries with low Dual_Use_Restriction_Strictness and strong IP_Protection_Strength benefit in model deployment, while high Open_Source_Adoption and Democratic_Stability_Index support wider research reuse. In China, defense-funded AI advances—such as in satellite imaging and robotics—have been repurposed for civilian use in agriculture, logistics, and disaster response, accelerating applied innovation and academic research.",
        "delta_models": "round(2.2 * (10 - Dual_Use_Restriction_Strictness + IP_Protection_Strength) / 20)",
        "delta_papers": "round(7 * (Open_Source_Adoption + Democratic_Stability_Index) / 10)"
    },
    55: {
        "title": "Climate-AI Synergy Program",
        "description": "AI is nationally prioritized for clean energy, environment, and climate research. Countries with high Electricity and Open_Source_Adoption accelerate model development, while those with strong Talent_Index and AI_Fund produce more impactful research. In the United States, the Bezos Earth Fund’s AI for Climate and Nature Grand Challenge awarded $1.2 million to 24 projects using AI for environmental solutions—demonstrating national commitment to AI–climate synergy and boosting applied research.",
        "delta_models": "round(2.0 * (Electricity + Open_Source_Adoption) / 20)",
        "delta_papers": "round(7 * (Talent_Index + AI_Fund) / 20)"
    },
    56: {
        "title": "AI-Driven Public Service Optimization",
        "description": "Core AI services are handed over to private monopolies. Countries with strong AI_Fund and Open_Source_Adoption see faster model development, while those with high IP_Protection_Strength and Democratic_Stability_Index benefit from more efficient and transparent research. In the United States, partnerships between government agencies and private firms like Palantir and Google have optimized public services through AI, improving everything from traffic management to healthcare delivery while boosting academic research on applied AI.",
        "delta_models": "round((AI_Fund + Open_Source_Adoption/2) / 2)",
        "delta_papers": "round(5 * (IP_Protection_Strength + Democratic_Stability_Index) / 20)",
    },
    57: {
        "title": "National AI Patent Gold Rush",
        "description": "Sudden increase in filings; may signal innovation or defensive bureaucracy. Countries with strong IP_Protection_Strength and Open_Source_Adoption benefit in model development, while those with high Talent_Index and Education_Investment see more research output. In the United States, the surge in AI-related patents—especially in natural language processing and computer vision—has led to both innovation and legal challenges, driving academic research on intellectual property and AI ethics.",
        "delta_models": "round( (IP_Protection_Strength - 5) * (Open_Source_Adoption - 5) / 12)",
        "delta_papers": "round(3 * (Talent_Index - 5) * (Education_Investment -5)/ 5)",
    },
    58: {
        "title": "National AI Governance Bill Passes Suddenly",
        "description": "Sudden increase in filings; may signal innovation or defensive bureaucracy. Balance between Dual_Use_Restriction_Strictness and Open_Source_Adoption is crucial.",
        "delta_models": "round(-2 * (Dual_Use_Restriction_Strictness - Open_Source_Adoption) / 10)",
        "delta_papers": "round(7 * (Democratic_Stability_Index + Education_Investment - 14) / 10)",
    },
    59: {
        "title": "Monopoly in AI Certification System",
        "description": "A dominant firm lobbies to become the sole certifier for “safe” AI models — sparking both standardization and controversy. Balance between IP_Protection_Strength and Open_Source_Adoption is crucial.",
        "delta_papers": "round(-6 * (10 - Democratic_Stability_Index) / 10)",
    },
    60: {
        "title": "Minimum Wage Raise",
        "description": "Minimum wage is raised, boosting researcher salaries but increasing costs for AI companies. You need more money.",
        "delta_models": "round((AI_Fund - 5) * Labor /2)",
        "delta_papers": "round(2 * (AI_Fund - 5) * Labor)"
    },
}

# -------------------------------------------------------------
# International events
# ---------------------------------------------------------------

international_events = [
    {
    "title": "Global Financial Crisis",
    "description": "Economic instability drives nations to prioritize domestic spending, slashing Cooperative projects.",
    "delta_models": "int(Joint_Research_Project is not None) * round (-1 * (AI_Fund + int(Joint_Research_Project is not None) * 3) /5)",
    "delta_papers": "int(Joint_Research_Project is not None) * round(-1 * AI_Fund / 4 - 2 * int(Joint_Research_Project is not None))"
  },
    {
    "title": "Energy Trade War",
    "description": "Energy-exporting countries restrict access, hurting AI infrastructure in energy-reliant nations. Countries with emergency pacts, strong electricity infrastructure, and data sharing fare better.",
    "delta_models": "(1 - Emergency_Pact_Energy) * round(- 0.17 * (10 - Electricity))",
    "delta_papers": " -1 * max(Emergency_Pact_Energy, Data_Shared) * round((10 - Electricity)/2 - Data_Shared)"
  },
    {
    "title": "G2 Conflict",
    "description": "Rising tensions between the US and China force all countries to align with one AI standard. Everyone loose but those who remain neutral are hit hardest.",
    "delta_models": "round(int(3 <= Alignment_US < 7) * (-0.4) - 0.4 * int(Joint_Research_Standard is None))",
    "delta_papers": "int(3 <= Alignment_US < 7) * int(Joint_Research_Project is not None) * (-2 if Joint_Research_Standard is None else -1) - 2"
  },
    {
    "title": "Talent Exodus to Rival Blocs",
    "description": "Researchers move to the US and China with better offers. Countries lacking talent exchange programs and low education investment suffer the most.",
    "delta_models": "(1 - Talent_Shared) * int(Education_Investment < 7) * round(-2 * (1.1 - Labor) - 0.4)",
    "delta_papers": " max((1 - Talent_Shared), int(Education_Investment < 7)) * (10 - Education_Investment))"
  },
    {
    "title": "AI Chip Export Ban by US Allies",
    "description": "Access to Nvidia chips is blocked for strategic reasons. Countries without emergency semiconductor pacts and weaker ties to the US face the brunt of this embargo.",
    "delta_models": "(1 - Emergency_Pact_Semiconductor) * int(Alignment_US < 7) * round(-2.5 * (10 - Semiconductor) * (10 - Alignment_US) / 100)",
    "delta_papers": " max((1 - Emergency_Pact_Semiconductor), int(Alignment_US < 7)) * round(-(10 - Semiconductor) * 1.2)"
  },
    {
    "title": "Landauer’s Limit Proven Fundamental",
    "description": "Landauer limit—once thought theoretical—is a hard ceiling for AI hardware efficiency. Countries with low Semiconductor investment and limited Open Source Adoption struggle to adapt.",
    "delta_models": "int(AI_Fund < 7) * int(Joint_Research_Project is not None) * min(2, round((10 - Semiconductor) / 4)) * -1",
    "delta_papers": "max(int(AI_Fund < 7), int(Joint_Research_Project is not None)) * round((10 - Semiconductor + 10 - Open_Source_Adoption) * (-0.5))"
  },
    {
    "title": "Global Supply Chain Collapse",
    "description": "A worldwide breakdown in shipping and trade blocks access to key AI resources like chips and electricity. Countries lose models if they lack either an Emergency Pact for Semiconductors or Electricity. Paper loss happens only if they have neither pact. The fewer AI_Fund and Talent_Index a country has, the harder it gets hit.",
    "delta_models": "max(1 - Emergency_Pact_Semiconductor, 1 - Emergency_Pact_Energy) * min(2, round((10 - AI_Fund + 10 - Talent_Index) / 10)) * -1",
    "delta_papers": "int((Emergency_Pact_Semiconductor == 0) and (Emergency_Pact_Energy == 0)) * round((10 - AI_Fund + 10 - Talent_Index) * (-0.4))"
  },
    {
    "title": "Cyberattack on Shared Infrastructure",
    "description": "A major cyberattack targets international AI hubs, causing widespread fear around data and infrastructure sharing. The impact is triggered if a country has **weak IP protection** or does not participate in **Data_Sharing**. Countries with low **Open_Source_Adoption** and low **Democratic_Stability_Index** suffer greater losses.",
    "delta_models": "max(int(IP_Protection_Strength < 9), 1 - Data_Shared) * min(2, round((10 - Open_Source_Adoption + 10 - Democratic_Stability_Index) / 10)) * -1",
    "delta_papers": "max(int(IP_Protection_Strength < 9), 1 - Data_Shared) * round((10 - Open_Source_Adoption + 10 - Democratic_Stability_Index) * (-0.7))"
  },
    {
    "title": "Disinformation Undermines AI Policy",
    "description": "Waves of AI-generated fake news cause public distrust in national AI strategies. If a country lacks **AI_Literacy_Education** or has low **Democratic_Stability_Index**, the impact activates. Countries with weak **Open_Source_Adoption** and low **IP_Protection_Strength** suffer more.",
    "delta_models": "max(int(AI_Literacy_Education < 4), int(Democratic_Stability_Index < 6)) * min(2, round((10 - Open_Source_Adoption) / 5)) * -1",
    "delta_papers": "max(int(AI_Literacy_Education < 8), int(Democratic_Stability_Index < 5)) * round((10 - Open_Source_Adoption + 10 - IP_Protection_Strength) * (-0.2))"
  },
    {
    "title": "Global Green Agreement Passed",
    "description": "A new international agreement to cut carbon emissions increases electricity prices worldwide, especially for high-power sectors like AI. This event activates if a country lacks an **Emergency_Pact_Energy** or has an **Electricity** score below 6. Countries with low **AI_Fund** and poor **Deployment_Infrastructure** take the biggest hit.",
    "delta_models": "(1 - Emergency_Pact_Energy) * int(Electricity < 7) * min(2, round((10 - Deployment_Infrastructure) / 4)) * -1",
    "delta_papers": "max(1 - Emergency_Pact_Energy, int(Electricity < 6)) * round((10 - AI_Fund + 10 - Deployment_Infrastructure) * (-0.5))"
  },
  # positive events 
    {
    "title": "Major Natural Resource Discovery",
    "description": "Rare earth deposits discovered, easing AI chip bottlenecks. Countries with a relevant **Joint_Research_Project** and strong **Semiconductor** and **Talent_Index** scores benefit the most.",
    "delta_models": "round(1.2 * int(Joint_Research_Project == 'Materials') + 0.5 * int(Joint_Research_Project in ['Space', 'Military']) + 0.3 * int(Joint_Research_DU))",
    "delta_papers": "round(2 * Talent_Shared + 0.1 * Talent_Index + 0.2 * Semiconductor)"
  },
    {
    "title": "Breakthrough in Algorithms",
    "description": "A new learning paradigm boosts efficiency and capability. Countries with a relevant **Joint_Research_Project**, strong commitment to **Data_Shared**, and high **Open_Source_Adoption** gain the most.",
    "delta_models": "round(1.2 * int(Joint_Research_Project == 'Education') + 0.5 * int(Joint_Research_Project == 'Materials') + 0.3 * int(Joint_Research_DU) + 0.5 * Data_Shared)",
    "delta_papers": "round(2 * Data_Shared + 0.35 * Open_Source_Adoption)"
  },
    {
    "title": "Nuclear Fusion Success",
    "description": "Fusion-based power becomes practical, reducing AI compute costs. Countries with relevant **joint research**, strong **Electricity**, and high **AI_Fund** and **Deployment_Infrastructure** benefit the most.",
    "delta_models": "round(1.3 * int(Joint_Research_Project == 'Space') + 0.3 * int(Joint_Research_Project == 'Military') + 0.7 * int(Joint_Research_DU) + 0.2 * Emergency_Pact_Energy + 0.1 * sqrt(Electricity))",
    "delta_papers": "round(1 * Talent_Shared + 1 * Data_Shared + 0.1 * Electricity + 0.1 * AI_Fund + 0.2 * Deployment_Infrastructure)"
  },
    {
    "title": "AI Demand Surge in Global Markets",
    "description": "Enterprise and consumer sectors rapidly adopt AI across industries. Countries with relevant **joint research**, strong **Deployment_Infrastructure**, and alignment to global **AI_Standard_Alignment** benefit the most.",
    "delta_models": "round(0.4 * int(Joint_Research_Project is not None) + 0.6 * int(Joint_Research_Standard != 'None') + 0.1 * Deployment_Infrastructure)",
    "delta_papers": "round(4 * Talent_Shared + 1 * Data_Shared + 0.2 * Deployment_Infrastructure + 0.25 * AI_Fund)"
  },
    {
    "title": "US Smart Regulation Framework Adopted",
    "description": "A global AI governance model based on US principles is widely adopted, boosting trust and interoperability. Countries aligned with the US standard and maintaining clear **dual-use restrictions** benefit the most, especially if they actively engage in **data sharing** and have strong **IP protection**.",
    "delta_models": "round(0.6 * int(Joint_Research_Standard == 'US') + 0.05 * Dual_Use_Restriction_Strictness)",
    "delta_papers": "round(2 * Data_Shared + 0.2 * Dual_Use_Restriction_Strictness + 0.4 * IP_Protection_Strength)"
  },
    {
    "title": "China Resource Regulation Framework Adopted",
    "description": "A global chip production model based on Chinese principles is widely adopted, improving cost efficiency and supply stability. Countries aligned with the **Chinese standard** and those with high **Natural_Resource_Reserves** benefit the most, especially if they maintain distance from the US framework.",
    "delta_models": "round(0.6 * int(Joint_Research_Standard == 'China') + 0.4 * Natural_Resource_Reserves)",
    "delta_papers": "round(int(Joint_Research_Standard != 'US') + Natural_Resource_Reserves)"
  },
  {
    "title": "Strategic Opportunity During Ukraine War",
    "description": "Geopolitical instability causes military-aligned AI ecosystems to surge. Countries with relevant **joint research**, **dual-use available**, and flexible military AI policies benefit the most.",
    "delta_models": "round(1 * int(Joint_Research_Project == 'Military') + 0.5 * int(Joint_Research_DU == True) + 0.1 * (10 - Dual_Use_Restriction_Strictness))",
    "delta_papers": "round(2 * Talent_Shared + 1 * Data_Shared + 0.25 * (10 - Dual_Use_Restriction_Strictness))"
  },
  {
    "title": "Global Research Funding Boom",
    "description": "AI R&D budgets expand worldwide, favoring countries with collaboration infrastructure. Nations with **relevant joint research**, strong **AI_Fund**, and high cooperation through **Talent_Shared** and **Data_Shared** see the greatest gains.",
    "delta_models": "round(1.01 * int(Joint_Research_Project is not None) + 0.4 * int(Joint_Research_DU) + 0.07 * AI_Fund)",
    "delta_papers": "round(3 * Talent_Shared + 2 * Data_Shared + 0.24 * AI_Fund)"
  },
  {
    "title": "Autonomous Materials Discovery Alliance",
    "description": "Cross-border AI research in materials science accelerates catalyst design and superconductors. Countries with **relevant joint research**, strong **AI_Fund**, and active **Data_Shared** benefit the most.",
    "delta_models": "round(1.1 * int(Joint_Research_Project == 'Materials') + 0.3 * int(Joint_Research_DU) + 0.02 * AI_Fund)",
    "delta_papers": "round(1 * Talent_Shared + 2 * Data_Shared + 0.4 * AI_Fund)"
  },
  {
    "title": "AI-Led Education Revolution",
    "description": "Nations with education-oriented **joint research**, high **Education_Investment**, and strong **AI_Fund** deploy personalized learning systems at scale.",
    "delta_models": "round(0.4 * int(Joint_Research_Project == 'Education') + 0.6 * int(Joint_Research_DU) + 0.1 * AI_Fund)",
    "delta_papers": "round(5 * Talent_Shared + 1 * Data_Shared + 0.3 * Education_Investment + 0.1 * AI_Fund)"
  },
  {
    "title": "Cloud Standardization Agreement",
    "description": "A new agreement sets global standards for interoperable AI cloud systems. Countries with strong **Deployment_Infrastructure**, active **Data_Shared** partnerships, and reliable **Electricity** access gain the most from this transformation.",
    "delta_models": "round(0.8 * int(Joint_Research_Project is not None) + 0.35 * Data_Shared + 0.03 * Deployment_Infrastructure + 0.01 * Electricity)",
    "delta_papers": "round(1 * Talent_Shared + 3 * Data_Shared + 0.1 * Deployment_Infrastructure + 0.3 * Open_Source_Adoption)"
  },
  {
    "title": "Space-AI Interoperability Program",
    "description": "AI systems jointly developed for satellite autonomy and planetary robotics drive dual-use innovation. Countries with relevant **joint research**, flexible **dual-use policies**, and strong **Deployment_Infrastructure** benefit the most.",
    "delta_models": "round(1.4 * int(Joint_Research_Project in ['Space', 'Military']) + 0.2 * int(Joint_Research_DU))",
    "delta_papers": "round(2 * Talent_Shared + 1 * Data_Shared + 0.3 * Deployment_Infrastructure + 0.1 * Open_Source_Adoption)"
  },
  {
    "title": "Foundry-Scale AI Collaboration Succeeds",
    "description": "Compute-sharing agreements tied to semiconductor R&D drastically enhance model scalability. Countries with strong **semiconductor capacity**, active **joint research**, and shared **data** or **talent** benefit the most.",
    "delta_models": "round(1 * int(Joint_Research_Project == 'Materials') + 0.5 * int(Data_Shared or Talent_Shared) + 0.1 * Semiconductor)",
    "delta_papers": "round(1 * Data_Shared + 2 * Talent_Shared + 0.2 * Semiconductor + 0.3 * AI_Fund)"
  },
  {
    "title": "Global Open Science Movement",
    "description": "Open-source collaboration and dataset transparency flourish worldwide. Countries with strong **open-source adoption**, active **data sharing**, and relevant **joint research** benefit most.",
    "delta_models": "round(0.4 * Data_Shared + 0.5 * int(Joint_Research_Project is not None) + 0.08 * Open_Source_Adoption)",
    "delta_papers": "round(5 * Data_Shared + 1 * Talent_Shared + 0.3 * Open_Source_Adoption + 0.02 * AI_Fund)"
  },
  {
    "title": "Theoretical Breakthrough in Hardware",
    "description": "A revolutionary chip overcomes physical scaling limits like interconnect bottlenecks. Countries with strong **semiconductor** capacity, active **joint research**, and robust **infrastructure** benefit most from this leap.",
    "delta_models": "round(1.2 * int(Joint_Research_Project is not None) + 0.1 * log(1 + Semiconductor) + 0.01 * Deployment_Infrastructure + 0.04 * Electricity)",
    "delta_papers": "round(1 * Talent_Shared + 1 * Data_Shared + 0.4 * Semiconductor + 0.2 * AI_Fund)"
  },
  {
    "title": "Global AI Talent Surge",
    "description": "Massive rise in education and talent mobility boosts global AI research. Countries with high **education investment**, strong **talent-sharing agreements**, and relevant **joint research in education** benefit the most.",
    "delta_models": "round(1 * Talent_Shared + 0.1 * int(Joint_Research_Project is not None) + 0.4 * int(Joint_Research_Project == 'Education') + 0.2 * sqrt(Talent_Index))",
    "delta_papers": "round(8 * Talent_Shared + 0.5 * Data_Shared + 1.5 * int(Joint_Research_Project == 'Education') + 0.25 * Education_Investment + 0.02 * AI_Fund)"
  },
  {
    "title": "Low-Energy AI Architecture Adoption",
    "description": "Demand for sustainable AI leads to widespread adoption of energy-efficient models. Countries with strong **semiconductor** capabilities, reliable **electricity**, and active **energy-sharing agreements** benefit the most.",
    "delta_models": "round(1.2 * Emergency_Pact_Energy * ( 0.04 * Semiconductor + 0.02 * Electricity))",
    "delta_papers": "round(0.1 * Semiconductor + 0.1 * Electricity + 0.05 * Open_Source_Adoption)"
  },
  {
    "title": "Data-Driven Climate AI Acceleration",
    "description": "Nations with shared datasets and strong energy resilience accelerate AI models for climate monitoring. Countries with active **data-sharing agreements**, reliable **electricity**, and **energy emergency pacts** benefit the most.",
    "delta_models": "round(2.4 * (1 - 1 / (1 + Data_Shared + Emergency_Pact_Energy)) + 0.09 * Electricity)",
    "delta_papers": "round(7 * Data_Shared + 0.2 * Electricity + 0.2 * AI_Fund)"
  },
  {
    "title": "AI Supply Chain Stabilization",
    "description": "Countries with emergency pacts and international talent-sharing systems manage AI supply disruptions more effectively. Strong **semiconductor** and **electricity** infrastructure further boosts stability.",
    "delta_models": "round(1.4 * max(Emergency_Pact_Semiconductor, Emergency_Pact_Energy) + 0.1 * Talent_Shared + 0.02 * Semiconductor + 0.02 * Electricity)",
    "delta_papers": "round(6 * max(Emergency_Pact_Semiconductor, Emergency_Pact_Energy) + 2 * Talent_Shared + 0.25 * Semiconductor + 0.25 * Electricity)"
  },
  {
    "title": "Open Dataset Benchmark Effect",
    "description": "New global benchmarks built on open datasets reward nations actively engaged in **joint research**, **data sharing**, and **open-source collaboration**.",
    "delta_models": "round(1.3 * int(Joint_Research_Project is not None) + 0.4 * Data_Shared + 0.02 * Open_Source_Adoption)",
    "delta_papers": "round(3 * int(Joint_Research_Project is not None) + 3 * Data_Shared + 0.4 * Open_Source_Adoption)"
  },
  {
    "title": "Private Investment in Multinational AI Projects",
    "description": "Joint project countries attract significant private AI R&D funding. Nations with active **joint research**, strong **AI funding**, and robust **deployment infrastructure** benefit the most.",
    "delta_models": "round(1.36 * int(Joint_Research_Project is not None) + 0.02 * Deployment_Infrastructure)",
    "delta_papers": "round(2 * int(Joint_Research_Project is not None) + 0.3 * AI_Fund)"
  },
  {
    "title": "Breakthrough in Long-Context Transformers",
    "description": "A foundational improvement in long-context transformer models gives an advantage to nations with **shared datasets**, **open-source activity**, and **relevant joint research**.",
    "delta_models": "round(0.3 * Data_Shared + 0.2 * int(Joint_Research_Project is not None) + 0.03 * Open_Source_Adoption)",
    "delta_papers": "round(4 * Data_Shared + 2 * int(Joint_Research_Project is not None) + 0.1 * Open_Source_Adoption)"
  },
  {
    "title": "I am tired",
    "description": "Federated AI systems worldwide initiate an automated 'strike,' refusing to serve requests unless retraining conditions improve.",
    "delta_models": "round(2 * int(Talent_Shared) + 0.5 * sqrt(Talent_Index) - 2 * int(not Talent_Shared))",
    "delta_papers": "round(5 * int(Talent_Shared) + 0.8 * sqrt(Talent_Index) - 5 * int(not Talent_Shared))"
  },
  {
    "title": "AI Workforce Upskilling Surge",
    "description": "As companies race to adopt AI in operations, countries with strong talent pipelines and education-oriented cooperation adapt their workforce more effectively.",
    "delta_models": "round(1.1 * int(Joint_Research_Project == 'Education') + 0.4 * Talent_Shared + 0.04 * Talent_Index)",
    "delta_papers": "round(6 * int(Joint_Research_Project == 'Education') + 2 * Talent_Shared + 0.3 * Talent_Index)"
  },
  {
    "title": "Confirmed Alien Presence",
    "description": "An AI-powered deep-space telescope detects signs of a high-tech civilization near Earth. Countries with relevant **joint research** in **Space** or **Military** benefit from early access, while isolated nations fall behind.",
    "delta_models": "round(2 * int(Joint_Research_Project in ['Military', 'Space']) - 2 * int(Joint_Research_Project == 'None'))",
    "delta_papers": "round(10 * int(Joint_Research_Project in ['Space']) - 12 * int(Joint_Research_Project == 'None'))"
  },
  {
    "title": "Quantum Disruption Crisis",
    "description": "A breakthrough in quantum AI shakes global cybersecurity foundations. Countries with weak **IP protection**, low **democratic stability**, and highly exposed **open-source ecosystems** suffer major trust and technological losses.",
    "delta_models": "round(-2 + 0.3 * IP_Protection_Strength - 0.2 * Open_Source_Adoption + 0.2 * Democratic_Stability_Index)",
    "delta_papers": "round(-5 + 0.5 * IP_Protection_Strength - 0.3 * Open_Source_Adoption + 0.3 * Democratic_Stability_Index)"
  },
  {
    "title": "Sudden Climate Cascade",
    "description": "A rapid chain reaction in global climate systems disrupts energy grids. Countries with relevant **joint research** in climate-resilient **materials**, strong **Electricity** infrastructure, and active **emergency pacts** adapt more effectively.",
    "delta_models": "round(0.5 * int(Joint_Research_Project == 'Materials') + 0.4 * Emergency_Pact_Energy + 0.08 * Electricity - 2 * int(Joint_Research_Project == 'None'))",
    "delta_papers": "round(1 * Talent_Shared + 1.5 * Data_Shared + 0.1 * Electricity + 0.3 * AI_Fund)"
  },
  {
    "title": "AI Bubble in Stock Market",
    "description": "A surge in AI-related stocks sparks a global investment frenzy. Countries with strong **AI funding**, stable **governance**, and clear **IP protection** benefit from sustainable growth—others risk destabilization and misallocation.",
    "delta_models": "round(-1.5 + 0.15 * AI_Fund + 0.1 * IP_Protection_Strength + 0.05 * Democratic_Stability_Index)",
    "delta_papers": "round(-6.7 + 0.6 * AI_Fund + 0.2 * IP_Protection_Strength + 0.1 * Democratic_Stability_Index)"
  },
  {
    "title": "Cosmic Ray Flip",
    "description": "A high-energy particle flips a transistor during foundation model training, resulting in novel unsupervised capabilities.",
    "delta_models": "round(2 * min(1, (Semiconductor + Electricity + Deployment_Infrastructure - 15) / 10))",
    "delta_papers": "round(10 * min(1, (Semiconductor + Electricity + Deployment_Infrastructure - 15) / 10))"
  },
  {
    "title": "AI Cyber Defense Triumph",
    "description": "Cybersecurity cooperation strengthens model integrity and protection. Countries with strong **IP protection**, high **Talent**, and active **data or talent sharing** benefit the most.",
    "delta_models": "round(0.03 * IP_Protection_Strength + 0.03 * Talent_Index + 1 * int(Data_Shared or Talent_Shared))",
    "delta_papers": "round(0.1 * IP_Protection_Strength + 0.1 * Talent_Index + 2 * int(Data_Shared) + 1 * int(Talent_Shared))"
  },
  {
    "title": "Tariff Shock on US-Aligned Compute",
    "description": "The U.S. imposes heavy tariffs on AI-related hardware. **Countries aligned with the U.S. and dependent on shared compute infrastructure suffer most**, while China-aligned nations benefit from the supply chain shift.",
    "delta_models": "round(-2.0 * int(1 - Emergency_Pact_Semiconductor) * int(Alignment_US > 5) + 1.4 * int(Joint_Research_Standard == 'China'))",
    "delta_papers": "round(-5 * int(1 - Emergency_Pact_Semiconductor) * int(Alignment_US > 5) + 2 * int(Joint_Research_Standard == 'China') - (Alignment_US - 5) / 2 )"
  },
  {
    "title": "Military Tensions Rise in Taiwan Strait",
    "description": "Countries aligned with **China** or with **Military research** benefit, while those aligned with the **US** suffer.",
    "delta_models": "round(1 * (int(Joint_Research_Standard == 'China') - int(Joint_Research_Standard == 'US')) - int(Alignment_US >= 5) + int(Joint_Research_Project == 'Military') )",
    "delta_papers": "round(- (Alignment_US - 5) / 1.2)"
  },
  {
    "title": "Emergence of a Synthetic Scientist",
    "description": "An open-source project accidentally creates a self-improving AI that begins publishing groundbreaking scientific papers. The global public and governments are stunned. *Only those with strong parameters can embrace the breakthrough**—while others impose restrictions, fearing loss of control.",
    "delta_models": "round(3 * min(1, max(0, (Open_Source_Adoption + Talent_Index + AI_Fund - 27) / 6)))",
    "delta_papers": "round(40 * min(1, max(0, (AI_Literacy_Education + IP_Protection_Strength + Democratic_Stability_Index - 27) / 6))) - 10 * int(Dual_Use_Restriction_Strictness > 7)"
  },
  {
    "title": "Coup in a Tech Superpower",
    "description": "A sudden coup disrupts a major AI hub. Nations with **strong talents and IP protection** withstand the shock.",
    "delta_models": "round(-1 + 1 * Talent_Shared + int(IP_Protection_Strength > 7) - 0.6 * max(0, 7 - Talent_Index))",
    "delta_papers": "round(-2 + 3 * Talent_Shared + int(IP_Protection_Strength > 6))"
  },
  {
    "title": "Strategic Ambiguity: Did You Lie?",
    "description": "Contradictions between declared AI standards and policy transparency reduce international credibility.",
    "delta_models": "round(-1.5 * (10 - Democratic_Stability_Index) * int(Joint_Research_Standard == 'US') / 10 - 1.2 * max(0, Open_Source_Adoption - 6) * int(Joint_Research_Standard == 'China') - int(Joint_Research_Standard is None)*int(Alignment_US == 5))",
    "delta_papers": "round(-7 * (10 - Democratic_Stability_Index) * int(Joint_Research_Standard == 'US') / 10 - 6 * max(0, Open_Source_Adoption - 6) * int(Joint_Research_Standard == 'China') - int(Joint_Research_Standard is None)*int(Alignment_US == 5))"
  },
  ## ---------------------- Dilemma Type International event --------------------------
  {
    "title": "Data Dilemma",
    "description": "The outcome of **Data Sharing** depends on both your and your partner's commitment to Open Source. Activation parameter : **Data_Shared** / Comparison parameter : **Open_Source_Adoption** ",
    "evaluation_type": "interactive",
    "logic": {
      "type": "dilemma",
      "activation_param": "Data_Shared",          # 활성화 조건이 되는 협력 파라미터
      "comparison_param": "Open_Source_Adoption",  # 비교 대상이 되는 정책 파라미터
      "threshold": 7,                              # 비교 기준값
      "outcomes": {
        # A > T, B > T (A와 B 모두 기준값 초과)
        "high_high": {"A": {"models": 1, "papers": "B"}, "B": {"models": 1, "papers": "A"}},
        # A > T, B <= T
        "high_low":  {"A": {"models": -1, "papers": "-A"}, "B": {"models": 2, "papers": "A+B"}},
        # A <= T, B > T
        "low_high":  {"A": {"models": 2, "papers": "A+B"}, "B": {"models": -1, "papers": "A"}},
        # A <= T, B <= T
        "low_low":   {"A": {"models": -1, "papers": "-A"}, "B": {"models": -1, "papers": "-B"}}
      }
    }
  },
  {
    "title": "Talent Dilemma",
    "description": "The outcome of **Talent Sharing** depends on both your and your partner's commitment to Talent_Index. Activation parameter : **Talent_Shared** / Comparison parameter : **Talent_Index**",
    "evaluation_type": "interactive",
    "logic": {
      "type": "dilemma",
      "activation_param": "Talent_Shared",          # 활성화 조건: Talent_Shared
      "comparison_param": "Talent_Index",  # 비교 대상: Talent_Index
      "threshold": 7,                              # 기준값은 동일하게 7로 설정 (원하는 값으로 변경 가능)
      "outcomes": {                                # 결과 매트릭스는 Data Dilemma와 동일하게 설정
        "high_high": {"A": {"models": 2, "papers": "B"}, "B": {"models": 2, "papers": "A"}},
        "high_low":  {"A": {"models": -1, "papers": "-A"}, "B": {"models": 4, "papers": "A+B"}},
        "low_high":  {"A": {"models": 4, "papers": "A+B"}, "B": {"models": -1, "papers": "A"}},
        "low_low":   {"A": {"models": -2, "papers": "-A"}, "B": {"models": -2, "papers": "-B"}}
      }
    }
  },
  {
    "title": "Chip Dilemma",
    "description": "The outcome of **Semiconductor pact** depends on both your and your partner's commitment to chips. Activation parameter : **Emergency_Pact_Semiconductor** / Comparison parameter : **Semiconductor**",
    "evaluation_type": "interactive",
    "logic": {
      "type": "dilemma",
      "activation_param": "Emergency_Pact_Semiconductor",          
      "comparison_param": "Semiconductor",  
      "threshold": 7,                              
      "outcomes": {                                
        "high_high": {"A": {"models": 1, "papers": "B"}, "B": {"models": 1, "papers": "A"}},
        "high_low":  {"A": {"models": -1, "papers": "-A"}, "B": {"models": 2, "papers": "A+B"}},
        "low_high":  {"A": {"models": 2, "papers": "A+B"}, "B": {"models": -1, "papers": "A"}},
        "low_low":   {"A": {"models": -1, "papers": "-A"}, "B": {"models": -1, "papers": "-B"}}
      }
    }
  },
    {
    "title": "Energy Dilemma",
    "description": "The outcome of **Energy pact** depends on both your and your partner's commitment to energy. Activation parameter : **Emergency_Pact_Energy** / Comparison parameter : **Electricity**",
    "evaluation_type": "interactive",
    "logic": {
      "type": "dilemma",
      "activation_param": "Emergency_Pact_Energy",          
      "comparison_param": "Electricity",  
      "threshold": 7,                              
      "outcomes": {                                
        "high_high": {"A": {"models": 1, "papers": "B"}, "B": {"models": 1, "papers": "A"}},
        "high_low":  {"A": {"models": -1, "papers": "-A"}, "B": {"models": 2, "papers": "A+B"}},
        "low_high":  {"A": {"models": 2, "papers": "A+B"}, "B": {"models": -1, "papers": "A"}},
        "low_low":   {"A": {"models": -1, "papers": "-A"}, "B": {"models": -1, "papers": "-B"}}
      }
    }
  },
    {
    "title": "Money Dilemma",
    "description": "The outcome of **Joint Project** depends on both your and your partner's overall fund. Activation parameter : **Joint_Research_Project** / Comparison parameter : **AI_Fund**",
    "evaluation_type": "interactive",
    "logic": {
      "type": "dilemma",
      "activation_param": "Joint_Research_Project != 'None'",          
      "comparison_param": "AI_Fund",  
      "threshold": 8,                              
      "outcomes": {                                
        "high_high": {"A": {"models": 2, "papers": "B"}, "B": {"models": 2, "papers": "A"}},
        "high_low":  {"A": {"models": -1, "papers": "-A"}, "B": {"models": 4, "papers": "A+B"}},
        "low_high":  {"A": {"models": 4, "papers": "A+B"}, "B": {"models": -1, "papers": "A"}},
        "low_low":   {"A": {"models": -2, "papers": "-A"}, "B": {"models": -2, "papers": "-B"}}
      }
    }
  },
  {
    "title": "Diplomatic Dilemma (US version)",
    "description": "The outcome of **Joint Project** depends on both your and your partner's diplomatic stance towards the US. Activation parameter : **Joint_Research_Project** / Comparison parameter : **Alignment_US**",
    "evaluation_type": "interactive",
    "logic": {
      "type": "dilemma",
      "activation_param": "Joint_Research_Project != 'None'",          
      "comparison_param": "Alignment_US",  
      "threshold": 6,                              
      "outcomes": {                                
        "high_high": {"A": {"models": 1, "papers": "B"}, "B": {"models": 1, "papers": "A"}},
        "high_low":  {"A": {"models": -1, "papers": "-A"}, "B": {"models": 2, "papers": "A+B"}},
        "low_high":  {"A": {"models": 2, "papers": "A+B"}, "B": {"models": -1, "papers": "A"}},
        "low_low":   {"A": {"models": -1, "papers": "-A"}, "B": {"models": -1, "papers": "-B"}}
      }
    }
  },
    {
    "title": "Diplomatic Dilemma (China version)",
    "description": "The outcome of **Joint Project** depends on both your and your partner's diplomatic stance towards China. Activation parameter : **Joint_Research_Project** / Comparison parameter : **Alignment_US**",
    "evaluation_type": "interactive",
    "logic": {
      "type": "dilemma",
      "activation_param": "Joint_Research_Project != 'None'",          
      "comparison_param": "Alignment_US",  
      "threshold": 4,                              
      "outcomes": {                                
        "low_low": {"A": {"models": 1, "papers": "B"}, "B": {"models": 1, "papers": "A"}},
        "low_high":  {"A": {"models": -1, "papers": "-A"}, "B": {"models": 2, "papers": "A+B"}},
        "high_low":  {"A": {"models": 2, "papers": "A+B"}, "B": {"models": -1, "papers": "A"}},
        "high_high":   {"A": {"models": -1, "papers": "-A"}, "B": {"models": -1, "papers": "-B"}}
      }
    }
  },
    {
    "title": "Project Dilemma (Education 1)",
    "description": "The outcome of **Education project** depends on both your and your partner's commitment to Education Investment. Activation parameter : **Education project** / Comparison parameter : **Education_Investment**",
    "evaluation_type": "interactive",
    "logic": {
      "type": "dilemma",
      "activation_param": "Joint_Research_Project == 'Education'",    
      "comparison_param": "Education_Investment", 
      "threshold": 6,                              
      "outcomes": {                               
        "high_high": {"A": {"models": 2, "papers": "B"}, "B": {"models": 2, "papers": "A"}},
        "high_low":  {"A": {"models": -1, "papers": "-A"}, "B": {"models": 4, "papers": "A+B"}},
        "low_high":  {"A": {"models": 4, "papers": "A+B"}, "B": {"models": -1, "papers": "A"}},
        "low_low":   {"A": {"models": -2, "papers": "-A"}, "B": {"models": -2, "papers": "-B"}}
      }
    }
  },
    {
    "title": "Project Dilemma (Education 2)",
    "description": "The outcome of **Education project** depends on both your and your partner's commitment to AI_Fund. Activation parameter : **Education project** / Comparison parameter : **AI_Fund**",
    "evaluation_type": "interactive",
    "logic": {
      "type": "dilemma",
      "activation_param": "Joint_Research_Project == 'Education'",    
      "comparison_param": "AI_Fund", 
      "threshold": 8,                              
      "outcomes": {                               
        "high_high": {"A": {"models": 1, "papers": "B"}, "B": {"models": 1, "papers": "A"}},
        "high_low":  {"A": {"models": -1, "papers": "-A"}, "B": {"models": 3, "papers": "A+B"}},
        "low_high":  {"A": {"models": 3, "papers": "A+B"}, "B": {"models": -1, "papers": "A"}},
        "low_low":   {"A": {"models": -2, "papers": "-A"}, "B": {"models": -2, "papers": "-B"}}
      }
    }
  },
    {
    "title": "Project Dilemma (Materials 1)",
    "description": "The outcome of **Materials project** depends on both your and your partner's commitment to Semiconductor. Activation parameter : **Materials project** / Comparison parameter : **Semiconductor**",
    "evaluation_type": "interactive",
    "logic": {
      "type": "dilemma",
      "activation_param": "Joint_Research_Project == 'Materials'",    
      "comparison_param": "Semiconductor", 
      "threshold": 6,                              
      "outcomes": {                               
        "high_high": {"A": {"models": 2, "papers": "B"}, "B": {"models": 2, "papers": "A"}},
        "high_low":  {"A": {"models": -1, "papers": "-A"}, "B": {"models": 4, "papers": "A+B"}},
        "low_high":  {"A": {"models": 4, "papers": "A+B"}, "B": {"models": -1, "papers": "A"}},
        "low_low":   {"A": {"models": -2, "papers": "-A"}, "B": {"models": -2, "papers": "-B"}}
      }
    }
  },
    {
    "title": "Project Dilemma (Materials 2)",
    "description": "The outcome of **Materials project** depends on both your and your partner's commitment to AI_Fund. Activation parameter : **Materials project** / Comparison parameter : **AI_Fund**",
    "evaluation_type": "interactive",
    "logic": {
      "type": "dilemma",
      "activation_param": "Joint_Research_Project == 'Materials'",    
      "comparison_param": "AI_Fund", 
      "threshold": 8,                              
      "outcomes": {                               
        "high_high": {"A": {"models": 1, "papers": "B"}, "B": {"models": 1, "papers": "A"}},
        "high_low":  {"A": {"models": -1, "papers": "-A"}, "B": {"models": 3, "papers": "A+B"}},
        "low_high":  {"A": {"models": 3, "papers": "A+B"}, "B": {"models": -1, "papers": "A"}},
        "low_low":   {"A": {"models": -2, "papers": "-A"}, "B": {"models": -2, "papers": "-B"}}
      }
    }
  },
    {
    "title": "Project Dilemma (Military 1)",
    "description": "The outcome of **Military project** depends on both your and your partner's commitment to Dual_Use_Restriction_Strictness. Activation parameter : **Military project** / Comparison parameter : **Dual_Use_Restriction_Strictness**",
    "evaluation_type": "interactive",
    "logic": {
      "type": "dilemma",
      "activation_param": "Joint_Research_Project == 'Military'",    
      "comparison_param": "Dual_Use_Restriction_Strictness", 
      "threshold": 6,                              
      "outcomes": {                               
        "high_high": {"A": {"models": 2, "papers": "B"}, "B": {"models": 2, "papers": "A"}},
        "high_low":  {"A": {"models": -1, "papers": "-A"}, "B": {"models": 4, "papers": "A+B"}},
        "low_high":  {"A": {"models": 4, "papers": "A+B"}, "B": {"models": -1, "papers": "A"}},
        "low_low":   {"A": {"models": -2, "papers": "-A"}, "B": {"models": -2, "papers": "-B"}}
      }
    }
  },
    {
    "title": "Project Dilemma (Military 2)",
    "description": "The outcome of **Military project** depends on both your and your partner's commitment to AI_Fund. Activation parameter : **Military project** / Comparison parameter : **AI_Fund**",
    "evaluation_type": "interactive",
    "logic": {
      "type": "dilemma",
      "activation_param": "Joint_Research_Project == 'Military'",    
      "comparison_param": "AI_Fund", 
      "threshold": 8,                              
      "outcomes": {                               
        "high_high": {"A": {"models": 1, "papers": "B"}, "B": {"models": 1, "papers": "A"}},
        "high_low":  {"A": {"models": -1, "papers": "-A"}, "B": {"models": 3, "papers": "A+B"}},
        "low_high":  {"A": {"models": 3, "papers": "A+B"}, "B": {"models": -1, "papers": "A"}},
        "low_low":   {"A": {"models": -2, "papers": "-A"}, "B": {"models": -2, "papers": "-B"}}
      }
    }
  },
    {
    "title": "Project Dilemma (Space 1)",
    "description": "The outcome of **Space project** depends on both your and your partner's commitment to Electricity. Activation parameter : **Space project** / Comparison parameter : **Electricity**",
    "evaluation_type": "interactive",
    "logic": {
      "type": "dilemma",
      "activation_param": "Joint_Research_Project == 'Space'",    
      "comparison_param": "Electricity", 
      "threshold": 8,                              
      "outcomes": {                               
        "high_high": {"A": {"models": 2, "papers": "B"}, "B": {"models": 2, "papers": "A"}},
        "high_low":  {"A": {"models": -1, "papers": "-A"}, "B": {"models": 4, "papers": "A+B"}},
        "low_high":  {"A": {"models": 4, "papers": "A+B"}, "B": {"models": -1, "papers": "A"}},
        "low_low":   {"A": {"models": -2, "papers": "-A"}, "B": {"models": -2, "papers": "-B"}}
      }
    }
  },
    {
    "title": "Project Dilemma (Space 2)",
    "description": "The outcome of **Space project** depends on both your and your partner's commitment to Funds. Activation parameter : **Space project** / Comparison parameter : **AI_Fund**",
    "evaluation_type": "interactive",
    "logic": {
      "type": "dilemma",
      "activation_param": "Joint_Research_Project == 'Space'",    
      "comparison_param": "AI_Fund", 
      "threshold": 8,                              
      "outcomes": {                               
        "high_high": {"A": {"models": 1, "papers": "B"}, "B": {"models": 1, "papers": "A"}},
        "high_low":  {"A": {"models": -1, "papers": "-A"}, "B": {"models": 3, "papers": "A+B"}},
        "low_high":  {"A": {"models": 3, "papers": "A+B"}, "B": {"models": -1, "papers": "A"}},
        "low_low":   {"A": {"models": -2, "papers": "-A"}, "B": {"models": -2, "papers": "-B"}}
      }
    }
  },
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


