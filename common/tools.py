import os
from typing import Optional

import requests


def fmt(s: str, *args, **kwargs):
    return s.format(*args, **kwargs)


def page_content(url: str) -> Optional[str]:
    '''This function takes a URL as argument and tries to download it
    using requests. Upon success, it returns the page contents as string.'''
    try:
        r = requests.get(url)
    except requests.exceptions.ConnectionError:
        print("failed to connect to url " + url)
        return None
    if r.ok:
        return r.text
    else:
        print("failed to download url " + url)
        return None


def save(text: str, directory: str, filename: str):
    '''Write "text" to the file "filename" located in directory "directory",
    creating "directory" if necessary. If "directory" is the empty string, use
    the current directory.'''
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, filename)
    with open(path, 'w', encoding='utf-8') as file_out:
        file_out.write(text)
    return None
