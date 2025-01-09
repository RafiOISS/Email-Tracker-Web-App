document.addEventListener("DOMContentLoaded", () => {
    const countryFilter = document.getElementById("filter-country");
    const searchInput = document.getElementById("search-input");
    const tableBody = document.getElementById("table-body");
  
    // Fetch initial data
    fetchData();
  
    // Event listener for country filter
    countryFilter.addEventListener("change", fetchData);
  
    // Event listener for search input
    searchInput.addEventListener("input", fetchData);
  
    function fetchData() {
      const country = countryFilter.value;
      const search = searchInput.value;
  
      fetch(`/api/data?country=${country}&search=${search}`)
        .then((response) => response.json())
        .then((data) => {
          tableBody.innerHTML = ""; // Clear the table
  
          data.forEach((item) => {
            const row = document.createElement("tr");
            row.innerHTML = `
              <td class="border px-4 py-2">${item.name}</td>
              <td class="border px-4 py-2">${item.country}</td>
              <td class="border px-4 py-2">${item.application_deadline}</td>
              <td class="border px-4 py-2"><a href="${item.website}" class="text-blue-500" target="_blank">Visit</a></td>
            `;
            tableBody.appendChild(row);
          });
        })
        .catch((error) => {
          console.error("Error fetching data:", error);
        });
    }
  });
  