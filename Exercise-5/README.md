# Exercise 5: Data analysis with Pandas 

In this exercise, we will be doing data analysis using the [Pandas - Python Data Analysis Library](http://pandas.pydata.org/). So far, we have only used example data stored in list variables, and this week we will be loading data files and interacting with actual data sets. 

In this exercise you are asked to analyze temperature data from Kumpula, Helsinki (in Southern Finland) and Rovaniemi (a city in northern Finland) and to explore how their summer temperatures have differed in 2017.

After making your changes to the notebook, you will need to upload it to GitHub.

- **Exercise 5 is due by the start of the next lesson (9:15 am, 9 October 2019)**.
- Don't forget to check out the [hints for this week's exercise](https://geo-python.github.io/site/lessons/L5/exercise-5.html) if you're having trouble.
- Scores on this exercise are out of **20 points (Problems 1-3)**. Problem 4 is optional.

## Before you start

### Clone the Exercise 5 repository

Make sure you cloned your own repository (repository name contains your GitHub username). After solving the problems, remember to commit your changes and push them to GitHub. Remember also to answer all written questions in the exercise, in addition to the programming tasks.

### Input data

We will use NOAA weather data obtained from [here](https://www7.ncdc.noaa.gov/CDO/cdopoemain.cmd?datasetabbv=DS3505&countryabbv=&georegionabbv=&resolution=40). The data has been stored in a CSV file (comma delimited text file) which is stored in this repository: [data/6153237444115dat.csv](data/6153237444115dat.csv).

You can read the full description of the data and all the attributes from this file: [data/3505doc.txt](data/3505doc.txt) that is also available in this exercise repository. 

The first five rows of the data look like following:

```
USAF,WBAN,YR--MODAHRMN,DIR,SPD,GUS,CLG,SKC,L,M,H,VSB,MW,MW,MW,MW,AW,AW,AW,AW,W,TEMP,DEWP,SLP,ALT,STP,MAX,MIN,PCP01,PCP06,PCP24,PCPXX,SD
028450,99999,201705010000,174,10,14,***,***,*,*,*,2.2,**,**,**,**,67,**,**,**,8,31,31,1009.2,*****,984.1,***,***,*****,*****,*****,*****,35
028450,99999,201705010020,180,10,***,4,***,*,*,*,2.9,**,**,**,**,10,**,**,**,*,30,30,******,29.74,******,***,***,*****,*****,*****,*****,**
028450,99999,201705010050,190,10,***,4,***,*,*,*,2.1,**,**,**,**,10,**,**,**,*,30,30,******,29.74,******,***,***,*****,*****,*****,*****,**
028450,99999,201705010100,188,12,16,***,***,*,*,*,3.2,**,**,**,**,77,**,**,**,*,31,30,1009.1,*****,984.0,***,***,*****,*****,*****,*****,35
```

**NOTICE**: the data includes \* -characters that represent NoData values.

The most important attributes for this exercise are:

 - **USAF** = the station ID number
   - 028450 : Rovaniemi
   - 029980 : Helsinki Kumpula
 - **YR--MODAHRMN** = Year-Month-Day-Hour-Minute in Greenwich Mean Time (GMT)
 - **TEMP** = Temperature in Fahrenheit
 - **MAX** = Maximum temperature in Fahrenheit
 - **MIN** = Minimum temperature in Fahrenheit
 
## Getting started

Always remove these two lines when starting to work on an exercise:
```
# REPLACE THE ERROR BELOW WITH YOUR OWN CODE
raise NotImplementedError()
```
This error will tell us if you have not even started to solve the problem when checking the exercises :)

### Problems

- [Problem 1: Basic statistics](Exercise-5-problem-1.ipynb)
- [Problem 2: Data manipulation and subsetting](Exercise-5-problem-2.ipynb)
- [Problem 3: Data analysis](Exercise-5-problem-3.ipynb)
- [Problem 4: Data aggregation (Optional, but useful!)](Exercise-5-problem-4.ipynb)
- [Exercise 5 summary](Exercise-5-summary.ipynb)