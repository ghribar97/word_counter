Word Counter
============
Print byte, word, and line counts, count the number of bytes, whitespace-separated words, and newlines in each given FILE.
A word is a non-zero -length sequence of characters delimited by white space.

Installation
============
1. download and install python3 from[www.python.org](https://www.python.org/downloads/)
2. download [wordCounter.py](https://github.com/ghribar97/word_counter/blob/master/wordCounter.py) file 

Run
===
Open the folder with **wordCounter.py** file in a console.

Follow the given syntax or type ```python3 wordCounter.py --help```  for mor information.


Syntax
======

python3 wordCounter.py [-h] [-c] [-m] [-w] [-l] [-L] [--version] [FILE]

Version
=======
This is my implementation of the (well known) Linux program [WC](https://ss64.com/bash/wc.html) (Word Counter) 

Time comparison with the original WC:
-------------------------------------
For the comparison I have prepared a file [TestFile.txt](https://github.com/ghribar97/word_counter/blob/master/TestFile.txt).

In the console we run this two commands:
    
1. ```time python3 wordCounter.py -w -m -l -c -L TestFile.txt``` 
 
    ```$ 13 641 3378 3378 319 TestFile.txt```  
    ```real 0m0,131s```  
    ```user 0m0,046s```  
    ```sys 0m0,015s```
    
2. ```time wc -w -m -l -c -L TestFile.txt```

    ```$ 13 641 3378 3378 319 TestFile.txt```  
    ```real 0m0,062s```  
    ```user 0m0,000s```  
    ```sys 0m0,015s```
    
We can see, that the original version is more than two times faster than my implementation.
