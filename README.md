# vtop-coursereg-scrapper
Scrapping course registration info from vtop because they don't want to give us a pdf anymore :|

### Usage
- `pip install -r requirements.txt`
- Enter the required values in the `config` dictionary and add course codes of the required courses in the `courses` list
- Leaving the list empty will scrape all courses visible to you (BEWARE, YOU CAN GET SOFTLOCKED OUT FOR 15 MINUTES IF YOU DO THIS)
- `python scrape.py`

### Output
- A courses.csv file will be created.
