
# UBL Despatch Advice API

A FastAPI-based service designed to generate, validate, and manage UBL 2.1 Despatch Advice XML documents.

## Project Structure

The project follows a modular architecture to separate API routing, logic, and data models.

```text
.
├── app/
│   ├── api/v1/             # API Route handlers (Despatch, Health)
│   ├── core/              # Core logic (XML Generation, XSD Validation)
│   ├── models/            # Pydantic data models
│   ├── services/          # Business logic layer (Placeholders)
│   ├── templates/         # Jinja2 XML templates
│   └── xsd/               # UBL 2.1 Schema definitions
├── data/                  # Mock data for testing (JSON)
├── generated/             # Output folder for generated XMLs (Local only)
├── tests/                 # Unit and integration tests
├── run.py                 # Application entry point
├── requirements.txt       # Project dependencies
└── README.md              # Project documentation
```

## Setup and Installation

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd API-Architects
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
# On Windows:
.\venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## Running the Application

Start the server using the entry point script:

```bash
python run.py
```

The server will start at `http://127.0.0.1:8000`.

## API Documentation

Once the server is running, you can access the interactive API documentation:

- **Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

### Key Endpoints

| Method   | Endpoint                           | Description                               |
| :------- | :--------------------------------- | :---------------------------------------- |
| **POST** | `/ubl/v2/despatch-advice/generate` | Generates a UBL XML and returns the file. |
| **GET**  | `/ubl/v2/despatch-advice/list`     | Lists all previously generated documents. |
| **POST** | `/ubl/v2/despatch-advice/validate` | Validates an XML against the UBL 2.1 XSD. |
| **GET**  | `/ubl/v2/despatch-advice/health`   | Service health check.                     |

## Testing

To run the test suite, ensure you are in the root directory and run:

```bash
pytest
```

## Output

Generated XML files are stored in the `/generated` directory at the root level. Each file is named using the format:
`Despatch_{id}_{uuid}_{timestamp}.xml`

---

_Created by the API-Architects Team._
