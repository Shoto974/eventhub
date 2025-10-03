function events_filter() {
    date_deb = document.getElementById("date-deb").value
    date_fin = document.getElementById("date-fin").value
    category = document.getElementById("cat").value
    capacity = document.getElementById("cap").value

    card_container = document.getElementById("event_list")

    params = new URLSearchParams()
    if (date_deb !== "") params.append("date_deb", date_deb)
    if (date_fin !== "") params.append("date_fin", date_fin)
    if (category !== "") params.append("category", category)
    if (capacity !== "") params.append("capacity", capacity)


    if (params.size > 0) {
        url = `/events/filtered?${params.toString()}`

        fetch(url)
            .then(response => response.text())
            .then(html => {
                card_container.innerHTML = html
            });
    }


}