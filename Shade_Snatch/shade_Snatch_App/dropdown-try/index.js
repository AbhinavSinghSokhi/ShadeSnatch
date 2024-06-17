// document.addEventListener('DOMContentLoaded', () => {
//     const dropZone = document.getElementById('drop-zone');
//     const fileInput = document.getElementById('file-input');
//     const fileBrowser = document.getElementById('file-browser');

//     // Highlight the drop zone when a file is dragged over it
//     dropZone.addEventListener('dragover', (event) => {
//         event.preventDefault();
//         dropZone.classList.add('dragover');
//     });

//     // Remove the highlight when the dragged file leaves the drop zone
//     dropZone.addEventListener('dragleave', () => {
//         dropZone.classList.remove('dragover');
//     });

//     // Handle the dropped file
//     dropZone.addEventListener('drop', (event) => {
//         event.preventDefault();
//         dropZone.classList.remove('dragover');
//         const files = event.dataTransfer.files;
//         if (files.length) {
//             fileInput.files = files;
//         }
//     });

//     // Open file browser when clicking the browse link
//     fileBrowser.addEventListener('click', () => {
//         fileInput.click();
//     });

//     // Optional: Show a preview of the selected image (if desired)
//     fileInput.addEventListener('change', () => {
//         const files = fileInput.files;
//         if (files.length) {
//             const file = files[0];
//             const reader = new FileReader();
//             reader.onload = (event) => {
//                 const img = document.createElement('img');
//                 img.src = event.target.result;
//                 img.style.maxWidth = '100%';
//                 img.style.marginTop = '20px';
//                 dropZone.innerHTML = '';
//                 dropZone.appendChild(img);
//             };
//             reader.readAsDataURL(file);
//         }
//     });
// });


// document.addEventListener('DOMContentLoaded', () => {
//     const dropZone = document.getElementById('drop-zone');
//     const fileInput = document.getElementById('file-input');
//     const fileBrowser = document.getElementById('file-browser');

//     // Highlight the drop zone when a file is dragged over it
//     dropZone.addEventListener('dragover', (event) => {
//         event.preventDefault();
//         dropZone.classList.add('dragover');
//     });

//     // Remove the highlight when the dragged file leaves the drop zone
//     dropZone.addEventListener('dragleave', () => {
//         dropZone.classList.remove('dragover');
//     });

//     // Handle the dropped file
//     dropZone.addEventListener('drop', (event) => {
//         event.preventDefault();
//         dropZone.classList.remove('dragover');
//         const files = event.dataTransfer.files;
//         if (files.length) {
//             fileInput.files = files;
//             previewFile(files[0]);
//         }
//     });

//     // Open file browser when clicking the browse link
//     fileBrowser.addEventListener('click', () => {
//         fileInput.click();
//     });

//     // Handle the file selection via file browser
//     fileInput.addEventListener('change', () => {
//         const files = fileInput.files;
//         if (files.length) {
//             previewFile(files[0]);
//         }
//     });

//     // Function to preview the file
//     function previewFile(file) {
//         const reader = new FileReader();
//         reader.onload = (event) => {
//             const img = document.createElement('img');
//             img.src = event.target.result;
//             img.style.maxWidth = '100%';
//             img.style.marginTop = '20px';
//             dropZone.innerHTML = '';
//             dropZone.appendChild(img);
//         };
//         reader.readAsDataURL(file);
//     }
// });
document.addEventListener('DOMContentLoaded', () => {
    const dropZone = document.getElementById('drop-zone');
    const fileInput = document.getElementById('file-input');
    const fileBrowser = document.getElementById('file-browser');

    // Highlight the drop zone when a file is dragged over it
    dropZone.addEventListener('dragover', (event) => {
        event.preventDefault();
        dropZone.classList.add('dragover');
    });

    // Remove the highlight when the dragged file leaves the drop zone
    dropZone.addEventListener('dragleave', () => {
        dropZone.classList.remove('dragover');
    });

    // Handle the dropped file
    dropZone.addEventListener('drop', (event) => {
        event.preventDefault();
        dropZone.classList.remove('dragover');
        const files = event.dataTransfer.files;
        if (files.length) {
            fileInput.files = files;
            previewFile(files[0]);
        }
    });

    // Open file browser when clicking the browse link
    fileBrowser.addEventListener('click', () => {
        fileInput.click();
    });

    // Handle the file selection via file browser
    fileInput.addEventListener('change', () => {
        const files = fileInput.files;
        if (files.length) {
            previewFile(files[0]);
        }
    });

    // Function to preview the file
    function previewFile(file) {
        const reader = new FileReader();
        reader.onload = (event) => {
            const img = document.createElement('img');
            img.src = event.target.result;
            img.style.maxWidth = '100%';
            img.style.marginTop = '20px';
            dropZone.innerHTML = '';
            dropZone.appendChild(img);
        };
        reader.readAsDataURL(file);
    }
});
