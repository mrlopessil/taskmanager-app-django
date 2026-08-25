const toggleBtn = document.getElementById('toggleBtn');
const togglableContent = document.getElementById('togglableContent');

toggleBtn.addEventListener('click', () => {
    togglableContent.classList.toggle('hidden');

    toggleBtn.textContent = togglableContent.classList.contains('hidden') ? 'Show your completed tasks' : 'Hide your completed tasks';
});