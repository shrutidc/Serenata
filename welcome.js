document.addEventListener('DOMContentLoaded', function() {
    // Display the user's name
    const userName = localStorage.getItem('userName') || 'Friend';
    document.getElementById('userName').textContent = userName;

    const imageUpload = document.getElementById('imageUpload');
    const imagePreview = document.getElementById('imagePreview');
    const continueBtn = document.getElementById('continueBtn');

    imageUpload.addEventListener('change', function(event) {
        const file = event.target.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = function(e) {
                const img = document.createElement('img');
                img.src = e.target.result;
                img.classList.add('preview-image');
                imagePreview.innerHTML = '';
                imagePreview.appendChild(img);
                continueBtn.disabled = false;
            }
            reader.readAsDataURL(file);
        }
    });

    continueBtn.addEventListener('click', function() {
        // Here you can add logic to save the image or move to the next page
        console.log('Continue to the next page');
        // For example:
        // window.location.href = 'mood-selection.html';
    });
});