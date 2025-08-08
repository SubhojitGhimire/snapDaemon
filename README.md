# snapDaemon - Automatically Capture Screenshots at Timed Interval

![Python](https://img.shields.io/badge/Python-3.10-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

A simple, configurable Python script to automatically take screenshots at a set frequency. Ideal for time-lapse recordings of your screen, monitoring activity, or creating visual logs.

---

## Features

- **Configurable Interval**: Set the frequency in hours (`h`), minutes (`m`), or seconds (`s`).
- **Custom Save Location**: Specify any directory to save your screenshots.
- **Robust & Reliable**: Gracefully handles interruptions (`Ctrl+C`) and file system errors.
- **Easy to Use**: Simple command-line interface with helpful instructions.
- **Organized Output**: Screenshots are saved with clear, timestamped filenames (e.g., `screenshot_2025-08-01_14-30-26.png`).

## Requirements
```
PyAutoGUI==0.9.54
```

## Usage

Run the script from your terminal. You can customize its behavior using command-line arguments.

To run the application on-demand on default settings (1 screenshot every minute, saved to `./screenshots` folder), simply execute the snapDaemon.py script from the root directory: 
```bash
python snapDaemon.py
```

To run the application automatically and silently:
- Edit the ```snapDaemon.exe.vbs``` file in notepad, choose the correct path, then copy the vbs file to startup folder as such,
  ```
      Win + R to open "Run" systems app. OR search for "Run" on Start Menu Search Functionality.
      Type "shell:startup" and hit enter to open the startup folder. Generally located at C:\Users\SubhojitGhimire\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup
  ```

### Examples

1. Take 4 screenshots every hour and save to D:/Captures:
(This will take one screenshot every 15 minutes.)
```bash
python auto_screenshotter.py -p "D:/Captures" -t h -f 4
```

2. Take one screenshot every 2 minutes:
(This is equivalent to 30 screenshots per hour.)
```bash
python auto_screenshotter.py -t h -f 30
```

3. Take two screenshots every second:
(The script enforces a 1-second minimum interval to protect your system.)
```bash
python auto_screenshotter.py -t s -f 2
```

<h1></h1>

**This README.md file has been improved for overall readability (grammar, sentence structure, and organization) using AI tools.*