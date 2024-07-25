let buttons = document.querySelector(".buttons");
let btn = document.querySelectorAll("span");
let valores = document.getElementById("valores");
let toggleBtn = document.querySelector(".toggleBtn");
let body = document.querySelector("body");

//eval() para avaliar uma expressão aritmética; JavaScript avalia expressões aritméticas automaticamente.

for (let i = 0; i < btn.length; i++) {
  btn[i].addEventListener("click", function () {
    if (this.innerHTML == "=") {
      valores.innerHTML = eval(valores.innerHTML);
    } else {
      if (this.innerHTML == "limpar") {
        valores.innerHTML = ""; 
      } else {
        valores.innerHTML += this.innerHTML;
      }
    }
  });
}

toggleBtn.onclick = function () {
  body.classList.toggle("dark");
};