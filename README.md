# project_euler
Solution code to the problem bank from https://projecteuler.net/

Author:  
Luke Sabor  
lukesabor@gmail.com  
GitHub: @lsabor  

Co-authors (noted on specific problems):  
Andrew Roberts - GitHub: @ajroberts0417  

Project details:  
Started March 5, 2022  
Uses Python 3.10.0 or later  
The intention is to proceed through problems 1-100 from archives https://projecteuler.net/archives/ in order. That may be subject to change.  

File Structure:  
/project_euler
  *  README.md  
  *  requirements.txt  
  *  /modules/            <- helper modules that get used multiple times  
  *    *  sequences.py  
  *    *  primes.py  
  *    *  ...  
  *    *  trees.py  
  *  /caches/             <- caches for high-compute problems  
  *    *  /sequences/  
  *    *    *  Fibonacci.json  
  *    *    *  Natural.json  
  *    *    *  ...  
  *    *    *  Triangle_Numbers.json  
  *    *    *  /compound/  
  *    *    *    *  Triangle_Numbers_Prime_Factorization.json  
  *    *  /trees/  
  *    *    *  Collatz.json  
  *  /0X00s/  
  *    *  /00X0s/
  *    *    *  00X0.ipynb  <- example solution  
  *    *    *  00X1.ipynb  <- solution to problem 1  
  *    *    *  00X2.ipynb  
  *    *    *  ...  
  *    *    *  00X9.ipynb
  *    *  /0010s/
  *    *    *  0010.ipynb   
  *    *    *  ...  
  *    *    *  0019.ipynb  
  *    *  ...  
  *  /0100s/         <- this will only continue privately, see note below  
  *    *  /0010s/
  *    *    *  0100.ipynb  
  *    *    *  ...  
  *    *    *  0199.ipynb  
  *  ...  


From the conditions of using the website, one cannot publish solutions to problems past problem 100.  
"""  
Please do not deprive others of going through the same process by publishing your solution outside of Project Euler. Members found to be spoiling problems beyond the first one-hundred problems will have their accounts locked.  
"""  
I intend to continue soliving problems pas 100, but will put those solutions in a private repository viewable only upon request.  
