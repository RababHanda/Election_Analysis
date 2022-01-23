# Colorado Constituency Election Analysis

## Overview of Project
This project audits the election results from 3 Colorado constituencies from an anonymous year.

### Purpose

**Analytical:** The project analyzes the raw data from an election event to decipher trends and corelations between the various factors governing the voting and the results.

**Technical:** The project employs python coding skills, specifically loops & conditional statements, to achieve the requested results

## Election-Audit Results

- A total of **369,711** votes were cast in this congressional election
- The breakdown of the total votes across the counties were as follows, with Denver bringing in the highest percentage of the total votes at *82.8%*, Jefferson at *10.5%* followed by Arapahoe at a measly *6.7%*:

<p align="center">
<img src="/Resources/VotesPerCounty.png" width="60%" height="40%">
</p>

- The county of **Denver** had the largest turnout of voters
- Out of a total of 3 candidates, Charles Casper won *23%* of the total, Diana DeGette *73.8%* and Raymon Anthony Doane *3.1%*:

<p align="center">
<img src="/Resources/VotesPerCandidate.png" width="60%" height="40%">
</p>

- As a clear indication from the graph above, **Diana DeGette** won the election by a landslide, bagging **272,892** votes in total (*73.8%*)

## Election-Audit Summary

The script used for this audit is universal as it determines all values and factors while reading the data, therefore it can be easily used for analysing any such results. However the code can be polished a little more to:

1. | Objective | Modificaion | Example |
| --- | --- | --- |
| Simplify loading the file | Instead of using `os` to join the path, a separte variable can be declared that is equal to the the absolute location of the file. So in future the only change one will have to make is to change the location of the new file they want to auit | Doing so won't require the user to break up the location and add it to the parantheses in `os.path.join()` |
| git diff | Show file differences that haven't been staged |

In this report we only determine the turnout per county and the votes per candidate, however this script can be modified to achieve the following results as well:

2. **Votes cast per candidate from each county:** this can help determine how the population of a couty reacts to the candidate's manifestos, the winner from each county - as that might be different from the overall winner, etc. The most populated counties will have the power to sway the results to their favour, provided the turnout is proportional to the population.

    - To do so we will need to declare a new dictionary (which will have nested dictionaries in it). This new dictionary will have the following structure
    ```python
    votes_candidate_county = {
        'county1' : {'candidate1': votes1, 'candidate2': votes2, 'candidate3': votes3}
        'county2' : {'candidate1': votes2_1, 'candidate2': votes2_2, 'candidate3': votes2_3}
        'county3' : {'candidate1': votes3_1, 'candidate2': votes3_2, 'candidate3': votes3_3}
    }
    ```
    - Then, the following piece of code will do the work:

    ```python
    if county_name not in votes_county_candidate: 
            votes_county_candidate[county_name] ={}
        if candidate_name not in counties_result[county_name]:
            votes_county_candidate[county_name][candidate_name] = 1
        else:
            votes_county_candidate[county_name][candidate_name] += 1

    ```

### Modification Suggestions

| Objective | Modificaion |
| --- | --- |
| Votes cast per candidate from each county | List all new or modified files |
| git diff | Show file differences that haven't been staged |