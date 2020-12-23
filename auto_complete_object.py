class AutoCompleteData:
    def __init__(self, sentence, path, offset, score = 0):
        self.m_sentence = sentence
        self.m_path = path
        self.m_offset = offset
        self.m_score = score

    def set_score(self, user_text):
        self.m_score = len(user_text) * 2