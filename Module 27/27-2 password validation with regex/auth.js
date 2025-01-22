// alert();

const handleRegistration = (event) => {
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

    if (password === confirm_password) {
        document.getElementById("error").innerText = "";
        if (
            /^(?=.*[0-9])(?=.*[!@#$%^&*])[a-zA-Z0-9!@#$%^&*]{6,16}$/.test(password)
        ) {
            console.log(info);
        }
        else {
            document.getElementById("error").innerText = "pass must contain eight characters, at least one letter, one number and one special character:";
        }

    } else {
        document.getElementById("error").innerText = "Password and confirm password do not match";
        alert("Password and confirm password do not match");
    }
};




const getValue = (id) => {
    const value = document.getElementById(id).value;
    return value;
}

// const pass = "zahidul";
// console.log(/^(?=.*[0-9])(?=.*[!@#$%^&*])[a-zA-Z0-9!@#$%^&*]{6,16}$/.test(pass));
