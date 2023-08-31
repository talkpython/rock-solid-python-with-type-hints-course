// To run, in chapter 02.
// 1. npx tsc motorcycle.ts
// 2. node motorcycle.js
var MotorcycleType;
(function (MotorcycleType) {
    MotorcycleType["Sport"] = "sport";
    MotorcycleType["Naked"] = "naked";
    MotorcycleType["Touring"] = "touring";
    MotorcycleType["Adventure"] = "adventure";
    MotorcycleType["DualSport"] = "dual_sport";
    MotorcycleType["Motocross"] = "motocross";
    MotorcycleType["CrossCountry"] = "cross_country";
    MotorcycleType["Trail"] = "trail";
})(MotorcycleType || (MotorcycleType = {}));
var Motorcycle = /** @class */ (function () {
    function Motorcycle(model, style, engineSize, offRoad) {
        this.model = model;
        this.style = style;
        this.engineSize = engineSize;
        this.offRoad = offRoad;
    }
    Object.defineProperty(Motorcycle.prototype, "canJump", {
        get: function () {
            return this.offRoad;
        },
        enumerable: false,
        configurable: true
    });
    Motorcycle.createAdventure = function (model, engineSize) {
        var bike = new Motorcycle(model, MotorcycleType.Adventure, engineSize, true);
        return bike;
    };
    Motorcycle.prototype.toString = function () {
        return "".concat(this.model, " ").concat(this.engineSize, ", type: ").concat(this.style, ", off-road: ").concat(this.offRoad, ", can jump: ").concat(this.canJump);
    };
    return Motorcycle;
}());
function createSomeBikes() {
    return [
        Motorcycle.createAdventure("Himalayan", 410),
        Motorcycle.createAdventure("Tenere", 700),
        Motorcycle.createAdventure("KTM", 790),
        Motorcycle.createAdventure("Norden", 901)
    ];
}
console.log("Some bikes:");
var bikes = createSomeBikes();
for (var _i = 0, bikes_1 = bikes; _i < bikes_1.length; _i++) {
    var b = bikes_1[_i];
    console.log(b.toString());
}
