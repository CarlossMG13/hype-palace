/* Mobile Menu */
const openMenuBtn = document.getElementById("open-menu-btn");
const closeMenuBtn = document.getElementById("close-menu-btn");
const mobileMenuSlide = document.getElementById("mobile-menu-slide");
const overlay = document.getElementById("overlay");

/* Mobile cart */
const openCartBtn = document.getElementById("open-cart-btn");
const closeCartBtn = document.getElementById("close-cart-btn");
const mobileCartSlide = document.getElementById("mobile-cart-slide");

openMenuBtn.addEventListener("click", () => {
  mobileMenuSlide.classList.remove("-translate-x-full");
  overlay.classList.remove("hidden");
});

closeMenuBtn.addEventListener("click", () => {
  mobileMenuSlide.classList.add("-translate-x-full");
  overlay.classList.add("hidden");
});

openCartBtn.addEventListener("click", () => {
  mobileCartSlide.classList.remove("-translate-y-full");
  overlay.classList.remove("hidden");
});

closeCartBtn.addEventListener("click", () => {
  mobileCartSlide.classList.add("-translate-y-full");
  overlay.classList.add("hidden");
});
