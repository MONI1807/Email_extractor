"""
Task 2: Extract Email Addresses from a .txt File
==================================================
Reads a text file, finds all valid email addresses using regex,
removes duplicates, sorts them, and saves the results to a new file.

Concepts used: re, file handling, sets, sorting
"""

import re
import datetime


# ─────────────────────────────────────────────
#  REGEX PATTERN FOR EMAIL ADDRESSES
# ─────────────────────────────────────────────

# Matches standard emails like: user.name+tag@sub.domain.com
EMAIL_PATTERN = re.compile(
    r"[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}"
)


# ─────────────────────────────────────────────
#  STEP 1: CREATE A SAMPLE INPUT FILE
# ─────────────────────────────────────────────

def create_sample_file(filename: str) -> None:
    """Creates a sample .txt file with mixed content and email addresses."""
    sample_text = """
    Hello Team,

    Please reach out to alice@example.com for project details.
    You can also contact bob.smith@company.org or the helpdesk at support@helpdesk.io.

    CC: charlie_99@gmail.com and DIANA@WORK.NET

    Note: These are NOT valid emails — @no-user.com, user@, plaintext
    Duplicate test: alice@example.com appears again here.

    Regards,
    Manager
    """
    with open(filename, "w", encoding="utf-8") as f:
        f.write(sample_text)

    print(f"[INFO]  Sample input file created: '{filename}'")


# ─────────────────────────────────────────────
#  STEP 2: EXTRACT EMAILS FROM THE FILE
# ─────────────────────────────────────────────

def extract_emails(input_file: str, output_file: str) -> None:
    """
    Reads the input file, extracts all unique email addresses,
    and saves them (sorted) to the output file.

    Args:
        input_file:  Path to the source .txt file
        output_file: Path to the file where results will be saved
    """

    # --- Read the input file ---
    print(f"\n[STEP 1] Reading file: '{input_file}'")
    with open(input_file, "r", encoding="utf-8") as f:
        content = f.read()

    # --- Find all emails using regex ---
    print("[STEP 2] Scanning for email addresses...")
    found_emails = EMAIL_PATTERN.findall(content)

    if not found_emails:
        print("[INFO]  No email addresses found.")
        return

    # --- Remove duplicates and sort ---
    print("[STEP 3] Removing duplicates and sorting...")
    unique_emails = sorted(set(found_emails))

    # --- Show results in terminal ---
    print(f"\n  ✅  {len(unique_emails)} unique email(s) found:\n")
    for email in unique_emails:
        print(f"       {email}")

    # --- Save results to output file ---
    print(f"\n[STEP 4] Saving results to '{output_file}'...")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(f"# Email Extraction Results\n")
        f.write(f"# Date     : {timestamp}\n")
        f.write(f"# Source   : {input_file}\n")
        f.write(f"# Total    : {len(unique_emails)} unique email(s)\n")
        f.write(f"# {'─' * 40}\n\n")
        for email in unique_emails:
            f.write(email + "\n")

    print(f"[DONE]  Results saved to '{output_file}' ✅")


# ─────────────────────────────────────────────
#  MAIN — RUN EVERYTHING
# ─────────────────────────────────────────────

def main():
    INPUT_FILE  = "contacts.txt"       # Source file to scan
    OUTPUT_FILE = "extracted_emails.txt"  # Where results are saved

    print("=" * 50)
    print("   EMAIL EXTRACTOR — Task Automation Script")
    print("=" * 50)

    # Create the sample input file
    create_sample_file(INPUT_FILE)

    # Extract and save emails
    extract_emails(INPUT_FILE, OUTPUT_FILE)

    print("\n" + "=" * 50)
    print("  All done! Check 'extracted_emails.txt' 🎉")
    print("=" * 50)


if __name__ == "__main__":
    main()
