const btn = document.getElementById("generateBtn");
const output = document.getElementById("output");

btn.addEventListener("click", async () => {
  const goal = document.getElementById("goalInput").value.trim();
  if (!goal) {
    alert("Please enter a goal.");
    return;
  }

  output.innerHTML = "<p>⏳ Generating plan...</p>";

  try {
    const res = await fetch("http://127.0.0.1:8000/generate-plan", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ goal }),
    });
    const data = await res.json();
    output.innerHTML = `<pre>${JSON.stringify(data.plan, null, 2)}</pre>`;
  } catch (err) {
    output.innerHTML = `<p style='color:red;'>Error: ${err.message}</p>`;
  }
});
