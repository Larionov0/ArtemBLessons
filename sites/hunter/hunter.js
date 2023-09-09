var data = {
    turn_number: 0,
    animals: [
        {
            type: 'chicken',
            hp: 5,
            max_hp: 5,
            i: 4,
            j: 3,
            is_alive: true
        },
        {
            type: 'chicken',
            hp: 5,
            max_hp: 5,
            i: 5,
            j: 4,
            is_alive: true
        },
    ],
    player: {
        name: 'Alex',
        details: 20,
        inventory: [],
        hp: 10,
        max_hp: 10,
        i: 1,
        j: 1
    }
}


var chicken_src = 'sprites/chicken.png'
var player_src = 'sprites/player.jpg'
var grass_src = 'sprites/grass.png'

var N = 14
var M = 16


function create_matrix(n, m, symbol=null){
    var matrix = [];
    for (var i = 0; i < n; i++){
        matrix.push([]);
        for (var j = 0; j < m; j++){
            matrix[i].push(symbol);
        }
    }
    return matrix;
}


function create_map_matrix(){
    var matrix = create_matrix(N, M, grass_src);
    for (var animal of data.animals){
        matrix[animal.i][animal.j] = chicken_src;
    }
    matrix[data.player.i][data.player.j] = player_src;
    return matrix;
}


function create_map(){
    var html = '';
    var matrix = create_map_matrix();
    for (var row of matrix){
        html += '<div class="row">';
        for (var cell of row){
            html += `<div class="cell"><img src="${cell}"></div>`;
        }
        html += '</div>';
    }

    return html;
}

function draw_map(){
    var map = document.getElementById('map');
    map.innerHTML = create_map();
}

draw_map()


function move_object(object, direction){
    var i = object.i;
    var j = object.j;
    if (direction == 'up'){
        if (i > 0){
            i -= 1;
        }
    }
    else if (direction == 'down'){
        if (i < N-1){
            i += 1;
        }
    }
    else if (direction == 'left'){
        if (j > 0){
            j -= 1;
        }
    }
    else if (direction == 'right'){
        if (j < M-1){
            j += 1;
        }
    }
    object.i = i;
    object.j = j;
}


function chicken_turn(chicken){
    var directions = ['up', 'down', 'left', 'right'];
    var direction = directions[Math.floor(Math.random() * directions.length)];  // random choice
    move_object(chicken, direction);
}


document.addEventListener('keydown', function(event){
    // WASD
    if (event.keyCode == 87){
        move_object(data.player, 'up');
    }
    else if (event.keyCode == 83){
        move_object(data.player, 'down');
    }
    else if (event.keyCode == 65){
        move_object(data.player, 'left');
    }
    else if (event.keyCode == 68){
        move_object(data.player, 'right');
    }

    for (var chicken of data.animals){
        if (!chicken.is_alive){
            continue;
        }

        if (chicken.i == data.player.i && chicken.j == data.player.j){
            chicken.is_alive = false;
            data.player.details += 3;
        }

        chicken_turn(chicken);
    }

    data.animals = data.animals.filter(function(chicken){ return chicken.is_alive; });
    data.turn_number += 1;

    if (data.turn_number % 6 == 0){
        data.animals.push({
            type: 'chicken',
            hp: 2,
            max_hp: 2,
            i: Math.floor(Math.random() * N),
            j: Math.floor(Math.random() * M),
            is_alive: true
        });
    }

    draw_map();
})
