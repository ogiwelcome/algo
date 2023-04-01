using System;

namespace Atcoder
{
  internal class Program
  {
    public static void Main(string[] args)
    {
      int k = int.Parse(Console.ReadLine());
      Console.WriteLine("{0:00}:{1:00}", 21 + k / 60, k % 60);
    }
  }
}
