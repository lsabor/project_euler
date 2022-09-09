# project_euler
Solution code to the problem bank from https://projecteuler.net/

Author:  
Luke Sabor  
lukesabor@gmail.com  
GitHub: @lsabor  

Co-authors (noted on specific problems):  
Andrew Roberts - GitHub: @ajroberts0417  
Geroge Jeffreys - georgej@bu.edu  
Michael Morgan - GitHub: @msmorgan  
DeMehr Haywood - GitHub: @demehr

Project details:  
Started March 5, 2022  
Uses Python 3.10.0 or later  
The intention is to proceed through problems 1-100 from archives https://projecteuler.net/archives/ in order. That may be subject to change.  

Install directions:  
intended for `pipenv`  
run `pipenv install --dev`  

_______________________________________________________________

File Structure:  
```
/project_euler/
 ├── README.md  
 ├── requirements.txt  
 ├── maths/                               <- helper modules that get used multiple times  
 |   ├── graphs/  
 |   |   ├── __init__.py  
 |   |   └── graphs.py  
 |   ├── ...  
 |   ├── sequences/  
 |   |   ├── __init__.py  
 |   |   ├── sequences.py  
 |   |   ├── special_sequences.py  
 |   |   ├── caches/                      <- caches for high-compute sequences  
 |   |   |   └──  PrimesSequence.json  
 |   |   └── compound/  
 |   |       ├──  __init__.py  
 |   |       └──  compound.py  
 |   └── ...  
 ├── tests/   
 |   ├── answer_tests/  
 |   |   ├── 00s.py                       <- tests the solution for first 10 problems
 |   |   └── ...  
 |   └── module_tests/  
 |       ├── graphs/  
 |       |   └── graphs_tests.py          <- tests for the maths.graphs module
 |       └── ...  
 └── 000-100/                             <- solution files
     ├── X0s/  
     |   ├── 0X0_ZZ_PROBLEM_NAME.py       <- first three digits (0X0) indicate problem number, 
     |   |                                   next two (ZZ) indicate difficulty level (00-95)  
     |   ├── 0X1_ZZ_PROBLEM_NAME.py  
     |   ├── ...  
     |   └── 0X9_ZZ_PROBLEM_NAME.py  
     ├── 10s/  
     |   ├── 010_ZZ_PROBLEM_NAME.py  
     |   ├── ...  
     |   └── 019_ZZ_PROBLEM_NAME.py  
     └── ...  
```


From the conditions of using the website, one cannot publish solutions to problems past problem 100.  
"""  
Please do not deprive others of going through the same process by publishing your solution outside of Project Euler. Members found to be spoiling problems beyond the first one-hundred problems will have their accounts locked.  
"""  
I intend to continue soliving problems past 100, but will put those solutions in a private repository viewable only upon request.  
