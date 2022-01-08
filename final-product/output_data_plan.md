|     Visualisation                                                                    |     Graph                   |     Rows                                                                       |     Columns                                    |     Markers                                                    |     Sheet                    |     To do                                                                                                |
|--------------------------------------------------------------------------------------|-----------------------------|--------------------------------------------------------------------------------|------------------------------------------------|----------------------------------------------------------------|------------------------------|----------------------------------------------------------------------------------------------------------|
|     Change in gender differences of speech time across the years                     |     Stacked column graph    |     SUM (Number of syllables   spoken)                                         |     Year                                       |     Gender (colours)                                           |     Years                    |     Complete and on dashboard                                                                            |
|     Power in parliament represented by number of seats taken up   across sessions    |     Seat map                |     SUM (Ratio of % of speech   time to % of MSPs by parliamentary session)    |     Parliamentary session                      |     Gender (colour)                                            |     Parliamentary session    |     Data is set up à dummy viz is on dashboard     Alanah to build seat map   viz                        |
|     Relationship between speech time and age across years                            |     Scatter graph           |     SUM (Age)                                                                  |     SUM (Proportion of   syllables spoken)     |     Gender (colour)     Years (interactive filter)             |     Years?                   |     Collate age data à stuck on how best to do this                                                      |
|     Absolute gender differences in amount of speech overall                          |     Speech bubbles          |     SUM (Number of syllables spoken)                                           |                                                |     Gender (size)                                              |     Years                    |     Data is set up     Alanah to build speech   bubble viz                                               |
|     Proportions of time men and women speak overall                                  |     Pie chart               |                                                                                |                                                |     Gender (colour)     SUM (Number of syllables)   (angle)    |     Years                    |     Complete and on dashboard                                                                            |
|     Party comparison of women speech time across sessions                            |     Tree map                |     SUM (Proportion of speech   time)                                          |     Parliamentary session                      |     Party (label + colour)     Gender (interactive filter)     |     Parliamentary session    |     Retrieve party data     Add to parliamentary session   sheet     Build data viz                      |
|     Regional differences of speech time across years                                 |     Regional heat map       |     SUM (Proportion of speech   time)                                          |     Region                                     |     Gender (colour)     Years (interactive filter)             |     Years                    |     Complete and on dashboard    |


## Dimensions (discrete)
-	Parliamentary sessions
-	Year
-	Gender
-	Political party
        -	Dataset -> Parties: Current and previous roles held by Members
-	Region 
        -	Dataset -> MSPs: Regions elected to current and previous

## Measures (continuous)
-	Number of speeches
-	Proportion of speeches
-	Number of syllables spoken
-	Proportion of syllables spoken
-	Number of MSPs (who spoke)
-	% of MSPs
-	Ratio of % of total syllables to % of total MSPs
-	Age
        -	While it is discrete in that we’re rounding it to whole numbers, as we won’t have data on every age we should make it continuous to each year is still represented in the graphs if that makes sense? Instead of it going from 35 to 39 or something 
        -	Need to link WikiDataID to other data outputs
        -	Struggling with how this would be represented in a spreadsheet – how would we fill in data for ages not there
