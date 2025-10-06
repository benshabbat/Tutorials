# Module Reloading Example

## Files in this folder:
- `my_module.py` - The main module
- `my_module_modified.py` - Updated version example
- `reload_example.py` - The main script

## How to run:

1. Run the `reload_example.py` file:
   ```
   python reload_example.py
   ```

2. When the program asks, copy the content from `my_module_modified.py` to `my_module.py`

3. Save the file and press Enter

4. See how the module reloads with the new changes!

## What happens:
- `importlib.reload()` reloads the module from disk
- Changes are loaded without closing the program
- This is useful for development and debugging