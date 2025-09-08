# .NET Entity Framework Minimal

## That I Use

 - .NET 8
 - Entity Framework
 - SQL Server

## Package Prerequisite

```
dotnet tool install --global dotnet-ef
dotnet add package Microsoft.EntityFrameworkCore
dotnet add package Microsoft.EntityFrameworkCore.SqlServer
dotnet add package Microsoft.EntityFrameworkCore.Design
```

## Set Migration
```
dotnet ef migrations add InitialCreate
dotnet ef database update
```


## Create New Project

Create .NET console project called "LearnEF"

## Source Code

### Models/Product.cs
```
namespace LearnEF.Models
{
    internal class Product
    {
        public int Id { get; set; }
        public string Name { get; set; }
        public decimal Price { get; set; }
    }
}
```

### Models/AppDbContext.cs
```
using Microsoft.EntityFrameworkCore;


namespace LearnEF.Models
{
    internal class AppDbContext : DbContext
    {
        public DbSet<Product> Products { get; set; } // Represents the "Products" table
        protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
        {
            optionsBuilder.UseSqlServer("Server=localhost;Database=learnef;User Id=sa;Password=1234;Trusted_Connection=True;TrustServerCertificate=True;");
        }
    }
}

```

### Repositories/IProductRepository.cs
```
using LearnEF.Models;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace LearnEF.Repositories
{
    internal interface IProductRepository
    {
        void Add(Product product);
        IEnumerable<Product> GetAll();
```

### Repositories/ProductRepository.cs
```
using LearnEF.Models;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace LearnEF.Repositories
{
    internal class ProductRepository : IProductRepository
    {
        private readonly AppDbContext _context;
        public ProductRepository(AppDbContext context)
        {
            _context = context;
        }
        public void Add(Product product) {
            _context.Products.Add(product);
            _context.SaveChanges();
        }
        public void Update(Product product) {
            _context.Products.Update(product);
            _context.SaveChanges();
        }
        public Product? GetByName(string name)
        {
            return _context.Products.FirstOrDefault(p => p.Name == name);
        }
        public void Delete(Product product) {
            _context.Products.Remove(product);
            _context.SaveChanges();
        }
        public IEnumerable<Product> GetAll() {
            return _context.Products;
        }
    }
}

```

### Program.cs
```
using LearnEF.Models;
using LearnEF.Repositories;

class Program
{
    static void Main(string[] args)
    {
        using (var context = new AppDbContext())
        {
            var repo = new ProductRepository(context);

            while (true)
            {
                Console.WriteLine("\n=== PRODUCT MENU ===");
                Console.WriteLine("1. Read Data");
                Console.WriteLine("2. Insert Data");
                Console.WriteLine("3. Update Data");
                Console.WriteLine("4. Delete Data");
                Console.WriteLine("5. Get By Name");
                Console.WriteLine("0. Exit");
                Console.Write("Choose menu: ");

                var choice = Console.ReadLine();

                switch (choice)
                {
                    case "1": // READ
                        var products = repo.GetAll();
                        Console.WriteLine("\n--- Product Data ---");
                        foreach (var p in products)
                            Console.WriteLine($"{p.Id} | {p.Name} - {p.Price}");
                        break;

                    case "2": // INSERT
                        Console.Write("Product Name: ");
                        string name = Console.ReadLine() ?? "";

                        Console.Write("Product Price: ");
                        decimal price;
                        decimal.TryParse(Console.ReadLine(), out price);

                        var newProduct = new Product { Name = name, Price = price };
                        repo.Add(newProduct);
                        Console.WriteLine("Product added successfully.");
                        break;

                    case "3": // UPDATE
                        Console.Write("Enter product name to update: ");
                        string updateName = Console.ReadLine() ?? "";
                        var existing = repo.GetByName(updateName);

                        if (existing != null)
                        {
                            Console.Write("New Price: ");
                            decimal newPrice;
                            decimal.TryParse(Console.ReadLine(), out newPrice);

                            existing.Price = newPrice;
                            repo.Update(existing);
                            Console.WriteLine("Product updated successfully.");
                        }
                        else
                        {
                            Console.WriteLine("Product not found.");
                        }
                        break;

                    case "4": // DELETE
                        Console.Write("Enter product name to delete: ");
                        string deleteName = Console.ReadLine() ?? "";
                        var toDelete = repo.GetByName(deleteName);

                        if (toDelete != null)
                        {
                            repo.Delete(toDelete);
                            Console.WriteLine("Product deleted successfully.");
                        }
                        else
                        {
                            Console.WriteLine("Product not found.");
                        }
                        break;

                    case "5": // GET BY NAME
                        Console.Write("Enter product name: ");
                        string searchName = Console.ReadLine() ?? "";
                        var product = repo.GetByName(searchName);

                        if (product != null)
                        {
                            Console.WriteLine($"Found: {product.Id} | {product.Name} - {product.Price}");
                        }
                        else
                        {
                            Console.WriteLine("Product not found.");
                        }
                        break;

                    case "0": // EXIT
                        Console.WriteLine("Exiting program...");
                        return;

                    default:
                        Console.WriteLine("Invalid choice.");
                        break;
                }
            }
        }
    }
}

```