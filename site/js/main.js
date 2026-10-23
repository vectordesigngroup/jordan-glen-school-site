(function () {
  var root = document.documentElement;
  var button = document.querySelector(".menu-toggle");
  var nav = document.getElementById("site-nav");
  if (!button || !nav) {
    return;
  }

  root.classList.add("js");

  var label = button.querySelector(".menu-label");

  function setOpen(open) {
    button.setAttribute("aria-expanded", open ? "true" : "false");
    nav.classList.toggle("is-open", open);
    if (label) {
      label.textContent = open ? "Close" : "Menu";
    }
  }

  button.addEventListener("click", function () {
    var open = button.getAttribute("aria-expanded") === "true";
    setOpen(!open);
  });

  document.addEventListener("keydown", function (event) {
    if (event.key === "Escape" && button.getAttribute("aria-expanded") === "true") {
      setOpen(false);
      button.focus();
    }
  });

  nav.addEventListener("click", function (event) {
    if (event.target.closest("a")) {
      setOpen(false);
    }
  });

  window.addEventListener("resize", function () {
    if (window.innerWidth >= 980) {
      setOpen(false);
    }
  });
})();
