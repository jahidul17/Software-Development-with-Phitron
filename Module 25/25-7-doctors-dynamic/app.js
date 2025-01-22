// alert()

const loadServices = () => {
    fetch("https://testing-8az5.onrender.com/services/")
        .then((res) => res.json())
        // .then((data) => console.log(data))
        .then((data) => displayService(data))
        .catch((err) => console.log(err))

};

const displayService = (element) => {
    console.log(element);
    element.forEach(element => {
        const parent = document.getElementById("service-container");
        const li = document.createElement("li");
        li.innerHTML = `
        <div class="card shadow h-100">
                            <div class="ratio ratio-16x9">
                                <img src=${element.image}>
                            </div>
                            <div class="card-body  p-3 p-xl-5">
                                <h3 class="card-title h5">${element.name}</h3>
                                <p class="card-text">${element.description.slice(0, 150)}</p>
                                <a href="#" class="btn btn-primary">Details</a>
                            </div>
                        </div>

        `;
        parent.appendChild(li)
    });
};
loadServices();


const loadDoctors = () => {
    fetch("https://testing-8az5.onrender.com/doctor/list/")
        .then((res) => res.json())
        .then((data) => displayDoctors(data.results));

}

const displayDoctors = (doctors) => {
    doctors?.forEach((element) => {
        console.log(element)
        const parent = document.getElementById("doctors");
        const div = document.createElement("div");
        div.classList.add("doc-card");
        div.innerHTML = `
            <img class="doc-img" src="./image/doctor-face.jpg" alt="">
                <h4>${element.full_name}</h4>
                <h6>${element.designation}</h6>
                <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Sequi, corrupti.</p>
                <p>
                    ${element?.specialization.map((item) => {
            return `<button>${item}</button>`
        })}
                </p>

                <button>Details</button>                
        `;
        parent.appendChild(div);

    });
};

loadDoctors()


