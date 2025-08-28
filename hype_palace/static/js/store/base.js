/* Mobile Menu */
const openMenuBtn = document.getElementById("open-menu-btn");
const closeMenuBtn = document.getElementById("close-menu-btn");
const mobileMenuSlide = document.getElementById("mobile-menu-slide");
const overlay = document.getElementById("overlay");

openMenuBtn.addEventListener("click", () => {
  mobileMenuSlide.classList.remove("-translate-x-full");
  overlay.classList.remove("hidden");
});

closeMenuBtn.addEventListener("click", () => {
  mobileMenuSlide.classList.add("-translate-x-full");
  overlay.classList.add("hidden");
});

// Corrección: Añadir el punto para seleccionar la clase
const openCartBtns = document.querySelectorAll(".open-cart-btn");
const closeCartBtn = document.getElementById("close-cart-btn");
const cartSlide = document.getElementById("cart-slide");

openCartBtns.forEach((button) => {
  button.addEventListener("click", () => {
    cartSlide.classList.remove("-translate-y-full");
    overlay.classList.remove("hidden");
  });
});

closeCartBtn.addEventListener("click", () => {
  cartSlide.classList.add("-translate-y-full");
  overlay.classList.add("hidden");
});
