var all_AI = [];
var game_board = {};
var player;
var landmarks = [];

function initialize() {
    game_board = {
        c: document.getElementById("myCanvas"),
        squareSize: 10,
        personSize: 3,
        boardSize: 600,
        //background_color: "#fafafa",
        background_color: "#777777",
        //gameState: "normal",
        //indexE: -1,

        initialize: function () {
            this.squaresAcross = this.boardSize / this.squareSize;
            this.ctx = this.c.getContext("2d");
        }
    };

    game_board.initialize();
    create_landmarks(10);
    make_AI();
    //player = new Player(randomCoordinate(), randomCoordinate());
    player = new Player(100000, 100000);

    render();
}


function make_AI() {
    add_faction(50, "#ff5555", 2);
    add_faction(50, "#5555ff", 4);
    add_faction(50, "orange", 1);
    add_faction(50, "green", 3);
    add_faction(75, "#000000", 0);
    add_faction(75, "#999999", 0);


    //add_faction(200, "#ff5555", 2);
    //add_faction(70, "#5555ff", 8);
    //add_faction(200, "orange", 3);
    //add_faction(70, "green", 8);
    //add_faction(70, "#000000", 8);
    //add_faction(70, "#999999", 8);
}

function add_faction(quantity, color, quad) {
    for (var w = 0; w < quantity; w++) {
        if (quad == 1) {
            all_AI.push(new AI(color, (randomCoordinate() + game_board.squaresAcross) / 2, (randomCoordinate() + game_board.squaresAcross) / 2 + 3));
        } else if (quad == 2) {
            all_AI.push(new AI(color, (randomCoordinate() + game_board.squaresAcross) / 2, randomCoordinate() / 2 - 3));
        } else if (quad == 3) {
            all_AI.push(new AI(color, randomCoordinate() / 2, randomCoordinate() / 2 - 3));
        } else if (quad == 4) {
            all_AI.push(new AI(color, randomCoordinate() / 2, (randomCoordinate() + game_board.squaresAcross) / 2 + 3));
        } else if (quad == 0) {
            all_AI.push(new AI(color, (randomCoordinate() + (game_board.squaresAcross / 2)) / 2, (randomCoordinate() + (game_board.squaresAcross / 2)) / 2));
        }else{
            all_AI.push(new AI(color, randomCoordinate(), randomCoordinate()));
        }
    }
}

function create_landmarks(quantity){
    for (var w = 0; w < quantity; w++) {
        landmarks.push(new Landmark(randomCoordinate(),randomCoordinate(),30));
    }
}


function randomCoordinate() {
    return Math.floor((Math.random() * game_board.squaresAcross));
}


function player_move(e) {
    var key;

    if (window.event) { // IE
        key = e.keyCode;
    } else if (e.which) { // Netscape/Firefox/Opera
        key = e.which;
    }

    var input = String.fromCharCode(key);

    // uldr
    // wasd
    // ijkl

    if (input == "w" || input == "i") {
        player.move("up");
    } else if (input == "a" || input == "j") {
        player.move("left");
    } else if (input == "s" || input == "k") {
        player.move("down");
    } else if (input == "d" || input == "l") {
        player.move("right");
    } else if (input == "q" || input == "u") {
        player.switch_mode();
        render();
        return;
    } else if (input == "e" || input == "o") {
        // stand still
    } else {
        return;
    }

    //var contact_ai = get_close_AI(next_x, next_y, 0);
    //if(contact_ai.length > 0){
    //    // event!
    //    var witnesses = get_close_AI(next_x, next_y);
    //    if(input == "w" || input == "a" || input == "s" || input == "d"){
    //        // attack
    //        contact_ai[0].your_reputation = (contact_ai[0].your_reputation-1.0)/2.0;
    //        contact_ai[0].player_stories.push("He attacked me");
    //        all_AI.splice(all_AI.indexOf(contact_ai[0]),1);
    //        for(var i in witnesses){
    //            var witness = witnesses[i];
    //            witness.your_reputation = (contact_ai[0].your_reputation-1.0)/2.0;
    //            witness.player_stories.push("He attacked my faction");
    //            witness.agro = true;
    //        }
    //    }else if(input == "i" || input == "j" || input == "k" || input == "l"){
    //        // support
    //        contact_ai[0].player_stories.push("He helped me"); // only add if the ai is in a battle
    //    }
    //}else{
    //    player.x = next_x;
    //    player.y = next_y;
    //}

    play_AI();
    render();
}

function shuffle_list(list) {
    for (var i = list.length; i > 0; i--) {
        var random_index = Math.floor(Math.random() * i);
        var temp = list[i - 1];
        list[i - 1] = list[random_index];
        list[random_index] = temp;
    }
}


function play_AI() {
    shuffle_list(all_AI);
    for (var i in all_AI) {
        var this_ai = all_AI[i];
        if (this_ai.dead) {
            //all_AI.splice(all_AI.indexOf(this_ai),1); // dangerous. Probably skips turns
            continue;
        }
        //console.log(this_ai);
        this_ai.take_turn();
    }

    // this is gross!
    while (true) {
        var found_a_body = false;
        for (var i in all_AI) {
            var this_ai = all_AI[i];
            if (this_ai.dead) {
                all_AI.splice(all_AI.indexOf(this_ai), 1);
                found_a_body = true;
                break;
            }
        }
        if (found_a_body) {
            continue;
        }
        break;
    }


    //if(Math.random() < 0.4) {
    //    add_faction(1, "orange", 1);
    //}
    //
    //if(Math.random() < 0.9) {
    //    add_faction(1, "green", 3);
    //}

}


function render() {

    if (player.dead) {
        game_board.background_color = "black";
    }
    // erase everything a start with black board each step
    for (var i = 0; i < game_board.squaresAcross; i++) {
        for (var j = 0; j < game_board.squaresAcross; j++) {
            if ((i % 2 == 0 && j % 2 == 1) || (i % 2 == 1 && j % 2 == 0)) {
                game_board.ctx.fillStyle = game_board.background_color;
                game_board.ctx.fillRect(i * game_board.squareSize, j * game_board.squareSize, game_board.squareSize, game_board.squareSize);
            } else {
                game_board.ctx.fillStyle = game_board.background_color;
                game_board.ctx.fillRect(i * game_board.squareSize, j * game_board.squareSize, game_board.squareSize, game_board.squareSize);
            }
        }
    }


    for (var i in all_AI) {
        var ai = all_AI[i];
        var size = game_board.personSize + ai.health;
        game_board.ctx.fillStyle = ai.color;
        game_board.ctx.fillRect(ai.x * game_board.squareSize, ai.y * game_board.squareSize, size, size);
    }


    var player_size = game_board.personSize + player.health;
    game_board.ctx.fillStyle = player.color;
    game_board.ctx.fillRect(player.x * game_board.squareSize, player.y * game_board.squareSize, player_size, player_size);

}