Got this small exercise as a part of interview.

1) A program that finds and displays the dates of a GitHub user's last 60 commits - "across" repositories..
2) Find the meantime between the last 60 commits and store all time values in an excel file.
I have created a PAT (personal access token) from Github to make sure that I am not restricted by the limits imposed by Github. **However** the Search API restricts the 30 max calls per minute 
[search API docs](https://docs.github.com/en/rest/reference/search#search-commits).

**Please also note the header value**
> **'accept': 'application/vnd.github.cloak-preview'**, # gave me a hard time since this is a preview and I somehow missed this (small text) on Github API documentation

**---- Running a python program  ----** 
if you are using windows, create a folder and run the command, should be the same for other OS as well, please create a directory as the **csv** will be downloaded in the directory you created.
run the program  ------- python exercise.py
   
**Make sure that you create your own PAT token**


