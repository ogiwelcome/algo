using System;

namespace Abc262b
{
    internal class Program
    {
        static void Main()
        {
            int y = int.Parse(Console.ReadLine());
            Console.WriteLine(y + (4 - (y - 2) % 4) % 4);
        }
    }
}
