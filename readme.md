## LS Explorer
Combining the best elements of bash ls with interactive fiction. 

``` shell
$ python run_ls_explorer.py
> ls projects/wiki/archive
It is dark. You are likely to be eaten by a grue. Seriously, these are old project files that went stale a million years ago -- probably nothing of value. Go look in projects/wiki/current to see a (mostly) working prototype. 

Look at files anyway? [y]/n
To go to projects/wiki/current, press [c].
```

### Description
This is a silly side project that adds some editorial flavor to the day-to-day drudgery of `ls` and `cd`. Instead of simply reporting the files and directories that exist, it gives you the opportunity to add annotations and editorial notes, offer redirects, and generally remind you what you think of your own filesystem. For now, it's written in Python (because that's easy) though if I ever decided to do this 'properly', it would be translated to C. 

* Started: 2/19/2016
* Continued: in very occasional fits and starts. Not a high priority in any way. 
* Author: Monica Toth

### Directories
* *src*: Where (most of?) the code lives. 
* *narrative*: User-input data and text that will form the narrative portions of the program. 
* *tests*: Tests.

### How to Get Started
(TODO) 