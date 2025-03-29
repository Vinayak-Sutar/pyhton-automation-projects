# VLC Resume Playback for One Piece Episodes

A Python script that detects when you play an episode of One Piece in VLC and resumes playback from a predefined timestamp stored in an Excel file. If you're not watching One Piece, it playfully reminds you to get back to it! 🏴‍☠️

---

## 📜 Features
- Automatically detects VLC playback.
- Extracts episode number from the filename, even handling 1080p and 720p cases.
- Resumes playback from a predefined timestamp stored in `excel_file.xlsx`.
- Closes the running VLC instance and relaunches it with the correct timestamp.
- If you're watching something else, a fun popup appears reminding you to watch One Piece! 😆

---

## 📦 Dependencies
Ensure you have the following installed before running the script:

```sh
pip install pandas openpyxl psutil
```

Make sure you have **VLC Media Player** installed and accessible via the command line.

---

## 🚀 How It Works
1. The script continuously monitors VLC for any playing videos.
2. If an episode of "One Piece" is detected:
   - Extracts the episode number from the filename, handling 1080p and 720p cases.
   - Searches for the correct start time in `excel_file.xlsx`.
   - Closes the existing VLC instance.
   - Relaunches VLC at the appropriate timestamp.
3. If you are playing something **other than One Piece**, a fun popup will appear, nudging you to switch! 😜

---

## 🔧 Make It Yours!

### Running on Windows or Mac?
This script primarily works for **Linux** with VLC in the terminal.
- **Windows users**: Replace the VLC launch command in `launch_vlc_with_start_time()` with the full path to `vlc.exe`.
- **Mac users**: Use `open -a VLC --args --start-time <time> <file>`.

### Adjust the Check Interval
The script checks every **5 seconds** for a playing file. If you want a different interval, modify:
```python
time.sleep(5)  # Change 5 to any number of seconds you prefer
```

---

## 📜 Future Work
- Update `excel_file.xlsx` with timestamps for new episodes beyond episode 1122.
- Improve episode number extraction for more filename variations.
- Add support for other media players.

---

## 📜 Usage
Run the script using:
```sh
python script.py
```
Make sure VLC is installed and your Excel file is correctly formatted.

---

## 🏴‍☠️ Now, go enjoy your One Piece episodes without worrying about rewinding! 🎬

