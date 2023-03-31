const form = document.getElementById('main_form');

function Main(event) {
    const username_text = document.getElementById("username_text").value;
    const password_text = document.getElementById("username_text").value;

    if (username_text === '' || password_text === '') {
        event.preventDefault();
        window.alert('Please Submit Login Info');
    }
    else {    
        form.requestSubmit(); //only works with submit buttons or events. Allows for contraint validation.
        localStorage.setItem("Login", username_text)
    }
}

document.getElementById("submission").addEventListener("click", Main);