from celery import shared_task
from .models import Document
from .ocr import extract_text_from_image


@shared_task
def process_document(document_id):
    try:
        document = Document.objects.get(id=document_id)
        document.status = "PROCESSING"
        document.save()

        file_path = document.file.path
        extracted_text = extract_text_from_image(file_path)

        document.extracted_text = extracted_text
        document.status = "COMPLETED"
        document.save()

    except Exception as e:
        document.status = "FAILED"
        document.save()
        raise e
