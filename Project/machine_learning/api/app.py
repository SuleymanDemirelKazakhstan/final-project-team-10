import celery.states as states
from flask import Flask, request ,url_for, jsonify
from worker import celery
import json

dev_mode = True
app = Flask(__name__)



@app.route("/colorize", methods=["POST"])
def process_image():
    data = request.get_json(force=True)
    task = celery.send_task('tasks.colorize', args=[data], kwargs={})
    response = {
        "task_id": str(task.id)
    }
    return json.dumps(response)




@app.route('/colorize/<task_id>')
def frequency_check_handler(task_id):
    task = celery.AsyncResult(task_id)  

    if task.state == states.PENDING:
        response = {
            "status": "IN_PROGRESS"
        }
    else:
        response = {
            "status": "DONE",
        }
    return json.dumps(response)


@app.route('/')
def health_check() -> str:
    response = {
        "Maxon": "1337"
    }
    return json.dumps(response)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8000')
