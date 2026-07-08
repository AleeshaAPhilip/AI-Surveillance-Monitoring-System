async function updateDashboard() {

    const response = await fetch("/status");

    const data = await response.json();

    document.getElementById("current-person").innerHTML =
        data.current_person;

    document.getElementById("known-count").innerHTML =
        data.known_count;

    document.getElementById("unknown-count").innerHTML =
        data.unknown_count;

}

setInterval(updateDashboard, 1000);

updateDashboard();