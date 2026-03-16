
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
git clone https://github.com/Raiyyan2067/API-Architects
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

## AWS Deployment

Access the API link with the following URL:
```bash
https://rhumzuhvabxxwsemnufzash5ue0wubck.lambda-url.ap-southeast-2.on.aws
```

Access routes by adding the endpoint to the end of the URL:
```bash
https://rhumzuhvabxxwsemnufzash5ue0wubck.lambda-url.ap-southeast-2.on.aws/ubl/v2/despatch-advice/list
```

Previous XML files can be accessed by adding the file name to the end of the following URL:
```bash
https://ubl-despatch-files-393035998882-ap-southeast-2-an.s3.ap-southeast-2.amazonaws.com
```

For example:
```bash
https://ubl-despatch-files-393035998882-ap-southeast-2-an.s3.ap-southeast-2.amazonaws.com/Despatch_D001_b0e63b53-f9bd-49fa-8983-f30c178b3e95_2026-03-16T-021144.xml
```


## API Documentation

Once the server is running, you can access the interactive API documentation:

### Running the server with python run.py:

- **Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

### Acessing Documentation from AWS
- **Lambda:** [https://rhumzuhvabxxwsemnufzash5ue0wubck.lambda-url.ap-southeast-2.on.aws/docs](https://rhumzuhvabxxwsemnufzash5ue0wubck.lambda-url.ap-southeast-2.on.aws/docs)

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

Generated XML files are stored in AWS S3. See the [AWS Deployment](#aws-deployment) section to see how to access them.

---

### 📋 Compliance with Specification (Sprint 2 Marks)*

#### 1. Non-Functional Requirements (Doc 2, Section 3.1)
*   *Performance:* The XML generation algorithm uses *Jinja2's compiled templates*, ensuring $O(n)$ time complexity (where $n$ is the number of items). This minimizes the computation time for the API response, meeting the requirement for "minimal amount of time to complete."
*   *Security:* (Note: Mention your team's plan here, e.g., "The service is designed to be integrated with an authentication middleware to ensure protected access to generation functionality.")

#### 2. Design Principles
*   *DRY (Don't Repeat Yourself):* By using a single ubl_generator.py service and a centralized Pydantic model, we avoid duplicating logic across the codebase.
*   *KISS (Keep It Simple):* We chose a *Template-based approach* rather than complex XML DOM manipulation to keep the logic readable and easy to maintain.
*   *Pythonic Conventions:* Adheres to *PEP 8* standards, using meaningful variable names, type hinting, and clear whitespace.

#### 3. Health Check Endpoint (Doc 3, Page 7, Guideline 6)
*   As per the General Guidelines for creating an API, we implemented a */health* endpoint. 
*   *Status:* Returns a 200 OK status and a timestamp to indicate "aliveness" and "statefulness" of the service.

#### 4. Data Modeling (Doc 2, Section 3.3)
*  The persistence layer is implemented using AWS S3 for storing generated XML files.
*  Interaction: The application layer (FastAPI) interacts with S3 via wrapper functions like `def list_despatch_advice()`. FastAPI calls these functions rather than talking to S3 directly. This ensures the domain logic         remains decoupled from the storage mechanism.
*  Benefits: scalable storage, centralized file access, and seamless integration with AWS Lambda deployments.

#### 5. Architectural Notation (Doc 2, Section 3.2)
*   Our system architecture follows the *SC4 notation* recommended in the lecture, highlighting the layers of abstraction (Server -> Application -> Persistence).

_Created by the API-Architects Team._
