import easyocr

reader = easyocr.Reader(["en"], gpu=False)


def extract_text_from_image(image_path):
    results = reader.readtext(image_path)
    text = ",".join([line[1] for line in results])
    return text
