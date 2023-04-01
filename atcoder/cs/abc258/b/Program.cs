using System;
using System.Collections.Generic;
using System.Linq;

namespace Atcoder
{
  internal class Program
  {
    public static void Main(string[] args)
    {
      var n = int.Parse(Console.ReadLine());
      var a = Array.ConvertAll(new bool[n], _ => Console.ReadLine());
      var di = new[] { 1, -1, 0, 0, 1, -1, -1, 1 };
      var dj = new[] { 0, 0, 1, -1, 1, 1, -1, -1 };
      var rn = Enumerable.Range(0, n).ToArray();
      var l = new List<string>();
      for (int i = 0; i < n; i++)
      {
        for (int j = 0; j < n; j++)
        {
          for (int d = 0; d < 8; d++)
          {
            l.Add(string.Join("", rn.Select(k => a[(i + k * di[d] + n) % n][(j + k * dj[d] + n) % n])));
          }
        }
      }
      Console.WriteLine(l.Max());
    }
  }
}
