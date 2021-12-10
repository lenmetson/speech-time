# Data 
harvard <- read.csv(here("data_raw", "rawdata.csv")) # 475869 obs. of 21 vars.
speeches <- harvard %>% filter(is_speech == 1) # 430577 obs. of 21 vars. 
rm(harvard)
speeches <- speeches %>% filter(!is.na(parl_id)) # drop all without parl_id, 399256 obs. of 21 vars. 

# Split into parliaments

# add in session names

years <- read.csv(here("data_raw", "years.csv"))

years$Election.Date <- as.Date(years$Election.Date, format = "%d-%m-%Y")
years$Dissolution.Date <- as.Date(years$Dissolution.Date, format = "%d-%m-%Y")

speeches$date <- as.Date(speeches$date, format = "%Y-%m-%d")


# add code to add a varible called Parliament_name

speeches$parly <- ifelse(speeches$date >= years[1,2] & speeches$date <= years[1,3], "1st",
                         ifelse(speeches$date >= years[2,2] & speeches$date <= years[2,3], "2nd",
                                ifelse(speeches$date >= years[3,2] & speeches$date <= years[3,3], "3rd",
                                       ifelse(speeches$date >= years[4,2] & speeches$date <= years[4,3], "4th",
                                              ifelse(speeches$date >= years[5,2] & speeches$date <= years[5,3], "5th",
                                                     ifelse(speeches$date >= years[6,2], "6th",
                                                            NA)))))) # 399256 obs. of 22 vars.

# Split into years

speeches_1 <- speeches %>% subset(speeches$parly == "1st")
speeches_2 <- speeches %>% subset(speeches$parly == "2nd")
speeches_3 <- speeches %>% subset(speeches$parly == "3rd")
speeches_4 <- speeches %>% subset(speeches$parly == "4th")
speeches_5 <- speeches %>% subset(speeches$parly == "5th")
#speeches_6 <- speeches %>% subset(is.na(speeches$parly))



# Split MPs into years

MSPs_1 <- speeches_1 %>%
  select(parl_id, name, gender, wikidataid, constituency, region, msp_type, office_held) %>%
  unique()
MSPs_1$parly <- "1st"

MSPs_2 <- speeches_2 %>%
  select(parl_id, name, gender, wikidataid, constituency, region, msp_type, office_held) %>%
  unique()
MSPs_2$parly <- "2nd"

MSPs_3 <- speeches_3 %>%
  select(parl_id, name, gender, wikidataid, constituency, region, msp_type, office_held) %>%
  unique()
MSPs_3$parly <- "3rd"

MSPs_4 <- speeches_4 %>%
  select(parl_id, name, gender, wikidataid, constituency, region, msp_type, office_held) %>%
  unique()
MSPs_4$parly <- "4th"

MSPs_5 <- speeches_5 %>%
  select(parl_id, name, gender, wikidataid, constituency, region, msp_type, office_held) %>%
  unique()
MSPs_5$parly <- "5th"

MSPs <- rbind(MSPs_1, MSPs_2, MSPs_3, MSPs_4, MSPs_5)


MSPs <- unique(MSPs)


gender <- MSPs %>% select(parl_id, gender)

#speeches <- left_join(speeches, gender, by = "parl_id") %>% unique()

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
speeches <- rbind(speeches_1, speeches_2, speeches_3, speeches_4, speeches_5) # 390586 obs. of 8 vars.
speeches <- left_join(speeches, gender, by = "parl_id") %>% unique() # 390586 obs. of 9 vars.
