import streamlit as st

# Data from your AI Studio prompt
CHARACTER_DATA = {
    # ... Paste your dictionary here ...
}

st.title("🕵️ Fog of Love: Dossier")

# 1. Player Selection
player_name = st.text_input("Enter your real name:")
selected_char = st.selectbox("Assign your character:", ["-- Select --"] + list(CHARACTER_DATA.keys()))

if selected_char != "-- Select --":
    char = CHARACTER_DATA[selected_char]
    
    st.header(f"Character: {selected_char}")
    st.subheader(f"Occupation: {char['Career']}")
    
    # 2. Public Traits
    st.write(f"**Your Traits:** {', '.join(char['Traits'])}")
    st.write(f"**What you seek:** {char['Seeks']}")
    
    # 3. Hidden Info (Expanders are perfect for bars!)
    with st.expander("👁️ VIEW YOUR SECRET"):
        st.error(f"Secret: {char['Secret']}")
        st.warning(f"Dealbreaker: {char['Dealbreaker']}")

    # 4. Known Intel
    st.subheader("🔍 Intel on Others")
    for fact in char['Known Intel']:
        st.info(fact)