from typing import TypedDict

PRIORITIES = {'low', 'medium', 'high'}

class Task(TypedDict):
    id: int
    title: str
    priotity: str
    tags: list[str]
    status: str


def make_task(id_: int, title: str, tags: list[str], priotity: str = "low") -> Task:
    
    if priotity not in PRIORITIES:
        raise ValueError("Приоритет задачи должен быть low, medium или high")
    
    task: Task = {
        'id': id_,
        'title': title.strip(),
        'priotity': priotity,
        'tags': tags,
        'status': 'new'
    }
    
    return task
