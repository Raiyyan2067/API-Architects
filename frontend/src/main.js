
const test = document.getElementById("test-button");
test.addEventListener("click", () => {
    fun();
    console.log("test-click")
});
const fun = () => {
    return fetch('http://127.0.0.1:8000/', {
        method: 'GET',
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

fun()
.then((response) => {
    console.log(response);
});
document.getElementById("main-text").innerText = new Date();