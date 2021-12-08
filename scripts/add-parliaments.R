# add in session names

years <- read.csv(here("data_raw", "years.csv"))

years$Election.Date <- as.Date(years$Election.Date, format = "%d-%m-%Y")
years$Dissolution.Date <- as.Date(years$Dissolution.Date, format = "%d-%m-%Y")

speeches$date <- as.Date(speeches$date, format = "%Y-%m-%d")


# add code to add a varible called Parliament_name

speeches$parly <- ifelse(speeches$date >= years[1,2] & speeches$date <= years[1,3], "First Scottish Parliament",
                       ifelse(speeches$date >= years[2,2] & speeches$date <= years[2,3], "Second Scottish Parliament",
                       ifelse(speeches$date >= years[3,2] & speeches$date <= years[3,3], "Third Scottish Parliament",
                       ifelse(speeches$date >= years[4,2] & speeches$date <= years[4,3], "Fourth Scottish Parliament",
                       ifelse(speeches$date >= years[5,2] & speeches$date <= years[5,3], "Fifth Scottish Parliament",
                       ifelse(speeches$date >= years[6,2], "Sixth Scottish Parliament",
                       NA))))))

# Split into years

speeches_1 <- speeches %>% subset(speeches$parly == "First Scottish Parliament")
speeches_2 <- speeches %>% subset(speeches$parly == "Second Scottish Parliament")
speeches_3 <- speeches %>% subset(speeches$parly == "Third Scottish Parliament")
speeches_4 <- speeches %>% subset(speeches$parly == "Fourth Scottish Parliament")
speeches_5 <- speeches %>% subset(speeches$parly == "Fifth Scottish Parliament")
#speeches_6 <- speeches %>% subset(is.na(speeches$parly))



# Split MPs into years

MSPs_1 <- speeches_1 %>%
  select(parl_id, name, gender, wikidataid, constituency, region, msp_type, office_held) %>%
  unique()
MSPs_1$parly <- "First Scottish Parliament"

MSPs_2 <- speeches_2 %>%
  select(parl_id, name, gender, wikidataid, constituency, region, msp_type, office_held) %>%
  unique()
MSPs_2$parly <- "Second Scottish Parliament"

MSPs_3 <- speeches_3 %>%
  select(parl_id, name, gender, wikidataid, constituency, region, msp_type, office_held) %>%
  unique()
MSPs_3$parly <- "Third Scottish Parliament"

MSPs_4 <- speeches_4 %>%
  select(parl_id, name, gender, wikidataid, constituency, region, msp_type, office_held) %>%
  unique()
MSPs_4$parly <- "Fourth Scottish Parliament"

MSPs_5 <- speeches_5 %>%
  select(parl_id, name, gender, wikidataid, constituency, region, msp_type, office_held) %>%
  unique()
MSPs_5$parly <- "Fifth Scottish Parliament"

MSPs_agg <- rbind(MSPs_1, MSPs_2, MSPs_3, MSPs_4, MSPs_5)

# keep only unique speeches

speeches_1 <- speeches_1 %>%
              select(date, name, parl_id, speech, item, type, committee, parly)
speeches_1 <- unique(speeches_1)

speeches_2 <- speeches_2 %>%
              select(date, name, parl_id, speech, item, type, committee, parly)
speeches_2 <- unique(speeches_2)

speeches_3 <- speeches_3 %>%
              select(date, name, parl_id, speech, item, type, committee, parly)
speeches_3 <- unique(speeches_3)

speeches_4 <- speeches_4 %>%
              select(date, name, parl_id, speech, item, type, committee, parly)
speeches_4 <- unique(speeches_4)

speeches_5 <- speeches_5 %>%
              select(date, name, parl_id, speech, item, type, committee, parly)
speeches_5 <- unique(speeches_5)


# bind back
speeches <- rbind(speeches_1, speeches_2, speeches_3, speeches_4, speeches_5)


