function Main(event) {
    const formData = new FormData(form);
    const username_text = document.getElementById("username_text").value;

    if (username_text === '') {
        event.preventDefault();
        window.alert('Input Login Information or go to Registration');
    }
    else {    
        try {
            formData.append('username_text', 'UNEXPECTED');

            let response = fetch('/next', {
                method: 'POST',
                body: formData
              });
              
              let result = response.json();
              alert(result.message);
        }
        catch {
            document.getElementById("old_data").value = 'error';
        }
        finally {
            document.getElementById("old_data").value = 'error';
            form.requestSubmit(); //only works with submit buttons or events. Allows for contraint validation.
        }
    }
}
const form = document.getElementById('main_form');
document.getElementById("submission").addEventListener("click", Main);