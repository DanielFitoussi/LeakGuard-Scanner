from presidio_analyzer import AnalyzerEngine
import time
import os

def run_test():
    print("--- Testing Presidio ---")

    # Initialize the engine
    analyzer = AnalyzerEngine()

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

    # Run analysis
    results = analyzer.analyze(text=text, language='en')

    end = time.time()

    # Prepare output string
    output = f"--- Presidio Results ---\nExecution Time: {end - start:.4f} seconds\n\n"

    for res in results:
        # Get the actual text from the result index
        found_text = text[res.start:res.end]
        output += f"Found: {found_text}, Type: {res.entity_type}, Score: {res.score:.2f}\n"

    # Save results to file
    with open("results_presidio.txt", "w", encoding="utf-8") as f:
        f.write(output)

    print("Done! Saved to results_presidio.txt")

if __name__ == "__main__":
    run_test()