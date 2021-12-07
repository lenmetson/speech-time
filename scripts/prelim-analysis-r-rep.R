# Analysis replication in R

# Load packages
if(!require("here"))install.packages("here")
source(here("scripts", "r-packages.R"))

# Load data
harvard <- read.csv(here("data_raw", "rawdata.csv"))

speeches <- harvard %>% filter(is_speech == 1)
rm(harvard)
speeches <- speeches %>% filter(!is.na(parl_id)) # drop all without parl_id


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

# By parliament

source(here("scripts", "analysis-by-parly.R"))


# n_m | n_f | p_m | p_f
n_m <- c(n_speeches_m1, n_speeches_m2, n_speeches_m3, n_speeches_m4, n_speeches_m5)
n_f <- c(n_speeches_f1, n_speeches_f2, n_speeches_f3, n_speeches_f4, n_speeches_f5)
p_m <- c(prop_speeches_m1, prop_speeches_m2, prop_speeches_m3, prop_speeches_m4, prop_speeches_m5) 
p_f <- c(prop_speeches_f1, prop_speeches_f2, prop_speeches_f3, prop_speeches_f4, prop_speeches_f5)

summary <- data.frame(n_m, n_f, p_m, p_f)


# explore different types of speeches
types <- data.frame(unique(speeches$item))
