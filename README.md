# vtop-coursereg-scrapper
Scrapping course registration info from vtop because they don't want to give us a pdf anymore :|

### Usage
- `pip install -r requirements.txt`
- Enter the required values in the `config` dictionary and add course codes of the required courses in the `courses` list
- `python scrape.py`
- leaving the list empty will scrape all courses (BEWARE, YOU CAN GET SOFTLOCKED OUT FOR 15 MINUTES IF YOU DO THIS)

### Output
- A courses.csv file will be created.
