from distutils.core import setup
import os
from typing import List

_PATH_ROOT = os.path.realpath(os.path.dirname(__file__))

def _load_requirements(path_dir: str, file_name: str = "requirements.txt", comment_char: str = "#") -> List[str]:
    """Load requirements from a file.
    >>> _load_requirements(_PATH_ROOT)
    ['numpy...', 'torch..."]
    """
    with open(os.path.join(path_dir, file_name)) as file:
        lines = [ln.strip() for ln in file.readlines()]
    reqs = []
    for ln in lines:
        # filer all comments
        if comment_char in ln:
            char_idx = min(ln.index(ch) for ch in comment_char)
            ln = ln[:char_idx].strip()
        # skip directly installed dependencies
        if ln.startswith("http") or ln.startswith("git") or ln.startswith("-r") or "@" in ln:
            continue
        if ln:  # if requirement is not empty
            reqs.append(ln)
    return reqs

BASE_REQUIREMENTS = _load_requirements(path_dir=_PATH_ROOT, file_name="requirements.txt")

if __name__ == "__main__":
    setup(name='py-phonem',
        version='1.0',
        description='Phonem encoding in german, french and italian',
        author='Corentin Royer',
        url='https://github.com/corentin-ryr/py-phonem',
        install_requires=BASE_REQUIREMENTS,
        )