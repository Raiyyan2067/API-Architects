// Page Elements
const pageTitle = document.getElementById("page-title");

const registerButton = document.getElementById("register-button");
const loginButton = document.getElementById("login-button");
const logoutButton = document.getElementById("logout-button");
const registerForm = document.getElementById("register-form");
const registerUser = document.getElementById("register-form-username");
const registerPass = document.getElementById("register-form-password");
const registerConf = document.getElementById("register-form-confirm");
const registerSubmit = document.getElementById("register-form-submit");
const loginForm = document.getElementById("login-form");
const loginUser = document.getElementById("login-form-username");
const loginPass = document.getElementById("login-form-password");
const loginSubmit = document.getElementById("login-form-submit");

const genButton = document.getElementById("generate-button");
const genForm = document.getElementById("generate-form");
const genXML = document.getElementById("generate-form-XML");
const genCarrier = document.getElementById("generate-form-carrier");
const genDate = document.getElementById("generate-form-date");
const genNotes = document.getElementById("generate-form-notes");

pageTitle.addEventListener("click", () => {
    pageUpdate();
})

registerButton.addEventListener("click", () => {
    pageUpdate("register-form");
})

loginButton.addEventListener("click", () => {
    pageUpdate("login-form");
})

logoutButton.addEventListener("click", () => {
    apiCall("ubl/auth/logout", "POST")
    .then(() => {
        setToken("");
        pageUpdate();
    })
})

registerForm.addEventListener("submit", (event) => {
    event.preventDefault();

    if (registerPass.value === registerConf.value && registerUser.value && registerPass.value) {
        const body = {
            "username": registerUser.value,
            "password": registerPass.value,
        }
        apiCall("ubl/auth/register", "POST", body)
        .then(() => {
            apiCall("ubl/auth/login", "POST", body)
            .then((response) => {
                setToken(response.access_token);
                pageUpdate();
            })
        })
    } else {
        alert("Must enter username and password, and passwords must match");
    }

    registerUser.value = "";
    registerPass.value = "";
    registerConf.value = "";
})

loginForm.addEventListener("submit", (event) => {
    event.preventDefault();

    const body = {
        "username": loginUser.value,
        "password": loginPass.value
    }
    apiCall("ubl/auth/login", "POST", body)
    .then((response) => {
        setToken(response.access_token);
        pageUpdate();
    })

    loginUser.value = "";
    loginPass.value = "";
})

genButton.addEventListener("click", () => {
    pageUpdate("generate-form")
});

genForm.addEventListener("submit", async (event) => {
    event.preventDefault();

    if (genXML.value) {
        // const text = await genXML.files[0].text()
        // const body = {
        //     "order_xml": text,
        //     "carrier": genCarrier.value,
        //     "dispatch_date": genDate.value,
        //     "notes": genNotes.value
        // }
        // console.log(JSON.stringify(body));
        // authApiCall("ubl/v3/despatch-advice/generate", "POST", body)
        // .then((response) => {
        //     console.log(response);
        // });

        // pageUpdate();
        // genXML.value = "";
        // genCarrier.value = "";
        // genDate.value = "";
        // genNotes.value = "";
        const formData = new FormData();
        formData.append("order_xml", genXML.files[0]);
        formData.append("carrier", genCarrier.value);
        formData.append("dispatch_date", genDate.value);
        formData.append("notes", genNotes.value);

        formcall("ubl/v3/despatch-advice/generate", "POST", formData)
        .then((response) => {
            console.log(response);
            pageUpdate();
        })
    } else {
        alert("Must upload XML file!");
    }
});

// Display login/logout buttons
const pageUpdate = (pageId) => {
    if (getToken()) {
        registerButton.style.display = 'none';
        loginButton.style.display = 'none';
        logoutButton.style.display = 'block';
    } else {
        registerButton.style.display = 'block';
        loginButton.style.display = 'block';
        logoutButton.style.display = 'none';
    }

    for (const page of document.querySelectorAll('.page')) {
        page.style.display = 'none';
    }
        
    if (pageId) {
        document.getElementById(pageId).style.display = 'block';
    } else {
        document.getElementById("main-page").style.display = 'block';
    }

    console.log(`pageUpdate(${pageId})`)
}

// Get session token
const getToken = () => {
    return localStorage.getItem("token");
}

// Set session token
const setToken = (token) => {
    localStorage.setItem("token", token);
}

const apiCall = (path, method, body) => {
    return fetch('http://127.0.0.1:8000/' + path, {
        method: method,
        headers: {
            'Content-type': 'application/json',
        },
        body: JSON.stringify(body)
    })
    .then((response) => response.json())
    .then((data) => {
        if (data && data.error) {
            alert(data.error);
        } else {
            return Promise.resolve(data);
        }
    });
};

const formcall = (path, method, form) => {
    return fetch("http://127.0.0.1:8000/" + path, {
        method: method,
        headers: {
            "Authorization": `Bearer ${getToken()}`
        },
        body: form
    })
    //.then((response) => response.json())
    .then((data) => {
        //if (data && data.error) {
        //    alert(data.error);
        //} else {
            return Promise.resolve(data);
        //}
    });
};

pageUpdate();