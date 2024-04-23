# novel-scraper

Simple Web Scraper using BeautifulSoup. (Python)

Adjusted to certain novel translation sites as I use.
Find all novel chapter text and writes to a text file.

Uses BeautifulSoup, TQDM, OS

To use install the following:

```python
  pip install beautifulsoup4
```
Progress Bar:
```python
  pip install tqdm
```

Issues:
Beautiful couldn't pull a deeply nested list of tags containing the chapter links of the novel. Manually added the HTML of the nested tags that it failed to retrieve.
