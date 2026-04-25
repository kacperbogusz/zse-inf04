# Dokumentacja: WPF

## Obsługa zdarzeń - przykład

```xml
<Window x:Class="SimpleApp.MainWindow"
        xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
        xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
        Title="Licznik" Height="200" Width="300">
    <Grid>
        <Button x:Name="MojPrzycisk" Content="0" Click="Klikniecie_Przycisku" FontSize="40"/>
    </Grid>
</Window>
```

```csharp
using System.Windows;

namespace SimpleApp
{
    public partial class MainWindow : Window
    {
        int licznik = 0; // Zmienna przechowująca liczbę

        public MainWindow()
        {
            InitializeComponent();
        }

        private void Klikniecie_Przycisku(object sender, RoutedEventArgs e)
        {
            licznik++; // Zwiększ o 1
            MojPrzycisk.Content = licznik.ToString(); // Zmień tekst przycisku
        }
    }
}
```
