import easyocr
import os

reader = easyocr.Reader(["en"], gpu=False)


def extract_text_from_image(image_path):
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"File not found: {image_path}")

    results = reader.readtext(image_path)
    text = ",".join([line[1] for line in results])
    return text
