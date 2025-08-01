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
            "Materials": 3, "Space": 3, "Biotics": 3
        }
    },
    "Joint_Research_DUR": {
        "desc": "Restrictions on military use or confidentiality agreements for joint research",
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
        "delta_papers": "-7 * (1 if IP_Protection_Strength < 6- else 0.5)"
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
}

# -------------------------------------------------------------
# International events
# ---------------------------------------------------------------

international_events = [
  {
    "title": "Theoretical Breakthrough in Algorithms",
    "description": "A new learning paradigm boosts efficiency and capability.",
    "delta_models": "round(1.5 * Data_Shared + 0.5 * int(Joint_Research_Project != 'None') + 0.2 * log(1 + Open_Source_Adoption))",
    "delta_papers": "round(10 * Data_Shared + 5 * int(Joint_Research_Project != 'None') + 0.4 * Open_Source_Adoption)"
  },
    {
    "title": "Trump",
    "description": "US-aligned countries with shared compute lose access to critical hardware, while others capitalize.",
    "delta_models": "round(-2 * int(Emergency_Pact_Semiconductor) * int(Joint_Research_Standard == 'US') + 1.5 * int(Joint_Research_Standard == 'China'))",
    "delta_papers": "round(-15 * int(Emergency_Pact_Semiconductor) * int(Joint_Research_Standard == 'US') + 10 * int(Joint_Research_Standard == 'China'))"
  },
    {
    "title": "China invades Taiwan",
    "description": "Countries aligned with China benefit; those aligned with the US and with strict civilian-only AI rules face penalties.",
    "delta_models": "round(2 * (int(Joint_Research_Standard == 'China') - int(Joint_Research_Standard == 'US')) + 1 * int(Joint_Research_DUR == 'No'))",
    "delta_papers": "round(10 * (int(Joint_Research_Standard == 'China') - int(Joint_Research_Standard == 'US')) - 5 * int(Joint_Research_DUR == 'Yes'))"
  },

]

international_events1 = [
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
    "delta_models": "max(-2, min(0, round(-1 * (1 - Shared_Research_Centers) + -1 * (1 - Joint_Project) + 0.3 * AI_Fund)))",
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
    "delta_models": "round(1.5 * Shared_Research_Centers + 0.3 * int(Joint_Project != 'No') + 0.2 * AI_Fund)",
    "delta_papers": "round(9 * Shared_Research_Centers + 5 * int(Joint_Project != 'No') + 0.4 * AI_Fund)"
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
    "delta_papers": "round(9 * int(Joint_Project == 'Materials') + 0.3 * AI_Fund)"
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
    "delta_papers": "round(10 * int(Joint_Project != 'No') + 0.3 * AI_Fund)"
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
    "delta_models": "round(3 * min(1, max(0, (Open_Source_Adoption + Talent_Index + AI_Fund - 27) / 6)))",
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


