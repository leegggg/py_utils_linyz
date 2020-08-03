from pathlib import Path
import os


def checkExist(patten, path: Path, function='prefix'):
    files = os.listdir(path)
    for file in files:
        if function == 'prefix':
            if file.startswith(patten):
                return path.joinpath(file)
        elif function == 'surfix':
            if file.endswith(patten):
                return path.joinpath(file)
        else:
            if file == patten:
                return path.joinpath(file)
    return None
