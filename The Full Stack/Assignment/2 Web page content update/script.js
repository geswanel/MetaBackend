const h1 = document.createElement('h1')
h1.innerText = "This text will be changed after input"

const input = document.createElement('input')
input.setAttribute('type', 'text')

document.body.appendChild(h1)
document.body.appendChild(input)

input.addEventListener('change', function() {
    console.log(input.value);
    h1.innerText = input.value;
});