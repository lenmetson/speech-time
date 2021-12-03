# Analysis replication in R

# Load packages
if(!require("here"))install.packages("here")
source(here("scripts", "r-packages"))

# Load data

harvard <- read.csv(here("data_raw", "rawdata.csv"))

speeches <- harvard %>% filter(is_speech == 1)
speeches <- speeches %>% filter(gender == "M" | "F")
# reconfigure to drop all without parl_id ?

speeches
