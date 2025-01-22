

const loadAllApointment = () => {
    const patient_id = localStorage.getItem("patient_id");

    fetch(`https://testing-8az5.onrender.com/appointment/?patient_id=${patient_id}`)
        .then((res) => res.json())
        .then((data) => {
            // console.log(data);
            data.forEach((itme) => {
                const parent = document.getElementById("table-body");
                const tr = document.createElement("tr");
                tr.innerHTML = `
                    <th scope="row">1</th>
                    <td>${itme.email}</td>
                    <td>Online</td>
                    <td>pending</td>
                    <td>X</td>
                    <td>1200</td>
                    ${itme.appointment_status == "Pending"
                        ? `<td class="text-danger">X</td>`
                        : `<td>X</td>`
                    }
                `;
                parent.appendChild(tr);
            });

        });
};


loadAllApointment()
