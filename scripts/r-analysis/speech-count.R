# Speech count by MSP

sp_1 <- speeches_1 %>%
  group_by(parl_id) %>%
  summarise(speeches = nrow())
syls_1$parly <- "1st"

syls_2 <- speeches_2 %>%
  group_by(parl_id) %>%
  summarise(syls = sum(syls))
syls_2$parly <- "2nd"

syls_3 <- speeches_3 %>%
  group_by(parl_id) %>%
  summarise(syls = sum(syls))
syls_3$parly <- "3rd"

syls_4 <- speeches_4 %>%
  group_by(parl_id) %>%
  summarise(syls = sum(syls))
syls_4$parly <- "4th"

syls_5 <- speeches_5 %>%
  group_by(parl_id) %>%
  summarise(syls = sum(syls))
syls_5$parly <- "5th"
