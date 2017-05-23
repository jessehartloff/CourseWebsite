function AI(color, x, y) {
    Character.call(this, color, x, y);

    this.agro = false;
    this.target = null;
    this.state = "normal"; // normal, hunting, helping, seeking healer, walk to location, breed?

    this.vision = 12;
    this.yell_distance = 7;

    this.probability_idle = Math.random()/2.0;
    //this.probability_idle = 0.0;

    this.faction = color;
    //this.faction = Math.random();

    // attack or support
    // 0.0 always supports
    // 0.5 balanced
    // 1.0 only attacks
    this.aggresion = Math.random();

    // what they think of you
    this.your_reputation = 0.0;
    this.player_stories = [];

    this.known_characters = {};
    this.known_landmarks = [];
    this.home_landmark = null;
}

AI.prototype = Object.create(Character.prototype);


AI.prototype.scan_for_targets = function () {
    if ((this.state === "hunting" && this.target.dead) ||
        (this.state === "hunting" && (this.target.faction === this.faction)) ||
        (this.state === "helping" && this.target.full_health())) {
        this.agro = false;
        this.target = null;
        this.state = "normal";
    }
    var closest_distance = Math.MAX_VALUE;
    var close_ai = this.get_close_AI(this.vision);

    //console.log(close_ai);
    for (var i in close_ai) {
        var ai = close_ai[i];
        if (ai === this) {
            continue;
        }
        var this_distance = this.distance(ai);
        if (this_distance >= closest_distance) {
            continue;
        } else {
            if (ai.faction != this.faction) {
                closest_distance = this_distance;
                this.agro = true;
                this.target = ai;
                this.state = "hunting";
                //console.log("hunting");
            } else if (!ai.full_health()) {
                closest_distance = this_distance;
                this.agro = true;
                this.target = ai;
                this.state = "helping";
            }
        }
    }
    if(this.faction === "player" && this.distance(player) <= closest_distance && !player.full_health()){
        this.agro = true;
        this.target = player;
        this.state = "helping";
    } else if (this.your_reputation < -0.5 && this.distance(player) <= closest_distance){
        this.agro = true;
        this.target = player;
        this.state = "hunting";
    }
    if(this.faction === "player" && this.state === "normal"){
        this.agro = true;
        this.target = player;
        this.state = "helping";
    }
    //console.log(this.state);
};

AI.prototype.scan_for_landmarks = function () {
    shuffle_list(landmarks);
    for (var i in landmarks) {
        var landmark = landmarks[i];
        if (this.distance_from_point(landmark.x, landmark.y) <= landmark.visible_distance + this.vision) {
            var found = false;
            for (var j in this.known_landmarks) {
                if (this.known_landmarks[j] == landmark) {
                    found = true;
                }
            }
            if (!found) {
                this.known_landmarks.push(landmark);
                if (this.home_landmark == null) {
                    this.home_landmark = landmark;
                }
            }
        }
    }
};

AI.prototype.move = function (direction, alternate_direction, three, four) {

    // TODO: Check for friend;y fire here (or in move towards, but probably here)

    if (Character.prototype.move.call(this, direction) === "bump" && alternate_direction != undefined) {
        //console.log("option 2");
        if (Character.prototype.move.call(this, alternate_direction) === "bump" && three != undefined) {
            //console.log("option 3");
            if (Character.prototype.move.call(this, three) === "bump" && four != undefined) {
                //console.log("option 4");
                Character.prototype.move.call(this, four);
            }
        }
    }
};

AI.prototype.collide = function (other_character) {
    Character.prototype.collide.call(this, other_character);
    if (this.faction === other_character.faction && this.state !== "helping") {
        //console.log("bump");
        return "bump";
    }else if (this.state == "hunting") {
        this.attack(other_character);
        return "attack";
    } else if (this.state == "helping") {
        this.help(other_character);
        return "help";
    }
    // abuse
    return "bump";
};

AI.prototype.attack = function (other_character) {
    Character.prototype.attack.call(this, other_character);
    if (this.faction === other_character.faction) {
        // TODO
        console.log("friendly fire: " + this.faction);
    }
    if (other_character.dead) {
        this.agro = false;
        this.target = null;
        this.state = "normal";
    }
};

AI.prototype.get_hit = function (attacker) {
    Character.prototype.get_hit.call(this, attacker);
    if (this.dead) {
        this.faction = attacker.faction;
        this.color = attacker.color;
        this.health = 1;
        this.dead = false;
        if(this.faction === "player"){
            this.your_reputation = 1.0;
        }
        //all_AI.splice(all_AI.indexOf(this),1);
    } else {
        this.agro = true;
        this.target = attacker;
        this.state = "hunting";
        if (attacker === player) {
            this.your_reputation = -1.0;
        }
    }
};


AI.prototype.help = function (other_character) {
    Character.prototype.help.call(this, other_character);
    if (other_character.full_health()) {
        this.agro = false;
        this.target = null;
        this.state = "normal";
    }
};


AI.prototype.get_help = function (helper) {
    Character.prototype.get_help.call(this, helper);
};


AI.prototype.witness_event = function (event) {

};

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

AI.prototype.take_turn = function () {
    this.scan_for_landmarks();
    if (Math.random() < this.probability_idle) {
        return;
    }
    this.scan_for_targets();
    if (!this.agro) {
        this.random_walk();
    } else {
        // agro
        var friends = this.get_close_AI(this.yell_distance);
        for (var i in friends) {
            if (friends[i].faction === this.faction && this.target !== friends[i]) {
                friends[i].agro = true;
                friends[i].target = this.target;
                friends[i].state = this.state;
            }
        }
        this.move_towards(this.target.x, this.target.y);
    }
};


AI.prototype.move_towards = function (x, y) {

    // TODO : Path-finding without friendly fire

    var delta_x = this.x - x;
    var delta_y = this.y - y;

    var x_move = delta_x < 0 ? "right" : "left";
    var y_move = delta_y > 0 ? "up" : "down";

    var reverse_x_move = delta_x < 0 ? "left" : "right";
    var reverse_y_move = delta_y < 0 ? "up" : "down";

    if (delta_x === 0) {
        if (Math.random() < 0.5) {
            this.move(y_move, x_move, reverse_x_move, reverse_y_move);
        } else {
            this.move(y_move, reverse_x_move, x_move, reverse_y_move);
        }
    } else if (delta_y === 0) {
        if (Math.random() < 0.5) {
            this.move(x_move, y_move, reverse_y_move, reverse_x_move);
        } else {
            this.move(x_move, reverse_y_move, y_move, reverse_x_move);
        }
    }
    else if (Math.random() < 0.5) {
        this.move(x_move, y_move, reverse_y_move, reverse_x_move);

    } else {
        this.move(y_move, x_move, reverse_x_move, reverse_y_move);

    }
};


AI.prototype.random_walk = function () {
    if(this.home_landmark == null) {

        //var next_x = this.x;
        //var next_y = this.y;
        //var potential_move = "";
        //var rng = Math.random();
        var potential_moves = ["left", "right", "up", "down"];
        shuffle_list(potential_moves);
        this.move(potential_moves[0], potential_moves[1], potential_moves[2], potential_moves[3]);
        //if (rng < 0.25) {
        //    next_x++;
        //    potential_move = "right";
        //} else if (rng < 0.5) {
        //    next_x--;
        //    potential_move = "left";
        //} else if (rng < 0.75) {
        //    next_y++;
        //    potential_move = "down";
        //} else {
        //    next_y--;
        //    potential_move = "up";
        //}
        //if (get_close_AI(next_x, next_y, 0).length == 0 && !(player.x === next_x && player.y === next_y)) {
        //    this.move(potential_move);
        //} else {
        // bump
        //console.log("bump");
    //}
    }else{
        this.move_towards(this.home_landmark.x, this.home_landmark.y);
    }
};
