Dictionary_com
==============

Python API/Scraper for Dictionary.com

#Prerequisites:
**BeautifulSoup 4** - https://pypi.python.org/pypi/beautifulsoup4/  
>pip install beautifulsoup4  

**Requests** - https://pypi.python.org/pypi/requests/2.3.0
>pip install requests

#Running:
```python
dr = DictionaryReference(input("Enter a word:"))
dr.save_to_mp3()
dr.get_definitions()
for df in dr.definition_list:
    print(df)
```
