// alert();




const handleRegistration = (event) => {
    event.preventDefault();
    const username = getValue("username");
    const first_name = getValue("first_name");
    const last_name = getValue("last_name");
    const email = getValue("email");
    const password = getValue("password");
    const confirm_password = getValue("confirm_password");
    const info = {
        username,
        first_name,
        last_name,
        email,
        password,
        confirm_password,
    };


    console.log({
        username,
        first_name,
        last_name,
        email,
        password,
        confirm_password
    });

};

const getValue = (id) => {
    const value = document.getElementById(id).value;
    return value;
};





