var names = ["John", "Ann", "Bob", "Alice", "Mary", "Jane", "Peter", "George", "Kate"]


// var i = 0

// while (i < names.length) {
//     console.log(names[i])
//     i += 1
// }

var i = 0
var count = 0

while (i < names.length) {
    var name = names[i].toLowerCase()

    if (name.includes("a")) {
        console.log(name)
        count += 1
    }

    i += 1
}

// console.log("There are " + count + " names with the letter 'a'")
console.log(`There are ${count} names with the letter 'a'`)
