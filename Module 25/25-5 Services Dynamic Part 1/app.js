// alert()

const loadServices = () => {
    fetch("https://testing-8az5.onrender.com/services/")
        .then((res) => res.json())
        // .then((data) => console.log(data))
        .then((data) => displayService(data))
        .catch((err) => console.log(err))

};

const displayService = (element) => {
    element.forEach(element => {
        console.log(element);
    });
};
loadServices();