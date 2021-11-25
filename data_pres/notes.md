# DS105M Presentation Notes

Please find accompanying notes for our presentation here.

## Introduction

This presentation will outline how we are managing our data, some early summary statistics of our data and finally an indication of the next steps for our project.

Some information on our presentation:

* Our presentation is coded in the R Markdown language (.Rmd). You can find the raw code in this repository under the `slides` folder. The file is called `rmdslides.Rmd`. When compiled in RStudio, the file converts the markdown language we have imputed into an HTML file (which you can find in the same folder). This HTML file is what we will view.

* The advantage of this approach is that it allows us to run code live in the markdown which updates each time it is compiled. Any of the summary statistics are code rather than text. This means that if one person makes a change to the data, the related slide does not have to be rewritten.

* If you want to run the presentation on your own machine consult the `README.md` file for the overall repository.

# Part 1: Summary and workflow

## Slide 1.1: Brief summary

Our project is aiming to visualise gender biases in Scottish Parliamentary debates. We know from other contexts that women generally tend to contribute less in professional and legislative settings because of gender discrimination in these environments. Our project aims to quantify and visualise this so as to inform people of the problem.

## Slide 1.2: Organisation

We thought carefully about how to organise our project. Our guiding principle is reproducibility. This is because we want to be fully transparent in our procedures and furthermore we want to make everything we do open-source so that others can improve it in the future. This also has the advantage of others being able to view and check our code so that if there are mistakes, they can be more easily flagged.

We define reproducibility as any user on any machine being able to run our full project using only the materials contained in our GitHub repository. There should be no financial cost to them and they should be able to edit and create their own project without restriction.

Because of this, we needed to make sure that everything we do to the data is programmatically done. For example, we use the HTTPS protocol to download our data in code rather than asking each user to download a copy manually. Furthermore all of our data wrangling is done programmatically so that anyone can get the same results as us simply by running our code.  

## Slide 1.3: Workflow

One challenge in obtaining our data is that we had divided tasks and each of us were using different tools to complete them. This included Atom, Spyder, CSS, RStudio. Therefore, we decided that GitHub would be the best way to ensure that we could all access the latest versions of what others were working on.

No matter what application we were using, we could commit changes either through the application (RStudio, Atom) or through the terminal from our local disk. For example, if Noemie changed something with the way the data is organised, those changes would come up when Len reran the code in our Markdown and Alanah's formatting would also show up.  This meant that we could work effectively on different parts of the project simultaneously.

# Part 2: the data

## Slide 2.1: Obtaining the data

The raw data for our project is contained on a server managed by Harvard Dataverse. This is an online repository where people can store large datafiles. It is intended for academic purposes. Researchers often upload replication data or datasets for others to use.

We are using the dataset ParlScot. This data is publicly available for free. It consists of scrapped data from Scottish plenary debates. The data is relational and is stored as semi-structured data.

Each row is a single entry in Hansard. The columns represent various meta-data about the speeches such as: the MSP who said it and various information about that MP.

We downloaded the data using the HTTP protocol. The code for this is shown below. It is written in R. The code will work on any machine so long as that machine has cloned our whole repository. Opening `speech-time.Rproj` will launch RStudio with the correct root directory specified. The `here()` function specifies relative paths so it will read files relative to your root directory.

```
install.packages(here)
library(here)
# specify the url
url <- "https://dataverse.harvard.edu/api/access/datafile/4432885"

# download the file into a specified path - add your analysis folder in between " "
download.file(url, here("data_raw", "rawdata.csv"))

```

This will add the raw data to the data_raw directory you can see on the GitHub. However the `.gitignore` file ensured that we didn't push the raw csv into GitHub from our local disks.


## Part 2.2: Summary statistics
The code we ran in for the Markdown is included here:

```
# Load file from disk (once downloaded)
harvard <- read.csv(here("data_raw", "rawdata.csv"))

# save only sppeches as an object
speeches <- subset(harvard, harvard$is_speech == 1)
```

We also ran some code in python locally (on disk) in parallel to cross check-results. This, among other things, allowed us to realize that we had been using different datasets, and to flag certain inconvenient n/a values in the dataset and drop them to facilitate analysis. The code that follows was first written and executed as it appears to have faster access to the statistics, and later rewritten in python. The switch has been principally motivated by the flexibility that python code offers. In effect, the possibility to define and modulate functions allowed us to obtain summary statistics on any variable present in the dataset and perform some elementary analytics faster. In essence, the marginal cost of using python once some  ad-hoc functions are defined is much lower than for using R. An important note is that this does not affect the reproducibility of the analysis on other machines as the python code can be directly read within R-studio, given the right packages are installed.


## Slide 2.3: Summary statistics on speeches

Number of speeches: `nrow(speeches)`

Number of speeches by women: `nrow(subset(speeches, speeches$gender == "F"))`

Percentage of speeches by women `(nrow(subset(speeches, speeches$gender == "F"))/ nrow(speeches))*100`


## Slide 2.4: Summary statistics on MSPs

We then create a dataframe of MSPs. When the dataset was compiled, the relational table for gender only has values for MSPs. So by dropping all rows of MSPs with no gender, we keep only MSPs

```
# select name and gender variables from speeches
msps <- speeches %>% select(name, gender)

# retain only unique values (because each MSPs' name is repeated in each speech)
msps <- unique(msps)

# non-MSPs have no gender associated so drop all rows with NA in gender
msps <- drop_na(msps)
```

Number of MSPs in our data: `nrow(msps)`

Number of women MSPs in our data: `nrow(subset(msps, msps$gender == "F"))`

Propotion of women MSPs in our data: `(nrow(subset(msps, msps$gender == "F"))/ nrow(msps))*100`

# Part 4: Where next

## Slide 4.1: Data Wrangling

The first step in the analysis is cleaning the data. In the early steps executed so far, we have subsetted the semi-structured dataset obtained as to only keep information on proper speeches, while discarding any formalities and introductory speeches that have procedural relevance but would not inform our analysis. 

The second step involved stripping the data of missing values and ensuring overall accuracy within the data. Initially, the count for the total number of speeches by women corresponded around 10% of total speeches. When checked against statistics available online, this seemed too exacerbated of a discrepency. This led us to double check the way we counted women MSPs and realized that many of the people we had identified were either "", and their inclusion in the calculus inflated the denominator and artificially reduced the proportion of speeches delivered by women MSPs. So we excluded these people from the data.

The third step is to partition this dataframe and, using csv libraries, export them as CSVs to the repository. The aim is to obtain structured, relational data that can easlily be appended in R (for example, once we have a dataframe with one column "name" and another "speech", we can append a column with "number of syllables"). In another dataframe with column "name" and "msp_type", we can see if any discrpency of the number of syllables in the speech seems to correlate with gender or with the type of MSP speeking. This can also allow us to source MSPs' twitter ID from their wikipedia pages using the wikiid variable present in the dataset, save this as a dataframe, and use SQL to extract the degree of social media activity by MSP.

The main data source for analysis is now ready to be used. We can now use some partitions of this dataframe to count the number of syllables spoken by MSPs and compare the obtained values between men and women.



## Slide 4.2: Analysis

As we already know how to operationalize pre-existing libraries for syllable count, here are some insights we would like to draw from the data:
- average and median number of syllables by gender
- whether this discrepency also exists on twitter
- perform some sentiment analysis on speeches to see if a gender-related lexic is found at a higher rate in women's speeches than in men's speeches.

## Slide 4.3: Visualisations planned

Our process thus far has been continually informed by our plans for the final product: various data visualisations of the gender differences in Scottish parliamentary contributions. We've done this by not only by ensuring that we're able to obtain the relevant data and insights for our product, but also by cross-checking that our data format is suitable for the program we are planning to use for the data visualiations (namely, Tableau Public).

| What we're planning to visualise                                                                                   | Graph                           | Variables                                                      |
|-------------------------------------------------------------------------------------------------------------------|---------------------------------|----------------------------------------------------------------|
| Change in gender differences of speech time over the years                                                        | Stacked column graph            | gender (m/f, columns), speech time (%, y axis), years (x axis) |
| Power in parliament represented by amount of seats taken up once gender differences in speech time are considered | Scottish parliamentary seat map | gender (m/f), speech time (%)                                  |
| Relationship between speech time and age                                                                          | Scatter graph                   | gender (m/f), speech time (n)                                  |
| Absolute gender differences in amount of speech                                                                   | Speech bubbles                  | gender (m/f), speech time (%)                                  |
| Proportions of time men and women speak                                                                           | Circle chart                    | gender (m/f), speech time (%)                                  |
| Party comparison of women speech time                                                                             | Stacked bar chart               | gender (m/f, bars), MP political party (y axis),               |
| Comparison of Twitter activity and speech time                                                                    | Line graph                      | speech time (n, y axis), Twitter followers (n, x axis)         |

Tableau Public is a free platform that can connect to data in a variety of formats like Excel, CSV, and JSON, as well as being able to connect to a server. We've chosen Tableau as a data visualisation tool as it can take in data and produce the required data visualisation output in a short time. We are planning on using a CSV Web Data Connector to connect Tableau directly to the CSV in our GitHub repository. This means that any changes in the data should automatically update the visualisations.
