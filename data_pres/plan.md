# Our plan

## Section 1: Workflow and data retrieval

* Workflow philosphy - reproducible research (LEN)
  * What: we want the entire project to be able to be run by any user on any machine, with no cost to themselves
  * Why reproducible
  * Show work-flow
  * Show GitHub and how we interact with it
    * External reasons;
      * Reproducibliy, transpatency
    * Internal reason;
      * Collaboration, version control, file backup

 * How we achieve that
   * Download from HTML (explain this) progromatically

 * Show work flow, GitHub set up
 * External reasons:
   *  Reproducibility, transparency
 * Internal reasons:
 * Collaboration, version control, backup


* How do we get the data?


## Section 2: Data processing, and summary stats

* How we cleaned the data

* What's going on?
  * MP descriptives
    * How many MPs
    * How many are women/men?
    * How many are regional/constituency?
  * Speech descriptives
    * How many speeches?
    * How many overall by women?
    * How many of each type?
    * Table: MP descriptive + no of speeches
    * How many years?
    * How many debates?


## Section 3: Where we're going with the data

* __Data analysis__
  * What tools we're using
    * R
      * Downloading the raw data
      * Counting sylablles
    * Python
      * Formatting the dataset
      * Scraping the Twitter API

* __Data visualiation (_AS to finish_)__
  * What we want to visualise
    * Change in gender differences of speech time over the years
      * Stacked column graph
      * Variables: gender (m/f, columns), speech time (%, y axis), years (x axis)
      * Interactive element: cursor moves across graph to show exact % each year, and any outstanding events (_what do we think of this?_)
    * Power in parliament represented by amount of seats taken up once gender differences in speech time is considered
      * Scottish parliamentary seat map
      * Variables: gender (m/f), speech time (%)
      * Interactive element: can click between actual number of seats and the speech-time-factored-in number of seats
    * Relationship between speech time and age
      * Scatter graph
      * Variables: gender (m/f), speech time (n)
      * Interactive element: can click between 'men' and 'women' graphs to compare the general shape/distribution of scatter
    * Absolute gender difference in amount of speech
      * 'Men'/'women' speech bubbles
      * Variables: gender (m/f), speech time (%)
    * Proportions of time men and women speak
      * Circle chart
      * Variables: gender (m/f), speech time (%)
    * Party comparison of women speech time
      * Stacked bar chart
      * Variables: gender (m/f, bars), MP political party (y axis), speech time (%, x axis)
    * Comparison of Twitter followers and speech time
      * Line graph
      * Variables: speech time (n, y axis), Twitter followers (n, x axis)
  * What tools we're using
    * Tableau Public
      * x


* __User interface (_Guys can you assist?_)__
  *
