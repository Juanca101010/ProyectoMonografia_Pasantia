var createTaskBtn = document.getElementById("create");
var modal = document.querySelector(".createtask");
var closeBtn = document.querySelector(".createtask .submit-btn");

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
