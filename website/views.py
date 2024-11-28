from flask import Blueprint, jsonify, render_template, request, flash
from flask_login import login_required, current_user
from .models import ToDo
from . import db
import json

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
  if request.method == 'POST':
    todo = request.form.get('todoInput')
    if len(todo) < 1:
      flash('ToDo is too short', category="danger")
    else:
      # add note
      new_todo = ToDo(todo_data=todo, user_id=current_user.id)
      db.session.add(new_todo)
      db.session.commit()
  # render temp - templates/index.html
  return render_template("home.html", user=current_user)


@views.route('/delete-todo', methods=['POST'])
def delete_todo():
  todo = json.loads(request.data)
  print("inside route")
  print(todo)
  todo_id = todo['todo_id']  # Key should match the one sent in JavaScript
  todo_item = ToDo.query.get(todo_id)
  if todo_item:
    if todo_item.user_id == current_user.id:
      db.session.delete(todo_item)
      db.session.commit()
      return jsonify({"message": "Todo deleted successfully"}), 200
  return jsonify({"message": "Todo not found"}), 404


@views.route('/edit-todo', methods=['POST'])
def edit_todo():
  data = json.loads(request.data)
  todo_id = data.get('todoId')
  new_text = data.get('newText')

  todo_item = ToDo.query.get(todo_id)

  if todo_item:
    if todo_item.user_id == current_user.id:
      # Update the todo item
      todo_item.todo_data = new_text
      db.session.commit()
      return jsonify({
          "success": True,
          "message": "Todo updated successfully"
      }), 200
    else:
      return jsonify({"success": False, "message": "Unauthorized"}), 403
  else:
    return jsonify({"success": False, "message": "Todo not found"}), 404
