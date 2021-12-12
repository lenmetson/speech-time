# DS105M Second Presentation Notes
Please find the accompanying notes for our presentation here.

## Introduction
This presentation will discuss the analysis of our data and the ideas we have for our final product.

Some information on our presentation:


## Part 1: Analysis

### Slide 1.1: Data wrangling

Problems with data:
* Asymmetric duplication in the speeches.
* Speeches doubled but order no. a running variable.
* This meant that we had to reshape the data so as to remove duplicated speeches

### Slide 1.2: Gender and speeches
#### 1.2.1 Gender and syllables
The `sylcounts` packages returns and estimate of the number of syllables in a vector of words. However, the output is a vector. For example, the output for the sentence `"I disagree with you"` would have the output `c(1, 3, 1, 1)`. However, we need an estimate the sum of syllables in a speech. I used the `lapply` function to sum the vectors for each speech.

*Include image*

#### 1.2.2 Gender and content

The basis of our analysis is that this question is important because women being able to speak in legislative settings means women will be more represented. This claim gets complex when we get into the political science of representation and especially representation based on group characteristics. Further, better specified analysis would be needed to test this assumption legitimately. However, just for illustration purposes we did a very basic dictionary content analysis to see if female MSPs did talk more about women.

This was done using string matching. First we cleaned the data by making it all lower case and removing punctuation marks. We then applied a string matching function using the library `stringr` which returned a numeric binary for whether a match was found:

```
gen_dict <- "woman*|women*|female*|femin*|sexism"
speeches$about_gen <-  as.integer(str_detect(speeches$speech, gen_dict))
```




### Slide 1.3: More variables: Wiki API



### Slide 1.4: Time

Summary  


## Part 2: Findings
### Slide 2.1
### Slide 2.2
### Slide 2.3 Gender and gender focus


                                                               ─────────────────────────
                                         (Intercept)                          0.05 ***  
                                                                             (0.00)     
                                         genderM                             -0.03 ***  
                                                                             (0.00)     
                                                               ─────────────────────────
                                         N                               390586         
                                         R2                                   0.01      
                                       ─────────────────────────────────────────────────
                                         *** p < 0.001; ** p < 0.01; * p < 0.05.        


### Slide 2.1: More detailed background
There have been six elections to the Scottish Parliament: 1999, 2003, 2007, 2011, 2016 and 2021. Thus there have only been 5 parliaments so far.

| Parliament              | Election Date | Dissolution Date |
|-------------------------|---------------|------------------|
| 1st Scottish Parliament | 12-05-1999    | 31-03-2003       |
| 2nd Scottish Parliament | 07-05-2003    | 02-04-2007       |
| 3rd Scottish Parliament | 14-05-2007    | 22-03-2011       |
| 4th Scottish Parliament | 11-05-2011    | 24-03-2016       |
| 5th Scottish Parliament | 12-05-2016    | 05-05-2021       |
| 6th Scottish Parliament | 13-05-2021    | NA               |



## Part 3: Final product ideas (AS)

### Slide 3.1:
