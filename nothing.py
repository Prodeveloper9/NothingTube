import tkinter as tk
from tkinter import filedialog
from pytube import YouTube

# Function to handle video download
def download_video():
    # Get the YouTube video URL from the user
    video_url = url_entry.get()
    
    # Create a YouTube object
    yt = YouTube(video_url)
    
    # Choose the highest resolution stream (you can customize this)
    stream = yt.streams.get_highest_resolution()
    
    # Ask the user for the download location
    download_path = filedialog.askdirectory()
    
    # Download the video to the selected location
    stream.download(download_path)
    
    # Display a success message
    status_label.config(text=f"Downloaded {yt.title} to {download_path}")

# Create a Tkinter window
root = tk.Tk()
root.title("YouTube Video Downloader")

# Create a label and entry for the YouTube URL
url_label = tk.Label(root, text="Enter YouTube URL:")
url_label.pack()
url_entry = tk.Entry(root)
url_entry.pack()

# Create a download button
download_button = tk.Button(root, text="Download Video", command=download_video)
download_button.pack()

# Create a label to display the download status
status_label = tk.Label(root, text="")
status_label.pack()

# Start the Tkinter main loop
root.mainloop()
