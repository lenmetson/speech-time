# This script counts syllables 

speeches_1$syls <- sylcount(speeches_1$speech) 
speeches_1$syls <- sapply(speeches_1$syls, sum)  

speeches_2$syls <- sylcount(speeches_2$speech) 
speeches_2$syls <- sapply(speeches_2$syls, sum)  

speeches_3$syls <- sylcount(speeches_3$speech) 
speeches_3$syls <- sapply(speeches_3$syls, sum) 

speeches_4$syls <- sylcount(speeches_4$speech) 
speeches_4$syls <- sapply(speeches_4$syls, sum)  

speeches_5$syls <- sylcount(speeches_5$speech) 
speeches_5$syls <- sapply(speeches_5$syls, sum)

speeches_syl <- rbind(speeches_1, speeches_2, speeches_3, speeches_4, speeches_5)



syls_1 <- speeches_1 %>%
  group_by(parl_id) %>%
  summarise(syls = sum(syls))
syls_1$parly <- "1st"
syls_1 <- left_join(syls_1, gender_1, by = "parl_id") %>% unique()

syls_2 <- speeches_2 %>%
  group_by(parl_id) %>%
  summarise(syls = sum(syls))
syls_2$parly <- "2nd"
syls_2 <- left_join(syls_2, gender_2, by = "parl_id") %>% unique()

syls_3 <- speeches_3 %>%
  group_by(parl_id) %>%
  summarise(syls = sum(syls))
syls_3$parly <- "3rd"
syls_3 <- left_join(syls_3, gender_3, by = "parl_id") %>% unique()

syls_4 <- speeches_4 %>%
  group_by(parl_id) %>%
  summarise(syls = sum(syls))
syls_4$parly <- "4th"
syls_4 <- left_join(syls_4, gender_4, by = "parl_id") %>% unique()

syls_5 <- speeches_5 %>%
  group_by(parl_id) %>%
  summarise(syls = sum(syls))
syls_5$parly <- "5th"
syls_5 <- left_join(syls_5, gender_5, by = "parl_id") %>% unique()

