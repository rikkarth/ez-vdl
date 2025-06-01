# Creating a Binary with PyInstaller

Follow these steps to create a standalone executable from your Python script using PyInstaller.

## 1. Install PyInstaller

```bash
pip install pyinstaller
```

## 2. Navigate to Your Script's Directory

```bash
cd /path/to/your/script
```

## 3. Create the Executable

Replace `your_script.py` with your script's filename:

```bash
pyinstaller --onefile your_script.py
```

- The `--onefile` flag bundles everything into a single executable.

## 4. Find Your Binary

After building, the executable will be in the `dist` folder:

```
dist/your_script
```

## 5. Run the Binary

```bash
./dist/your_script
```

---

For more options, see the [PyInstaller documentation](https://pyinstaller.org/).
