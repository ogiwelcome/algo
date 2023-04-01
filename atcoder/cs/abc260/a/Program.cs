using System;
using System.Linq;

class Program
{
  static void Main()
  {
    var s = Console.ReadLine();
    var dis = s?.ToCharArray().GroupBy(x => x).FirstOrDefault(x => x.Count() == 1);
    Console.WriteLine(dis == default ? "-1" : dis.First().ToString());
  }
}
