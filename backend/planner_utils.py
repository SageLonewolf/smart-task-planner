import os
import json
import openai
from datetime import datetime, timedelta

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_task_plan(goal_text: str):
    prompt = f"""
    You are an expert project planner.
    Break down the following goal into actionable tasks with:
    - Task name
    - Description
    - Estimated start and end days
    - Dependencies (if any)
    - Ensure tasks fit within total duration mentioned (if given).
    Return JSON in this format:
    {{
      "tasks": [
        {{
          "id": 1,
          "task": "Task name",
          "description": "What needs to be done",
          "duration": "Day 1-2",
          "dependencies": []
        }}
      ]
    }}
    Goal: "{goal_text}"
    """

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=500,
        temperature=0.7
    )

    text_output = response.choices[0].message["content"]

    try:
        plan = json.loads(text_output)
    except:
        plan = {"tasks": [{"id": 1, "task": "Define goal", "duration": "Day 1", "dependencies": []}]}

    return plan
