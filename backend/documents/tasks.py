from celery import shared_task
from .models import Document
from .ocr import extract_text_from_image
from .nlp_utils import clean_text, split_sentences
from .embeddings import get_text_embeddings
import logging


logger = logging.getLogger(__name__)


@shared_task(
    bind=True,
    autoretry_for=(Exception,),
    retry_kwargs={"max_retries": 3, "countdown": 5},
)
def process_document(self, document_id) -> None:
    try:
        try:
            document = Document.objects.get(id=document_id)
        except Document.DoesNotExist:
            logger.error(
                f"Failed processing document ID: {document_id} - Document does not exist."
            )
            # Do not retry for a missing document; it's a permanent error.
            return

        document.status = Document.STATUS_PROCESSING
        document.save(update_fields=["status"])

        logger.info(f"Started processing document ID: {document_id}")

        file_path = document.file.path
        raw_text = extract_text_from_image(file_path)
        cleaned_text = clean_text(raw_text)
        sentences = split_sentences(cleaned_text)
        embeddings = get_text_embeddings(sentences)

        document.extracted_text = cleaned_text
        document.embeddings = (
            embeddings.tolist() if hasattr(embeddings, "tolist") else embeddings
        )
        document.status = Document.STATUS_COMPLETED
        document.save(update_fields=["extracted_text", "embeddings", "status"])

        logger.info(f"Completed processing document ID: {document_id}")

    except Exception as e:
        logger.error(f"Failed processing document ID: {document_id} - {str(e)}")

        # If we still have a document instance, mark it as failed; otherwise, best-effort update.
        if "document" in locals():
            document.status = Document.STATUS_FAILED
            document.save(update_fields=["status"])
        else:
            Document.objects.filter(id=document_id).update(
                status=Document.STATUS_FAILED
            )

        raise self.retry(exc=e)
