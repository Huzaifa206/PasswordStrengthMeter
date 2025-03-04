import streamlit as st
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
        feedback.append(" Password should be at least 8 characters long.")
    
    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append(" Include both uppercase and lowercase letters.")
    
    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append(" Add at least one number (0-9).")
    
    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append(" Include at least one special character (!@#$%^&*).")
    
    # Strength Rating
    if score == 4:
        return "✅ Strong Password!", feedback
    elif score == 3:
        return "⚠️ Moderate Password - Consider adding more security features.", feedback
    else:
        return "❌ Weak Password - Improve it using the suggestions above.", feedback

def generate_strong_password(length=12):
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(characters) for _ in range(length))

# Streamlit UI
st.set_page_config(page_title="Password Strength Meter", page_icon="🔒", layout="centered")

st.markdown(
    """
    <style>
        .stApp {
            background-color: #d7e8f7;
        }
        .feedback {
            color: #d9534f;
            font-weight: bold;
        }
        .success {
            color: #5cb85c;
            font-weight: bold;
        }
        .moderate {
            color: #f0ad4e;
            font-weight: bold;
        }
        .button {
            background-color: #0275d8 !important;
            color: white !important;
            font-size: 16px;
            border-radius: 5px;
            padding: 10px;
            margin-top: 10px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<h1 style='text-align: center; font-size: 36px;'>🔒 Password Strength Meter</h1>", unsafe_allow_html=True)


with st.container():
    
    password = st.text_input("Enter your password:", type="password", placeholder="Type your password here...")

    
    if st.button("Check Strength", key="check", help="Click to evaluate password strength"):
        if password:
            strength, feedback = check_password_strength(password)
            color_class = "success" if "Strong" in strength else "moderate" if "Moderate" in strength else "feedback"
            st.markdown(f"<p class='{color_class}'>{strength}</p>", unsafe_allow_html=True)
            for tip in feedback:
                st.markdown(f"<p class='feedback'>{tip}</p>", unsafe_allow_html=True)
        else:
            st.warning("Please enter a password to check.")
    
    if st.button("Generate Strong Password", key="generate", help="Click to generate a strong password"):
        strong_password = generate_strong_password()
        st.success(f"Suggested Strong Password: `{strong_password}`")
    
    st.markdown("</div>", unsafe_allow_html=True)
