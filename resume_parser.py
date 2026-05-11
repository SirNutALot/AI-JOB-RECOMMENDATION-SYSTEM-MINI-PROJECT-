from pdf2image import convert_from_path
import pytesseract


# =========================
# TESSERACT PATH
# =========================
pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

# =========================
# POPPLER PATH
# =========================
POPPLER_PATH = r"C:\code\poppler\Library\bin"


# =========================
# OCR PDF TEXT EXTRACTION
# =========================
def extract_text_from_pdf(file_path):

    text = ""

    try:

        # CONVERT PDF TO IMAGES
        images = convert_from_path(
            file_path,
            poppler_path=POPPLER_PATH
        )

        # OCR EACH PAGE
        for image in images:

            extracted_text = pytesseract.image_to_string(image)

            text += extracted_text + "\n"

    except Exception as e:

        print(f"Error reading {file_path}: {e}")

    return text