bookMapping = {
    "settings": {
        "index": {
            "number_of_shards": 4
        }
    },
    "mappings": {
        "dynamic": True,
        "properties": {
            "tags": {
                "type": "keyword"
            },
            "ts": {
                "type": "date"
            },
            "book_uid": {
                "type": "keyword"
            },
            "path": {
                "type": "text",
                "fields": {
                    "keyword": {
                        "type": "keyword",
                        "ignore_above": 256
                    }
                }
            },
            "tags_text": {
                "type": "text",
                "analyzer": "simple",
                "search_analyzer": "simple",
                "fields": {
                    "keyword": {
                        "type": "keyword",
                        "ignore_above": 256
                    }
                }
            },
            "part_no": {
                "type": "long"
            },
            "title": {
                "type": "text",
                "analyzer": "smartcn",
                "search_analyzer": "smartcn",
                "fields": {
                    "keyword": {
                        "type": "keyword",
                        "ignore_above": 256
                    }
                }
            },
            "content": {
                "type": "text",
                "analyzer": "smartcn",
                "search_analyzer": "smartcn",
                "fields": {
                    "keyword": {
                        "type": "keyword",
                        "ignore_above": 256
                    }
                }
            }
        }
    }
}
