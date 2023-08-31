using System;
using System.Collections.Generic;

// Run with new project via:
// 1. dotnet new console -o mc -f net7.0
// 2. cd mc && dotnet run

namespace MotorcycleApp
{
    public enum MotorcycleType
    {
        Sport,
        Naked,
        Touring,
        Adventure,
        DualSport,
        Motocross,
        CrossCountry,
        Trail
    }

    public class Motorcycle
    {
        public string Model { get; private set; }
        public MotorcycleType Style { get; private set; }
        public int EngineSize { get; private set; }
        public bool OffRoad { get; private set; }

        public Motorcycle(string model, MotorcycleType style, int engineSize, bool offRoad)
        {
            Model = model;
            Style = style;
            EngineSize = engineSize;
            OffRoad = offRoad;
        }

        public bool CanJump => OffRoad;

        public static Motorcycle CreateAdventure(string model, int engineSize)
        {
            var bike = new Motorcycle(model, MotorcycleType.Adventure, engineSize, offRoad: true);
            return bike;
        }

        public override string ToString()
        {
            return $"{Model} {EngineSize}, type: {Style}, off-road: {OffRoad}, can jump: {CanJump}";
        }
    }

    class Program
    {
        static List<Motorcycle> CreateSomeBikes()
        {
            var motorcycles = new List<Motorcycle>
            {
                Motorcycle.CreateAdventure("Himalayan", 410),
                Motorcycle.CreateAdventure("Tenere", 700),
                Motorcycle.CreateAdventure("KTM", 790),
                Motorcycle.CreateAdventure("Norden", 901)
            };

            return motorcycles;
        }

        static void Main(string[] args)
        {
            Console.WriteLine("Some bikes:");
            var bikes = CreateSomeBikes();
            foreach (var b in bikes)
            {
                Console.WriteLine(b);
            }
        }
    }
}
