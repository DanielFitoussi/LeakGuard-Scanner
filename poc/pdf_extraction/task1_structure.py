import pdfplumber
import time
import os

def test_structure_preservation(filename):
    print(f"--- Testing High-Precision Extraction on {filename} (Pages 4 & 5 only) ---")
    output_filename = "poc/output_pdfplumber.txt"
    
    # וידוא שהתיקייה קיימת
    os.makedirs(os.path.dirname(output_filename), exist_ok=True)
    
    start_time = time.time()
    
    try:
        full_text = ""
        # פתיחת הקובץ עם pdfplumber
        with pdfplumber.open(filename) as pdf:
            print(f"Total pages in document: {len(pdf.pages)}")
            
            # --- השינוי כאן ---
            # אנחנו בוחרים רק את עמודים 4 ו-5 (אינדקסים 3 ו-4)
            target_pages = pdf.pages[3:5]
            
            # start=4 דואג ש-i יתחיל מ-4 ולא מ-0 (לצורך ההדפסה)
            for i, page in enumerate(target_pages, start=4):
                
                # layout=True מכריח את המנוע לשמור על המבנה הוויזואלי
                text = page.extract_text(layout=True, x_tolerance=2, y_tolerance=3)
                
                if text:
                    full_text += f"\n--- Page {i} ---\n"  # כאן i הוא כבר המספר הנכון (4 או 5)
                    full_text += text
                else:
                    full_text += f"\n--- Page {i} (No text found) ---\n"

        end_time = time.time()
        duration = end_time - start_time
        
        # שמירה לקובץ
        with open(output_filename, "w", encoding="utf-8") as f:
            f.write(full_text)
            
        print(f"Execution Time: {duration:.4f} seconds")
        print(f"SUCCESS: Structural text saved to '{output_filename}'")
        
    except Exception as e:
        print(f"Error: {e}")

# הרצה
if __name__ == "__main__":
    test_structure_preservation("poc/complex.pdf")