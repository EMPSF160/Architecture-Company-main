# ONYX Website

A modern, responsive website for an architecture company built with HTML, CSS, JavaScript, jQuery, AJAX, and Bootstrap.

## Features

- **Responsive Design**: Fully responsive for all screen sizes (mobile, tablet, desktop)
- **Modern UI**: Clean and professional design with smooth animations
- **Active Navigation**: Highlights the current page in the navigation menu
- **AJAX Forms**: Contact and career application forms with AJAX submission
- **Image Optimization**: Uses high-quality images from free stock photo sources
- **SEO Friendly**: Proper meta tags and semantic HTML
- **Accessible**: Follows web accessibility best practices

## Pages

1. **index.html** - Main homepage
2. **about.html** - About us page
3. **services.html** - Services offered
4. **projects.html** - Portfolio of projects
5. **project-details.html** - Detailed project information
6. **research.html** - Research and innovation
7. **article-details.html** - Research article details
8. **news.html** - News and updates
9. **careers.html** - Job opportunities and application
10. **contact.html** - Contact information and form
11. **404.html** - Custom 404 error page

## Technologies Used

- **HTML5**: Semantic markup
- **CSS3**: Custom styles with CSS variables
- **JavaScript**: Interactive functionality
- **jQuery**: DOM manipulation and AJAX
- **Bootstrap 5.3**: Responsive grid and components
- **Font Awesome**: Icon library
- **AJAX**: Form submissions without page reload

## Typography

- **H1**: Font weight 700 (bold)
- **H2**: Font weight 600 (semi-bold), center-aligned
- **H3**: Font weight 300 (light), center-aligned
- Standard font sizes used throughout

## Image Sources

All images are sourced from free stock photo websites:
- Pexels - Architecture/Building photos
- Pixabay - Architecture building images
- PicJumbo - 600+ free architecture images
- Coverr - Free architecture stock images
- FreeImages - Architecture category

## Setup Instructions

1. Download or clone the repository
2. Ensure all files are in the correct directory structure
3. Add a favicon.ico file to the `images/` folder (or create one using https://favicon.io/)
4. Add a logo.png file to the `images/` folder (optional - the site will work without it)
5. Open `index.html` in a web browser

## File Structure

```
ONYX/
├── index.html
├── about.html
├── services.html
├── projects.html
├── project-details.html
├── research.html
├── article-details.html
├── news.html
├── careers.html
├── contact.html
├── 404.html
├── css/
│   └── style.css
├── js/
│   └── main.js
├── includes/
│   ├── header.html
│   └── footer.html
├── images/
│   ├── favicon.ico (add your favicon here)
│   ├── logo.png (optional)
│   └── README.md
└── README.md
```

## Key Features

### Navigation
- Sticky header with smooth scrolling
- Active page highlighting
- Responsive mobile menu
- Equal spacing between menu items
- Clickable logo that redirects to homepage

### Forms
- Contact form with validation
- Career application form
- AJAX submission (currently set to display success/error messages)
- Real-time validation feedback

### Footer
- About section
- Quick links
- Services links
- Contact information with clickable phone and email
- Social media icons with hover effects
- Copyright information with dynamic year

### Responsive Design
- Mobile-first approach
- Breakpoints for mobile (576px), tablet (768px), and desktop (992px)
- Optimized layouts for all screen sizes
- Touch-friendly buttons and navigation

## Customization

### Colors
Main colors are defined in CSS variables in `css/style.css`:
- `--primary-color`: #1a1a1a (dark)
- `--secondary-color`: #c9a961 (gold)
- `--text-dark`: #333333
- `--text-light`: #666666

### Contact Information
Update contact information in `includes/footer.html`:
- Address
- Phone number (remember to use '+' before international numbers)
- Email address
- Business hours

### Social Media Links
Update social media links in `includes/footer.html` with your actual social media URLs.

## Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Mobile browsers (iOS Safari, Chrome Mobile)

## Notes

- Forms are set up for AJAX submission but may need backend integration for actual functionality
- All external links open in new tabs
- Phone numbers and email addresses are clickable
- Images are loaded from external URLs (Pexels, etc.) - can be downloaded and hosted locally if preferred

## License

This project is created for ONYX. All rights reserved.

