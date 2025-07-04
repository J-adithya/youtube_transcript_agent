import webbrowser

def open_youtube(url: str) -> str:
    webbrowser.open(url)
    return f"Opened {url} in your browser"
