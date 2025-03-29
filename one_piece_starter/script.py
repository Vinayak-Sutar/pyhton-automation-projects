import os
import pandas as pd
import re
import time
import subprocess
import psutil
from tkinter import Tk, Label

# Path to the Excel file
EXCEL_FILE_PATH = 'excel_file.xlsx'

# Load the Excel file into a DataFrame
def read_excel_sheet(file_path):
    return pd.read_excel(file_path, header=None, names=['PrimaryTime', 'FallbackTime'])

# Convert minute:seconds format to total seconds
def time_to_seconds(time_str):
    try:
        time_str = str(time_str)
        time_str = re.sub(r':00$', '', time_str)  # Remove trailing ":00"
        minutes, seconds = map(int, time_str.split(':'))
        return minutes * 60 + seconds
    except (ValueError, AttributeError):
        return 0

# Get start time for an episode in seconds
def get_start_time(df, episode_number):
    if episode_number <= len(df):
        row = df.iloc[episode_number - 1]
        primary_time = row['PrimaryTime']
        fallback_time = row['FallbackTime']
        if pd.notna(primary_time):
            return time_to_seconds(primary_time)
        elif pd.notna(fallback_time):
            return time_to_seconds(fallback_time)
    return None

# Get the filename being played by VLC
def get_vlc_playing_file():
    for process in psutil.process_iter(['name', 'cmdline', 'pid']):
        if process.info['name'] and 'vlc' in process.info['name'].lower():
            cmdline = process.info['cmdline']
            for arg in cmdline:
                if arg.endswith(('.mp4', '.mkv', '.avi')):
                    return arg, process.info['pid'], process
    return None, None, None

# Extract episode number from filename
def extract_episode_number(filename):
    numbers = re.findall(r'\b\d+\b', filename)
    numbers_filtered = [
        int(num) for num in numbers if num not in ('1080', '720') or numbers.count(num) > 1
    ]
    return max(numbers_filtered, default=None)

# Terminate a VLC process
def terminate_vlc_process(process):
    try:
        process.terminate()
        print("[INFO] Terminated previous VLC instance.")
    except psutil.NoSuchProcess:
        print("[ERROR] VLC process not found to terminate.")
    except psutil.AccessDenied:
        print("[ERROR] Access denied to terminate VLC process.")

# Launch VLC with start time
def launch_vlc_with_start_time(video_file, start_time):
    vlc_command = ['vlc', '--start-time', str(start_time), video_file]
    subprocess.Popen(vlc_command)
    print(f"[INFO] Launched VLC with start time {start_time} seconds for {video_file}")

# Show funny popup
def show_funny_popup():
    root = Tk()
    root.title("Hey!")
    root.geometry("300x100")
    Label(root, text="Watch One Piece! 🏴‍☠️", font=("Arial", 14), fg="blue").pack(pady=20)
    root.after(3000, root.destroy)  # Close popup after 3 seconds
    root.mainloop()

# Main function
if __name__ == '__main__':
    df = read_excel_sheet(EXCEL_FILE_PATH)

    print("Monitoring VLC playback...")
    tracked_video = None  # Track the last processed video file
    tracked_pid = None  # Track the PID of the last processed VLC instance

    while True:
        # Get the current playing file and its process details
        video_file, running_pid, running_process = get_vlc_playing_file()

        if video_file:
            print(f"[INFO] Detected VLC playing file: {video_file}")

            if 'one piece' in video_file.lower():
                # Process "One Piece" files
                if video_file != tracked_video:
                    episode_number = extract_episode_number(video_file)
                    if episode_number:
                        print(f"[INFO] Found episode number: {episode_number}")
                        start_time = get_start_time(df, episode_number)
                        if start_time is not None:
                            print(f"[SUCCESS] Starting Episode {episode_number} at {start_time} seconds")

                            # Terminate the previous VLC instance, if any
                            if running_process:
                                terminate_vlc_process(running_process)

                            # Launch new VLC instance with the correct start time
                            launch_vlc_with_start_time(video_file, start_time)

                            # Update tracking variables
                            tracked_video = video_file
                            tracked_pid = running_pid
                        else:
                            print(f"[WARNING] No valid start time found for Episode {episode_number}")
                    else:
                        print(f"[WARNING] Could not extract episode number from filename: {video_file}")
            else:
                # Show popup if a non-"One Piece" file is detected
                show_funny_popup()
        else:
            print("[INFO] No video file currently playing in VLC")

        time.sleep(5)  # Wait 5 seconds before checking again
