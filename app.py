from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

MAX = 10
queue_array = [None] * MAX
rear = -1
front = -1

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/queue/insert', methods=['POST'])
def queue_insert():
    global rear, front
    if rear == MAX - 1:
        return jsonify({"message": "Queue Overflow"})
    else:
        if front == -1:
            front = 0
        add_item = request.form['element']
        rear += 1
        queue_array[rear] = add_item
        return jsonify({"message": "Element inserted!"})

@app.route('/queue/delete', methods=['POST'])
def queue_delete():
    global front, rear
    if front == -1 or front > rear:
        return jsonify({"message": "Queue Underflow"})
    else:
        deleted_element = queue_array[front]
        front += 1
        if front == rear + 1:
            front = -1
            rear = -1
        return jsonify({"message": f"Element deleted from queue is: {deleted_element}"})

@app.route('/queue/display')
def display():
    queue = queue_array[front:rear + 1] if front != -1 else []
    return jsonify({"queue": queue})

@app.route('/queue/search', methods=['POST'])
def queue_search():
    person = request.form['person']
    if person in queue_array[front:rear + 1]:
        position = queue_array.index(person) + 1
        return jsonify({"message": f"Person is waiting at position: {position}"})
    else:
        return jsonify({"message": "Person is not in the queue"})

if __name__ == "__main__":
    app.run(debug=True)