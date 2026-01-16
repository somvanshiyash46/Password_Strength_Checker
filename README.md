# 🔐 Password Strength Checker (Python)

The **Password Strength Checker** is a Python-based cybersecurity tool that evaluates the strength of a password using multiple security checks such as length validation, character diversity, entropy calculation, dictionary attacks, sequence detection, and password reuse prevention.

This project is ideal for **cybersecurity students, ethical hackers, SOC analysts, and secure application developers**.

---

## 🛠️ Technologies Used

- Python 3
- Regular Expressions (`re`)
- Mathematical entropy calculation (`math`)

---

## 📂 Project Structure

Password-Strength-Checker/
│
├── password_strength_checker.py # Basic password strength checker
├── advanced.py # Advanced checker with entropy & history
└── README.md # Documentation


---

## 🚀 Execution Steps (Step-by-Step)

### ✅ Step 1: Install Python

Check whether Python is installed:
```bash
python --version

Expected Output:

Python 3.x.x


If not installed, download from:
https://www.python.org/downloads/

✅ Step 2: Clone the Repository
git clone https://github.com/your-username/password-strength-checker.git
cd password-strength-checker


Expected Output:

Cloning into 'password-strength-checker'...

▶️ Execution – Basic Version
✅ Step 3: Run Basic Password Strength Checker
python password_strength_checker.py


Expected Input:

Enter a password to check its strength:


Example Input:

Hello@123


Expected Output:

Password strength: Strong

▶️ Execution – Advanced Version
✅ Step 4: Run Advanced Password Strength Checker
python advanced.py


Expected Input:

Enter a password to check its strength:


Example Input:

P@ssw0rd123


Expected Output:

Password strength: Strong
Password entropy: 62.45 bits

Suggestions to improve your password:
- Password should not contain dictionary words.
- Increase password length for better security.
