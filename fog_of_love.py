import streamlit as st

# --- 1. THE DATA ---
CHARACTER_DATA = {
    "AURELIAN": {
        "Career": "Tech CEO",
        "Traits": ["Ambitious", "Charismatic", "Ruthless"],
        "Seeks": "Someone who challenges him",
        "Secret": "I’m technically bankrupt. My company is a fraud.",
        "Dealbreaker": "Laziness",
        "Known Intel": ["BRYN was fired from her last job.", "MIREK is hiding a criminal record."]
    },
    "BRYN": {
        "Career": "Defense Attorney",
        "Traits": ["Sharp", "Cynical", "Protective"],
        "Seeks": "Absolute loyalty",
        "Secret": "I lost a huge case on purpose to save a friend.",
        "Dealbreaker": "Betrayal",
        "Known Intel": ["NYSSA is not who she says she is.", "KAEL is cheating on his taxes."]
    },
    "CASSIA": {
        "Career": "Influencer",
        "Traits": ["Bubbly", "Observant", "Vain"],
        "Seeks": "Adoration",
        "Secret": "I’m 10 years older than I claim to be.",
        "Dealbreaker": "Being ignored",
        "Known Intel": ["IRIA hates children.", "ELOWEN is actually a spy."]
    },
    "DORIAN": {
        "Career": "Surgeon",
        "Traits": ["Precise", "Arrogant", "Cultured"],
        "Seeks": "Perfection",
        "Secret": "I have a tremor in my hand that I’m hiding.",
        "Dealbreaker": "Bad hygiene",
        "Known Intel": ["ORIN is in debt to the mafia.", "AURELIAN is lying about his wealth."]
    },
    "ELOWEN": {
        "Career": "Investigative Journalist",
        "Traits": ["Curious", "Skeptical", "Intense"],
        "Seeks": "The Truth",
        "Secret": "I’m writing an exposé on everyone in this room.",
        "Dealbreaker": "Lying",
        "Known Intel": ["LYRA is having an affair.", "CASSIA buys her followers."]
    },
    "FEN": {
        "Career": "Ex-Military",
        "Traits": ["Quiet", "Alert", "Disciplined"],
        "Seeks": "Peace",
        "Secret": "I’m currently AWOL (Absent Without Leave).",
        "Dealbreaker": "Loud noises",
        "Known Intel": ["DORIAN malpractice suit was settled out of court.", "MIREK is addicted to gambling."]
    },
    "IRIA": {
        "Career": "Gallery Owner",
        "Traits": ["Sophisticated", "Critical", "Cold"],
        "Seeks": "A Muse",
        "Secret": "I sell forgeries to rich tourists.",
        "Dealbreaker": "Bad taste",
        "Known Intel": ["CASSIA is actually broke.", "NYSSA is a government informant."]
    },
    "JAREK": {
        "Career": "Chef",
        "Traits": ["Passionate", "Volatile", "Creative"],
        "Seeks": "Passion",
        "Secret": "I lost my sense of taste after COVID.",
        "Dealbreaker": "Picky eaters",
        "Known Intel": ["BRYN defends guilty people knowingly.", "KAEL is planning to leave the country."]
    },
    "KAEL": {
        "Career": "Pilot",
        "Traits": ["Adventurous", "Flirty", "Unreliable"],
        "Seeks": "No strings attached",
        "Secret": "I’m grounded pending a drug test investigation.",
        "Dealbreaker": "Clinginess",
        "Known Intel": ["FEN has a fake passport.", "DORIAN is being sued."]
    },
    "LYRA": {
        "Career": "Musician",
        "Traits": ["Emotional", "Talented", "Dreamy"],
        "Seeks": "A Soulmate",
        "Secret": "I stole my hit song from my ex.",
        "Dealbreaker": "Cruelty",
        "Known Intel": ["ELOWEN is recording our conversations.", "AURELIAN is about to be arrested."]
    },
    "MIREK": {
        "Career": "Architect",
        "Traits": ["Visionary", "Stubborn", "Workaholic"],
        "Seeks": "Legacy",
        "Secret": "My buildings are structurally unsafe.",
        "Dealbreaker": "Disorder",
        "Known Intel": ["AURELIAN is a fraud.", "FEN is dangerous."]
    },
    "NYSSA": {
        "Career": "Hacker",
        "Traits": ["Rebellious", "Secretive", "Brilliant"],
        "Seeks": "A challenge",
        "Secret": "I deleted my own criminal record yesterday.",
        "Dealbreaker": "Technophobia",
        "Known Intel": ["IRIA is laundering money.", "ELOWEN knows too much."]
    },
    "ORIN": {
        "Career": "Politician",
        "Traits": ["Charming", "Manipulative", "Smooth"],
        "Seeks": "Power",
        "Secret": "I’m being blackmailed by an anonymous source.",
        "Dealbreaker": "Scandal",
        "Known Intel": ["DORIAN killed a patient.", "JAREK is stealing from the restaurant."]
    }
}

# --- 2. THE APP INTERFACE ---
st.title("🕵️ Fog of Love: Dossier")

# Player Selection
player_name = st.text_input("Enter your real name:")
selected_char = st.selectbox("Assign your character:", ["-- Select --"] + list(CHARACTER_DATA.keys()))

if selected_char != "-- Select --":
    char = CHARACTER_DATA[selected_char]
    
    st.header(f"Character: {selected_char}")
    st.subheader(f"Occupation: {char['Career']}")
    
    # Public Traits
    st.write(f"**Your Traits:** {', '.join(char['Traits'])}")
    st.write(f"**What you seek:** {char['Seeks']}")
    
    # Hidden Info
    with st.expander("👁️ VIEW YOUR SECRET"):
        st.error(f"Secret: {char['Secret']}")
        st.warning(f"Dealbreaker: {char['Dealbreaker']}")

    # Known Intel
    st.subheader("🔍 Intel on Others")
    for fact in char['Known Intel']:
        st.info(fact)

# --- 3. DETECTIVE'S NOTEBOOK ---
st.markdown("---")
st.subheader("🕵️ Detective's Notebook")

with st.expander("📝 Open Investigation Log"):
    st.caption("Use this to track your progress. Data resets if you refresh!")
    
    st.write("**❌ Eliminate Suspects:**")
    
    # The Grid Layout for Checkboxes
    col1, col2 = st.columns(2)
    all_suspects = list(CHARACTER_DATA.keys())
    
    for i, person in enumerate(all_suspects):
        if i % 2 == 0:
            col1.checkbox(person, key=f"elim_{person}")
        else:
            col2.checkbox(person, key=f"elim_{person}")

    st.write("**📝 Mission Notes:**")
    st.text_area("Type findings here...", height=150, key="player_notes")

# --- 4. ADMIN PANEL ---
st.markdown("---")
st.header("💘 The Rose Ceremony (Admin Only)")

if st.checkbox("Open Scoring Panel"):
    
    MATCH_LOGIC = {
        "AURELIAN": {"optimal": "MIREK", "compatible": ["LYRA", "DORIAN", "JAREK"], "disaster": ["IRIA", "BRYN", "NYSSA"]},
        "BRYN": {"optimal": "KAEL", "compatible": ["MIREK", "NYSSA", "CASSIA"], "disaster": ["JAREK", "ORIN", "AURELIAN"]},
        "CASSIA": {"optimal": "IRIA", "compatible": ["NYSSA", "ELOWEN", "LYRA"], "disaster": ["ORIN", "DORIAN", "JAREK"]},
        "DORIAN": {"optimal": "ORIN", "compatible": ["AURELIAN", "KAEL", "FEN"], "disaster": ["IRIA", "ELOWEN", "LYRA"]},
        "ELOWEN": {"optimal": "LYRA", "compatible": ["CASSIA", "IRIA", "NYSSA"], "disaster": ["FEN", "DORIAN", "KAEL"]},
        "FEN": {"optimal": "KAEL", "compatible": ["DORIAN", "MIREK", "LYRA"], "disaster": ["ELOWEN", "IRIA", "JAREK"]},
        "IRIA": {"optimal": "CASSIA", "compatible": ["ELOWEN", "NYSSA", "LYRA"], "disaster": ["DORIAN", "AURELIAN", "ORIN"]},
        "JAREK": {"optimal": "LYRA", "compatible": ["AURELIAN", "ORIN", "ELOWEN"], "disaster": ["BRYN", "KAEL", "FEN"]},
        "KAEL": {"optimal": "BRYN", "compatible": ["DORIAN", "FEN", "MIREK"], "disaster": ["JAREK", "ELOWEN", "ORIN"]},
        "LYRA": {"optimal": "ELOWEN", "compatible": ["AURELIAN", "CASSIA", "FEN"], "disaster": ["DORIAN", "BRYN", "KAEL"]},
        "MIREK": {"optimal": "AURELIAN", "compatible": ["FEN", "KAEL", "LYRA"], "disaster": ["NYSSA", "JAREK", "ELOWEN"]},
        "NYSSA": {"optimal": "CASSIA", "compatible": ["IRIA", "ELOWEN", "BRYN"], "disaster": ["AURELIAN", "ORIN", "FEN"]},
        "ORIN": {"optimal": "DORIAN", "compatible": ["JAREK", "AURELIAN", "KAEL"], "disaster": ["CASSIA", "IRIA", "NYSSA"]}
    }

    st.write("Enter the Final Couples to see who wins.")
    
    col_a, col_b = st.columns(2)
    with col_a:
        p1 = st.selectbox("Player 1 Character", ["--"] + list(MATCH_LOGIC.keys()), key="p1_score")
    with col_b:
        p2 = st.selectbox("Player 1's Choice", ["Single"] + list(MATCH_LOGIC.keys()), key="p2_score")

    if st.button("Calculate Match Score"):
        if p1 != "--":
            if p2 == "Single":
                st.success(f"Result for {p1}: 🦄 Single & Safe (+1)")
            else:
                data = MATCH_LOGIC[p1]
                if p2 == data['optimal']:
                    st.success(f"Result for {p1}: ⭐ PERFECT MATCH (+3)")
                elif p2 in data['compatible']:
                    st.success(f"Result for {p1}: 🟢 Compatible (+2)")
                elif p2 in data['disaster']:
                    st.error(f"Result for {p1}: 🔴 DISASTER (-2)")
                else:
                    st.info(f"Result for {p1}: ⚪ Neutral (0)")
        else:
            st.error("Please select a character first.")