let cookieModal = document.querySelector(".cookie-consent-modal");
let cancelCookieBtn = document.querySelector(".btn.cancel");
let acceptCookieBtn = document.querySelector(".btn.accept");

cancelCookieBtn.addEventListener("click", function (){
  cookieModal.classList.remove("active");
});

acceptCookieBtn.addEventListener("click", function (){
  cookieModal.classList.remove("active");
  localStorage.setItem("cookieAccepted", "yes");
});

function checkLocalStorage() {
  let cookieAccepted = localStorage.getItem("cookieAccepted");
  if (cookieAccepted === "yes") {
    cookieModal.classList.remove("active");
  } else {
    cookieModal.classList.add("active");
  }
}

setTimeout(function (){
  checkLocalStorage();
}, 2000);
