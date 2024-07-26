# FAQ Management FastAPI Application

This Python FastAPI backend application manages Frequently Asked Questions (FAQs). The application includes the following functionalities:

1. Parses a CSV document containing FAQs and inserts them into a PostgreSQL database upon startup.
2. If an FAQ already exists, the application ignores the duplicate entry on subsequent startups and only inserts missing FAQs.
3. Provides an API for adding new FAQs to the database.
4. Provides an API for listing FAQs with pagination.
5. Provides an API for retrieving details of an FAQ by its ID.
6. The entire application is containerized using Docker and includes both the backend and PostgreSQL database.
7. Uses `flake8` for linting the backend code.
8. Uses Alembic for managing database migrations.
9. Applies all available migrations upon application startup.
10. Bonus features:
    - Stores text embeddings of FAQs in the database upon startup using an AI model of choice.
    - Enables the `pgvector` extension to store vector data in the database.
    - Creates and stores embeddings in the database when adding new FAQs through the API.

## Getting Started

### Prerequisites

- Docker
- Docker Compose

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/scekic/invt-project.git
    cd invt-project
    ```

2. Build and run the Docker containers:
    ```sh
    docker-compose up --build
    ```

### Usage

- The application will parse and insert FAQs from the `app/faq_knowledge_base.csv` file into the database upon startup.
- To add a new FAQ via the API, send a POST request to `/faqs` with the FAQ data in JSON format.
- To list FAQs with pagination, send a GET request to `/faqs?page=<page_number>&size=<page_size>`.
- To get the details of an FAQ by its ID, send a GET request to `/faqs/{id}`.

### API Endpoints

- `POST /faqs`: Add a new FAQ.
- `GET /faqs`: List FAQs with pagination.
- `GET /faqs/{id}`: Get details of an FAQ by its ID.

### Linting

- The backend code is linted using `flake8`. To run `flake8`, use the following command:
    ```sh
    flake8
    ```

### Database Migrations

- Alembic is used to manage database migrations. To apply migrations, use the following command:
    ```sh
    alembic upgrade head
    ```

### Docker Compose

- The application and PostgreSQL database are containerized using Docker Compose. The `compose.yml` file defines the services and their configurations.

### Bonus Features

- Text embeddings of FAQs are generated and stored in the database using an AI model. The `pgvector` extension is enabled to store vector data.
- When adding a new FAQ through the API, embeddings are created and stored in the database.

#### Important
- The OpenAI API key specified in the `.env` file as `OPENAI_API_KEY` is experiencing an insufficient quota error. Despite attempts to connect a payment method to OpenAI and add credits, a "Your card has insufficient funds." message was encountered, even though the card has sufficient funds. To ensure embeddings work, replace the `OPENAI_API_KEY` with a new one and:
    - Uncomment all commented lines in `app/services/utils.py` (make sure to remove lines 37-39 from the same file).
    - Uncomment lines 14-18 in `app/services/faq.py`.
