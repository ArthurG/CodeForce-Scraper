# CodeForces Scraper
Scrape Question and tags for CodeForces

Why might you want to do that? Well, command line tools are quite useful for finding relevant questions. 

Sample commands
- Run the script
```
python3 scrape.py
```

- Find all math problems that are not greedy

```
cat my_txt.csv | grep "math" | grep -v "greedy" | head
```


- Find all math problems that are rated 1500

```
cat my_txt.csv | grep "math" | grep "1500" | head
```


