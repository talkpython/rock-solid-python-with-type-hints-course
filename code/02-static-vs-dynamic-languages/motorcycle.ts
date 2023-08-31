// To run, in chapter 02.
// 1. npx tsc motorcycle.ts
// 2. node motorcycle.js

enum MotorcycleType {
    Sport = "sport",
    Naked = "naked",
    Touring = "touring",
    Adventure = "adventure",
    DualSport = "dual_sport",
    Motocross = "motocross",
    CrossCountry = "cross_country",
    Trail = "trail"
}

class Motorcycle {
    model: string;
    style: MotorcycleType;
    engineSize: number;
    offRoad: boolean;

    constructor(model: string, style: MotorcycleType, engineSize: number, offRoad: boolean) {
        this.model = model;
        this.style = style;
        this.engineSize = engineSize;
        this.offRoad = offRoad;
    }

    get canJump(): boolean {
        return this.offRoad;
    }

    static createAdventure(model: string, engineSize: number): Motorcycle {
        const bike = new Motorcycle(model, MotorcycleType.Adventure, engineSize, true);
        return bike;
    }

    toString(): string {
        return `${this.model} ${this.engineSize}, type: ${this.style}, off-road: ${this.offRoad}, can jump: ${this.canJump}`;
    }
}

function createSomeBikes(): Motorcycle[] {
    return [
        Motorcycle.createAdventure("Himalayan", 410),
        Motorcycle.createAdventure("Tenere", 700),
        Motorcycle.createAdventure("KTM", 790),
        Motorcycle.createAdventure("Norden", 901)
    ];
}

console.log("Some bikes:");
const bikes = createSomeBikes();
for (const b of bikes) {
    console.log(b.toString());
}
