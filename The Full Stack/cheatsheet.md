# Description
Cheatsheet from this course

## bash and mysql
```bash
CREATE USER 'admindjango'@'localhost' IDENTIFIED BY 'employee@123!';
GRANT ALL ON *.* TO 'admindjango'@'localhost';
FLUSH PRIVILEGES;

```

## JS
```js
//document and elements
const el = document.createElement('p');
el.innerText = text;
el.setAttribute("class", "par");
document.body.appendChild(el);

//JSON
const bookings = JSON.parse('{{ bookings|safe }}');//json with DTL
const pretty_json = JSON.stringify(bookings, null, 2);

JSON.strigify(formdata)

// fetch
const form = document.getElementById('form');
form.addEventListener("submit", submitHandler); // event handler

function submitHandler(e) {
    e.preventDefault();

    fetch(form.action, {method:'POST', body: new FormData(form)}) //fetch api
    .then(response=>response.json())
    .then(data=>{
            if (data.message === 'success') {
                alert('Success!');
                form.reset()
        }
    });
}

//Date
const date = new Date();
document.getElementById('reservation_date').value = `${date.getFullYear()}-${(date.getMonth() + 1).toString().padStart(2, "0")}-${date.getDate().toString().padStart(2, "0")}`;


// flow
for (let item of data) {

}

for (let i = 0; i < 10; i++) {

}

```