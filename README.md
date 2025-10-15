#  Smart Task Planner

An AI-powered planner that breaks down your goal into actionable tasks with timelines and dependencies.

##  Features
- Enter any goal (e.g., “Launch a product in 2 weeks”)
- AI generates a structured plan with tasks, dependencies, and timelines
- FastAPI backend with LLM integration
- Optional simple frontend (HTML/JS/CSS)

##  Setup Instructions

### 1. Backend
```bash
cd backend
pip install -r requirements.txt
echo "OPENAI_API_KEY=your_key" > .env
uvicorn main:app --reload
```

Backend runs at: **http://127.0.0.1:8000**

### 2. Frontend
Open `frontend/index.html` in your browser.

## 🧩 Example API Usage
**POST** `http://127.0.0.1:8000/generate-plan`
```json
{ "goal": "Launch a product in 2 weeks" }
```

**Response:**
```json
{
  "goal": "Launch a product in 2 weeks",
  "plan": {
    "tasks": [
      {"id": 1, "task": "Define scope", "duration": "Day 1-2", "dependencies": []}
    ]
  }
}
```
