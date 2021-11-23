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

No matter what application we were using, we could commit changes either through the application (RStudio, Atom) or through the terminal from our local disk. For example, if Noemie changed something with the way the data is organised, those changes would come up when Len reran the code in our Markdown and Alanah's formatting would also show up. This meant that we could work effectively on different parts of the project simultaneously.

# Part 2: the data

## Slide 2.1: Obtaining the data

The raw data for our project is contained on a server managed by Harvard Dataverse. This is an online repository where people can store large datafiles. It is intended for academic purposes. Researchers often upload replication data or datasets for others to use.

We are using the dataset ParlScot. This data is publicly available for free. It consists of scrapped data from Scottish plenary debates. The data is relational and is stored as semi-structed data.

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



# Part 3: Summary statistics
The code we ran in for the Markdown is included here:

```
# Load file from disk (once downloaded)
harvard <- read.csv(here("data_raw", "rawdata.csv"))

# save only sppeches as an object
speeches <- subset(harvard, harvard$is_speech == 1)
```

Number of speeches: `nrow(speeches)`
Number of speeches by women: `nrow(subset(speeches, speeches$gender == "F"))`
Percentage of speeches by women `(nrow(subset(speeches, speeches$gender == "F"))/ nrow(speeches))*100

## Slide 3.1: Summary statistics on speeches



## Slide 3.2: Summary statistics on msps


# Part 4: Where next

## Slide 4.1: Data Wrangling

## Slide 4.2: Analysis

**Noemie**

## Slide 4.3: visualisations planned

**Alanah**
