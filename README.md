#  Multi-Level Password Authentication System

##  Project Overview

The Multi-Level Password Authentication System is a secure web application developed using Flask that enhances user authentication by implementing multiple layers of verification.

Unlike traditional systems that rely only on a password, this system uses a combination of authentication methods such as password validation, OTP verification, security questions, and symbol-based authentication.

This layered security approach significantly improves protection against unauthorized access and strengthens overall system reliability.

---

##  Objectives

* To implement a secure multi-factor authentication system
* To reduce unauthorized access using layered verification
* To demonstrate real-world security practices in web applications

---

##  Key Features

###  User Registration

* Register with username and password
* Set a security question and answer
* Choose a unique symbol for additional verification

---

###  Multi-Level Authentication Process

The system verifies users through the following steps:

1. **Password Verification**

   * Validates user credentials

2. **OTP Verification**

   * Generates a 6-digit One-Time Password
   * OTP expires within 30 seconds

3. **Security Question Verification**

   * User answers predefined question

4. **Symbol-Based Authentication**

   * User selects the correct symbol

Access is granted only after all levels are successfully completed.

---

###  Secure Dashboard

* Accessible only after successful authentication
* Ensures protected user environment

---

###  File Access & Modification

* Secure file access after login
* Controlled file modification
* Prevents unauthorized data access

---

##  Tech Stack

### Backend:

* Python
* Flask

### Frontend:

* HTML
* CSS

### Libraries:

* Flask
* Werkzeug

---

##  Project Structure

```id="mfa123"
app.py
templates/
static/
files/
requirements.txt
```

---

##  Installation & Setup

### 1️ Clone the repository

```id="mfa124"
git clone https://github.com/LakshmiBhavani-21/Multilevel-Password-Authentication.git
cd Multilevel-Password-Authentication
```

---

### 2️ Install dependencies

```id="mfa125"
pip install -r requirements.txt
```

---

### 3️ Run the application

```id="mfa126"
python app.py
```

---

### 4️ Open in browser

```id="mfa127"
http://127.0.0.1:5000
```

---

##  Security Highlights

* Multi-factor authentication improves security
* OTP with expiry prevents misuse
* Symbol-based verification adds extra protection
* Layered authentication reduces hacking risks

---

##  Screenshots

###  Login Page

(Add screenshot here)

###  OTP Verification

(Add screenshot here)

###  Security Question

(Add screenshot here)

###  Symbol Selection

(Add screenshot here)

### Dashboard

(Add screenshot here)

---

##  Future Enhancements

* Email/SMS-based OTP integration
* Database integration (MySQL/PostgreSQL)
* Role-based access control
* Cloud deployment (AWS/Render)

---

##  Author

Lakshmi Bhavani Kadali

---

## ⭐ If you like this project, give it a star!
