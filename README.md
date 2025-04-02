# 🚀 Template: FastAPI + Gunicorn + Docker

This is a boilerplate template for building scalable APIs using **FastAPI**, with production-ready deployment using **Gunicorn** and **Docker**.

---

## 📁 Project Structure

```
template-fastapi-gunicorn/
├── app/
│ ├── api/
│ │ ├── models/             # Models and Enums
│ │ ├── routes/             # API endpoints
│ │ └── services/           # Core services/providers
│ ├── core/
│ │ ├── config.py
│ │ ├── logging.py
│ ├── main.py
├── public/                 # Static/public assets
├── tests/                  # Evaluation, testing, and processing scripts
├── .gitignore
├── dependencies.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── README.md
└── .env                    # Environment variables (local)
```

---

## ⚙️ Features

- Modular folder structure for scalable development
- Environment variable support via `.env`
- Logging setup with custom formatting
- CORS middleware for cross-origin requests
- Docker & Docker Compose support
- Production-ready with **Gunicorn** and **Uvicorn workers**

---

## 🚧 Setup (Development)

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/template-fastapi-gunicorn.git
cd template-fastapi-gunicorn
```

### 2. Create and activate virtual environment

```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On Linux/Mac
python -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create a `.env` file with the following variables:

```env
OPENAI_API_KEY=your_openai_api_key
```

### 5. Run the server

```bash
python -m app:main
```

The Backend will be available at `http://localhost:8000`

## 🧪 Test the Health Route

```bash
curl http://localhost/8000
```

### Expected Response:

```json
{
  "status": "online",
  "service": "Template FASTAPI",
  "version": "1.0.0"
}
```

## 🚀 Docker Deployment

```bash
# Build and run the container using Docker Compose
docker-compose up --build
```

## ✍️ Maintainers

Built and maintained by the [TailoredAI](https://tailoredai.co) team.

---
