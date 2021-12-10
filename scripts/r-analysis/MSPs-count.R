# MSPs per parly

gender_1 <- MSPs_1 %>% select(parl_id, gender) %>% unique()

gender_2 <- MSPs_2 %>% select(parl_id, gender) %>% unique()

gender_3 <- MSPs_3 %>% select(parl_id, gender) %>% unique()

gender_4 <- MSPs_4 %>% select(parl_id, gender) %>% unique()

gender_5 <- MSPs_5 %>% select(parl_id, gender) %>% unique()

# Total

n_msp1 <- nrow(gender_1)
n_msp2 <- nrow(gender_2)
n_msp3 <- nrow(gender_3)
n_msp4 <- nrow(gender_4)
n_msp5 <- nrow(gender_5)

nf1  <- gender_1 %>%
  subset(gender_1$gender == "F") %>%
  nrow()
nf2 <- gender_2 %>%
  subset(gender_2$gender == "F") %>%
  nrow()
nf3 <- gender_3 %>%
  subset(gender_3$gender == "F") %>%
  nrow()
nf4 <- gender_4 %>%
  subset(gender_4$gender == "F") %>%
  nrow()
nf5 <- gender_5 %>%
  subset(gender_5$gender == "F") %>%
  nrow()

pf1 <- nf1/n_msp1
pf2 <- nf2/n_msp2
pf3 <- nf3/n_msp3
pf4 <- nf4/n_msp4
pf5 <- nf5/n_msp5

nm1 <- gender_1 %>%
  subset(gender_1$gender == "M") %>%
  nrow()
nm2 <- gender_2 %>%
  subset(gender_2$gender == "M") %>%
  nrow()
nm3 <- gender_3 %>%
  subset(gender_3$gender == "M") %>%
  nrow()
nm4 <- gender_4 %>%
  subset(gender_4$gender == "M") %>%
  nrow()
nm5 <- gender_5 %>%
  subset(gender_5$gender == "M") %>%
  nrow()

pm1 <- nm1/n_msp1
pm2 <- nm2/n_msp2
pm3 <- nm3/n_msp3
pm4 <- nm4/n_msp4
pm5 <- nm5/n_msp5
