document.addEventListener('DOMContentLoaded', () => {
    const csrfToken = document.querySelector('meta[name="csrf-token"]').getAttribute('content');
    const taskForm = document.getElementById('taskForm');
    const taskList = document.getElementById('taskList');
    const submitButton = taskForm.querySelector('button[type="submit"]');
    let editingTaskId = null;
    const modal = document.getElementById('modal');
    const openModalBtn = document.getElementById('openModalBtn');
    const closeBtn = document.querySelector('.close-button');

    // "Create New Task" button → opens modal window
    openModalBtn.addEventListener('click', () => {
        modal.style.display = 'block';
    });

    closeBtn.addEventListener('click', () => {
        modal.style.display = 'none';
        resetForm();
    });

    window.addEventListener('click', (event) => {
        if (event.target === modal) {
            modal.style.display = 'none';
            resetForm();
        }
    });

    function resetForm() {
        taskForm.reset();
        modal.style.display = 'none';
        editingTaskId = null;
        submitButton.textContent = "Create Task";
        cancelButton.style.display = "none";
    }

    // Create Cancel Editing button
    const cancelButton = document.getElementById('cancelButton');
    cancelButton.textContent = "Cancel Editing";
    cancelButton.type = "button";
    cancelButton.style.display = "none"; // hidden by default
    submitButton.insertAdjacentElement('afterend', cancelButton);

    const fetchTasks = async () => {
        const res = await fetch('/tasks');
        const tasks = await res.json();
        taskList.innerHTML = '';

        tasks.forEach(task => {
            const li = document.createElement('li');
            li.innerHTML = `
                ${task.Titel} (${new Date(task.Beginn).toUTCString()} → ${task.Ende ? new Date(task.Ende).toUTCString() : '///'}) 
                <button class="editBtn">Edit</button> 
                <button class="deleteBtn">Delete</button>
                `;
            
            // Delete button
            li.querySelector('.deleteBtn').addEventListener('click', async () => {
                if (!confirm("Are you sure you want to delete this task?")) return;

                await fetch(`/tasks/${task.AufgabeID}`, { 
                    method: 'DELETE',
                    headers: {'X-CSRFToken': csrfToken}
                });
                fetchTasks();
            });

            // Edit button
            li.querySelector('.editBtn').addEventListener('click', () => {
                // Fill form with task data
                document.getElementById('titel').value = task.Titel;

                document.getElementById('beginn').value = task.Beginn ? new Date(task.Beginn).toISOString().slice(0, 16) : '';
                document.getElementById('ende').value = task.Ende ? new Date(task.Ende).toISOString().slice(0, 16) : '';
                
                document.getElementById('ort').value = task.Ort;
                document.getElementById('koordinaten').value = task.Koordinaten;
                document.getElementById('notiz').value = task.Notiz || '';
                document.getElementById('kategorie_id').value = task.KategorieID;
                document.getElementById('prioritaet_id').value = task.PrioritaetID;
                document.getElementById('fortschritt_id').value = task.FortschrittID;

                modal.style.display = 'block'; // ← open modal
                editingTaskId = task.AufgabeID;
                submitButton.textContent = "Update Task";
                cancelButton.style.display = "inline-block";
            });

            taskList.appendChild(li);
        });
    };

    taskForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        const taskData = {
            titel: document.getElementById('titel').value.trim(),
            beginn: document.getElementById('beginn').value,
            ende: document.getElementById('ende').value || null,
            ort: document.getElementById('ort').value.trim() || null,
            koordinaten: document.getElementById('koordinaten').value.trim() || null,
            notiz: document.getElementById('notiz').value.trim() || null,
            kategorie_id: parseInt(document.getElementById('kategorie_id').value),
            prioritaet_id: parseInt(document.getElementById('prioritaet_id').value),
            fortschritt_id: parseInt(document.getElementById('fortschritt_id').value)
        };

        if (editingTaskId) {
            // EDIT mode → PUT
            await fetch(`/tasks/${editingTaskId}`, {
                method: 'PUT',
                headers: { 
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrfToken
                },
                body: JSON.stringify(taskData)
            });
            editingTaskId = null;
            submitButton.textContent = "Create Task";
            cancelButton.style.display = "none";
        } else {
            // CREATE mode → POST
            await fetch('/tasks', {
                method: 'POST',
                headers: { 
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrfToken
                },
                body: JSON.stringify(taskData)
            });
        }

        taskForm.reset();
        modal.style.display = 'none';
        fetchTasks();
    });

    // Cancel editing button logic
    cancelButton.addEventListener('click', () => {
        taskForm.reset();
        modal.style.display = 'none';
        editingTaskId = null;
        submitButton.textContent = "Create Task";
        cancelButton.style.display = "none";
    });

    fetchTasks();
});
