import streamlit as st
from PasswordLogic import generate_password, check_strength

st.set_page_config(
    page_title="Strong Password Generator",
    page_icon="🔒",
    layout="centered"
)

st.title("🔒 Strong Password Generator")
st.markdown("Generate a secure, random password tailored to your needs.")


st.sidebar.header("Configuration")

length = st.sidebar.slider(
    label="Password length:",
    min_value=8,
    max_value=32,
    value=12,
    help="The longer the password, the more secure it is."
)

col1, col2 = st.sidebar.columns(2)

with col1:
    use_lower = st.checkbox("Lower case(a-z)", value=True)
    use_upper = st.checkbox("Upper case (A-Z)", value=True)

with col2:
    use_digits = st.checkbox("Numbers (0-9)", value=True)
    use_special = st.checkbox("Special marks (!@#%)", value=True)

if st.sidebar.button("🎲 Generate password", type="primary", use_container_width=True):


    try:
        generated_password = generate_password(
            length=length,
            use_lowercase=use_lower,
            use_uppercase=use_upper,
            use_digits=use_digits,
            use_special=use_special
        )
        st.header("Your password is:")
        st.code(generated_password, language="plaintext")

        st.button("📋 Copy to clipboard",
                  on_click=lambda: st.toast("✅ Password is copied to clipboard!"),
                  key="copy_button")

        strength = check_strength(generated_password)
        st.write(f"**Password strength:** {strength}")

    except ValueError as e:
        st.error(f"❌ {e}")

st.markdown("---")
st.markdown(

    unsafe_allow_html=True
)