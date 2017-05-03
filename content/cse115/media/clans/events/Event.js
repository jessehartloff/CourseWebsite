function Event(x, y, type, range, subject, object) {
    this.x = x;
    this.y = y;
    this.type = type;
    this.range = range;
    this.subject = subject;
    this.object = object;
}

Event.prototype.broadcast = function () {
    var close_ai = get_close_AI(this.x, this.y, this.range);
    for (i in close_ai) {
        var ai = close_ai[i];
        ai.witness_event(this)
    }
};