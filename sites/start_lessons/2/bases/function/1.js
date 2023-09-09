function adder(a, b) {
    return a + b;
}

// console.log(adder(2, 3));


function counter(string, needded_letter){
    var count = 0
    for (var lettter of string){
        if (lettter == needded_letter){
            count += 1
        }
    }

    return count
}


// console.log(counter("Hello aaegaegll agllllarga lagrl larg", "l"))


function create_matrix(height, width, symbol='-'){
    var matrix = []
    for (var i = 0; i < height; i++){
        var row = []
        for (var j = 0; j < width; j++){
            row.push(symbol)
        }
        matrix.push(row)
    }

    return matrix
}

function print_matrix(matrix){
    let text = ''
    for (var row of matrix){
        text += row.join(' ') + '\n'
    }

    console.log(text)
}

print_matrix(create_matrix(5, 6))

