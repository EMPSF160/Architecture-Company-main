// ONYX / ONYX - Modern Architecture Interactive Engine

$(document).ready(function() {
    
    // ===== Active Page Highlighting =====
    function setActiveNavLink() {
        const currentPage = window.location.pathname.split('/').pop() || 'index.html';
        const currentPageBase = currentPage.replace('.html', '') || 'index';
        
        $('.navbar-nav .nav-link').each(function() {
            const href = $(this).attr('href');
            if (!href) return;
            const hrefBase = href.replace('.html', '') || 'index';
            
            if (href === currentPage || 
                hrefBase === currentPageBase || 
                (currentPage === '' && (href === 'index.html' || hrefBase === 'index'))) {
                $(this).addClass('active');
            } else {
                $(this).removeClass('active');
            }
        });
    }
    setActiveNavLink();

    // ===== Navbar Blur & Background On Scroll =====
    $(window).on('scroll', function() {
        if ($(this).scrollTop() > 40) {
            $('header').addClass('scrolled');
        } else {
            $('header').removeClass('scrolled');
        }
    });

    // ===== Smooth Scroll for Anchor Links =====
    $('a[href^="#"]').on('click', function(e) {
        const href = $(this).attr('href');
        if (href === '#' || href === '') return;
        const target = $(href);
        if (target.length) {
            e.preventDefault();
            $('html, body').stop().animate({
                scrollTop: target.offset().top - 90
            }, 800);
        }
    });

    // ===== Scroll Reveal Animation Engine =====
    function initScrollReveal() {
        const revealElements = document.querySelectorAll(
            '.reveal-on-scroll, .card, .bento-card, .process-step-card, .cta-card, .testimonial-card, .section-title'
        );
        
        if (!('IntersectionObserver' in window)) {
            revealElements.forEach(el => el.classList.add('is-visible'));
            return;
        }

        const observer = new IntersectionObserver((entries, obs) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('is-visible');
                    obs.unobserve(entry.target);
                }
            });
        }, {
            threshold: 0.12,
            rootMargin: '0px 0px -40px 0px'
        });

        revealElements.forEach((el, index) => {
            el.classList.add('reveal-on-scroll');
            if (!el.classList.contains('delay-1') && !el.classList.contains('delay-2') && !el.classList.contains('delay-3')) {
                const delayMod = (index % 4) + 1;
                el.classList.add(`delay-${delayMod}`);
            }
            observer.observe(el);
        });
    }
    initScrollReveal();

    // ===== Animated Stat Counters =====
    function initStatCounters() {
        const counters = document.querySelectorAll('[data-counter]');
        if (!counters.length) return;

        const counterObserver = new IntersectionObserver((entries, obs) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const counter = entry.target;
                    const target = parseFloat(counter.getAttribute('data-counter'));
                    const prefix = counter.getAttribute('data-prefix') || '';
                    const suffix = counter.getAttribute('data-suffix') || '';
                    const isDecimal = target % 1 !== 0;
                    const duration = 2000;
                    const startTime = performance.now();

                    function updateCounter(currentTime) {
                        const elapsed = currentTime - startTime;
                        const progress = Math.min(elapsed / duration, 1);
                        // Ease out cubic
                        const easeOut = 1 - Math.pow(1 - progress, 3);
                        const currentVal = isDecimal ? (easeOut * target).toFixed(1) : Math.floor(easeOut * target);
                        
                        counter.textContent = `${prefix}${currentVal}${suffix}`;
                        
                        if (progress < 1) {
                            requestAnimationFrame(updateCounter);
                        } else {
                            counter.textContent = `${prefix}${target}${suffix}`;
                        }
                    }
                    requestAnimationFrame(updateCounter);
                    obs.unobserve(counter);
                }
            });
        }, { threshold: 0.5 });

        counters.forEach(counter => counterObserver.observe(counter));
    }
    initStatCounters();

    // ===== Interactive 3D Card Hover Tilt Effect =====
    const tiltCards = document.querySelectorAll('.card, .bento-card, .process-step-card');
    tiltCards.forEach(card => {
        card.addEventListener('mousemove', function(e) {
            const rect = card.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;
            const centerX = rect.width / 2;
            const centerY = rect.height / 2;
            const deltaX = (x - centerX) / centerX;
            const deltaY = (y - centerY) / centerY;

            card.style.transform = `perspective(1000px) rotateX(${-deltaY * 4}deg) rotateY(${deltaX * 4}deg) translateY(-6px)`;
        });

        card.addEventListener('mouseleave', function() {
            card.style.transform = '';
        });
    });

    // ===== Floating Back to Top Button =====
    const backToTopBtn = $('<button class="back-to-top" aria-label="Back to top"><i class="fas fa-chevron-up"></i></button>');
    $('body').append(backToTopBtn);

    $(window).on('scroll', function() {
        if ($(this).scrollTop() > 350) {
            backToTopBtn.css('display', 'flex').fadeIn(200);
        } else {
            backToTopBtn.fadeOut(200);
        }
    });

    backToTopBtn.on('click', function() {
        $('html, body').animate({ scrollTop: 0 }, 700);
    });

    // ===== Contact & Inquiry Form Handling =====
    $('#contactForm, #careerForm, #loginForm, #registerForm').on('submit', function(e) {
        e.preventDefault();
        
        const form = $(this);
        const submitBtn = form.find('button[type="submit"]');
        const originalText = submitBtn.html();
        const formMessages = form.find('.form-message');
        
        // Show loading state
        submitBtn.prop('disabled', true).html('<i class="fas fa-spinner fa-spin"></i> Processing...');
        formMessages.removeClass('success error').hide();

        setTimeout(() => {
            formMessages.removeClass('error').addClass('success').html('<i class="fas fa-check-circle me-2"></i> Thank you! Your request has been received. Our lead architect will be in touch promptly.').fadeIn();
            form[0].reset();
            submitBtn.prop('disabled', false).html(originalText);
        }, 800);
    });

    // ===== Interactive Category Filtering (Projects, News, Careers) =====
    $('.filter-btn').on('click', function() {
        const filterValue = $(this).attr('data-filter');
        const container = $(this).closest('section').find('.filter-container');
        
        // Update active class
        $(this).siblings('.filter-btn').removeClass('active');
        $(this).addClass('active');

        if (filterValue === 'all') {
            container.find('.filter-item').fadeIn(350).css('display', 'block');
        } else {
            container.find('.filter-item').each(function() {
                const category = $(this).attr('data-category');
                if (category && category.includes(filterValue)) {
                    $(this).fadeIn(350).css('display', 'block');
                } else {
                    $(this).fadeOut(200);
                }
            });
        }
    });

    // ===== Dark Mode Locked =====
    function enforceDarkTheme() {
        document.documentElement.setAttribute('data-theme', 'dark');
        localStorage.setItem('theme', 'dark');
        $('#themeIcon').removeClass('fa-sun').addClass('fa-moon');
        $('#themeText').text('Dark Mode (Active)');
    }
    enforceDarkTheme();

    // Set dynamic current year in footer
    const yearEl = document.getElementById('currentYear');
    if (yearEl) {
        yearEl.textContent = new Date().getFullYear();
    }
});

