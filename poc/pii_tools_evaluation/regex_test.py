import re
import time
import os

def run_test():
    print("--- Testing Regex ---")

# קבלת הנתיב של התיקייה שבה הסקריפט נמצא כרגע
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "input.txt")

# Read text from file
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()
    except FileNotFoundError:
        print(f"Error: Could not find input.txt at {file_path}")
        return

    start = time.time()

    # Simple regex for email
    email_pattern = r'[a-zA-Z0-9._]+@[a-zA-Z0-9]+\.[a-zA-Z]+'
    
    # Simple regex for phone (05X-XXXXXXX)
    phone_pattern = r'05\d-?\d{7}'

    # Simple regex for ID (9 digits)
    id_pattern = r'\b\d{9}\b'

    # Find all matches
    emails = re.findall(email_pattern, text)
    phones = re.findall(phone_pattern, text)
    ids = re.findall(id_pattern, text)

    end = time.time()
    
    # Prepare the output string
    output = f"""
    --- Regex Results ---
    Execution Time: {end - start:.4f} seconds
    
    Emails found: {emails}
    Phones found: {phones}
    IDs found: {ids}
    """

    # Save results to a file
    with open("results_regex.txt", "w", encoding="utf-8") as f:
        f.write(output)
    
    print("Done! Saved to results_regex.txt")

if __name__ == "__main__":
    run_test()