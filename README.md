# AI-Powered Document Intelligence Platform
## Overview
This project is an AI-powered Document Intelligence System built using
**Django, Django REST Framework, Celery,** and **Redis**.

Users can upload documents (images/PDFs), which are processed
asynchronously using **OCR** and **NLP** techniques. Extracted text is converted
into semantic embeddings, enabling intelligent search over documents.

Authentication is enforced using Django REST Framework permissions.
**Users can only access documents they own.**

---

## 🚀 Key Features

- Secure user authentication using JWT
- Document upload (PDF & images)
- Asynchronous OCR and NLP processing
- Semantic document search using vector embeddings
- RESTful APIs built with Django REST Framework
- Admin dashboard for monitoring tasks
- Dockerized local deployment

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
[ Client ]
    ↓
[ Django REAST API ] ------> [ Redis ]
          ↓                     ↓
[ Authentication (JWT) ]     [ Celery Worker ]
          ↓                      |
[ PostgreSQL Database ]          ├── OCR
                                 ├── Text Processing                       
                                 └── Embedding Generation                                
```

---

## 📂 Project Structure
```
Document-Intelligence-System
├── docker-compose.yml
├── requirements.txt
├── README.md
└── backend/
  ├── manage.py
  ├── accounts/
  │   ├── admin.py
  │   ├── models.py
  │   ├── serializers.py
  │   └── views.py
  ├── documents/
  │   ├── embeddings.py
  │   ├── ocr.py
  │   ├── serializers.py
  │   └── views.py
  ├── backend/
  │   ├── __init__.py
  │   ├── asgi.py
  │   ├── celery.py
  │   ├── settings.py
  │   ├── urls.py
  │   └── wsgi.py
  └── media/
    └── documents/
```

---

## 🔌 API Endpoints

| Method | Endpoint | Description |
|------|--------|-------------|
| POST | /api/auth/register/ | User registration |
| POST | /api/auth/login/ | JWT login |
| POST | /api/documents/upload/ | Upload document |
| GET | /api/documents/ | List documents |
| GET | /api/documents/{id}/status/ | Document Status
| POST | /api/search/ | Semantic search |

*POST /api/documents/upload/*

- Authentication: Required
- Body: multipart/form-data
- Fields:
  - file: document file
  - title: document title

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