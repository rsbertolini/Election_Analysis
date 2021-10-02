# Election_Analysis
$ git config --global core.autocrlf true

## Overview of Project
The purpose of this project was to familiarize ourselves with file input/output handling.  We read in a comma delimited file of votes and tallied multiple data points in the file and output those results to both the terminal and a text file.  The file only contained 3 values per row but we were able to compute both total counts and percentage counts for both candidates and county data.


## Election Audit Results
* The total number of votes cast in this congressional election was 369,711
* Largest county turnout was Denver

**County Results**
-----------------------------------------------------------------------
Jefferson: 10.5% (38,855 total votes)
Denver: 82.8% (306,055 total votes)
Arapahoe: 6.7% (24,801 total votes)


**Candidate Results**
------------------------------------------------------------------------
Charles Casper Stockham: 23.0% (85,213 total votes)
Diana DeGette: 73.8% (272,892 total votes)
Raymon Anthony Doane: 3.1% (11,606 total votes)

**Winning Candidate
Winner: Diana DeGette
Winning Vote Count: 272,892
Winning Percentage: 73.8%**

## Election Audit Summary
This module could be refactored and used for other election results such as local proposition votes that are for/against, 
where candidate name is replaced by a voter's for/against decision on a ballot proposition.  Another example of where this 
module could be refactored is with local school board elections where county name is replaced by school district.
