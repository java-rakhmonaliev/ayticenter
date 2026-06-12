/* IT Center Yaypan — motion layer */
(function () {
  const EASE = 'cubic-bezier(0.16,1,0.3,1)';

  /* ── Scroll reveal ───────────────────────────────────── */
  const revealObserver = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        entry.target.classList.add('visible');
        revealObserver.unobserve(entry.target);
      });
    },
    { threshold: 0.1 }
  );

  document.querySelectorAll('[data-stagger]').forEach((parent) => {
    parent.querySelectorAll('.reveal').forEach((child, i) => {
      child.style.setProperty('--rv-delay', i * 90 + 'ms');
    });
  });

  document.querySelectorAll('.reveal').forEach((el) => revealObserver.observe(el));

  /* ── Count-up numbers ────────────────────────────────── */
  const countObserver = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        const el = entry.target;
        countObserver.unobserve(el);
        const target = parseFloat(el.dataset.count) || 0;
        const suffix = el.dataset.suffix || '';
        const t0 = performance.now();
        const dur = 1400;
        const step = (now) => {
          const p = Math.min(1, (now - t0) / dur);
          const k = 1 - Math.pow(1 - p, 3);
          el.textContent = Math.round(target * k) + suffix;
          if (p < 1) requestAnimationFrame(step);
        };
        requestAnimationFrame(step);
      });
    },
    { threshold: 0.4 }
  );
  document.querySelectorAll('[data-count]').forEach((el) => countObserver.observe(el));

  /* ── 3D tilt cards ───────────────────────────────────── */
  const touchOnly = window.matchMedia('(hover: none)').matches;
  if (!touchOnly) {
    document.querySelectorAll('.tilt-card').forEach((card) => {
      card.addEventListener('mousemove', (e) => {
        const r = card.getBoundingClientRect();
        const x = (e.clientX - r.left) / r.width - 0.5;
        const y = (e.clientY - r.top) / r.height - 0.5;
        card.style.transform =
          'perspective(900px) rotateX(' + (-y * 5).toFixed(2) + 'deg) rotateY(' + (x * 7).toFixed(2) + 'deg) translateY(-4px)';
      });
      card.addEventListener('mouseleave', () => {
        card.style.transition = 'transform 0.55s ' + EASE;
        card.style.transform = 'none';
        setTimeout(() => { card.style.transition = ''; }, 560);
      });
    });

    /* ── Magnetic buttons ──────────────────────────────── */
    document.querySelectorAll('[data-mag]').forEach((el) => {
      el.addEventListener('mousemove', (e) => {
        const r = el.getBoundingClientRect();
        const x = (e.clientX - r.left) / r.width - 0.5;
        const y = (e.clientY - r.top) / r.height - 0.5;
        el.style.transform = 'translate(' + (x * 10).toFixed(1) + 'px,' + (y * 8).toFixed(1) + 'px)';
      });
      el.addEventListener('mouseleave', () => {
        el.style.transition = 'transform 0.4s ' + EASE;
        el.style.transform = 'none';
        setTimeout(() => { el.style.transition = ''; }, 410);
      });
    });
  }

  /* ── Scroll progress bar ─────────────────────────────── */
  const progress = document.querySelector('[data-progress]');
  if (progress) {
    const onScroll = () => {
      const h = document.documentElement;
      const max = h.scrollHeight - h.clientHeight;
      progress.style.width = (max > 0 ? (h.scrollTop / max) * 100 : 0) + '%';
    };
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
  }

  /* ── Hero typing animation ───────────────────────────── */
  const typedEl = document.getElementById('typed');
  if (typedEl) {
    let words = ['DASTURLASH', 'GRAFIK DIZAYN', 'PYTHON', 'SMM', 'ROBOTOTEXNIKA'];
    const src = document.getElementById('typed-words');
    if (src) {
      try {
        const parsed = JSON.parse(src.textContent);
        if (Array.isArray(parsed) && parsed.length) words = parsed.map((w) => String(w).toUpperCase());
      } catch (e) { /* keep defaults */ }
    }
    let wi = 0;
    let deleting = false;
    const tick = () => {
      const w = words[wi];
      let t = typedEl.textContent;
      let delay = 80;
      if (!deleting) {
        t = w.slice(0, t.length + 1);
        if (t === w) { deleting = true; delay = 2100; }
      } else {
        t = w.slice(0, t.length - 1);
        if (t.length === 0) { deleting = false; wi = (wi + 1) % words.length; delay = 420; }
        else delay = 38;
      }
      typedEl.textContent = t;
      setTimeout(tick, delay);
    };
    setTimeout(tick, 600);
  }

  /* ── Smooth anchor scroll ────────────────────────────── */
  document.querySelectorAll('a[href^="#"]').forEach((a) => {
    a.addEventListener('click', (e) => {
      const target = document.querySelector(a.getAttribute('href'));
      if (!target) return;
      e.preventDefault();
      target.scrollIntoView({ behavior: 'smooth' });
    });
  });
})();
