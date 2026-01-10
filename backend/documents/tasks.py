from celery import shared_task
from .models import Document
from .ocr import extract_text_from_image
from .nlp_utils import clean_text, split_sentences
import logging


logger = logging.getLogger(__name__)


@shared_task(
    bind=True,
    autoretry_for=(Exception,),
    retry_kwargs={"max_retries": 3, "countdown": 5},
)
def process_document(self, document_id) -> None:
    try:
        document = Document.objects.get(id=document_id)
        document.status = Document.STATUS_PROCESSING
        document.save(update_fields=["status"])

        logger.info(f"Started processing document ID: {document_id}")

        file_path = document.file.path
        raw_text = extract_text_from_image(file_path)
        cleaned_text = clean_text(raw_text)
        sentences = split_sentences(cleaned_text)

        document.extracted_text = cleaned_text
        document.status = Document.STATUS_COMPLETED
        document.save(update_fields=["extracted_text", "status"])

        logger.info(f"Completed processing document ID: {document_id}")

    except Exception as e:
        logger.error(f"Failed processing document ID: {document_id} - {str(e)}")

        Document.objects.filter(id=document_id).update(status=Document.STATUS_FAILED)
        document.save(update_fields=["status"])
        raise self.retry(exc=e)
