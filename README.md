# 🔒 Password Strength Meter

## 📌 Overview
The **Password Strength Meter** is a simple yet effective web application built using **Python and Streamlit**. It allows users to check the strength of their passwords based on predefined security rules and provides feedback on how to improve weak passwords. Additionally, it includes a feature to generate strong passwords automatically.

## 🚀 Features
- ✅ **Check Password Strength**: Evaluates passwords based on length, uppercase/lowercase letters, numbers, and special characters.
- 🔐 **Generate Strong Passwords**: Suggests a secure password that meets all strength criteria.
- 🎨 **User-Friendly Interface**: Simple and intuitive UI with an attractive design.
- 📋 **Instant Feedback**: Provides real-time suggestions to improve password security.
- 📌 **Responsive Layout**: Optimized for different screen sizes.

## 🛠️ Technologies Used
- **Python** 🐍
- **Streamlit** 🌐 (for UI)
- **Regular Expressions (re module)** 🔍 (for password validation)
- **Random & String module** 🔢 (for password generation)
- **HTML & CSS** 🎨 (for styling)

## 🔧 Installation & Usage
Follow these steps to run the Password Strength Meter on your local machine:

### 1️⃣ Install Dependencies
Ensure you have **Python 3** installed, then install **Streamlit** using:
```bash
pip install streamlit
```

### 2️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/password-strength-meter.git
cd password-strength-meter
```

### 3️⃣ Run the Application
```bash
streamlit run app.py
```

## 📊 Password Strength Criteria
A password is evaluated based on the following rules:

| Strength Level | Criteria |
|--------------|--------------------------------------------------------------------------------|
| ❌ Weak      | Missing key elements such as length, uppercase/lowercase, numbers, or symbols |
| ⚠️ Moderate  | Has some security features but can be improved                                |
| ✅ Strong    | Meets all criteria: length (≥8), uppercase & lowercase letters, numbers, and symbols |


## 🏗️ Future Improvements
🔹 Add a database to check against commonly used passwords
🔹 Improve password generation with user-defined complexity levels
🔹 Dark mode support
🔹 Deploy the app online

---
💡 **Developed by Huzaifa Ahmed Siddiqui**

