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
        .then((response) => {
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
    }
}

// Get session token
const getToken = () => {
    return localStorage.getItem("token");
}

// Set session token
const setToken = (token) => {
    localStorage.setItem("token", token);
}

const test = document.getElementById("test-button");
test.addEventListener("click", () => {
    apiCall("", "GET")
    .then((response) => {
        console.log("test-click")
        console.log(response)
    });
});
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
        if (data.error) {
            alert(data.error);
        } else {
            return Promise.resolve(data);
        }
    });
};

pageUpdate();