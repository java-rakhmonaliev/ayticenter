// IT Center Yaypan — main.js
// Alpine.js handles most interactivity.
// This file is for any additional vanilla JS.

document.addEventListener('DOMContentLoaded', () => {
  // Smooth anchor scrolling (for any on-page links)
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
      const target = document.querySelector(this.getAttribute('href'));
      if (target) {
        e.preventDefault();
        target.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    });
  });
});
