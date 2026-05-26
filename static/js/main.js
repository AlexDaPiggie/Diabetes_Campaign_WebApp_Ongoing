/* ── Intersection Observer: reveal elements on scroll ── */
(function () {
  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          const delay = parseInt(entry.target.getAttribute('data-reveal-delay')) || 0;
          if (delay > 0) {
            setTimeout(() => {
              entry.target.classList.add('revealed');
            }, delay);
          } else {
            entry.target.classList.add('revealed');
          }
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
        if (entry.isIntersecting && !entry.target.closest('.personal-story')) {
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

/* ── Waffle Chart Scan Trigger ── */
(function () {
  const initWaffleScan = () => {
    const waffle = document.getElementById('waffle-chart');
    if (!waffle) return;

    const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            waffle.classList.add('scanning');

            const icons = waffle.querySelectorAll('.waffle-icon');
            
            if (prefersReducedMotion) {
              // Immediate reveal for accessibility
              icons.forEach((icon) => {
                const status = icon.getAttribute('data-status');
                icon.classList.add(`waffle-icon--${status}`);
              });
            } else {
              // Staggered reveal of icons based on status
              icons.forEach((icon, index) => {
                const status = icon.getAttribute('data-status');
                // Delay reveal until scan bar reaches approx position
                const delay = (index / icons.length) * 2000;
                setTimeout(() => {
                  icon.classList.add(`waffle-icon--${status}`);
                }, delay + 300);
              });
            }

            observer.unobserve(waffle);
          }
        });
      },
      { threshold: 0.5 }
    );

    observer.observe(waffle);
  };

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initWaffleScan);
  } else {
    initWaffleScan();
  }
})();

/* ── Personal Story Sequenced Animation ── */
(function () {
  const section = document.querySelector('.personal-story');
  if (!section) return;

  const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  const source = section.querySelector('.personal-story__source');
  const callout = section.querySelector('.personal-story__callout');
  const statNumbers = section.querySelectorAll('.personal-story__stats .motion-stat');
  const statLabels = section.querySelectorAll('.personal-story__stats .font-ui');
  const animateNumbers = section.querySelectorAll('.animate-number');

  // Hide elements via JS so content is visible without JS
  if (source) source.classList.add('ps-hidden');
  if (callout) callout.classList.add('ps-hidden');
  statNumbers.forEach(el => el.classList.add('ps-hidden'));
  statLabels.forEach(el => el.classList.add('ps-hidden'));

  if (prefersReducedMotion) {
    [source, callout].forEach(el => { if (el) el.classList.remove('ps-hidden'); });
    statNumbers.forEach(el => el.classList.remove('ps-hidden'));
    statLabels.forEach(el => el.classList.remove('ps-hidden'));
    animateNumbers.forEach(el => {
      el.textContent = el.dataset.targetText || el.dataset.targetNumber || el.textContent;
    });
    return;
  }

  let animated = false;

  const observer = new IntersectionObserver(
    (entries) => {
      if (entries[0].isIntersecting && !animated) {
        animated = true;
        runAnimation();
        observer.unobserve(section);
      }
    },
    { threshold: 0.2 }
  );

  observer.observe(section);

  function runAnimation() {
    // Phase 1: Source fade in (0–500ms)
    if (source) source.classList.remove('ps-hidden');

    // Phase 2: Stats group fade in (500–1000ms)
    setTimeout(() => {
      statNumbers.forEach(el => el.classList.remove('ps-hidden'));
      statLabels.forEach(el => el.classList.remove('ps-hidden'));
    }, 500);

    // Phase 3: Synchronized number counting (1000–2500ms)
    setTimeout(() => {
      animateNumbersSync(animateNumbers, 750);
    }, 1750);

    // Phase 4: Callout fade in (1750–2250ms)
    setTimeout(() => {
      if (callout) callout.classList.remove('ps-hidden');
    }, 1750);
  }

  function animateNumbersSync(elements, duration) {
    const numberPattern = /^([^0-9]*)(\d[\d,]*(?:\.\d+)?)(.*)$/;

    const targets = Array.from(elements).map(el => {
      const raw = el.dataset.targetText || el.dataset.targetNumber || el.textContent;
      const match = (raw || '').trim().match(numberPattern);
      if (match) {
        return {
          el,
          prefix: match[1],
          value: parseFloat(match[2].replace(/,/g, '')),
          suffix: match[3],
        };
      }
      return { el, prefix: '', value: 0, suffix: '', raw };
    });

    // Pre-measure and lock widths to prevent layout shift during animation
    targets.forEach(t => {
      if (t.raw) return;
      const finalText = `${t.prefix}${t.value}${t.suffix}`;
      const prevText = t.el.textContent;
      t.el.textContent = finalText;
      const w = t.el.offsetWidth;
      t.el.style.width = w + 'px';
      t.el.textContent = prevText;
    });

    const startTime = performance.now();

    function step(now) {
      const elapsed = now - startTime;
      const progress = Math.min(elapsed / duration, 1);

      targets.forEach(t => {
        if (t.raw) {
          t.el.textContent = t.raw;
          return;
        }
        if (progress >= 1) {
          t.el.textContent = `${t.prefix}${t.value}${t.suffix}`;
          return;
        }
        const current = t.value * progress;
        const hasDecimal = String(t.value).includes('.');
        const formatted = hasDecimal
          ? current.toFixed(1)
          : Math.floor(current).toLocaleString();
        t.el.textContent = `${t.prefix}${formatted}${t.suffix}`;
      });

      if (progress < 1) {
        requestAnimationFrame(step);
      }
    }

    requestAnimationFrame(step);
  }
})();
