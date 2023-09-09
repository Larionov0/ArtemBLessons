var p = document.getElementById('my_p')


for (var i = 0; i < 10; i++){
    p.innerHTML += '<br>' + i
}


var ul = document.getElementById('ul')
var names = ["John", "Ann", "Bob", "Alice", "Mary", "Jane", "Peter", "George", "Kate"]

for (var name of names) {
    ul.innerHTML += '<li>' + name + '</li>'
}


var button = document.getElementById('add_button')
var input = document.getElementById('input_name')

button.onclick = function(){
    var new_name = input.value
    if (new_name.length < 2) {
        alert('Name is too short')
        return
    }
    if (new_name.length > 30) {
        alert('Name is too long')
        return
    }

    ul.innerHTML += '<li>' + new_name[0].toUpperCase() + new_name.slice(1).toLowerCase() + '</li>'
    input.value = ''
}
