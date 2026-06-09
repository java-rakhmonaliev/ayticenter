// IT Center Yaypan — main.js
// NotBoring interactivity: tilt, reveal, juice

// ── Scroll reveal ──
const revealObserver = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry, i) => {
      if (entry.isIntersecting) {
        const el = entry.target;
        const delay = el.dataset.delay || 0;
        setTimeout(() => {
          el.classList.add('visible');
        }, delay);
        revealObserver.unobserve(el);
      }
    });
  },
  { threshold: 0.12, rootMargin: '0px 0px -40px 0px' }
);

document.querySelectorAll('.reveal').forEach((el) => {
  revealObserver.observe(el);
});

// ── Stagger children ──
document.querySelectorAll('[data-stagger]').forEach((parent) => {
  const children = parent.querySelectorAll('.reveal');
  children.forEach((child, i) => {
    child.dataset.delay = i * 70;
  });
});

// ── 3D Tilt cards ──
function initTiltCards() {
  document.querySelectorAll('.tilt-card').forEach((card) => {
    card.addEventListener('mousemove', (e) => {
      const rect = card.getBoundingClientRect();
      const cx = rect.left + rect.width / 2;
      const cy = rect.top + rect.height / 2;
      const dx = (e.clientX - cx) / (rect.width / 2);
      const dy = (e.clientY - cy) / (rect.height / 2);
      const maxTilt = 10;
      card.style.transform = `perspective(800px) rotateY(${dx * maxTilt}deg) rotateX(${-dy * maxTilt}deg) translateZ(4px)`;
      card.style.transition = 'transform 0.1s ease';
      // Highlight shimmer follows cursor
      const shimmer = card.querySelector('.card-shimmer');
      if (shimmer) {
        shimmer.style.background = `radial-gradient(circle at ${((e.clientX - rect.left) / rect.width) * 100}% ${((e.clientY - rect.top) / rect.height) * 100}%, rgba(255,255,255,0.08) 0%, transparent 60%)`;
      }
    });
    card.addEventListener('mouseleave', () => {
      card.style.transform = 'perspective(800px) rotateY(0deg) rotateX(0deg) translateZ(0)';
      card.style.transition = 'transform 0.5s cubic-bezier(0.22,1,0.36,1)';
      const shimmer = card.querySelector('.card-shimmer');
      if (shimmer) shimmer.style.background = '';
    });
  });
}

initTiltCards();

// Re-init after any DOM changes
const tiltObserver = new MutationObserver(() => initTiltCards());
tiltObserver.observe(document.body, { childList: true, subtree: true });

// ── Button press physics ──
document.querySelectorAll('.btn-primary, .btn-ghost').forEach((btn) => {
  btn.addEventListener('mousedown', () => {
    btn.style.transform = 'scale(0.96) translateY(1px)';
    btn.style.transition = 'transform 80ms ease';
  });
  btn.addEventListener('mouseup', () => {
    btn.style.transform = '';
    btn.style.transition = 'transform 300ms cubic-bezier(0.34,1.56,0.64,1)';
  });
  btn.addEventListener('mouseleave', () => {
    btn.style.transform = '';
    btn.style.transition = 'transform 300ms cubic-bezier(0.34,1.56,0.64,1)';
  });
});

// ── Navbar scroll transform ──
const navbar = document.getElementById('navbar');
if (navbar) {
  let lastY = 0;
  window.addEventListener('scroll', () => {
    const y = window.scrollY;
    if (y > 60) {
      navbar.classList.add('scrolled');
    } else {
      navbar.classList.remove('scrolled');
    }
    lastY = y;
  }, { passive: true });
}

// ── Smooth anchor scroll ──
document.querySelectorAll('a[href^="#"]').forEach((a) => {
  a.addEventListener('click', (e) => {
    const target = document.querySelector(a.getAttribute('href'));
    if (target) {
      e.preventDefault();
      target.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
  });
});

// ── Hero ambient orb cursor follow ──
const heroOrb = document.getElementById('hero-cursor-orb');
if (heroOrb) {
  document.addEventListener('mousemove', (e) => {
    const x = (e.clientX / window.innerWidth) * 100;
    const y = (e.clientY / window.innerHeight) * 100;
    heroOrb.style.transform = `translate(${(x - 50) * 0.3}px, ${(y - 50) * 0.3}px)`;
  });
}

// ── Course counter (animated number if in view) ──
function animateNumber(el) {
  const target = parseInt(el.dataset.count, 10);
  if (isNaN(target)) return;
  let current = 0;
  const step = Math.ceil(target / 30);
  const timer = setInterval(() => {
    current = Math.min(current + step, target);
    el.textContent = current;
    if (current >= target) clearInterval(timer);
  }, 30);
}

const countEls = document.querySelectorAll('[data-count]');
const countObserver = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    if (entry.isIntersecting) {
      animateNumber(entry.target);
      countObserver.unobserve(entry.target);
    }
  });
}, { threshold: 0.5 });
countEls.forEach((el) => countObserver.observe(el));
