# Election Analysis

## Overview of Election Audit
In this project, we have been tasked by a Colorado Board of Elections employee to complete the election audit of a recent local congressional election.  Specifically, we were to accomplish the following:
*	Calculate the total number of votes cast.
*	Get a complete list of candidates who received votes.
*	Calculate the total number of votes each candidate received.
*	Calculate the percentage of votes each candidate won.
*	Determine the winner of the election based on the popular vote.

After presenting a summary of the results of each of the above tasks, we then shift our focus to the analysis done on the election audit for the individual counties involved.  Specifically, we accomplished the following:
*	Calculate the voter turnout for each county involved.
*	Calculate the percentage of votes cast from each county 
*	Determine which county had the highest turnout of votes

Finally, we conclude our project by stating ways in which our code could be used generally for any election (with some slight modifications).

## Election-Audit Results
What follows is a bulleted list and a screenshot of all of the data generated from our analysis:
*	In total, there were 369,711 votes cast.

*	The candidates in the election were:
	*	Charles Casper Stockham
	*	Diana Degette
	*	Raymon Anthony Doane

*	The candidate results were:
	*	Charles Casper Stockham received 85,213 votes, which was 23.0% of the total number of votes cast.
	*	Diana DeGette received 272,892 votes, which was 73.8% of the total number of votes cast.
	*	Raymon Anthony Doane received 11,606 votes, which was 3.1% of the total number of votes cast.

*	The winner of the election was:
	*	Diana DeGette, who received 272,892 votes, which was 73.8% of the total number of votes cast.

*	The county results were:
	*	Jefferson County: 38,855 votes (10.5% of the total number of votes)
	*	Denver County: 306,055 votes (82.8% of the total number of votes)
	*	Arapahoe County: 24,801 votes (6.7% of the total number of votes)

*	From the above data, we see that Denver County had the highest number of voters.




<img width="960" alt="2022-11-09 (1)" src="https://user-images.githubusercontent.com/115128743/200970571-f6330c2b-b9da-4c1d-8ea9-269d718b9379.png">

## Election-Audit Summary
From the above data listed in the “Election-Audit Results” section, we can see that our code generates a large amount of statistical data from the election data that we were given.  Not only is this beneficial in terms of completing this project’s goals, but it is also beneficial for any election audit that desired similar conclusions.  Assuming we had a data source that contained the appropriate voter information, we could, for example, generate a list of data showcasing what method voters used to cast their votes (in-person votes before election day, in-person votes on election day, by mail, punch cards, etc.) with only minor modifications to our current code.  This would be done in almost the exact same way in which we generated the data for the individual candidates and the individual counties; we would tally up the number of different ways in which voters cast their votes using the same type of looping mechanism used in our current analysis.  In addition to this, we could also perform analyses on much larger areas.  Given that we did analysis on several different counties for the Colorado election, the process used to gather this data could easily yield election results for entire states for larger elections.  This would be as simple as renaming several variables in our code to display state names as opposed to the county names presented here.  Overall, it should be recognized that our analysis is not limited to just generating the results that we have shown here.

## Resources
The following resources were used to produce the results of the analysis given above:
*	The given data source was a csv file titled “election_results.csv” that contained 369,711 rows of voter data.
*	The software used was Python version 3.7.6

