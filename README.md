Dictionary_com
==============

Python API/Scraper for Dictionary.com

#Prerequisites:
Written in Python 3.4  
**BeautifulSoup 4** - https://pypi.python.org/pypi/beautifulsoup4/  
>pip install beautifulsoup4  

**Requests** - https://pypi.python.org/pypi/requests/2.3.0
>pip install requests

#Running:
Example:
```python
dr = DictionaryReference(input("Enter a word:"))
dr.save_to_mp3()
dr.save_to_html()
dr.get_definitions()
for df in dr.definition_list:
    print(df)
```

1. Creating object with argument of desired word
2. object.save_to_mp3(filen_ame="desired_file_name".mp3) saves mp3 file.   
3. object.get_definitions() retrieves all via definitions and stores them in the object.definition_list as Definition objects:  

**DictionaryReference**
- .word - word that is being defined.  
- .definition_list - definition items.  
- .get_definitions() - fills in object.definition_list with Definition objects.  
- .save_to_mp3() - saves pronounciation to mp3 file:  
args: file_name - name of a mp3 file  
- .get_html() - returns html of the word definition page as a string.  

**Definition:**  
- .word - word that is being defined.  
- .type - word type (noun etc.).  
- .definition - definition of a word.  
- .origin - origin of the word.  

## Run example:
```python
import Dictionary_com
Dictionary_com.main()
```




