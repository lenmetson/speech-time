#source(here("scripts", "r-analysis", "women_in_positions.R"))

positions_gender <- MSPs %>%
  select(gender, office_held, parly, parl_id) %>%
  filter(office_held != ".") %>%
  filter(office_held != "n/a") %>%
  filter(office_held != "N/A") %>%
  filter(!is.na(office_held))


#positions_gender %>% filter(parly=="1st") %>% nrow()
#positions_gender %>% filter(parly=="1st") %>% filter(gender == "M") %>% nrow()
#positions_gender %>% filter(parly=="1st") %>% filter(gender == "F") %>% nrow()

pos_m_1 <- positions_gender %>% filter(parly=="1st") %>% filter(gender == "M") %>% nrow()
pos_f_1 <- positions_gender %>% filter(parly=="1st") %>% filter(gender == "F") %>% nrow()
pos_p_1<- pos_f_1/(pos_f_1+pos_m_1)

pos_m_2 <- positions_gender %>% filter(parly=="2nd") %>% filter(gender == "M") %>% nrow()
pos_f_2 <- positions_gender %>% filter(parly=="2nd") %>% filter(gender == "F") %>% nrow()
pos_p_2<- pos_f_2/(pos_f_2+pos_m_2)

pos_m_3 <- positions_gender %>% filter(parly=="3rd") %>% filter(gender == "M") %>% nrow()
pos_f_3 <- positions_gender %>% filter(parly=="3rd") %>% filter(gender == "F") %>% nrow()
pos_p_3<- pos_f_3/(pos_f_3+pos_m_3)

pos_m_4 <- positions_gender %>% filter(parly=="4th") %>% filter(gender == "M") %>% nrow()
pos_f_4 <- positions_gender %>% filter(parly=="4th") %>% filter(gender == "F") %>% nrow()
pos_p_4<- pos_f_4/(pos_f_4+pos_m_4)

pos_m_5 <- positions_gender %>% filter(parly=="5th") %>% filter(gender == "M") %>% nrow()
pos_f_5 <- positions_gender %>% filter(parly=="5th") %>% filter(gender == "F") %>% nrow()
pos_p_5<- pos_f_1/(pos_f_5+pos_m_5)

parly <- c("1st", "2nd", "3rd", "4th", "5th")
total <- c(pos_f_1+pos_m_1, pos_f_2+pos_m_2, pos_f_3+pos_m_3, pos_f_4+pos_m_4, pos_f_5+pos_m_5)
M <- c(pos_m_1, pos_m_2, pos_m_3, pos_m_4, pos_m_5)
F <- c(pos_f_1, pos_f_2, pos_f_3, pos_f_4, pos_f_5)
perc_F <- c(pos_p_1, pos_p_2, pos_p_3, pos_p_4, pos_p_5)

prop_pos_f <- data.frame(parly, total, M, F, perc_F)

rm(pos_m_1, pos_m_2, pos_m_3, pos_m_4, pos_m_5,
  pos_f_1, pos_f_2, pos_f_3, pos_f_4, pos_f_5,
  pos_p_1, pos_p_2, pos_p_3, pos_p_4, pos_p_5,
  parly, total, M, F, perc_F)

pos_over_parly <- ggplot(prop_pos_f, aes(x=parly, y=F)) + geom_bar(stat="identity")
pos_over_parly
