# Brightness Adjuster

## Description
`brightness_adjust.py` is a Python script that automatically adjusts your laptop screen brightness based on room lighting. It captures an image using your laptop's front camera, analyzes its brightness, and tweaks your screen accordingly.

📌 **Important:** You need to set the correct **display output device name** for brightness adjustment to work on your system.

---

## Installation & Dependencies
Before running the script, install the required libraries:

```sh
pip install pillow pygame
```

---
### ⚠️ This script only works on Linux!  
- **Windows users:** Try adjusting brightness using PowerShell:  
  ```powershell
  (Get-WmiObject -Namespace root/WMI -Class WmiMonitorBrightnessMethods).WmiSetBrightness(1, 70)
  ```
- **Mac users:** You can change brightness with:  
  ```sh
  brightness 0.7
  ```
  (Requires `brew install brightness`)

## How It Works  

1️⃣ **Takes a Picture 📸**  
   - The script starts by turning on your laptop’s front camera.  
   - It captures an image and saves it as `"filename.jpg"`.  

2️⃣ **Analyzes the Brightness 🌞🌙**  
   - Converts the image to greyscale.  
   - Reads the pixel brightness values using a histogram.  
   - Calculates an overall brightness level (0 - dark, 1 - bright).  

3️⃣ **Adjusts Your Screen 🖥️**  
   - Takes the calculated brightness and adds a small *offset* (`0.2`).  
   - Uses `xrandr` to set the new screen brightness.  
   - Uses a variable (`output_device`) for the display name instead of hardcoding `"eDP"`.  
   - Deletes the captured image to keep things clean.  

4️⃣ **Repeats Every 30 Seconds 🔁**  
   - The script runs in an infinite loop, adjusting brightness every 30 seconds.  
   - You can change this interval as needed.  

---

## How Brightness is Calculated  
- The image is converted to greyscale (black & white).  
- Each pixel has a brightness value (0-255).  
- The script counts how many pixels have each brightness level.  
- A weighted formula calculates the average brightness.  
- The brightness is normalized between `0` (darkest) and `1` (brightest).  
- A small offset is added (`+0.2`) to make sure the screen isn’t too dim.  
- You can tweak this offset based on your preference.  

---

## Make It Yours! 🛠️  

### Set the correct display output device:  
Run the command:  
```sh
xrandr --current
```
Find your display name (e.g., `eDP-1`, `HDMI-1`, etc.).  
Update the `output_device` variable in the script.  

### Customize the behavior:  
- Want it to run every **10 minutes**? Change `time.sleep(30)` to `time.sleep(600)`.  
- Too **bright** or **too dim**? Adjust `brightness_offset = 0.2` to a value you like.  

Now just run the script and let your laptop take care of the brightness for you! 🚀  

---

## Usage  
Run the script with:  
```sh
python brightness_adjust.py
```
Let your laptop automatically adjust brightness for you! 🚀  



