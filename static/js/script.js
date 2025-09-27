// Get all delete buttons
const deleteButtons = document.querySelectorAll('.delete-button');

// Add event listener to each delete button
deleteButtons.forEach((button) => {
    button.addEventListener('click', (e) => {
        // Get the modal ID from the button's data-target attribute
        const modalId = button.dataset.target;
        // Get the modal element
        const modal = document.getElementById(modalId);
        // Show the modal
        const modalInstance = new bootstrap.Modal(modal);
        modalInstance.show();
    });
});
// Get all delete buttons
const deleteButtons = document.querySelectorAll('.delete-button');

// Add event listener to each delete button
deleteButtons.forEach((button) => {
    button.addEventListener('click', (e) => {
        // Get the modal ID from the button's data-target attribute
        const modalId = button.dataset.target;
        // Get the modal element
        const modal = document.getElementById(modalId);
        // Show the modal
        const modalInstance = new bootstrap.Modal(modal);
        modalInstance.show();
    });
});
// Delete button click event handler
function deleteTour(id) {
  fetch(`/delete/${id}/`, {
    method: 'DELETE',
  })
  .then((response) => response.json())
  .then((data) => console.log(data))
  .catch((error) => console.error(error));
}
// Delete button click event handler
function deleteTour(id) {
  fetch(`/delete/${id}/`, {
    method: 'DELETE',
  })
  .then((response) => response.json())
  .then((data) => console.log(data))
  .catch((error) => console.error(error));
}


// Get the modal
var modal = document.getElementById("deleteTourModal-{{ forloop.counter }}");

// Get the button that opens the modal
var btn = document.getElementById("myBtn{{ forloop.counter }}");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks the button, open the modal
btn.onclick = function() {
  modal.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
  modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}






