import fitz  # PyMuPDF
import time
import os

def test_pymupdf(filename):
    print(f"--- Testing PyMuPDF on {filename} (Pages 4 & 5 only) ---")
    
    # הגדרת שם קובץ הפלט
    output_filename = "poc/output_pymupdf.txt"
    
    # וידוא שהתיקייה poc קיימת (כדי למנוע שגיאה אם היא לא)
    os.makedirs(os.path.dirname(output_filename), exist_ok=True)
    
    start_time = time.time()
    
    try:
        doc = fitz.open(filename)
        text = ""
        
        # --- השינוי כאן: לולאה רק על אינדקס 3 ו-4 (עמודים 4 ו-5) ---
        for i in range(3, 5):
            # בדיקה שהעמוד קיים (למקרה שהקובץ קצר מדי)
            if i < len(doc):
                page = doc.load_page(i)  # טעינת העמוד הספציפי
                text += page.get_text() + "\n\n"
            else:
                print(f"Warning: Page {i+1} does not exist in the PDF.")
        
        end_time = time.time()
        duration = end_time - start_time
        
        # שמירה לקובץ טקסט
        with open(output_filename, "w", encoding="utf-8") as f:
            f.write(text)
            
        print(f"Execution Time: {duration:.4f} seconds")
        print(f"SUCCESS: Output saved to '{output_filename}'")
        
    except Exception as e:
        print(f"Error: {e}")

# הרצה (ודא שהקובץ complex.pdf קיים בתיקיית poc)
test_pymupdf("poc/complex.pdf")