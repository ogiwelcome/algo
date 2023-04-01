using System;
using System.Linq;
using System.Collections.Generic;

class Program
{
  static void Main()
  {
    var list = Console.ReadLine().Split(' ').Select(int.Parse).ToList();
    int a = list[0];
    int b = list[1];
    int d = list[2];
    var sin = Math.Sin(d * (Math.PI / 180));
    var cos = Math.Cos(d * (Math.PI / 180));
    Console.WriteLine($"{(a * cos) - (b * sin)} {a * sin + b * cos}");
  }
}
