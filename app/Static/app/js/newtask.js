var createTaskBtn = document.getElementById("create-task-btn");
var modal = document.getElementById("create-task-modal");
var closeBtn = document.getElementsByClassName("cerrar")[0];

createTaskBtn.onclick = function () {
  modal.style.display = "block";
};

closeBtn.onclick = function () {
  modal.style.display = "none";
};

window.onclick = function (event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
};

