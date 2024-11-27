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
