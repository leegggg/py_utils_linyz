import urllib.parse
from pathlib import Path

from requests.sessions import Session
from .common import req


class DownloadUtil():
    def __init__(self):
        self.req: Session = req

    def downLoadData(self, url, basePath: Path, name=None, extension=None, overwrite=True, show=False):
        from clint.textui import progress
        epubResponse = self.req.get(url, stream=True)
        realUrl = epubResponse.url
        urlPath = Path(urllib.parse.urlparse(realUrl).path)
        if not extension:
            extension = urlPath.suffix
        if not name:
            name = urlPath.stem
        fileName = name + extension
        path = basePath.joinpath(fileName)
        if overwrite:
            if path.is_file() or path.is_dir():
                if show:
                    print("skip for not overwrite")
                return realUrl
        if epubResponse.ok:
            with open(path, 'wb') as epubFile:
                total_length = epubResponse.headers.get('content-length')
                if total_length:
                    total_length = int(total_length)
                chunks = epubResponse.iter_content(chunk_size=1024)
                if show and total_length:
                    nbBlocks = int(total_length) / 1024 + 1
                    chunks = progress.bar(
                        it=chunks,
                        expected_size=nbBlocks, label="{}\t".format(fileName))
                for chunk in chunks:
                    if chunk:
                        epubFile.write(chunk)
                        epubFile.flush()
                if total_length and path.stat().st_size < total_length:
                    raise IOError()
        return realUrl
