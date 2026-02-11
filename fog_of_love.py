import streamlit as st

# Data from your AI Studio prompt
CHARACTER_DATA = {
    # ... Paste your dictionary here ...
}

# --- PASTE THIS BELOW YOUR CHARACTER_DATA DICTIONARY ---

st.title("🕵️ Fog of Love: Dossier")

# 1. Player Selection
player_name = st.text_input("Enter your real name:")
# Add a default option so the app doesn't error on load
selected_char = st.selectbox("Assign your character:", ["-- Select --"] + list(CHARACTER_DATA.keys()))

if selected_char != "-- Select --":
    char = CHARACTER_DATA[selected_char]
    
    st.header(f"Character: {selected_char}")
    st.subheader(f"Occupation: {char['Career']}")
    
    # 2. Public Traits
    st.write(f"**Your Traits:** {', '.join(char['Traits'])}")
    st.write(f"**What you seek:** {char['Seeks']}")
    
    # 3. Hidden Info
    with st.expander("👁️ VIEW YOUR SECRET"):
        st.error(f"Secret: {char['Secret']}")
        st.warning(f"Dealbreaker: {char['Dealbreaker']}")

    # 4. Known Intel
    st.subheader("🔍 Intel on Others")
    for fact in char['Known Intel']:
        st.info(fact)

# --- DETECTIVE'S NOTEBOOK ---
st.markdown("---")
st.subheader("🕵️ Detective's Notebook")

with st.expander("📝 Open Investigation Log"):
    st.caption("Use this to track your progress. Data resets if you refresh!")
    
    st.write("**❌ Eliminate Suspects:**")
    col1, col2 = st.columns(2)
    all_suspects = list(CHARACTER_DATA.keys())
    
    # This loop creates the checkboxes
    for i, person in enumerate(all_suspects):
        if i % 2 == 0:
            col1.checkbox(person, key=f"elim_{person}")
        else:
            col2.checkbox(person, key=f"elim_{person}")

    st.write("**📝 Mission Notes:**")
    st.text_area("Type findings here...", height=150, key="player_notes")

# --- ADMIN PANEL ---
st.markdown("---")
st.header("💘 The Rose Ceremony (Admin Only)")

if st.checkbox("Open Scoring Panel"):
    
    # Scoring Logic
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
            score = 0
            result_text = ""
            
            if p2 == "Single":
                score = 1
                result_text = "🦄 Single & Safe (+1)"
            else:
                data = MATCH_LOGIC[p1]
                if p2 == data['optimal']:
                    score = 3
                    result_text = "⭐ PERFECT MATCH (+3)"
                elif p2 in data['compatible']:
                    score = 2
                    result_text = "🟢 Compatible (+2)"
                elif p2 in data['disaster']:
                    score = -2
                    result_text = "🔴 DISASTER (-2)"
                else:
                    score = 0
                    result_text = "⚪ Neutral (0)"
            
            st.success(f"Result for {p1}: {result_text}")
        else:
            st.error("Please select a character first.")