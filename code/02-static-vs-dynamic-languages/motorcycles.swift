// Run with swiftc motorcycles.swift -o mc
import Foundation

enum MotorcycleType: String {
    case sport
    case naked
    case touring
    case adventure
    case dualSport = "dual_sport"
    case motocross
    case crossCountry
    case trail
}

class Motorcycle {
    let model: String
    let style: MotorcycleType
    let engineSize: Int
    let offRoad: Bool?

    init(model: String, style: MotorcycleType, engineSize: Int, offRoad: Bool) {
        self.model = model
        self.style = style
        self.engineSize = engineSize
        self.offRoad = offRoad
    }

    var canJump: Bool {
        return offRoad!
    }

    static func createAdventure(model: String, engineSize: Int) -> Motorcycle {
        let bike = Motorcycle(model: model, style: .adventure, engineSize: engineSize, offRoad: true)
        return bike
    }

    var description: String {
        return "\(model) \(engineSize), type: \(style.rawValue), off-road: \(offRoad!), can jump: \(canJump)"
    }
}

func createSomeBikes() -> [Motorcycle] {
    let motorcycles = [
        Motorcycle.createAdventure(model: "Himalayan", engineSize: 410),
        Motorcycle.createAdventure(model: "Tenere", engineSize: 700),
        Motorcycle.createAdventure(model: "KTM", engineSize: 790),
        Motorcycle.createAdventure(model: "Norden", engineSize: 901)
    ]

    return motorcycles
}

print("Some bikes:")
let bikes = createSomeBikes()
for b in bikes {
    print(b.description)
}
