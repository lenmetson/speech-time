| What we're wanting to visualise                                                                                   | Graph                           | Variables                                                      |
|-------------------------------------------------------------------------------------------------------------------|---------------------------------|----------------------------------------------------------------|
| Change in gender differences of speech time over the years                                                        | Stacked column graph            | gender (m/f, columns), speech time (%, y axis), years (x axis) |
| Power in parliament represented by amount of seats taken up once gender differences in speech time are considered | Scottish parliamentary seat map | gender (m/f), speech time (%)                                  |
| Relationship between speech time and age                                                                          | Scatter graph                   | gender (m/f), speech time (n)                                  |
| Absolute gender differences in amount of speech                                                                   | Speech bubbles                  | gender (m/f), speech time (%)                                  |
| Proportions of time men and women speak                                                                           | Circle chart                    | gender (m/f), speech time (%)                                  |
| Party comparison of women speech time                                                                             | Stacked bar chart               | gender (m/f, bars), MP political party (y axis),               |
| Comparison of Twitter activity and speech time                                                                    | Line graph                      | speech time (n, y axis), Twitter followers (n, x axis)         |


# Notes
Will have two sheets distinct through how they separate time:
1.	Parliamentary sessions
a.	Dividing data by political lines
b.	Used for visualisations that have political elements to them  seat map, party comparison
2.	Years
a.	Dividing data by linear annual lines
b.	Used for visualisations that show either a) changes over time or b) general relationships across all years of parliament (can average/sum across all years)

## Dimensions (discrete)
-	Parliamentary sessions
-	Year
-	Gender
-	Political party
o	Dataset -> Parties: Current and previous roles held by Members
-	Region 
o	Dataset -> MSPs: Regions elected to current and previous

## Measures (continuous)
-	Number of speeches
-	Proportion of speeches
-	Number of syllables spoken
-	Proportion of syllables spoken
-	Number of MSPs (who spoke)
-	% of MSPs
-	Ratio of % of total syllables to % of total MSPs
-	Age
o	While it is discrete in that we’re rounding it to whole numbers, as we won’t have data on every age we should make it continuous to each year is still represented in the graphs if that makes sense? Instead of it going from 35 to 39 or something 
o	Need to link WikiDataID to other data outputs
o	Struggling with how this would be represented in a spreadsheet – how would we fill in data for ages not there
