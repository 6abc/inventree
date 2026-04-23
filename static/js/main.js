// Load saved theme or default to light
const savedTheme = localStorage.getItem('theme') || 'light';
const htmlEl = document.documentElement;
const themeToggleBtn = document.getElementById('themeToggle');
const themeIcon = document.getElementById('themeIcon');

function setTheme(theme) {
    htmlEl.setAttribute('data-bs-theme', theme);
    localStorage.setItem('theme', theme);
    themeIcon.className = theme === 'dark' ? 'bi bi-sun-fill' : 'bi bi-moon-stars';
}

// Initialize theme
setTheme(savedTheme);

// Toggle on click
themeToggleBtn.addEventListener('click', () => {
    const newTheme = htmlEl.getAttribute('data-bs-theme') === 'light' ? 'dark' : 'light';
    setTheme(newTheme);
});