

## 1: Module Quiz

## 2 Creating a grid layout
```css
.container {
    /* Add rules here */
    display: grid;
    max-width: 900px;
    min-height: 50vh;
    grid-template-columns: 100%;
    grid-template-rows: auto auto 1fr auto auto;
    grid-template-areas: "header" "left" "main" "right" "footer";
}
/* Add media rules for container class below */
@media (min-width: 440px) {
    .container {
    /* Add rules here */
      grid-template-columns: 150px 1fr 150px;
      grid-template-rows: auto 1fr auto;
      grid-template-areas: "header header header"
                           "left main right"
                           "footer footer footer";
    }
}
/* grid area property to define area of grids */
```


## 2: Exercise: Declaring variables


## 2: Exercsise: Web page content update
- `prompt` function to take user input and then manipulate DOM to display it.
dynamically create a page
```js
var h1 = document.createElement('h1')
h1.innerText = "Type into the input to make this text change"

var input = document.createElement('input')
input.setAttribute('type', 'text')

document.body.innerText = '';
document.body.appendChild(h1);
document.body.appendChild(input);

input.addEventListener('change', function() {
    h1.innerText = input.value
})
```


## 2: Module Quiz


## 3: Connect Django to MySQL

## 3: Submitting a form with JS

## 3: Module Quiz