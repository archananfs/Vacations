##VACATION
This code can be used to calculate the maximum holiday span for the given vacation days.

##Prerequisites
Following python libraries:
datetime
holidays
numpy

##Usage 
Create a object with number of Holidays and Country as parameters.
For country code refer https://pypi.org/project/holidays/
Example: 
Input: Country = USA, Number of vacation days = 15, year = 2020
h = Vacation()
h.get_vacation_options(15, 'US',2020)

Output:
 2020-11-26 2021-01-05 40 days
 2020-11-25 2021-01-04 40 days
 2020-11-24 2021-01-01 38 days
 2020-11-21 2020-12-31 40 days


