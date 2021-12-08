# Analysis replication in R

# Load packages
if(!require("here"))install.packages("here")
source(here("scripts", "r-packages.R"))

# Load data
harvard <- read.csv(here("data_raw", "rawdata.csv"))
speeches <- harvard %>% filter(is_speech == 1)
rm(harvard)
speeches <- speeches %>% filter(!is.na(parl_id)) # drop all without parl_id

# Split into parliaments
source(here("scripts", "add-parliaments.R"))

MSPs_agg <- unique(MSPs_agg)

gender <- MSPs_agg %>% select(parl_id, gender)

speeches <- left_join(speeches, gender, by = "parl_id") %>% unique()


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


# By parliament

source(here("scripts", "analysis-by-parly.R"))
source(here("scripts", "MSPs-per-parly.R"))

# Make results table

# n_m | n_f | p_m | p_f | n_msps_m | n_msps_f | p_msps_m | p_msps_f | n_total
n_m <- c(n_speeches_m1, n_speeches_m2, n_speeches_m3, n_speeches_m4, n_speeches_m5, ((n_speeches_m1 + n_speeches_m2 + n_speeches_m3 + n_speeches_m4 + n_speeches_m5)/5))
n_f <- c(n_speeches_f1, n_speeches_f2, n_speeches_f3, n_speeches_f4, n_speeches_f5, ((n_speeches_f1 + n_speeches_f2 + n_speeches_f3 + n_speeches_f4 + n_speeches_f5)/5))
p_m <- c(prop_speeches_m1, prop_speeches_m2, prop_speeches_m3, prop_speeches_m4, prop_speeches_m5, ((prop_speeches_m1 + prop_speeches_m2 + prop_speeches_m3 + prop_speeches_m4 + prop_speeches_m5)/5))
p_f <- c(prop_speeches_f1, prop_speeches_f2, prop_speeches_f3, prop_speeches_f4, prop_speeches_f5, ((prop_speeches_f1 + prop_speeches_f2 + prop_speeches_f3 + prop_speeches_f4 + prop_speeches_f5)/5))
n_msps_m <- c(nm1, nm2, nm3, nm4, nm5, ((nm1+nm2+nm3+nm4+nm5)/5))
n_msps_f <- c(nf1, nf2, nf3, nf4, nf5, ((nf1+nf2+nf3+nf4+nf5)/5))
n_total <- c(n_msp1, n_msp2, n_msp3, n_msp4, n_msp5, ((n_msp1 + n_msp2 + n_msp3 + n_msp4 + n_msp5)/5))
p_msps_m <- c(pm1, pm2, pm3, pm4, pm5, ((pm1+pm2+pm3+pm4+pm5)/5))
p_msps_f <- c(pf1, pf2, pf3, pf4, pf5, ((pf1+pf2+pf3+pf4+pf5)/5))



summary <- data.frame(n_m, n_f, p_m, p_f, n_msps_m, n_msps_f, n_total, p_msps_m, p_msps_f)

rownames(summary) <- c("First Parliament", "Second Parliament", "Third Parliament", "Fourth Parliament", "Fifth Parliament", "Mean")

colnames(summary) <- c("Number speeches by men", "Number of speeches by women", "Proportion of speeches by men", "Proportion of speeches by women", "Number of men", "Number of women", "Number of MSPs", "% MSPs who are men", "% MSPs who are women")

write.csv(summary, here("output_data", "summary.csv"))


# MSPs



# explore different types of speeches
#types <- data.frame(unique(speeches$item))
