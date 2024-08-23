class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = dict()
        for file_name in self.file_names:
            with open(file_name, encoding='utf-8') as file:
                file_words = []
                for line in file:
                    for char in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                        line = line.replace(char, ' ')
                    line = line.lower().split()
                    file_words.extend(x for x in line)
                all_words[file_name] = file_words
        return all_words

    def find(self, word):
        all_finds = dict()
        for name, words in self.get_all_words().items():
            if word.lower() in words:
                all_finds[name] = words.index(word.lower()) + 1
        return all_finds

    def count(self, word):
        all_calculations = dict()
        for name, words in self.get_all_words().items():
            if word.lower() in words:
                all_calculations[name] = words.count(word.lower())
        return all_calculations


finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                      'Rudyard Kipling - If.txt',
                      'Mother Goose - Monday’s Child.txt')
print(finder1.get_all_words())
print(finder1.find('the'))
print(finder1.count('the'))
