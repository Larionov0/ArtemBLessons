var names = ["John", "Ann", "Bob", "Alice", "Mary", "Jane", "Peter", "George", "Kate"]


// for (var a = 0; a < 10; a += 2){
//     console.log(a)
// }

// for (var i = 0; i < names.length; i += 1) {
//     var name = names[i].toLowerCase()
//     if (name.includes("a")) {
//         console.log(name)
//     }
// }

for (var name of names) {
    if (name.toLowerCase().includes("a")) {
        console.log(name)
    }
}
