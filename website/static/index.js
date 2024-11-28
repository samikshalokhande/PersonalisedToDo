function deleteToDo(todo_id) {
  fetch('/delete-todo', {
    method: 'POST',  // Corrected 'methods' to 'method'
    headers: {
      'Content-Type': 'application/json',  // Add Content-Type header
    },
    body: JSON.stringify({ todo_id: todo_id })  // Corrected key to match Flask route
  })
  .then((response) => {
    if (response.ok) {
      window.location.href = "/";  // Reload the page after successful deletion
    } else {
      alert("Error deleting todo.");
    }
  })
  .catch((error) => {
    console.error('Error:', error);
    alert('There was an error processing your request.');
  });
}




function editToDo(todo_id) {
  // Hide the current text and show the input field for editing
  document.getElementById(`todo-text-${todo_id}`).style.display = 'none';
  document.getElementById(`edit-input-${todo_id}`).style.display = 'block';
}

function saveEdit(todo_id) {
  const updatedText = document.getElementById(`edit-todo-input-${todo_id}`).value;

  // Send the updated text to the backend
  fetch('/edit-todo', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      todoId: todo_id,
      newText: updatedText
    })
  })
  .then(response => response.json())
  .then(data => {
    if (data.success) {
      // Update the text in the DOM and hide the input field
      document.getElementById(`todo-text-${todo_id}`).innerText = updatedText;
      document.getElementById(`todo-text-${todo_id}`).style.display = 'block';
      document.getElementById(`edit-input-${todo_id}`).style.display = 'none';
    } else {
      alert('Failed to update todo.');
    }
  })
  .catch(error => {
    console.error('Error:', error);
    alert('Error updating todo.');
  });
}

function cancelEdit(todo_id) {
  // Cancel the edit and hide the input field
  document.getElementById(`todo-text-${todo_id}`).style.display = 'block';
  document.getElementById(`edit-input-${todo_id}`).style.display = 'none';
}
