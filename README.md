# Election_Analysis
Programming with Python

# Project Overview: Election_ Analysis


In this analysis I’ll be analyzing and extracting data from a CSV file, using Python programming language with Visual Studio Code to write, run, and edit scripts, and familiarize with the command line to navigate and create files. All, to produce a script that’ll audit elections results automatically.

Tom, a Colorado Board of Election employee for a US congressional district, wants assistance with automating an election audit to report:
- The total of votes cast,
- A complete list of the candidates who received votes 
- total votes for each candidate, 
- Percentage of votes for each candidate, and 
- the winner of the election based on the popular vote. 

The election results data set is embedded in a CSV file that will be connected to and extracted from, but instead of using Microsoft office Excel, we’ll be auditing the results using Python Programming Language. Tom wants to author an automatic code that can be employed for future election audits at any level.


# Resources:
- Data Source: election_results.csv
- Software: Python 3.6.1, Visual Studio Code, 1.38.1


## Summary of CSV file
There were 369,711 votes casted in the election.

The candidates were:
  1. Charles Casper Stockham
  2. Diana DeGette
  3. Raymon Anthony Doane

The candidate results were:
  - Charles Stockham received 23% of the popular vote with 85,213 vote count
  - Diana DeGette received  73.8% of the popular vote with a 272,892 vote count
  - Raymon Doane received 3.1% of the popular vote with a 11,606 vote count

The winner of the election was:
  - Diana Degette with 73.8% of the popular vote and a 272,892 vote count!
 <img width="317" alt="Screen Shot 2022-06-01 at 5 15 54 PM" src="https://user-images.githubusercontent.com/105556091/171503258-8ecd7517-0bfc-473e-b910-a43a96d4b8bf.png">

	

### Challenge Overview
In addition to the Candidate Results audit, we’ll use the same data set to audit the results by county. 

Producing:
- The voter turnout by county
- Percentage of the total vote cast by each county
- Identifying the County with the largest turnout

#### Challenge Result 
The election was casted over 3 counties:
  - Jefferson County
  - Denver County
  - Arapahoe County

The county results were:
  - Jefferson County had 10.5% of the total vote, with a 38,855 vote count
  - Denver County had 82.8% of the total vote, with a 306,055 vote count
  - Arapahoe had 6.7% of the total vote, with a 24,801 vote count

The county with the largest turnout was:
  - Denver County with 82% of the total vote and 306,055 votes casted!

![image](https://user-images.githubusercontent.com/105556091/171515839-c3a3543c-d5f7-4d5f-957a-4d769b2b5774.png)


##### Challenge Summary
In the Future, this script can be modified to perform additional election audits. These modification will need to be of :
- Correcting the respective file paths: What folders to extract the data from and text files to write the produced output to
![image](https://user-images.githubusercontent.com/105556091/171500227-ac721d28-d65a-43f6-9e8a-baccb2a8951d.png)


- Illustrating an appropriate data index for the respective data set: Your .csv file or .xlxs my be organized or reformatted with contrasting columns, rows, and additional information. You want to be sure the correct information is being reference.
![image](https://user-images.githubusercontent.com/105556091/171499504-19f86b7f-b78a-481b-b0ae-5a4d385bd5c0.png)
![image](https://user-images.githubusercontent.com/105556091/171500087-9a502a42-e155-4feb-983d-fe4da1b59c60.png)


- Reviewing the logical operators for the “IF” statements so that they produce the warranted result. 
![image](https://user-images.githubusercontent.com/105556091/171500401-783b4fb2-4d9c-4cf9-98b0-20739a34a790.png)


- And, updating the F-strings for the  county output results, so that they read in respect to the level of the election: County, City, or State.
<img width="360" alt="F_string-ref" src="https://user-images.githubusercontent.com/105556091/171499287-d30c5747-dd67-4db0-b5fb-834c64c5daf2.png">
