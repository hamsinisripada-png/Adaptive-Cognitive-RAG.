# Adaptive Cognitive RAG (AC-RAG)

> **A production-grade retrieval intelligence system that thinks before it answers.**

Adaptive Cognitive RAG (AC-RAG) is an advanced, agent-driven Retrieval-Augmented Generation (RAG) platform designed to autonomously plan, execute, evaluate, and refine retrieval strategies before generating responses. Instead of performing a single vector search, AC-RAG coordinates multiple specialized agents that analyze intent, optimize queries, perform hybrid retrieval, validate evidence, detect knowledge gaps, and verify citations.

---

## 🚀 Features

- Multi-Agent Retrieval Architecture
- Intelligent Query Planning
- Adaptive Retrieval Routing
- Hybrid Search (Vector + Keyword + Graph)
- Knowledge Graph Integration
- Evidence Graph Construction
- Recursive Multi-Hop Retrieval
- Automatic Query Reformulation
- Confidence Scoring
- Gap Detection
- Contradiction Detection
- Reflection & Self-Verification
- Citation Validation
- Long-Term Memory
- Retrieval History
- Evaluation Framework
- Real-Time Dashboard
- REST API
- Docker Deployment
- Comprehensive Testing
- OpenTelemetry Observability
- Production-Ready Architecture

---

## 🛠 Technology Stack

### Backend

- Python 3.13
- FastAPI
- LangGraph
- PydanticAI / OpenAI Agents SDK
- SQLAlchemy
- PostgreSQL
- Redis
- Neo4j
- Qdrant

### Frontend

- Next.js
- React
- TypeScript
- Tailwind CSS

### AI & Retrieval

- OpenAI
- Voyage AI
- Sentence Transformers
- Hybrid Retrieval
- BM25
- Vector Search
- Knowledge Graph Search

### DevOps

- Docker
- Docker Compose
- GitHub Actions
- Ruff
- Mypy
- Pytest
- Alembic
- OpenTelemetry
- LangSmith

---

## 📂 Repository Structure

```text
adaptive-cognitive-rag/
│
├── backend/
├── frontend/
├── api/
├── agents/
├── planner/
├── router/
├── retrievers/
├── memory/
├── reasoning/
├── evaluation/
├── embeddings/
├── ingestion/
├── knowledge_graph/
├── database/
├── middleware/
├── services/
├── workers/
├── tests/
├── benchmarks/
├── docker/
├── docs/
├── scripts/
├── examples/
├── .github/
├── docker-compose.yml
├── pyproject.toml
├── README.md
└── LICENSE
```

---

## 🧠 Core Architecture

```text
User
  │
  ▼
Intent Agent
  │
  ▼
Task Planner
  │
  ▼
Retrieval Router
  │
  ├──────────────┐
  │              │
Vector DB     Knowledge Graph
  │              │
  ├──────────────┤
  ▼              ▼
Hybrid Retrieval Engine
        │
        ▼
Evidence Quality Engine
        │
        ▼
Gap Detector
        │
        ▼
Query Optimizer
        │
        ▼
Recursive Retrieval
        │
        ▼
Contradiction Detector
        │
        ▼
Confidence Engine
        │
        ▼
Reflection Agent
        │
        ▼
Citation Validator
        │
        ▼
Response Generator
```

---

## 📦 Planned Components

- Intent Agent
- Planner Agent
- Retrieval Router
- Query Optimizer
- Hybrid Retrieval Engine
- Vector Search
- BM25 Search
- Knowledge Graph Search
- Memory Agent
- Reflection Agent
- Evidence Graph Builder
- Confidence Engine
- Gap Detector
- Contradiction Detector
- Citation Validator
- Evaluation Engine
- Dashboard
- API Gateway

---

## 🚀 Getting Started

### Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/adaptive-cognitive-rag.git

cd adaptive-cognitive-rag
```

### Backend

```bash
uv sync

uv run uvicorn app.main:app --reload
```

### Frontend

```bash
cd frontend

npm install

npm run dev
```

---

## 🐳 Docker

```bash
docker compose up --build
```

---

## ✅ Running Tests

```bash
pytest
```

---

## 🔍 Code Quality

```bash
ruff check .

mypy .

pytest
```

---

## 🌐 API

The platform exposes REST APIs for:

- Agent Execution
- Retrieval
- Document Ingestion
- Memory
- Knowledge Graph
- Evaluation
- Benchmarking
- Health Monitoring
- Metrics

---

## 🎯 Project Goals

- Autonomous Retrieval Planning
- Evidence-Driven Reasoning
- Adaptive Query Optimization
- Production-Grade RAG Infrastructure
- Explainable Retrieval Decisions
- Reliable Citation Validation
- Enterprise Deployment

---

## 🗺 Roadmap

- [ ] Core Infrastructure
- [ ] Database Layer
- [ ] Vector Store
- [ ] Document Ingestion
- [ ] Embedding Pipeline
- [ ] Retrieval Router
- [ ] Planner Agent
- [ ] Memory System
- [ ] Knowledge Graph
- [ ] Reflection Engine
- [ ] Evaluation Framework
- [ ] Dashboard
- [ ] Docker Deployment
- [ ] CI/CD Pipeline
- [ ] v1.0 Release

---

## 🤝 Contributing

Contributions are welcome. Please open an issue to discuss significant changes before submitting a pull request.

---

## 📄 License

This project is licensed under the MIT License.

---

## 👩‍💻 Author

**Hamsini Sripaada**

AI & Data Science Engineer

Building intelligent systems, autonomous agents, and advanced retrieval architectures.
