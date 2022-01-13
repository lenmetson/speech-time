# Guidance
* **Executive summary** focusing a very brief outline of:
    1. Motivation
    2. Data
    3. Brief outlook of methods
    4. Results
    5. Conclusions
* **Motivation** for your project; i.e., why were you interested in the topic chosen?
* **Justification**: why is your project relevant?
* **Aim**. Be sure of making crystal clear what was your aim with the data analyses.
* **Data**: What data sources did you use? Be sure of being presenting a thorough description of data sources. (not only include URLs but a line or two on what is the data source). How many data points did you gather? Descriptive statistics of your data.
* **Methodology**: How did you analysed the data? What tools did you use?
* **Results**: What are the findings of your analysis?
* **Conclusion**
* **Appendix**: Include in your GitHub page a section with reference to any code you use and data used (if possible).

-----
# Are women underrepresented in Scottish Politics?


## Motivation for our project
We wanted to use the data science tools we have learned about to quantify the extent to which women are represented in Parliamentary politics. The case we looked at was the Scottish Parliament.

There are three aspects to representation that we explored:
1. Whether women have a proportional amount of MSPs
1. Whether women in parliament have equal time to speak
1. Whether women in parliament use their position to represent women's issues

## Justification for our project

* Fourth-wave feminism's advocation for greater representation of women - including traditionally marginalised groups such as women of colour and trans women - in politics is premised on the notion that society would be more equitable if policies incorporate perspectives of all people
* Inspired by this argument for the equitable representation of gendered perspectives in political settings, we were interested in exploring women's representation in Scottish parliament across time to see the progress Scotland has made in not only including more women in parliamentary debates, but by including more contributions by women to the debates themselves
* Contextualising our data:
  * ["Scottish election 2021: Record number of women elected" - BBC](https://www.bbc.co.uk/news/uk-scotland-scotland-politics-57047370)  
  * ["The Scottish Parliament’s record on women’s representation is in the balance" - Democratic Audit](http://eprints.lse.ac.uk/54565/1/Meryl%20Kenny%20democraticaudit.com-The_Scottish_Parliaments_record_on_womens.pdf)
  * ["Backwards for gender equality in the new Scottish parliament? Or a new Scottish velvet triangle?" - Center for Constitutional Change](https://www.centreonconstitutionalchange.ac.uk/opinions/backwards-gender-equality-new-scottish-parliament-or-new-scottish-velvet-triangle)

## Aim
We had three aims:
1. Use parliamentary transcripts to quantify how much women and men speak and relate our findings to patterns in other demographic variables such as age and region.
1. Run a content analysis to see whether gender correlates with whether MSPs talk about womens' issues.
1. Visualise the data we find to tell a story about women's representation in the Scottish Parliament


## Data
We used a pre-scraped dataset of speeches by Scottish Members of Parliament (MSPs). The data has entries from the opening of the Scottish Parliament so we were able to analyse all speeches made in the Scottish Parliament.

[Link to Harvard Dataverse Page](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/EQ9WBE)

The relevant dataset was downloaded by HTTP request using an R wrapper.

```
# specify the url
url <- "https://dataverse.harvard.edu/api/access/datafile/4432885"

# download the file into a specified path - add your analysis folder in between " "
download.file(url, here("data_raw", "rawdata.csv"))
```

### Descriptive statistics on Raw Data


|          | Total   | Female  | % Female |
|----------|---------|---------|----------|
| Speeches | 430,577 | 125,078 | 29.05%   |
| MSPs     | 306     | 105     | 34.31%   |


Additional data on age was aquired from WikiData. Using python, code was written to connect to WikiData's API and pull each MSPs birthdate.


## Methodology

We made some key assumptions that had to be checked. Whilst the aim of our project was not to make inferential conclusions, it is important to discuss potential limitations in our data.

Why syllables:
* The assumption is that the more syllables a speech is, the more time it takes to say.
* Having time on the floor of parliament is a precious resource for politicians. They use it to signal to voters, bring policies forward and influence legislation.  
* We used it instead of raw number of speeches because syllables take into account how much time is given and we assumed that many short speeches are less impactful than an MSP given space to make long speeches. Length of speech is also defined by an MSP's with importance to a piece of legislation or debate, so MSPs who give longer speeches are the most influential. Therefore, we choose it as a more senstitive proxy for measuring influence.
* We did however, replicate all analysis using number of speeches and found similar results.  

* Ministers and Sturgeon:
  * Ministers are likely to have more fixed opportunities to speak in Parliament. For example, they are required to make speeches in answer to speeches.
  * The election of Nicola Sturgeon, a woman, as First Minister meant that she was speaking for a very significant amount of time. In the most recent parliamentary session, Sturgeon accounted for almost 10% of all speeches.
  * We ran the analysis with no ministers and found there was no upward trend in the amount that women spoke. Therefore, the improving picture we saw is most likely due to women entering more ministerial positions.


Steps:

1. Data collection and cleaning
  * We collected data from the [Harvard Dataverse](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/EQ9WBE). The dataset has been scraped from HTML files containing transcripts of parliamentary speech published on the Scottish Parliament Website.
1. Syllable analysis
  * Our main analysis was how much time women spoke in the Scottish Parliament.
  * We decided to explore using syllable count instead of number of speeches because we thought it relevant the *time* that women get to speak. Ultimately the results were similar but it was good to establish syllables as a way of measuring speech time.
1. Content analysis
  * As well as analysing how much women speak, we wanted to look at what men and women talk *about*.
  * We created a dictionary with words associated with women's rights issues, and related to reproductive/sexual rights. We assigned weights to each token using our team's field knowledge of the issue.
  * One assumption in our analysis is that speeches that contain words directly related to gender issues such as "women", "men", "girls", "sexual" as well as words that, alone, would be correlated to other issues such as "stereotype", "pay", and "violence" should be categorized as "highly correlated to womens' rights".
  * To include this in our analysis, we based our algorithm on the NLP workshop given in DS105, and included an "if then" look to increase the score if more than one word from the dictionary is included in the speech.
  * The resulting speech scores, which are essentially weighted averages of dictionary words that are in the speeches, adjusted for the increased correlation from the presence of multiple words, are stored in the original data frame as an additional series.

1. Visualisation
    * We used Tableau to visualise the data once we had them all in CSV form, to eventually build the final product as a narrative of how women's representation in Scottish parliament has evolved throughout time
    * This also involved adjusting certain CSVs on the local machine for certain visual results; this was done intentionally to produce quicker results in data structure, which worked with the fact that the connections made from Tableau were also public. These CSVs are uploaded to the `output_data` folder
    * Here, we used worksheets for each visualisation, dashboards for the summary dashboard and each page of the story, and then finally the story feature as the final product, where we collated everything built to construct the narrative of the project, ultimately forming our final product


## Results
* We found some interesting descriptive results about the role of women in Scottish Parliamentary proceedings.
* Looking at the number of seats taken up, the average number of seats taken up by men across all parliaments are 86, whereas this number I only 48 for women. Furthermore, there has been little variation on both sides of these means, suggesting little progress in getting more women taking up seats.
* Initially, female MSPs spoke disproportionally less than there were women in the Scottish Parliament. However, over time, this rose so that women were speaking roughly as much as there were women in Parliament (i.e., the ratio of speech by women to amount of women taking up seats has increased towards 1:1). This being said, much of this trend has been driven by Nicola Sturgeon becoming First Minister.
* We also found there to be an upwards trend for the amount of speech by both genders which had mentions of women’s issues in it. This growth has been steadily increasing since 2012,  suggesting that for the past decade, there have been important and sustaining shifts in the structure of Scottish Politics that have driven conversation around women’s issues. With that being said, women have been the significant drivers of this change. For example, in 2019, when conversation around women’s issues were at its peak, the proportion of this conversation by women were 64%, opposed to just 36% of men speaking about women’s issues.


## Conclusion

## Appendix
1. [Harvard Dataverse](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/EQ9WBE)
2. [Data.parliament.scot](https://data.parliament.scot/#/home)
3. [Parliamentary Seat Map Maker](https://parliamentdiagram.toolforge.org/parlitest.php)
4. [Tableau Public final product](https://public.tableau.com/app/profile/alanah7895/viz/DS105/DS105STORY?publish=yes)
