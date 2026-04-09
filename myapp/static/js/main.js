// ====================
// Kafae Oon Jai Café - Main JavaScript
// ====================

document.addEventListener('DOMContentLoaded', function() {
    
    // 1. Smooth Scroll
    window.scrollToSection = function(id) {
        const element = document.getElementById(id);
        if (element) {
            element.scrollIntoView({ behavior: 'smooth' });
        }
    };

    // 2. Navbar Scroll Effect
    const navbar = document.querySelector('.navbar');
    if (navbar) {
        window.addEventListener('scroll', () => {
            if (window.scrollY > 50) {
                navbar.classList.add('scrolled');
            } else {
                navbar.classList.remove('scrolled');
            }
        });
    }

    // 3. Star Rating System
    const stars = document.querySelectorAll('.star-item');
    const starHidden = document.getElementById('revStarHidden');
    
    if (stars.length > 0 && starHidden) {
        stars.forEach(star => {
            star.addEventListener('click', function() {
                const val = this.getAttribute('data-value');
                starHidden.value = val;
                
                // จัดการสีดาว
                stars.forEach(s => s.classList.remove('selected'));
                this.classList.add('selected');
                
                // เลือกดาวทั้งหมดที่น้อยกว่าด้วย
                stars.forEach(s => {
                    if (s.getAttribute('data-value') <= val) {
                        s.classList.add('selected');
                    }
                });
            });
        });
    }

    // 4. Review Form Submission (AJAX หรือ Preview)
    const reviewForm = document.getElementById('reviewForm');
    const reviewList = document.getElementById('reviewList');
    
    if (reviewForm && reviewList) {
        reviewForm.addEventListener('submit', function(e) {
            // ไม่ต้อง e.preventDefault() ถ้าอยากให้ Django จัดการ
            // แต่ถ้าอยาก preview ก่อนส่ง ให้ใช้ e.preventDefault()
            
            const name = document.getElementById('revName')?.value;
            const starCount = starHidden?.value || 5;
            const message = document.getElementById('revMessage')?.value;
            
            if (!name || !message) return;
            
            // Preview ก่อนส่ง (optional)
            const newReview = document.createElement('div');
            newReview.className = 'review-card fade-in appear';
            newReview.innerHTML = `
                <div class="stars">${"⭐".repeat(starCount)}</div>
                <p>"${message}"</p>
                <span class="customer">- คุณ${name}</span>
            `;
            
            reviewList.prepend(newReview);
            
            // ล้างฟอร์มหลังส่ง (ถ้าใช้ AJAX ไม่ต้องล้าง)
            // this.reset();
            
            // ถ้าไม่ใช้ AJAX ให้ส่งฟอร์มปกติ
            // alert("ส่งรีวิวเรียบร้อยแล้ว!");
        });
    }

    // 5. Reveal Animations (Fade In)
    const fadeElements = document.querySelectorAll('.fade-in');
    if (fadeElements.length > 0) {
        const observerOptions = { 
            threshold: 0.1,
            rootMargin: "0px 0px -50px 0px"
        };
        
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('appear');
                }
            });
        }, observerOptions);

        fadeElements.forEach(el => observer.observe(el));
    }

    // 6. Mobile Menu Toggle (ถ้ามี)
    const menuToggle = document.querySelector('.menu-toggle');
    const mainMenu = document.querySelector('.main-menu');
    
    if (menuToggle && mainMenu) {
        menuToggle.addEventListener('click', () => {
            mainMenu.classList.toggle('active');
        });
    }

});