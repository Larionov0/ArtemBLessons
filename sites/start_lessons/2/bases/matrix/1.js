function matrixer(matrix){
    for (var i = 0; i < matrix.length; i+=1){
        for (var j = 0; j < matrix[i].length; j+=1){
            if (i % 2 == 1 && j % 2 == 1){
                matrix[i][j] = 0
            }
        }
    }
}

function print_matrix(matrix){
    let text = ''
    for (var row of matrix){
        text += row.join(' ') + '\n'
    }

    console.log(text)
}

var matrix = [
    [7, 1, 6, 2, 8, 5, 3, 4, 9],
    [5, 3, 4, 9, 6, 7, 2, 1, 8],
    [2, 8, 9, 3, 4, 1, 6, 5, 7],
    [8, 4, 5, 1, 7, 3, 9, 6, 2],
    [6, 9, 7, 5, 2, 8, 4, 3, 1],
]
console.log(matrixer(matrix))

print_matrix(matrix)
