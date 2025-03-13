import streamlit as st # type: ignore
import re
import random
import string

def check_password_strength(password):
    score = 0
    feedback = []
    
    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")
    
    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Include both uppercase and lowercase letters.")
    
    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Add at least one number (0-9).")
    
    # Special Character Check
    if re.search(r"[!@#$%^&*()_+=\-\[\]{}|;:'\",.<>?/`~]", password):
        score += 1
    else:
        feedback.append("Include at least one special character (!@#$%^&* and more).")
    
    # Strength Rating
    if score == 4:
        return "✅ Strong Password!", feedback, "#5cb85c", 1.0
    elif score == 3:
        return "⚠️ Moderate Password - Consider adding more security features.", feedback, "#f0ad4e", 0.75
    elif score == 2:
        return "⚠️ Weak Password - Add more security elements.", feedback, "#f0ad4e", 0.5
    else:
        return "❌ Very Weak Password - Improve it using the suggestions above.", feedback, "#d9534f", 0.25

def generate_strong_password(length=12):
    characters = string.ascii_letters + string.digits + "!@#$%^&*()_+=-[]{}|;:'\",.<>?/`~"
    return ''.join(random.choice(characters) for _ in range(length))

# Streamlit UI
st.set_page_config(page_title="Password Strength Meter", page_icon="🔒", layout="centered")

st.markdown("""
    <style>
        .stApp { background-color: #d7e8f7; }
        .feedback { color: #d9534f; font-weight: bold; }
        .success { color: #5cb85c; font-weight: bold; }
        .moderate { color: #f0ad4e; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center;'>🔒 Password Strength Meter</h1>", unsafe_allow_html=True)

with st.container():
    password = st.text_input("Enter your password:", type="password", placeholder="Type your password here...")
    
    if st.button("Check Strength", key="check", help="Click to evaluate password strength"):
        if password:
            strength, feedback, color, strength_ratio = check_password_strength(password)
            st.markdown(f"<p style='color:{color}; font-weight:bold;'>{strength}</p>", unsafe_allow_html=True)
            for tip in feedback:
                st.markdown(f"<p class='feedback'>{tip}</p>", unsafe_allow_html=True)
            
            # Password Strength Bar
            st.progress(strength_ratio)
        else:
            st.warning("Please enter a password to check.")

    st.markdown("---")
    
    length = st.slider("Select password length:", min_value=8, max_value=20, value=12)
    if st.button("Generate Strong Password", key="generate", help="Click to generate a strong password"):
        strong_password = generate_strong_password(length)
        with st.expander("Click to reveal your strong password"):
            st.code(strong_password, language='')
