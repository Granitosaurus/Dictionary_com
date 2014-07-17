__author__ = 'Bernard @ bernardas.alisauskas@gmail.com'
import requests
import bs4


class DictionaryReference:
    """Creates http://dictionary.reference.com/ object which can be used to retrieve definitions and audio pronunciations
    of a passed word.
    args:
    word - word of which definitions will be retrieved"""

    def __init__(self, word):
        self.word = word
        self.definition_list = []
        self.__request = None
        self.__soup = None
        self.__get_page_contents()

    def __get_page_contents(self):
        """Retrieve dictionary page contents, runs automatically upon creation of an object"""
        self.__request = requests.get('http://dictionary.reference.com/browse/' + self.word)
        self.__soup = bs4.BeautifulSoup(self.__request.text)

    def get_definitions(self):
        """Finds definitions in the page soup and appends them to self.definition_list"""
        tables = self.__soup.find_all('div', class_="KonaBody")
        # tables_extra = tables[-4:] #TODO find use for tables_extra
        tables = tables[:]
        for table in tables:
            if table['style'] == '':
                continue
            text = table.find('div', class_='pbk').text
            text = text.split(' ')
            word_type = text[1]
            text = " ".join(text[2:]).strip()
            self.definition_list.append(Definition(self.word, word_type, text))
        with open(self.word + '.html', 'w') as html_file:
            print("Writing to {0}.html".format(self.word))
            html_file.write(self.__soup.prettify())

    def save_to_mp3(self, file_name=None):
        """Saves mp3 pronunciation sound file
        file_name - name of the file, must include .mp3 suffix; Default = self.word + '.mp3'
        """
        if file_name is None:
            file_name = self.word + '.mp3'
        try:
            with open(file_name, 'wb') as mp3_file:
                file_url = self.__soup.find('a', class_='audspk')['href']
                mp3_file.write(requests.get(file_url).content)
                print("writing to: {0}".format(file_name))
        except:
            print("Failed to save mp3 file")

    def __str__(self):
        return "The Dictionary_com object for word: {}".format(self.word)


class Definition:
    """Definition object, contains definition list, main definition and a type of a word that is being defined"""
    def __init__(self, word, word_type, definitions,):
        self.word = word
        self.type = word_type
        self.definition = definitions

    def __str__(self):
        return "Word: {0}\nType: {1}\nDefinition: {2}".format(self.word, self.type, self.definition)


def main():
    """Example api process"""
    dr = DictionaryReference(input("Enter a word:"))
    dr.save_to_mp3()
    dr.get_definitions()
    for df in dr.definition_list:
        print(df)

if __name__ == '__main__':
    main()