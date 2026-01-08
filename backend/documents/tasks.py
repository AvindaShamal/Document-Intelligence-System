from celery import shared_task
import time


@shared_task
def dummy_process_document(document_id) -> str:
    """
    A dummy task that simulates processing a document.
    """
    print(f"Starting processing document with ID: {document_id}")
    time.sleep(10)  # Simulate a time-consuming task
    print(f"Finished processing document with ID: {document_id}")
    return f"Document {document_id} processed successfully."
