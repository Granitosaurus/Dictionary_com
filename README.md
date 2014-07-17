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
dr.get_definitions()
for df in dr.definition_list:
    print(df)
```

1. Creating object with argument of desired word
2. object.save_to_mp3(filen_ame="desired_file_name".mp3) saves mp3 file.   
3. object.get_definitions() retrieves all via definitions and stores them in the object.definition_list as Definition objects:
**Definition:**
* .word - word that is being defined
* .type - word type (noun etc.)
* .definition - definition of a word

## Run example:
```python
import Dictionary_com
Dictionary_com.main()
```




