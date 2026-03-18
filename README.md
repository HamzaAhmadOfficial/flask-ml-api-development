# Week 8 – Flask Backend & API Development
# ML Internship – Week 8 Task

##  Overview
This project demonstrates backend development using Flask, including:
- REST API creation
- Machine Learning model deployment
- Image classification API (TFLite)
- Database integration using SQLite
- API authentication and logging

---

##  Project Structure
```
week8_flask_api/
│
├── flask_basics.py
├── flask_ml_api.py
├── flask_image_api.py
├── flask_rest_api.py
│
├── model.pkl
├── model.tflite
│
├── templates/
│   └── index.html
│
└── README.md
```

---

##  Installation

Install dependencies:

```
pip install flask flask-sqlalchemy numpy pillow tensorflow
```

---

##  Task 8.1 – Flask Basics API

### Endpoints

| Method | Endpoint | Description |
|--------|----------|------------|
| GET | / | Welcome message |
| GET | /data | Get all items |
| POST | /data | Add item |
| PUT | /data/<id> | Update item |
| DELETE | /data/<id> | Delete item |

---

##  Task 8.2 – ML Model API

### Endpoint
POST /predict

### Input
```
{
  "features": [5.1, 3.5, 1.4, 0.2]
}
```

### Output
```
{
  "prediction": 0
}
```

---

##  Task 8.3 – Image Classification API

### Endpoints

| Method | Endpoint |
|--------|---------|
| POST | /classify |
| POST | /classify_batch |

### Features
- Image upload (jpg, png, webp)
- Preprocessing
- Prediction with confidence

---

## 🗄️ Task 8.4 – REST API with Database

### Database
SQLite (predictions.db)

### Endpoints

| Method | Endpoint | Description |
|--------|----------|------------|
| POST | /predictions | Save prediction |
| GET | /predictions | Get all predictions |
| GET | /predictions?page=1 | Pagination |

---

##  API Authentication

Use API Key in header:

```
x-api-key: 123456
```

---

##  Logging
All API requests are logged using Python logging module.

---

##  How to Run

Run each file separately:

```
python flask_basics.py
python flask_ml_api.py
python flask_image_api.py
python flask_rest_api.py
```

---

##  Notes
- Ensure model.pkl and model.tflite are present
- Use Postman or browser for testing APIs

---

##  Author
Hamza Ahmad
AI/ML Intern
