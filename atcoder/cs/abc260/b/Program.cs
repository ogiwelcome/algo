using System;
using System.Collections.Generic;
using System.Linq;
namespace abc260_b
{
  class Program
  {
    static void Main(string[] args)
    {
      var arr = Array.ConvertAll(Console.ReadLine().Split(), int.Parse);
      var n = arr[0];
      var x = arr[1];
      var y = arr[2];
      var z = arr[3];
      var a = Array.ConvertAll(Console.ReadLine().Split(), int.Parse);
      var b = Array.ConvertAll(Console.ReadLine().Split(), int.Parse);

      var r = new List<int>();
      var q = Enumerable.Range(0, n).Select(i => (id: i + 1, a: a[i], b: b[i])).ToArray();

      q = q.OrderBy(p => -p.a).ThenBy(p => p.id).ToArray();
      r.AddRange(q[..x].Select(p => p.id));
      q = q[x..];

      q = q.OrderBy(p => -p.b).ThenBy(p => p.id).ToArray();
      r.AddRange(q[..y].Select(p => p.id));
      q = q[y..];

      q = q.OrderBy(p => -p.a - p.b).ThenBy(p => p.id).ToArray();
      r.AddRange(q[..z].Select(p => p.id));
      q = q[z..];

      r.Sort();
      Console.WriteLine(string.Join("\n", r));
    }
  }
}
