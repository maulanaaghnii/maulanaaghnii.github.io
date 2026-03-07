# C# Events and Delegates

Events enable a class or object to notify other classes when something of interest occurs.

## Delegates
A delegate is a type that represents references to methods with a particular parameter list and return type.
```csharp
public delegate void Notify(string message);
```

## Events
Events are built on top of delegates to provide a "publish-subscribe" model.
```csharp
public class ProcessBusinessLogic
{
    public event EventHandler ProcessCompleted; // Built-in delegate

    public void StartProcess()
    {
        Console.WriteLine("Process Started!");
        OnProcessCompleted(EventArgs.Empty);
    }

    protected virtual void OnProcessCompleted(EventArgs e)
    {
        ProcessCompleted?.Invoke(this, e);
    }
}
```

## Subscribing
```csharp
var bl = new ProcessBusinessLogic();
bl.ProcessCompleted += (sender, e) => Console.WriteLine("Finished!");
bl.StartProcess();
```

---
*Back to **[C# Basics](csharp-basics.md)**.*
