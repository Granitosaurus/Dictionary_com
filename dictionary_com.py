import re
import requests
import bs4
__author__ = 'Bernard @ bernardas.alisauskas@gmail.com'

"""
Dictionary.com scraper/API package for Python, see https://github.com/Granitas/Dictionary_com for more details.
Copyright - feel free to do whatever you like.
"""


class DictionaryReference:
    """
    Creates http://dictionary.reference.com/ object which can be used to retrieve definitions and audio pronunciations
    of a passed word.

    Keyword Arguments:
    word -- word of which definitions will be retrieved
    """

    def __init__(self, word):
        self.word = word
        self.definition_list = []
        self.extra_list = []
        self._request = None
        self._soup = None
        self._get_page_contents()

    def _get_page_contents(self):
        """Retrieve dictionary page contents, runs automatically upon creation of an object"""
        self._request = requests.get('http://dictionary.reference.com/browse/' + self.word)
        self._soup = bs4.BeautifulSoup(self._request.text)

    def get_definitions(self):
        """Finds definitions in the page soup and appends them to self.definition_list"""
        tables = self._soup.find_all('div', class_="KonaBody")
        for table in tables:
            if table['style'] == '':
                # print(table)
                # key = table.find('div', class_='dicTl').text
                # item = table.find('language').text
                # print(key)
                # print(item)
                continue
            text = table.find('div', class_='pbk').text
            text = text.split(' ')
            word_type = text[1].replace(',', '')
            text = " ".join(text[2:]).strip()
            origin = re.sub("Origin:|\s+", " ", table.find('div', class_="ety").text).strip()

            self.definition_list.append(Definition(self.word, word_type, text, origin))

    def save_html(self, file_name=None):
        """
        Saves the html of a definition

        Keyword arguments:
        file_name -- name of a saved file, include .html suffix (default self.word + .html)
        """
        if file_name is None:
            file_name = '{word}.html'.format(word=self.word)
        with open(file_name, 'w') as html_file:
            print("Writing to {0}.html".format(self.word))
            html_file.write(self._soup.prettify())

    def get_html(self):
        """Returns string html of a definition"""
        return self._soup.prettify()

    def save_to_mp3(self, file_name=None):
        """
        Saves mp3 pronunciation sound file.

        Keyword Arguments:
        file_name -- name of the file, must include .mp3 suffix (default self.word + '.mp3')
        """
        if file_name is None:
            file_name = self.word + '.mp3'
        try:
            with open(file_name, 'wb') as mp3_file:
                file_url = self._soup.find('a', class_='audspk')['href']
                mp3_file.write(requests.get(file_url).content)
                print("writing to: {0}".format(file_name))
        except (FileNotFoundError, PermissionError) as e:
            print("Failed to save mp3 file: {error}".format(error=e))

    def __str__(self):
        return "The Dictionary_com object for word: {}".format(self.word)


class Definition:
    """
    Definition object, used to store definitions retrieved by DictionaryReference object.

    Keyword arguments:
    word -- word that is being defined
    type -- word type (i.e. noun)
    definition -- word definition
    origin -- word origin
    """
    def __init__(self, word, word_type, definition, origin):
        self.word = word
        self.type = word_type
        self.definition = definition
        self.origin = origin

    def __str__(self):
        return "Word: {0}\nType: {1}\nDefinition: {2}\nOrigin: {3}".format(self.word, self.type, self.definition,
                                                                                self.origin)


def main():
    """Example api process"""
    dr = DictionaryReference(input("Enter a word:"))
    dr.save_to_mp3()
    dr.save_html()
    dr.get_definitions()
    for df in dr.definition_list:
        print(df)
    print('html:\n{separator}\n{html}\n{separator}'.format(html=dr.get_html(), separator='-'.center(79, '-')))

if __name__ == '__main__':
    main()