namespace NameControl
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello, World!");
            // program küsib nime
            // kui nimi on, siis konsool vastab: Tere, sinu nimi
            // kui ei ole, siis konsool vastab ERROR, ja beep 3 korda
            // Kasuta if else 

            Console.WriteLine("Siseta nimi");
            string nimi = Console.ReadLine();

            if (nimi == "")
            {
                Console.WriteLine("ERROR");
                for (int i = 0; i < 3; i++)
                {
                    Console.Beep();
                }
            }
            else
                Console.WriteLine("Tere, " + nimi);
        }
    }
}
