
import streamlit as st
from okey_logic import find_combinations, recommend_discard

st.set_page_config(page_title="Metin2 Okey-Karten-Analyse", layout="centered")
st.title("🃏 Metin2 Okey-Karten-Analyse")

st.markdown("Gib bis zu 5 Handkarten ein (Format z. B. `4r`, `5b`, `1y`).")

cards = []
cols = st.columns(5)
for i in range(5):
    with cols[i]:
        card = st.text_input(f"Karte {i+1}", key=f"card_{i}")
        if card:
            cards.append(card.strip().lower())

if st.button("🔍 Analyse starten"):
    combinations = find_combinations(cards)
    if combinations:
        st.success("✅ Gültige Kombination(en) gefunden!")
        for combo in combinations:
            st.write(" + ".join(f"{v}{c}" for v, c in combo))
    else:
        st.warning("❌ Keine gültige Kombination gefunden.")
        discard = recommend_discard(cards)
        if discard:
            st.info(f"💡 Vorschlag: Wirf **{discard}** ab.")
        else:
            st.info("Keine Empfehlung möglich.")
