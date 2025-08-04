import sys
import yt_dlp

if len(sys.argv) < 2:
    print("Usage: python YT_Downloader.py <YouTube_URL>")
    sys.exit(1)
url = sys.argv[1]
ydl_opts = {
    'format': 'bestvideo+bestaudio/best',
    'outtmpl':  r'F:\myProject\%(title)s.%(ext)s', 
    'merge_output_format': 'mp4',
    'noplaylist': True,  
}
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    info = ydl.extract_info(url, download=False)  
    print(f"Title: {info['title']}")
    print(f"Views: {info.get('view_count', 'N/A')}")
    ydl.download([url])
    print("Download complete!")
# Run CODE:     
'''
# How to run :
open power shell
python F:/myProject/YT_Downloder.py " (link from youtube) "
'''