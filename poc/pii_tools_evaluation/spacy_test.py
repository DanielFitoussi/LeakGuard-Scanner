import spacy
import time
import os

def run_test():
    print("--- Testing SpaCy ---")

    # Load the small english model
    nlp = spacy.load("en_core_web_sm")

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

    # Process the text
    doc = nlp(text)

    end = time.time()

    # Prepare output string
    output = f"--- SpaCy Results ---\nExecution Time: {end - start:.4f} seconds\n\n"

    # Add detected entities to output
    for ent in doc.ents:
        output += f"Text: {ent.text}, Label: {ent.label_}\n"

    # Save results to file
    with open("results_spacy.txt", "w", encoding="utf-8") as f:
        f.write(output)

    print("Done! Saved to results_spacy.txt")

if __name__ == "__main__":
    run_test()