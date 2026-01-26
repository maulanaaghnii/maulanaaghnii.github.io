# ASP.NET Core REST API

Building RESTful services is a primary use case for ASP.NET Core.

## Controllers and Actions
Controllers handle incoming HTTP requests and return responses.
```csharp
[ApiController]
[Route("api/[controller]")]
public class ProductsController : ControllerBase
{
    [HttpGet]
    public IActionResult GetAll() => Ok(_productService.List());

    [HttpGet("{id}")]
    public IActionResult GetById(int id) => Ok(_productService.Find(id));

    [HttpPost]
    public IActionResult Create(Product product)
    {
        _productService.Add(product);
        return CreatedAtAction(nameof(GetById"), new { id = product.Id }, product);
    }
}
```

## Practical Tips
- **Use DTOs**: Never expose your database entities directly.
- **HTTP Methods**: Use `GET` for retrieval, `POST` for creation, `PUT` for updates, and `DELETE` for removal.
- **Status Codes**: Return appropriate codes like `200 OK`, `201 Created`, `400 Bad Request`, `404 Not Found`.

---
*Check **[JWT Authentication](dotnet-jwt-authentication.md)** for securing your API.*
