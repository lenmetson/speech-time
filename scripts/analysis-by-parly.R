# this script splits up the scripts into different parliaments
#source(here("scripts", "add-parliaments.R"))
# Create varibales for First Parly
speeches_1 <- left_join(speeches_1, gender, by = "parl_id") %>% unique()

n_speeches1 <- nrow(speeches_1)

n_speeches_f1 <- speeches_1 %>%
  subset(speeches_1$gender == "F") %>%
  nrow()

n_speeches_m1 <- speeches_1 %>%
  subset(speeches_1$gender == "M") %>%
  nrow()

prop_speeches_f1 <- n_speeches_f1/n_speeches1

prop_speeches_m1 <- n_speeches_m1/n_speeches1

prop_speeches_m1 + prop_speeches_f1 # check == 1

# Create varibales for Second Parly
speeches_2 <- left_join(speeches_2, gender, by = "parl_id") %>% unique()
n_speeches2 <- nrow(speeches_2)
n_speeches_f2 <- speeches_2 %>%
  subset(speeches_2$gender == "F") %>%
  nrow()
n_speeches_m2 <- speeches_2 %>%
  subset(speeches_2$gender == "M") %>%
  nrow()
prop_speeches_f2 <- n_speeches_f2/n_speeches2
prop_speeches_m2 <- n_speeches_m2/n_speeches2
prop_speeches_m2 + prop_speeches_f2 # check == 1

# 3rd Parly
speeches_3 <- left_join(speeches_3, gender, by = "parl_id") %>% unique()
n_speeches3 <- nrow(speeches_3)
n_speeches_f3 <- speeches_3 %>%
  subset(speeches_3$gender == "F") %>%
  nrow()
n_speeches_m3 <- speeches_3 %>%
  subset(speeches_3$gender == "M") %>%
  nrow()
prop_speeches_f3 <- n_speeches_f3/n_speeches3
prop_speeches_m3 <- n_speeches_m3/n_speeches3
prop_speeches_m3 + prop_speeches_f3 # check == 1

# 4th Parly
speeches_4 <- left_join(speeches_4, gender, by = "parl_id") %>% unique()
n_speeches4 <- nrow(speeches_4)

n_speeches_f4 <- speeches_4 %>%
  subset(speeches_4$gender == "F") %>%
  nrow()

n_speeches_m4 <- speeches_4 %>%
  subset(speeches_4$gender == "M") %>%
  nrow()

prop_speeches_f4 <- n_speeches_f4/n_speeches4

prop_speeches_m4 <- n_speeches_m4/n_speeches4

prop_speeches_m4 + prop_speeches_f4 # check == 1

# 5th Parly
speeches_5 <- left_join(speeches_5, gender, by = "parl_id") %>% unique()
n_speeches5 <- nrow(speeches_5)

n_speeches_f5 <- speeches_5 %>%
  subset(speeches_5$gender == "F") %>%
  nrow()

n_speeches_m5 <- speeches_5 %>%
  subset(speeches_5$gender == "M") %>%
  nrow()

prop_speeches_f5 <- n_speeches_f5/n_speeches5

prop_speeches_m5 <- n_speeches_m5/n_speeches5

prop_speeches_m5 + prop_speeches_f5 # check == 1
