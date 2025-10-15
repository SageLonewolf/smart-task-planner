from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from planner_utils import generate_task_plan

app = FastAPI(title="Smart Task Planner")

class GoalInput(BaseModel):
    goal: str

@app.get("/")
def root():
    return {"message": "Smart Task Planner API is running."}

@app.post("/generate-plan")
def generate_plan(data: GoalInput):
    goal_text = data.goal.strip()
    if not goal_text:
        raise HTTPException(status_code=400, detail="Goal text cannot be empty.")
    
    try:
        plan = generate_task_plan(goal_text)
        return {"goal": goal_text, "plan": plan}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
