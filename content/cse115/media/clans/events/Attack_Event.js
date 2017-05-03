function Attack_Event(attacker, attacked) {
    Event.call(this, attacked.x, attacked.y, "attack", 10, attacker, attacked);
}

Attack_Event.prototype = Object.create(Event.prototype);
