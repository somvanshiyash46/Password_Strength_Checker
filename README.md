```md
# 🔐 Password Strength Checker (Python)

The **Password Strength Checker** is a Python-based cybersecurity tool that evaluates the strength of a password using multiple security checks such as length validation, character diversity, entropy calculation, dictionary attack prevention, and password reuse detection.

---

## 🛠️ Technologies Used

- Python 3
- Regular Expressions (`re`)
- Math library (`math`)

---

## 📂 Project Structure



Password-Strength-Checker/
│
├── password_strength_checker.py
├── advanced.py
└── README.md



---

## 🚀 Execution Steps (Copy–Paste Friendly)

### Step 1: Check Python Installation
```bash
python --version
````

Expected Output:

```
Python 3.x.x
```

---

### Step 2: Run Basic Password Checker

```bash
python password_strength_checker.py
```

Expected Input:

```
Enter a password to check its strength:
```

Example Input:

```
Hello@123
```

Expected Output:

```
Password strength: Strong
```

---

### Step 3: Run Advanced Password Checker

```bash
python advanced.py
```

Expected Input:

```
Enter a password to check its strength:
```

Example Input:

```
P@ssw0rd123
```

Expected Output:

```
Password strength: Strong
Password entropy: 62.45 bits

Suggestions to improve your password:
- Password should not contain dictionary words.
- Increase password length for better security.
```

---

## 🔍 Password Strength Levels

| Score | Strength    |
| ----- | ----------- |
| 0 – 2 | Very Weak   |
| 3 – 4 | Weak        |
| 5 – 6 | Moderate    |
| 7 – 8 | Strong      |
| 9+    | Very Strong |

---

## 🔐 Security Checks Implemented

* Minimum length validation
* Uppercase & lowercase letters
* Numbers & special characters
* Sequential pattern detection
* Repeating character detection
* Dictionary word detection
* Password entropy calculation
* Password reuse prevention

---

## 🧪 Sample Inputs & Outputs

### Weak Password

Input:

```
password123
```

Output:

```
Password strength: Weak
```

---

### Strong Password

Input:

```
S3cur3@Pass!98
```

Output:

```
Password strength: Very Strong
```

---

## 👨‍💻 Author

**Yash Somvanshi**
Cybersecurity Student | Ethical Hacker | SOC Analyst Aspirant

---



```

---


