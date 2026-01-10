from pdfminer.high_level import extract_text
import time
import os

def test_pdfminer(filename):
    print(f"--- Testing PDFMiner on {filename} (Pages 4 & 5 only) ---")
    
    # הגדרת שם קובץ הפלט
    output_filename = "poc/output_pdfminer.txt"
    
    # וידוא שהתיקייה קיימת
    os.makedirs(os.path.dirname(output_filename), exist_ok=True)

    start_time = time.time()
    
    try:
        # --- השינוי כאן: הוספת הפרמטר page_numbers ---
        # עמוד 4 = אינדקס 3
        # עמוד 5 = אינדקס 4
        pages_to_extract = [3, 4]
        
        text = extract_text(filename, page_numbers=pages_to_extract)
        
        end_time = time.time()
        duration = end_time - start_time
        
        # שמירה לקובץ טקסט
        with open(output_filename, "w", encoding="utf-8") as f:
            f.write(text)
            
        print(f"Execution Time: {duration:.4f} seconds")
        print(f"SUCCESS: Output saved to '{output_filename}'")
        
    except Exception as e:
        print(f"Error: {e}")

# הרצה
test_pdfminer("poc/complex.pdf")