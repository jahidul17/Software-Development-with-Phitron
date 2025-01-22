// alert();

const handlelRegistration = (event) => {
    event.preventDefault();
    // console.log("box");
    const first_name = getValue("username");
    const last_name = getValue("last_name");
    const email = getValue("email");
    const password = getValue("password");
    const confirm_password = getValue("confirm_password");
    console.log({
        username,
        first_name,
        last_name,
        email,
        password,
        confirm_password,
    });
};

const getValue = (id) => {
    const value = document.getElementById(id).value;
    return value;
}
