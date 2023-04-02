using System;
using System.Collections.Generic;
using System.Linq;

namespace Abc262b
{
    internal class Program
    {
        static void Main()
        {
            int[] arr = Console.ReadLine().Split().Select(int.Parse).ToArray();
            int n = arr[0];
            int m = arr[1];
            bool[,] e = new bool[n + 1, n + 1];
            for (int i = 0; i < m; i++)
            {
                arr = Console.ReadLine().Split().Select(int.Parse).ToArray();
                e[arr[0] - 1, arr[1] - 1] = true;
                e[arr[1] - 1, arr[0] - 1] = true;
            }
            int count = 0;
            for (int i = 0; i < n; i++)
            {
                for (int j = i + 1; j < n; j++)
                {
                    for (int k = j + 1; k < n; k++)
                    {
                        if (e[i, j] && e[j, k] && e[k, i]) count++;
                    }
                }
            }
            Console.WriteLine(count);
        }
    }
}
