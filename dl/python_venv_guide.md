# 🐍 Python Virtual Environment Guide

## 📁 1. Global Installation (C: Drive)

* Install **Python** globally on your system from [python.org](https://python.org).
* This ensures Python is available system-wide, but we **don't use global installation for project libraries**.

---

## 🧪 2. Create a Virtual Environment (Per Project)

Each project should have **its own isolated virtual environment** so dependencies don't conflict.

```bash
python -m venv <env-name>
```

* Replace `<env-name>` with your preferred environment name, e.g., `venv`, `env`, or `cust`.

**Example:**

```bash
python -m venv cust
```

---

## ▶️ 3. Activate the Virtual Environment

**On Windows:**

```bash
.\cust\Scripts\activate
```

**On macOS/Linux:**

```bash
source cust/bin/activate
```

✅ Once activated, you'll see the environment name in your terminal prompt.

---

## 📦 4. Install Libraries in the Virtual Environment

Now you can install Python packages **only inside this environment**:

```bash
pip install pandas numpy matplotlib scikit-learn
```

---

## 📜 5. Use `requirements.txt`

Create a `requirements.txt` file listing all dependencies:

```text
pandas
numpy
matplotlib
scikit-learn
```

Then install all dependencies at once:

```bash
pip install -r requirements.txt
```

**💡 Tip:** Generate `requirements.txt` automatically from your current environment:

```bash
pip freeze > requirements.txt
```

---

## 🔄 6. Deactivate the Virtual Environment

When done, deactivate it with:

```bash
deactivate
```

---

## ✅ Best Practices

* Always use a **virtual environment per project**.
* Keep a `requirements.txt` for easy dependency installation.
* Never install project-specific packages **globally**.
* Use `.gitignore` to exclude virtual environment folders (e.g., `venv/`, `cust/`) from version control.

---

## 🚀 Quick Reference

| Action | Command |
|--------|---------|
| Create venv | `python -m venv <env-name>` |
| Activate (Windows) | `.\<env-name>\Scripts\activate` |
| Activate (macOS/Linux) | `source <env-name>/bin/activate` |
| Install packages | `pip install <package-name>` |
| Install from file | `pip install -r requirements.txt` |
| Generate requirements | `pip freeze > requirements.txt` |
| Deactivate | `deactivate` |