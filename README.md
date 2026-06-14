# 📧 Email Extractor — Task Automation with Python

A beginner-friendly Python script that automatically scans a `.txt` file, extracts all valid email addresses using **Regular Expressions (Regex)**, removes duplicates, sorts them alphabetically, and saves the clean results to a new file — with a timestamp.

---

## 🚀 Features

- ✅ Extracts all valid email addresses from any `.txt` file
- ✅ Removes duplicate emails automatically
- ✅ Sorts results alphabetically
- ✅ Saves output to a new file with a timestamp header
- ✅ Ignores invalid email formats (e.g. `@no-user.com`, `user@`)
- ✅ Auto-generates a sample input file for instant testing

---

## 🛠 Tech Stack & Concepts Used

| Concept | Usage |
|--------|-------|
| `re` module | Regex pattern to find email addresses |
| File Handling | `open()`, `read()`, `write()` |
| `set()` | Remove duplicate emails |
| `sorted()` | Alphabetical ordering |
| `datetime` | Timestamp in the output file |
| Functions | Clean, reusable code structure |

---

## 📁 Project Structure

```
task_automation/
├── email_extractor.py      # Main script
├── contacts.txt            # Auto-created sample input file
├── extracted_emails.txt    # Auto-created output file with results
└── README.md               # Project documentation
```

---

## ⚙️ How to Run

### 1. Clone or Download the Project

```bash
git clone https://github.com/your-username/email-extractor.git
cd email-extractor
```

Or simply download `email_extractor.py` and open it in VS Code.

### 2. Make Sure Python is Installed

```bash
python --version
```

> Requires Python 3.6 or above. Download from [python.org](https://www.python.org) if needed.

### 3. Run the Script

```bash
python email_extractor.py
```

No external libraries needed — uses Python's built-in modules only.

---

## 📊 Sample Output

**Terminal:**
```
==================================================
   EMAIL EXTRACTOR — Task Automation Script
==================================================
[INFO]  Sample input file created: 'contacts.txt'

[STEP 1] Reading file: 'contacts.txt'
[STEP 2] Scanning for email addresses...
[STEP 3] Removing duplicates and sorting...

  ✅  5 unique email(s) found:

       DIANA@WORK.NET
       alice@example.com
       bob.smith@company.org
       charlie_99@gmail.com
       support@helpdesk.io

[STEP 4] Saving results to 'extracted_emails.txt'...
[DONE]  Results saved to 'extracted_emails.txt' ✅
```

**extracted_emails.txt:**
```
# Email Extraction Results
# Date     : 2024-11-20 10:45:32
# Source   : contacts.txt
# Total    : 5 unique email(s)
# ────────────────────────────────────────

DIANA@WORK.NET
alice@example.com
bob.smith@company.org
charlie_99@gmail.com
support@helpdesk.io
```

---

## 🔍 How It Works

### 1. Read the File
```python
with open(input_file, "r", encoding="utf-8") as f:
    content = f.read()
```
Opens the input `.txt` file and loads all content as a single string.

### 2. Regex Pattern Matching
```python
EMAIL_PATTERN = re.compile(
    r"[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}"
)
found_emails = EMAIL_PATTERN.findall(content)
```
The regex scans the entire text and returns a list of every email-like pattern it finds.

### 3. Deduplicate & Sort
```python
unique_emails = sorted(set(found_emails))
```
`set()` removes duplicates. `sorted()` arranges them A → Z.

### 4. Save Results
```python
with open(output_file, "w", encoding="utf-8") as f:
    for email in unique_emails:
        f.write(email + "\n")
```
Writes the clean list to a new `.txt` file.

---

## 🔡 Understanding the Regex

```
[a-zA-Z0-9._%+\-]+  @  [a-zA-Z0-9.\-]+  \.  [a-zA-Z]{2,}
        ▲            ▲         ▲           ▲        ▲
   username part     @    domain name      .    .com/.org/.io
```

| Part | Matches |
|------|---------|
| `[a-zA-Z0-9._%+\-]+` | Letters, numbers, dots, underscores before `@` |
| `@` | The literal `@` symbol |
| `[a-zA-Z0-9.\-]+` | Domain name (e.g. `gmail`, `company`) |
| `\.[a-zA-Z]{2,}` | Extension with 2+ letters (`.com`, `.org`, `.io`) |

---

## 🎯 Use Cases

- Cleaning up messy contact lists
- Pulling emails from exported CRM or newsletter data
- Processing log files or reports
- Any scenario where email addresses are buried in unstructured text

---

## 🙋 Project Link

Task 2 — Task Automation with Project Scripts

GitHub Repository Link : https://github.com/MONI1807/Email_extractor.git

---
