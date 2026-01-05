# AI-Powered Document Intelligence Platform

A production-ready backend system built with **Django** and **Machine Learning** to process, analyze, and semantically search documents using OCR and NLP techniques.

---

## 🚀 Features

- Secure user authentication using JWT
- Document upload (PDF & images)
- Asynchronous OCR and NLP processing
- Semantic document search using vector embeddings
- RESTful APIs built with Django REST Framework
- Role-based access control
- Admin dashboard for monitoring tasks

---

## 🧠 AI & ML Capabilities

- OCR using EasyOCR
- Text embedding using Sentence Transformers
- Semantic similarity search using FAISS
- Asynchronous ML processing using Celery

---

## 🏗️ Tech Stack

### Backend
- Django
- Django REST Framework
- PostgreSQL
- JWT Authentication

### AI / ML
- EasyOCR
- HuggingFace Sentence Transformers
- FAISS

### Async & DevOps
- Celery
- Redis
- Docker

---

## 📐 System Architecture
```
Client
  ↓
Django REST API
  ↓
Authentication (JWT)
  ↓
Document Upload
  ↓
Celery Worker
  ├── OCR
  ├── Text Processing
  └── Embedding Generation
  ↓
PostgreSQL + FAISS
  ↓
Semantic Search API
```

---

## 📂 Project Structure
```
backend/
├── accounts/
├── documents/
├── search/
├── celery.py
├── settings.py
├── urls.py
```

---

## 🔌 API Endpoints

| Method | Endpoint | Description |
|------|--------|-------------|
| POST | /api/auth/register/ | User registration |
| POST | /api/auth/login/ | JWT login |
| POST | /api/documents/upload/ | Upload document |
| GET | /api/documents/ | List documents |
| POST | /api/search/ | Semantic search |

---

## ⚙️ Setup Instructions

```bash
git clone https://github.com/your-username/document-intelligence.git
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

---

## 🧪 Sample Use Case

1. User uploads a scanned document (receipt, invoice, form)
2. OCR extracts text asynchronously
3. NLP pipeline generates vector embeddings
4. User searches documents using natural language
5. System returns semantically similar documents

## 🎯 Why This Project?

This project demonstrates:
- Backend engineering best practices
- Real-world ML model deployment
- Asynchronous task handling
- Secure API development

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

## Contact

For any questions or inquiries, feel free to contact me at [avindashamal@gmail.com].