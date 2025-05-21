document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("taskForm");

  form.addEventListener("submit", function (event) {
    event.preventDefault();

    const data = {
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

    fetch("http://127.0.0.1:5000/tasks", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(data)
    })
      .then(response => {
        if (!response.ok) {
          throw new Error("Failed to create task.");
        }
        return response.json();
      })
      .then(result => {
        console.log("Task created:", result);
        alert("Task created successfully!");
        form.reset(); // Clear form fields
      })
      .catch(error => {
        console.error("Error:", error);
        alert("Task creation failed!");
      });
  });
});
