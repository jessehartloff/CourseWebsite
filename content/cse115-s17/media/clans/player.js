function Player(x, y) {
    //this.attack_color = "#fafa00";
    //this.attack_color = "purple";
    //this.help_color = "#00fafa";
    this.attack_color = "pink";
    this.help_color = "yellow";
    Character.call(this, this.attack_color, x, y);
    this.mode = "attack";
    this.faction = "player";
}

Player.prototype = Object.create(Character.prototype);

Player.prototype.switch_mode = function(){
    if(this.mode == "attack"){
        this.mode = "help";
        this.color = this.help_color;
    }else{
        this.mode = "attack";
        this.color = this.attack_color;
    }
};

Player.prototype.collide = function (other_character) {
    Character.prototype.collide.call(this, other_character);
    if(this.mode === "attack"){
        this.attack(other_character);
    }else if(this.mode === "help"){
        this.help(other_character);
    }
};