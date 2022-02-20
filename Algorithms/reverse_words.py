class Solution:
    def reverseWords(self, s: str) -> str:
        reverse_words = []

        for i in s.split():
            i = i[::-1]
            reverse_words.append(i)
        reverse_words = ' '.join(reverse_words)
        return reverse_words

    def reverseWordsOneLine(self, s):
        return ' '.join(s.split()[::-1])[::-1]

    def reverseWordsThreeLine(self, s: str) -> str:
        split_list = s.split(" ")
        split_list = [i[::-1] for i in split_list]
        return " ".join(split_list)