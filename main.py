import streamlit as st

from src.character_generator import generate_character

st.set_page_config(page_title="Wow Race & Class Generator")


st.title("WoW Classic 2024")
st.header("Character Generator")


faction = st.selectbox("Select your faction", ["Alliance", "Horde", "Random"])

if st.button("Generate your new character"):
    character, img = generate_character(faction)
    # Centralise text and write large font
    st.divider()
    st.markdown("<p style='text-align: center; font-size: 40px'>A new hero of Azeorth is born</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center; font-size: 38px; color: gold'>{character}</p>", unsafe_allow_html=True)
    st.divider()
    if img != "":
        st.image(img)



placeholder = st.empty()
with placeholder.container():

    reset_btn = st.button("Reset")

if reset_btn:
    placeholder.empty()