# Analysis replication in R

# Load packages
if(!require("here"))install.packages("here")
source(here("scripts", "r-packages.R"))

# Load data
harvard <- read.csv(here("data_raw", "rawdata.csv"))

speeches <- harvard %>% filter(is_speech == 1)
rm(harvard)
speeches <- speeches %>% filter(!is.na(parl_id)) # drop all without parl_id

# explore different types of speeches
#types <- data.frame(unique(speeches$item))

# define counts of speeches
n_speeches <- nrow(speeches)
n_speeches_f <- speeches %>%
  subset(speeches$gender == "F") %>%
  nrow()
n_speeches_m <- speeches %>%
  subset(speeches$gender == "M") %>%
  nrow()

prop_speeches_f <- n_speeches_f/n_speeches
prop_speeches_m <- n_speeches_m/n_speeches

prop_speeches_m + prop_speeches_f

MSPs_all <- speeches %>%
  select(parl_id, name, gender, wikidataid) %>%
  unique()
