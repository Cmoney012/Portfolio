const navLinks = document.querySelectorAll('.navbar a');
const sections = document.querySelectorAll('.content section');

navLinks.forEach(link => {
  link.addEventListener('click', e => {
    e.preventDefault();
    const targetId = link.getAttribute('href');
    const targetSection = document.querySelector(targetId);
    console.log(targetId);

    navLinks.forEach(link => link.classList.remove('active'));
    link.classList.add('active');

    sections.forEach(section => section.classList.remove('active'));
    targetSection.classList.add('active');
  });
});

const perGameCheckbox = document.getElementById("per_game_checkbox");
const submitButton = document.getElementById("submit_button");

submitButton.addEventListener("click", async () => {
  const perGame = perGameCheckbox.checked;
  const response = await fetch('/api/stats/?per_game=${perGame}');
  const stats = await response.json();

  // update the stats with the per-game calculation
  const updatedStats = updateStatsPerGame(stats, perGame);

  // update the HTML table with the new stats
  const rows = document.getElementsByTagName("tr");
  for (let i = 1; i < rows.length; i++) {
    const cells = rows[i].getElementsByTagName("td");
    cells[1].innerHTML = updatedStats[cells[0].innerHTML].games;
    cells[2].innerHTML = updatedStats[cells[0].innerHTML].shots;
    cells[3].innerHTML = updatedStats[cells[0].innerHTML].goals;
    cells[4].innerHTML = updatedStats[cells[0].innerHTML].saves;
    cells[5].innerHTML = updatedStats[cells[0].innerHTML].assists;
    cells[6].innerHTML = updatedStats[cells[0].innerHTML].score;
    cells[7].innerHTML = updatedStats[cells[0].innerHTML].shootingPercentage;
  }
});

// Get the filter inputs
const filterInputs = document.querySelectorAll('.filter-input');

// Add an event listener to each filter input
filterInputs.forEach(input => {
  input.addEventListener('change', event => {
    // Get the current value of the input
    const value = event.target.value;
    
    // Store the value in localStorage
    localStorage.setItem(input.id, value);
  });
});

// When the page loads, read the values from localStorage and apply them as the default filters
filterInputs.forEach(input => {
  const value = localStorage.getItem(input.id);
  if (value) {
    input.value = value;
  }
});