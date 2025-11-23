// Zoom Controls
function zoomIn() {
    document.body.style.transform = 'scale(1.2)';
    document.body.style.transformOrigin = '0 0';
}
function resetZoom() {
    document.body.style.transform = 'scale(1)';
    document.body.style.transformOrigin = '0 0';
}
function zoomOut() {
    document.body.style.transform = 'scale(0.8)';
    document.body.style.transformOrigin = '50% 0';
}
window.addEventListener('scroll', function() {
    let backToTopButton = document.getElementById('back-to-top');
    if (window.pageYOffset > 300) { // Show button after scrolling 300px
        backToTopButton.style.display = 'block';
    } else {
        backToTopButton.style.display = 'none';
    }
});