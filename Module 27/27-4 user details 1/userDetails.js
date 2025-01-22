const loadUserDetails = () => {
    const user_id = localStorage.getItem("user_id");
    fetch(`https://testing-8az5.onrender.com/users/${user_id}`)
        .then((res) => res.json())
        // .then((data) => console.log(data));
        .then((data) => {
            const parent = document.getElementById("user-details-container");
            const div = document.createElement("user-all");
            div.classList.add("user-all");
            div.innerHTML = `
            <div class="user-img">
                <img src="./image/doctor-face.jpg" alt="">
            </div>
            <div class="user-info">
                <h1>${data.username}</h1>
                <h3>Username</h3>
                <h3>gia@gmail.com</h3>
            </div>
            `;
            parent.appendChild(div)
        })
};
loadUserDetails();


