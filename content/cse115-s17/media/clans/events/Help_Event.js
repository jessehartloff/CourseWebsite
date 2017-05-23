function Help_Event(color, x, y) {
    Event.call(this, color, x, y);

}

Help_Event.prototype = Object.create(Event.prototype);
