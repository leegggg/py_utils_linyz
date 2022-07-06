from datetime import datetime
import hashlib
from opensearchpy import OpenSearch
from .esMapping import bookMapping
from .footprintCreater import IDFingerprinter as FootPrintCreator

allowedPos = ['ns', 'n', 'vn', 'v']


def makeHashId(content: str):
    hash_object = hashlib.sha1(content.encode())
    return hash_object.hexdigest()


class SearchEngineClient():
    def __init__(self, auth, host='localhost', port=9200, index_name='book'):
        self.fingerprintCreator = FootPrintCreator()
        self.index_name = index_name
        self.client = OpenSearch(
            hosts=[{'host': host, 'port': port}],
            http_compress=True,  # enables gzip compression for request bodies
            http_auth=auth,
            # client_cert = client_cert_path,
            # client_key = client_key_path,
            use_ssl=True,
            verify_certs=False,
            ssl_assert_hostname=False,
            ssl_show_warn=False,
            # ca_certs = ca_certs_path
        )
        if not self.client.indices.exists(index=index_name):
            response = self.client.indices.create(index=index_name, body=bookMapping)
            print('\nCreating index:')
            print(response)

    def post(self, book_uid: str, content: str, title: str, path="", part_no=0, fingerprint=None, tags_text=None, tags=None, ts=None):
        """
        item = {
            "book_uid": bookUid,   # required
            "path": str(textFile),
            "part_no": 0,
            "title": title,        # required
            "content": content,    # required
            "fingerprint": fingerprint,
            "tags_text": ",".join(tags),
            "tags": tags,
            "ts": datetime.now()
        }
        """

        if not fingerprint:
            fingerprint = self.fingerprintCreator.gen(content)

        if not ts:
            ts = datetime.now()

        if not tags:
            tags = []

        if not tags_text:
            tags_text = ",".join(tags)

        body = {
            "book_uid": book_uid,
            "path": path,
            "part_no": part_no,
            "title": title,
            "content": content,
            "fingerprint": fingerprint,
            "tags_text": tags_text,
            "tags": tags,
            "ts": ts
        }

        response = self.client.index(
            id=book_uid,
            index=self.index_name,
            body=body,
            refresh=True
        )

        return response
