async function runTask() {
  const res = await fetch("https://TU-RENDER-PRINCIPAL.onrender.com/run");
  const data = await res.json();
  document.getElementById("output").textContent = JSON.stringify(data, null, 2);
}
