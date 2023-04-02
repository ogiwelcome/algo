using System;

namespace Abc261a
{
    internal class Program
    {
        public static void Main(string[] args)
        {
            var arr = Array.ConvertAll(Console.ReadLine().Split(), int.Parse);
            int l1 = arr[0];
            int r1 = arr[1];
            int l2 = arr[2];
            int r2 = arr[3];
            Console.WriteLine(Math.Max(0, Math.Min(r1, r2) - Math.Max(l1, l2)));
        }
    }
}
