using System;
using System.Linq;
using System.Collections.Generic;

namespace Atcoder257a
{
  internal class Program
  {
    public static void Main(string[] args)
    {
      var list = Console.ReadLine().Split(' ').Select(int.Parse).ToList();
      int n = list[0];
      int m = list[1];
      int x = list[2];
      int t = list[3];
      int d = list[4];
      if (m >= x) Console.WriteLine(t);
      else Console.WriteLine(t - d * (x - m));
    }
  }
}
