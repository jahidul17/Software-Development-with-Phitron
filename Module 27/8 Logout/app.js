// alert()

const loadServices = () => {
    fetch("https://testing-8az5.onrender.com/services/")
        .then((res) => res.json())
        // .then((data) => console.log(data))
        .then((data) => displayService(data))
        .catch((err) => console.log(err))

};

const displayService = (element) => {
    // console.log(element);
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


const loadDoctors = (search) => {
    document.getElementById("doctors").innerHTML = "";
    document.getElementById("spinner").style.display = "block";
    console.log(search);
    fetch(`https://testing-8az5.onrender.com/doctor/list/?search=${search ? search : ""}`)
        .then((res) => res.json())
        .then((data) => {
            console.log(data);
            displayDoctors(data?.results);
            if (data.results.length > 0) {
                document.getElementById("spinner").style.display = "none";
                document.getElementById("nodata").style.display = "none";
                displayDoctors(data?.results);
            }
            else {
                document.getElementById("doctors").innerHTML = "";
                document.getElementById("nodata").style.display = "block";

            }
        });

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

                <button><a target="_blank" href="docDetails.html?doctorId=${element.id}">Details</a></button>                
        `;
        parent.appendChild(div);

    });
};




const loadDesignation = () => {
    fetch("https://testing-8az5.onrender.com/doctor/designation/")
        .then((res) => res.json()
            .then((data) => {
                data.forEach((item) => {
                    const parent = document.getElementById("drop-deg");
                    const li = document.createElement("li");
                    li.classList.add('dropdown-item');
                    li.innerText = item?.name;
                    parent.appendChild(li);

                })
            })
        )
}

loadDesignation()

const loadSpecialization = () => {
    fetch("https://testing-8az5.onrender.com/doctor/specialization/")
        .then((res) => res.json()
            .then((data) => {
                data.forEach((item) => {
                    const parent = document.getElementById("drop-spe");
                    const li = document.createElement("li");
                    li.classList.add('dropdown-item');
                    li.innerHTML = `
                    <li onclick="loadDoctors('${item.name}')">${item.name}</li>
                    `;

                    // li.innerText = item?.name;
                    parent.appendChild(li);

                })
            })
        )
}

loadSpecialization()


const handleSearch = () => {
    const value = document.getElementById("search").value;
    // console.log(value);
    loadDoctors(value)
};


loadDoctors();
handleSearch();


const loadReview = () => {
    fetch("https://testing-8az5.onrender.com/doctor/review/")
        .then((res) => res.json())
        // .then((data) => console.log(data));
        .then((data) => displayReview(data));

}

const displayReview = (reviews) => {
    reviews.forEach((review) => {
        const parent = document.getElementById("review-container");
        const div = document.createElement("div");
        div.classList.add("review-card");
        div.innerHTML = `
        <img src="./image/doctor-face.jpg" alt="">
                    <h4>${review.reviewer}</h4>
                    <p>${review.body.slice(0, 100)}</p>

                    <h6>${review.rating}</h6>
        `;
        parent.appendChild(div)
    }
    )


}

loadReview();

