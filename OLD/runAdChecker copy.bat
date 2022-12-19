@echo off

echo Starting AdChecker
echo -----------------

python AdChecker.py https://www.google.com/search?q=marble+fountain "Fine's Gallery" 10

python AdChecker.py https://www.google.com/search?q=marble+statues "Fine's Gallery" 10 

python AdChecker.py https://www.google.com/search?q=marble+fireplaces "Fine's Gallery" 10 

python AdChecker.py https://www.google.com/search?q=bronze+fountain "Fine's Gallery" 10 

python AdChecker.py https://www.google.com/search?q=bronze+statues "Fine's Gallery" 10 

python AdChecker.py https://www.google.com/search?q=religious+statues "Fine's Gallery" 10 

python AdChecker.py https://www.google.com/search?q=bronze+dolphin "Fine's Gallery" 10 

python mychart.py
echo -----------------
echo AdChecker Complete
pause