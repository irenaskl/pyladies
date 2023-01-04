from string import ascii_lowercase, ascii_uppercase
import re

class Subtitles:

    ORIGINAL_SUBTITLES = 'Forrest.Gump.1994.srt'
    THE_MOST_USE_WORDS = '20k.txt'
    EN_CZ_DICTIONARY = 'en-cs.txt'


    def original_subtitles(self, filename=ORIGINAL_SUBTITLES) -> None:
        '''Converts the subtitles to a list'''
        with open(filename, 'r') as f:
            subtitles = f.read()
        # Remove of unnecessary characters
        self.original_list = re.findall(r'\w+', subtitles)

    def filter_text(self) -> None:
        '''Filters only text from the original subtitles list'''
        temporary_list = []
        for i in self.original_list:
            if i[0] in ascii_lowercase or i[0] in ascii_uppercase:
                temporary_list.append(i.lower())
        self.original_list = temporary_list

    def remove_duplicities(self) -> None:
        '''Removes duplicities from the original subtitles'''
        temporary_list = [*set(self.original_list)]
        temporary_list.sort()
        self.original_list = temporary_list

    def unknown_words(self, file=THE_MOST_USE_WORDS) -> None:
        '''Removes the most use words'''
        with open(file, 'r') as f:
            known_words = (f.read()).split()
        unknown_words = []

        for i in self.original_list:
            if i not in known_words:
                unknown_words.append(i)
        self.original_list = unknown_words

    def format_dictionary(self, file=EN_CZ_DICTIONARY):
        '''Convert string dictionary to dict format'''
        with open(file, 'r') as f:
             dictionary_list = (f.read()).split('\n')

        self.dictionary_dict = dict()

        for i in dictionary_list:
            key, *val = i.split('\t')
            self.dictionary_dict[key] = val

        for key in self.dictionary_dict:
            print(key)



if __name__ == '__main__':
    forrest = Subtitles()
    forrest.original_subtitles()
    forrest.filter_text()
    forrest.remove_duplicities()
    forrest.unknown_words()
    forrest.format_dictionary()
    #print(forrest.original_list)
