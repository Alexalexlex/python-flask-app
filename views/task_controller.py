from flask import Blueprint, request, jsonify
from services.task_service import TaskService

task_controller = Blueprint("task_controller", __name__)
task_service = TaskService()


@task_controller.route("/tasks", methods=["GET"])
def get_tasks():
    tasks = task_service.list_tasks()
    return jsonify({"tasks": tasks})


@task_controller.route("/tasks", methods=["POST"])
def add_task():
    task = request.json.get("task")
    if not task:
        return jsonify({"error": "Task is required"}), 400
    new_task = task_service.add_task(task)
    return jsonify({"task": new_task}), 201
