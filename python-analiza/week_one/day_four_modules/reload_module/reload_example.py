# reload_example.py - Module Reloading Example

# Reloading a Module
# Write a script that imports a custom module, modifies it,
# and reloads it using importlib.reload().

import importlib
import my_module

def test_module():
    """Function that tests the current module"""
    print("=== Testing Module ===")
    print(f"Message: {my_module.MESSAGE}")
    print(f"Greeting: {my_module.greet('David')}")
    print(f"Version: {my_module.get_version()}")
    print()

def main():
    print("Module Reloading Example with importlib.reload()")
    print("=" * 50)
    
    # First test of the module
    print("1. First test:")
    test_module()
    
    # Instructions for user to modify the module
    print("Now modify the my_module.py file:")
    print("- Change MESSAGE to 'This is the updated module'")
    print("- Change get_version() to return 'Version 2.0'")
    print("- Add something to the greet() function")
    print()
    
    input("Press Enter after saving the changes...")
    
    # Reload the module
    print("2. Reloading the module...")
    importlib.reload(my_module)
    print("Module reloaded successfully!")
    print()
    
    # Test after reload
    print("3. Test after reload:")
    test_module()
    
    print("Example completed! Notice how the changes were loaded without closing the program.")

if __name__ == "__main__":
    main()