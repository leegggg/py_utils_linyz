import jieba.analyse
allPos = ["n", "f", "s", "t", "nr", "ns", "nt", "nw", "nz", "v", "vd", "vn", "a", "ad", "an", "d", "m", "q", "r", "p", "c", "u", "xc", "w", "PER", "LOC", "ORG", "TIME"]
allowedPos = ['ns', 'n', 'vn', 'v']


class IDFingerprinter():
    def __init__(self):
        self.jiebaAnalyser = jieba.analyse.TFIDF()
        # self.jiebaAnalyser.set_idf_path("data/jieba_dict/wdic.txt")
        # self.jiebaAnalyser.set_stop_words("data/jieba_dict/stopword/stopwords.txt")
        pass

    def gen(self, content):
        keywords = self.jiebaAnalyser.extract_tags(content, topK=12)
        return ",".join(keywords)


class TextRankFingerprinter():
    def __init__(self):
        self.jiebaAnalyser = jieba.analyse.TextRank()
        # self.jiebaAnalyser.set_idf_path("data/jieba_dict/wdic.txt")
        # self.jiebaAnalyser.set_stop_words("data/jieba_dict/stopword/stopwords.txt")
        pass

    def gen(self, content):
        keywords = self.jiebaAnalyser.extract_tags(content, topK=12, allowPOS=allowedPos)
        return ",".join(keywords)
