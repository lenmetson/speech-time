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

syls_2 <- speeches_2 %>%
  group_by(parl_id) %>%
  summarise(syls = sum(syls))

syls_3 <- speeches_3 %>%
  group_by(parl_id) %>%
  summarise(syls = sum(syls))

syls_4 <- speeches_4 %>%
  group_by(parl_id) %>%
  summarise(syls = sum(syls))

syls_5 <- speeches_5 %>%
  group_by(parl_id) %>%
  summarise(syls = sum(syls))

syls_all <- rbind(syls_1, syls_2, syls_3, syls_4, syls_5)
