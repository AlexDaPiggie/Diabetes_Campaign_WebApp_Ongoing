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

/* ── Page scroll progress ── */
(function () {
  const bar = document.querySelector('.scroll-progress__bar');
  if (!bar) return;

  let ticking = false;

  function updateScrollProgress() {
    const maxScroll = document.documentElement.scrollHeight - window.innerHeight;
    const progress = maxScroll > 0 ? Math.min(Math.max(window.scrollY / maxScroll, 0), 1) : 1;

    bar.style.transform = `scaleX(${progress})`;
    ticking = false;
  }

  function requestProgressUpdate() {
    if (ticking) return;
    requestAnimationFrame(updateScrollProgress);
    ticking = true;
  }

  updateScrollProgress();
  window.addEventListener('scroll', requestProgressUpdate, { passive: true });
  window.addEventListener('resize', requestProgressUpdate);
  window.addEventListener('load', updateScrollProgress);
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

/* ── Number animation on scroll ── */
(function () {
  const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const ratioPattern = /^(\d[\d,]*)\s+in\s+(\d[\d,]*)$/i;
  const numberPattern = /^([^0-9]*)(\d[\d,]*(?:\.\d+)?)(.*)$/;

  const parseStatTarget = (targetText) => {
    const normalizedTarget = (targetText || '').trim();
    const ratioMatch = normalizedTarget.match(ratioPattern);

    if (ratioMatch) {
      return {
        type: 'ratio',
        left: Number(ratioMatch[1].replace(/,/g, '')),
        right: Number(ratioMatch[2].replace(/,/g, '')),
      };
    }

    const numberMatch = normalizedTarget.match(numberPattern);
    if (numberMatch) {
      return {
        type: 'number',
        prefix: numberMatch[1],
        value: Number(numberMatch[2].replace(/,/g, '')),
        suffix: numberMatch[3],
      };
    }

    return {
      type: 'text',
      value: normalizedTarget,
    };
  };

  const formatAnimatedStat = (target, progress) => {
    if (target.type === 'ratio') {
      const left = Math.floor(target.left * progress).toLocaleString();
      const right = Math.floor(target.right * progress).toLocaleString();
      return `${left} in ${right}`;
    }

    if (target.type === 'number') {
      const value = Math.floor(target.value * progress).toLocaleString();
      return `${target.prefix}${value}${target.suffix}`;
    }

    return target.value;
  };

  const animateNumber = (element) => {
    const targetText = element.dataset.targetText || element.dataset.targetNumber || element.textContent;
    const parsedTarget = parseStatTarget(targetText);

    if (prefersReducedMotion) {
      element.textContent = targetText;
      return;
    }

    if (parsedTarget.type === 'text') {
      element.textContent = targetText;
      return;
    }

    const duration = 500;
    let startTime = null;

    element.textContent = formatAnimatedStat(parsedTarget, 0);

    const animationStep = (currentTime) => {
      if (!startTime) startTime = currentTime;
      const progress = Math.min((currentTime - startTime) / duration, 1);

      element.textContent = progress < 1
        ? formatAnimatedStat(parsedTarget, progress)
        : targetText;

      if (progress < 1) {
        requestAnimationFrame(animationStep);
      }
    };

    requestAnimationFrame(animationStep);
  };

  const numberObserver = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          animateNumber(entry.target);
          numberObserver.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.5 } // Trigger when 50% of the element is visible
  );

  document.querySelectorAll('.animate-number').forEach((el) => {
    numberObserver.observe(el);
  });
})();
