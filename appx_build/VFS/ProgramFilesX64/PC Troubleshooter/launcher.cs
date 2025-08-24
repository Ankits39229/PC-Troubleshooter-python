using System;
using System.Diagnostics;
using System.IO;

class Program
{
    static void Main()
    {
        try
        {
            string appDir = Path.GetDirectoryName(System.Reflection.Assembly.GetExecutingAssembly().Location);
            string pythonScript = Path.Combine(appDir, "main.py");
            
            ProcessStartInfo startInfo = new ProcessStartInfo
            {
                FileName = "python",
                Arguments = $"\"{pythonScript}\"",
                WorkingDirectory = appDir,
                UseShellExecute = false
            };
            
            Process.Start(startInfo);
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Error launching PC Troubleshooter: {ex.Message}");
            Console.WriteLine("Press any key to exit...");
            Console.ReadKey();
        }
    }
}