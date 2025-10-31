# Projet : Prédiction du Risque Cardiovasculaire
![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-Framework-green?logo=fastapi)
## Objectif du projet
Ce projet a pour objectif de créer une API complète pour prédire le risque cardiovasculaire à partir de données médicales.  
Le projet est structuré en deux parties dans la branche **main** :
- `app/` : contient le backend FastAPI, gestion des endpoints et de la documentation Swagger interactive.
- `ML/` : contient la partie Machine Learning, incluant le modèle de prédiction, le prétraitement des données et les fonctions de prédiction.

---

## Installation

1. **Cloner le dépôt et se placer sur la branche main**
```bash
git clone https://github.com/khadija199904/API_machine_learning
cd API_machine_learning
git checkout main
```
2. **Créer un environnement virtuel**
```bash
python -m venv venv
venv\Scripts\activate     
```
3. **Installer les dépendances**
```bash
pip install -r requirements.txt
```

## Structure du projet
``` bash
main/
│
├─ .github/              # GitHub Actions / Workflows
│
├─ app/        # Backend FastAPI
│
├─ ML/         # Partie Machine Learning
│
└─ requirements.txt
```
### Commandes d’exécution
Pour lancer l’API FastAPI :
``` bash
uvicorn app.main:app --reload
```

 - API : http://127.0.0.1:8000

 - Swagger UI : http://127.0.0.1:8000/docs


=======
README API 
=======
# Cardio Risk API

A FastAPI-based REST API for cardiovascular disease risk prediction and patient management. This application uses machine learning models to predict cardiovascular risk based on patient health metrics and provides endpoints for patient data management.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Database Schema](#database-schema)
- [Machine Learning Models](#machine-learning-models)
- [Testing](#testing)
- [Development](#development)

## Overview

The Cardio Risk API is designed to help healthcare providers assess cardiovascular disease risk in patients. It combines traditional patient data management with machine learning-powered risk prediction, allowing users to:

- Store and retrieve patient health records
- Predict cardiovascular risk using trained ML models
- Analyze patient data including blood pressure, glucose levels, and cardiac biomarkers

## Features

- **Patient Management**: Create and retrieve patient records with comprehensive health metrics
- **Risk Prediction**: ML-powered cardiovascular risk assessment using XGBoost
- **RESTful API**: Clean, well-documented API endpoints following REST principles
- **Data Validation**: Robust input validation using Pydantic schemas
- **Persistent Storage**: SQLite database for patient data storage
- **Automated Testing**: Unit and integration tests included

## Technology Stack

| Technology | Purpose |
|-----------|---------|
| **FastAPI** | Modern, high-performance web framework |
| **SQLAlchemy** | SQL toolkit and ORM |
| **Pydantic** | Data validation and settings management |
| **XGBoost** | Gradient boosting machine learning framework |
| **Pandas** | Data manipulation and analysis |
| **Joblib** | Model serialization and deserialization |
| **SQLite** | Lightweight relational database |
| **pytest** | Testing framework |
| **Python 3.13** | Programming language |

## Project Structure

```
api/
├── app/
│   ├── __init__.py
│   ├── main.py                              # FastAPI application entry point
│   │
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py                        # Configuration and settings
│   │   └── database.py                      # Database connection and session management
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   ├── patient.py                       # SQLAlchemy Patient model
│   │   ├── best_pipeline_XGBoost.pkl        # Trained XGBoost model
│   │   └── best_pipeline_with_GS_RandomForest.pkl    # Alternative RF model
│   │
│   ├── schemas/
│   │   └── patient.py                       # Pydantic validation schemas
│   │
│   ├── api/
│   │   ├── __init__.py
│   │   ├── patients.py                      # Patient CRUD endpoints
│   │   └── predict.py                       # Prediction endpoint
│   │
│   └── tests/
│       └── test_api.py                      # Unit and integration tests
│
├── cardio.db                                # SQLite database (auto-generated)
├── .gitignore
└── README.md
```

## Installation

### Prerequisites

- Python 3.13 or higher
- pip package manager

### Setup Steps

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd api
   ```

2. **Create and activate a virtual environment:**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # Linux/Mac
   python -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install fastapi uvicorn sqlalchemy pydantic pandas joblib xgboost scikit-learn pytest
   ```

4. **Initialize the database:**
   The database will be automatically created when you first run the application.

## Configuration

Configuration is managed through the [app/core/config.py](app/core/config.py) file using Pydantic settings.

### Default Settings

- **Project Name**: Cardio Risk API
- **Version**: 1.0.0
- **Database URL**: `sqlite:///./cardio.db`

### Environment Variables

You can override default settings by creating a `.env` file in the project root:

```env
DATABASE_URL=sqlite:///./cardio.db
PROJECT_NAME=Cardio Risk API
```

## Usage

### Starting the Server

Run the development server with hot reload:

```bash
uvicorn app.main:app --reload
```

The API will be available at `http://127.0.0.1:8000`

### Interactive API Documentation

FastAPI provides automatic interactive API documentation:

- **Swagger UI**: `http://127.0.0.1:8000/docs`
- **ReDoc**: `http://127.0.0.1:8000/redoc`

## API Endpoints

### Root Endpoint

#### `GET /`
Welcome message and API information.

**Response:**
```json
{
  "message": "Welcome to Cardio Risk API"
}
```

### Patient Management

#### `GET /api/patients/`
Retrieve all patients from the database.

**Response:**
```json
[
  {
    "id": 1,
    "age": 45,
    "gender": 1,
    "pressurehight": 140.5,
    "pressurelow": 90.0,
    "glucose": 105.5,
    "kcm": 2.5,
    "troponin": 0.05,
    "impluse": 75.0,
    "status": 1
  }
]
```

#### `POST /api/patients/`
Create a new patient record without prediction.

**Request Body:**
```json
{
  "age": 45,
  "gender": 1,
  "pressurehight": 140.5,
  "pressurelow": 90.0,
  "glucose": 105.5,
  "kcm": 2.5,
  "troponin": 0.05,
  "impluse": 75.0
}
```

**Response:**
```json
{
  "id": 1,
  "age": 45,
  "gender": 1,
  "pressurehight": 140.5,
  "pressurelow": 90.0,
  "glucose": 105.5,
  "kcm": 2.5,
  "troponin": 0.05,
  "impluse": 75.0,
  "status": null
}
```

### Prediction

#### `POST /api/predict`
Predict cardiovascular risk and save patient data to database.

**Request Body:**
```json
{
  "age": 45,
  "gender": 1,
  "pressurehight": 140.5,
  "pressurelow": 90.0,
  "glucose": 105.5,
  "kcm": 2.5,
  "troponin": 0.05,
  "impluse": 75.0
}
```

**Response:**
```json
{
  "id": 1,
  "age": 45,
  "gender": 1,
  "pressurehight": 140.5,
  "pressurelow": 90.0,
  "glucose": 105.5,
  "kcm": 2.5,
  "troponin": 0.05,
  "impluse": 75.0,
  "status": 1
}
```

**Status Values:**
- `0`: Low cardiovascular risk (negative prediction)
- `1`: High cardiovascular risk (positive prediction)

## Database Schema

### Patient Table

| Column | Type | Description |
|--------|------|-------------|
| `id` | Integer | Primary key, auto-increment |
| `age` | Integer | Patient age in years |
| `gender` | Integer | 1 = Male, 0 = Female |
| `pressurehight` | Float | Systolic blood pressure (mmHg) |
| `pressurelow` | Float | Diastolic blood pressure (mmHg) |
| `glucose` | Float | Blood glucose level (mg/dL) |
| `kcm` | Float | Cardiac biomarker measurement |
| `troponin` | Float | Troponin level (cardiac injury marker) |
| `impluse` | Float | Heart pulse/rate (bpm) |
| `status` | Integer | Prediction result (0 or 1), nullable |

## Machine Learning Models

The API includes two pre-trained machine learning models:

### Primary Model: XGBoost
- **File**: [app/models/best_pipeline_XGBoost.pkl](app/models/best_pipeline_XGBoost.pkl)
- **Algorithm**: Extreme Gradient Boosting
- **Purpose**: Cardiovascular risk classification
- **Status**: Currently active in prediction endpoint

### Alternative Model: Random Forest
- **File**: [app/models/best_pipeline_with_GS_RandomForest.pkl](app/models/best_pipeline_with_GS_RandomForest.pkl)
- **Algorithm**: Random Forest with Grid Search optimization
- **Purpose**: Alternative classification model
- **Status**: Available but not currently used

### How Prediction Works

1. Patient health metrics are received via POST request
2. Data is validated using Pydantic schemas
3. Metrics are converted to a pandas DataFrame
4. The XGBoost model makes a prediction (0 or 1)
5. Patient data with prediction is saved to the database
6. Response includes the patient record with predicted status

## Testing

### Running Tests

Execute the test suite using pytest:

```bash
# Run all tests
pytest

# Run with verbose output
pytest -v

# Run specific test file
pytest app/tests/test_api.py
```

### Test Coverage

The test suite in [app/tests/test_api.py](app/tests/test_api.py) includes:
- Root endpoint validation
- Patient creation functionality
- Patient retrieval operations
- Sample data validation

## Development

### Adding New Features

1. **Create a new endpoint:**
   - Add route handler in [app/api/](app/api/)
   - Define Pydantic schemas in [app/schemas/](app/schemas/)
   - Update database models if needed in [app/models/](app/models/)

2. **Modify the ML model:**
   - Train your model using your preferred algorithm
   - Save the model using joblib
   - Update [app/api/predict.py](app/api/predict.py) to load the new model

3. **Add tests:**
   - Create test functions in [app/tests/](app/tests/)
   - Follow the existing test patterns

### Best Practices

- Always validate input data using Pydantic schemas
- Use dependency injection for database sessions
- Write tests for new endpoints
- Update documentation when adding features
- Follow PEP 8 style guidelines

### Database Migrations

For schema changes:
1. Modify the model in [app/models/patient.py](app/models/patient.py)
2. Delete `cardio.db` to recreate the database
3. Or use Alembic for proper migrations:
   ```bash
   pip install alembic
   alembic init alembic
   # Configure and create migrations
   ```

## API Response Codes

| Code | Description |
|------|-------------|
| `200` | Success |
| `201` | Created |
| `400` | Bad Request (validation error) |
| `404` | Not Found |
| `422` | Unprocessable Entity (invalid data) |
| `500` | Internal Server Error |

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is available for use under your chosen license.

## Contact

For questions or support, please open an issue in the repository.

---

Built with FastAPI and machine learning for better cardiovascular health assessment.
>>>>>>> feature/api
