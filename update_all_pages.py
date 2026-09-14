#!/usr/bin/env python3
"""
Script to update all HTML pages with embedded header and footer
Run this script to update all pages at once
"""

import os
import re

# Header HTML template - needs active class to be set
HEADER_TEMPLATE = '''<header>
    <nav class="navbar navbar-expand-lg">
        <div class="container">
            <a class="navbar-brand" href="index.html">
                <img src="images/logo.png" alt="ONYX Logo" onerror="this.style.display='none'; this.nextElementSibling.style.display='inline';">
                <span style="display: none;">ONYX.</span>
                ONYX
            </a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav ms-auto">
                    <li class="nav-item">
                        <a class="nav-link {home_active}" href="index.html">Home</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link {about_active}" href="about.html">About</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link {services_active}" href="services.html">Services</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link {projects_active}" href="projects.html">Projects</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link {research_active}" href="research.html">Research</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link {news_active}" href="news.html">News</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link {careers_active}" href="careers.html">Careers</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link {contact_active}" href="contact.html">Contact</a>
                    </li>
                </ul>
            </div>
        </div>
    </nav>
</header>'''

# Footer HTML
FOOTER_HTML = '''<footer>
    <div class="container">
        <div class="footer-content">
            <div class="footer-section">
                <h4>About Us</h4>
                <p>We are a leading architecture company dedicated to creating innovative and sustainable designs that inspire and transform communities.</p>
                <div class="social-icons">
                    <a href="https://www.facebook.com" target="_blank" rel="noopener noreferrer" class="social-icon facebook" aria-label="Facebook">
                        <i class="fab fa-facebook-f"></i>
                    </a>
                    <a href="https://www.twitter.com" target="_blank" rel="noopener noreferrer" class="social-icon twitter" aria-label="Twitter">
                        <i class="fab fa-twitter"></i>
                    </a>
                    <a href="https://www.instagram.com" target="_blank" rel="noopener noreferrer" class="social-icon instagram" aria-label="Instagram">
                        <i class="fab fa-instagram"></i>
                    </a>
                    <a href="https://www.linkedin.com" target="_blank" rel="noopener noreferrer" class="social-icon linkedin" aria-label="LinkedIn">
                        <i class="fab fa-linkedin-in"></i>
                    </a>
                    <a href="https://www.youtube.com" target="_blank" rel="noopener noreferrer" class="social-icon youtube" aria-label="YouTube">
                        <i class="fab fa-youtube"></i>
                    </a>
                </div>
            </div>
            
            <div class="footer-section">
                <h4>Quick Links</h4>
                <ul>
                    <li><a href="index.html">Home</a></li>
                    <li><a href="about.html">About Us</a></li>
                    <li><a href="services.html">Our Services</a></li>
                    <li><a href="projects.html">Projects</a></li>
                    <li><a href="research.html">Research</a></li>
                    <li><a href="news.html">News & Updates</a></li>
                    <li><a href="careers.html">Careers</a></li>
                    <li><a href="contact.html">Contact Us</a></li>
                </ul>
            </div>
            
            <div class="footer-section">
                <h4>Services</h4>
                <ul>
                    <li><a href="services.html">Architectural Design</a></li>
                    <li><a href="services.html">Interior Design</a></li>
                    <li><a href="services.html">Urban Planning</a></li>
                    <li><a href="services.html">Renovation</a></li>
                    <li><a href="services.html">Consultation</a></li>
                    <li><a href="services.html">Project Management</a></li>
                </ul>
            </div>
            
            <div class="footer-section">
                <h4>Contact Info</h4>
                <div class="footer-contact-info">
                    <p><i class="fas fa-map-marker-alt" style="margin-right: 8px;"></i>123 Architecture Street, Design City, DC 12345</p>
                    <p><a href="tel:+1234567890" class="phone-number"><i class="fas fa-phone" style="margin-right: 8px;"></i>+1 (234) 567-890</a></p>
                    <p><a href="mailto:info@architecturecompany.com" class="email-address"><i class="fas fa-envelope" style="margin-right: 8px;"></i>info@architecturecompany.com</a></p>
                    <p><i class="fas fa-clock" style="margin-right: 8px;"></i>Mon - Fri: 9:00 AM - 6:00 PM</p>
                </div>
            </div>
        </div>
        
        <div class="footer-bottom">
            <p>&copy; <span id="currentYear"></span> ONYX. All rights reserved.</p>
        </div>
    </div>
</footer>'''

# Script template to replace the load script
SCRIPT_REPLACEMENT = '''    <!-- Bootstrap JS -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    
    <!-- jQuery -->
    <script src="https://code.jquery.com/jquery-3.7.0.min.js"></script>
    
    <!-- Custom JS -->
    <script src="js/main.js"></script>
    
    <!-- Set current year in footer -->
    <script>
        document.getElementById('currentYear').textContent = new Date().getFullYear();
    </script>'''

# Map pages to their active nav item
PAGE_ACTIVE_MAP = {
    'index.html': 'home',
    'about.html': 'about',
    'services.html': 'services',
    'projects.html': 'projects',
    'project-details.html': 'projects',
    'research.html': 'research',
    'article-details.html': 'research',
    'news.html': 'news',
    'careers.html': 'careers',
    'contact.html': 'contact',
    'login.html': '',  # No active item for login
    'register.html': '',  # No active item for register
    '404.html': '',  # No active item for 404
}

def get_active_classes(page_name):
    """Get active classes for a given page"""
    active_page = PAGE_ACTIVE_MAP.get(page_name, '')
    classes = {
        'home_active': 'active' if active_page == 'home' else '',
        'about_active': 'active' if active_page == 'about' else '',
        'services_active': 'active' if active_page == 'services' else '',
        'projects_active': 'active' if active_page == 'projects' else '',
        'research_active': 'active' if active_page == 'research' else '',
        'news_active': 'active' if active_page == 'news' else '',
        'careers_active': 'active' if active_page == 'careers' else '',
        'contact_active': 'active' if active_page == 'contact' else '',
    }
    return classes

def update_file(filepath):
    """Update a single HTML file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    page_name = os.path.basename(filepath)
    active_classes = get_active_classes(page_name)
    header_html = HEADER_TEMPLATE.format(**active_classes)
    
    # Replace header placeholder
    content = re.sub(
        r'<!-- Header -->\s*<div id="header-placeholder"></div>',
        f'<!-- Header -->\n    {header_html}',
        content,
        flags=re.DOTALL
    )
    
    # Replace footer placeholder
    content = re.sub(
        r'<!-- Footer -->\s*<div id="footer-placeholder"></div>',
        f'<!-- Footer -->\n    {FOOTER_HTML}',
        content,
        flags=re.DOTALL
    )
    
    # Replace load script
    content = re.sub(
        r'<!-- Load Header and Footer -->\s*<script>\s*\$\s*\(\s*function\s*\(\)\s*\{\s*\$\("#header-placeholder"\)\.load\("includes/header\.html"\);\s*\$\("#footer-placeholder"\)\.load\("includes/footer\.html"\);\s*\}\s*\);\s*</script>',
        SCRIPT_REPLACEMENT,
        content,
        flags=re.DOTALL
    )
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f'Updated: {page_name}')

def main():
    """Main function to update all HTML files"""
    html_files = [
        'projects.html',
        'project-details.html',
        'research.html',
        'article-details.html',
        'news.html',
        'careers.html',
        'contact.html',
        '404.html',
        'login.html',
        'register.html',
    ]
    
    for filename in html_files:
        filepath = os.path.join('.', filename)
        if os.path.exists(filepath):
            update_file(filepath)
        else:
            print(f'File not found: {filename}')

if __name__ == '__main__':
    main()

