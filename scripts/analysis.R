#
if(!require("here"))install.packages("here")
# We need to source our summary data
#source(here("scripts", "download-csv-http.R"))# If you haven't downloaded the data yet, uncomment this line
# Next source the script that creates the summary data
#source(here("scripts", "prelim-analysis-r-rep.R")) # takes quite a long time to run
# If you have already run, comment out and load summary data directly

data <- read.csv(here("output_data", "summary.csv"))

source(here("scripts", "counts_script.R"))

# Task 
## Add gender and names 
# re-run all