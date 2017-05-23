function Character(color, x, y) {
    this.x = Math.round(x);
    this.y = Math.round(y);

    this.color = color;
    this.max_health = 3;
    this.health = this.max_health;
    this.dead = false;

}

Character.prototype.collide = function (other_character) {
    // abstract
};

Character.prototype.attack = function (other_character) {
    other_character.get_hit(this);
    new Attack_Event(this, other_character).broadcast();
};


Character.prototype.get_hit = function(attacker){
    this.health--;
    if(this.health <= 0){
        this.dead = true;
    }
};

Character.prototype.help = function (other_character) {
    other_character.get_help(this);
    new Help_Event(this, other_character).broadcast();
};


Character.prototype.get_help = function(helper){
    if(this.health < this.max_health){
        this.health++;
    }
};

Character.prototype.full_health = function(){
    return this.health == this.max_health;
};

Character.prototype.distance = function (other_character) {
    return this.distance_from_point(other_character.x, other_character.y);
};

Character.prototype.distance_from_point = function (x,y) {
    return Math.abs(this.x - x) + Math.abs(this.y - y);
};

//Character.prototype.distance_2 = function (other_character) {
//    var base_distance = Math.abs(this.x - other_character.x) + Math.abs(this.y - other_character.y);
//    var center_x = (this.x + other_character.x)/2;
//    var center_y = (this.y + other_character.y)/2;
//    var obstacles = get_close_AI(other_character.x, other_character.y, 1);
//    //var obstacles = get_close_AI(center_x, center_y, base_distance/2);
//    return base_distance +obstacles/2;
//    //return base_distance;
//};

Character.prototype.check_collision = function (other_character) {
    return this.distance(other_character) == 0;
};

Character.prototype.move = function (direction) {
    var old_x = this.x;
    var old_y = this.y;

    switch (direction) {
        case "up":
            this.y--;
            break;
        case "down":
            this.y++;
            break;
        case "left":
            this.x--;
            break;
        case "right":
            this.x++;
            break;
    }

    var result = "moved";

    if (this != player && this.check_collision(player)) {
        result = this.collide(player);
        this.x = old_x;
        this.y = old_y;
    }


    for (var i in all_AI) {
        var ai = all_AI[i];
        if (this === ai) {
            continue;
        }
        if (this.check_collision(ai)) {
            result = this.collide(ai);
            this.x = old_x;
            this.y = old_y;
        }
    }

    return result;
};

Character.prototype.get_close_AI = function (threshold) {
    if (threshold === undefined) {
        threshold = 15;
    }
    var close_AI = [];
    for (var i in all_AI) {
        var ai = all_AI[i];
        if(ai.dead){
            continue;
        }
        if (this.distance(ai) <= threshold) {
            close_AI.push(ai);
        }
    }
    return close_AI;
};


function get_close_AI(x, y, threshold) {
    return new Character(null, x, y).get_close_AI(threshold);
}
