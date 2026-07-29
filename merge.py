import requests

URLS = [
    "https://jhsevetns-fhd.rtxcric.workers.dev/playlist.m3u",
    "https://raw.githubusercontent.com/doctor-8trange/zyphora/refs/heads/main/data/sony.m3u",
    "https://raw.githubusercontent.com/doctor-8trange/zyphx8/refs/heads/main/data/fancode.m3u",
    "https://raw.githubusercontent.com/doctor-8trange/nexphi0/refs/heads/main/data/icc.m3u"
]

def get_playlist(url):
    r = requests.get(url, timeout=30)
    r.raise_for_status()
    return r.text

merged = "#EXTM3U\n"

for url in URLS:
    playlist = get_playlist(url)
    lines = playlist.splitlines()

    # Remove #EXTM3U header from each source playlist
    if lines and lines[0].startswith("#EXTM3U"):
        lines = lines[1:]

    merged += "\n".join(lines) + "\n"

with open("playlist.m3u", "w", encoding="utf-8") as f:
    f.write(merged)

print("Merged 4 playlists successfully!")
