# Github Trends

# Quickstart

The program finds repositories on Github created in the previous week, takes 20 high-starred of them and counts the amount of open issues. It outputs the repository name, number of issues and a url to the repo

The script requires the installed Python interpreter version 3.5 and library **requests**



```bash
$ pip install -r requirements.txt
```

Example of script launch on Linux, Python 3.5:

```bash
$ python github_trending.py

Repository: hangzhou_house_knowledge
Url: https://github.com/houshanren/hangzhou_house_knowledge
Issues: 2

Repository: requests-html
Url: https://github.com/kennethreitz/requests-html
Issues: 2

Repository: 30-seconds-of-css
Url: https://github.com/atomiks/30-seconds-of-css
Issues: 2

Repository: mpvue
Url: https://github.com/Meituan-Dianping/mpvue
Issues: 2
...
```
# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
