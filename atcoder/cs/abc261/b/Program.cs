using System;

namespace Abc261b
{
    internal class Program
    {
        static void Main()
        {
            int n = int.Parse(Console.ReadLine());
            string[] a = new string[n];
            for (int i = 0; i < n; i++) a[i] = Console.ReadLine();
            bool flag = true;
            for (int i = 0; i < n; i++)
            {
                for (int j = 0; j < n; j++)
                {
                    if ((a[i][j] == 'W' && a[j][i] != 'L') || (a[i][j] == 'L' && a[j][i] != 'W') || (a[i][j] == 'D' && a[j][i] != 'D'))
                    {
                        flag = false;
                    }
                }
            }
            if (flag)
            {
                Console.WriteLine("correct");
            }
            else
            {
                Console.WriteLine("incorrect");
            }
        }
    }
}
