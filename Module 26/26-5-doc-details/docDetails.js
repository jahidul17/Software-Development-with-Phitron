const getparems = () => {
    const param = new URLSearchParams(window.location.search).get("doctorId");
    console.log(param);
    fetch(`https://testing-8az5.onrender.com/doctor/list/${param}`)
        .then((res) => res.json())
        .then((data) => displayDetails(data));

    fetch('')
};

const displayDetails = (element) => {
    console.log(element);
    const parent = document.getElementById("doc-details");
    const div = document.createElement("div");
    div.classList.add("doc-details-container");
    div.innerHTML = `
    <div class="doctor-img">
            <img src=${element.image} alt="">

        </div>
        <div class="doc-info">
            <h1>${element.full_name}</h1>
             ${element.specialization.map((item) => {
        return `<button class="doc-details-btn">${item}</button>`;
    })
        }
           
            <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Cumque, eaque.</p>
            <h4>Fees: ${element.fee} BDT</h4>
            <button>Take Application</button>
        </div>
    `;
    parent.appendChild(div);
}
getparems();

