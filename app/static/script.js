document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("taskForm");

    form.addEventListener("submit", function (e) {
        e.preventDefault();

        const taskData = {
            titel: document.getElementById("titel").value,
            beginn: document.getElementById("beginn").value,
            ende: document.getElementById("ende").value,
            ort: document.getElementById("ort").value,
            koordinaten: document.getElementById("koordinaten").value,
            notiz: document.getElementById("notiz").value,
            kategorie_id: parseInt(document.getElementById("kategorie_id").value),
            prioritaet_id: parseInt(document.getElementById("prioritaet_id").value),
            fortschritt_id: parseInt(document.getElementById("fortschritt_id").value),
            benutzer_id: parseInt(document.getElementById("benutzer_id").value)
        };

        // Log the task object to the console
        console.log("Submitting task:", taskData);

        fetch("/tasks", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(taskData)
        })
            .then(response => response.json())
            .then(data => {
                console.log("Response from server:", data);
                loadTasks(); // Update list after creating a new task
                form.reset(); // Optionally clear the form
            })
            .catch(error => console.error("Error submitting task:", error));
    });

    function loadTasks() {
        fetch("/tasks")
            .then(response => response.json())
            .then(tasks => {
                const list = document.getElementById("taskList");
                list.innerHTML = "";
                tasks.forEach(task => {
                    const li = document.createElement("li");
                    li.textContent = `${task.Titel} (${task.Beginn} → ${task.Ende})`;
                    list.appendChild(li);
                });
            })
            .catch(error => console.error("Error loading tasks:", error));
    }

    // Load all tasks on page load
    loadTasks();
});
