/* ── Intersection Observer: reveal elements on scroll ── */
(function () {
  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('revealed');
          observer.unobserve(entry.target);
        }
      });
    },
    {
      threshold: 0.15,
      rootMargin: '0px 0px -30px 0px',
    }
  );

  document.querySelectorAll('.reveal').forEach((el) => observer.observe(el));
})();

/* ── Lazy loading images ── */
(function () {
  const imgObserver = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;

        const img = entry.target;
        const src = img.getAttribute('data-src');
        if (!src) return;

        img.src = src;
        img.onload = () => img.classList.add('loaded');
        imgObserver.unobserve(img);
      });
    },
    { rootMargin: '200px 0px' }
  );

  document.querySelectorAll('img.lazy').forEach((img) => imgObserver.observe(img));
})();

/* ── Nav scroll effect ── */
(function () {
  const nav = document.querySelector('nav');
  if (!nav) return;

  let ticking = false;

  function updateNav() {
    if (window.scrollY > 10) {
      nav.classList.add('nav-scrolled');
    } else {
      nav.classList.remove('nav-scrolled');
    }
    ticking = false;
  }

  window.addEventListener('scroll', () => {
    if (!ticking) {
      requestAnimationFrame(updateNav);
      ticking = true;
    }
  });
})();

/* ── Smooth anchor scroll offset (account for fixed nav) ── */
(function () {
  document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
    anchor.addEventListener('click', function (e) {
      const targetId = this.getAttribute('href');
      if (targetId === '#') return;

      const target = document.querySelector(targetId);
      if (!target) return;

      e.preventDefault();

      const navHeight = 64;
      const top = target.getBoundingClientRect().top + window.scrollY - navHeight;

      window.scrollTo({ top, behavior: 'smooth' });
    });
  });
})();
