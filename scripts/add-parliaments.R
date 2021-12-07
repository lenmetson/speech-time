# add in session names

years <- read.csv(here("data_raw", "years.csv"))

years$Election.Date <- as.Date(years$Election.Date, format = "%d-%m-%Y")
years$Dissolution.Date <- as.Date(years$Dissolution.Date, format = "%d-%m-%Y")

speeches$date <- as.Date(speeches$date, format = "%Y-%m-%d")


# add code to add a varible called Parliament_name

speeches$parliament <- ifelse(speeches$date >= years[1,2] & speeches$date <= years[1,3], "First Scottish Parliament",
                       ifelse(speeches$date >= years[2,2] & speeches$date <= years[2,3], "Second Scottish Parliament",
                       ifelse(speeches$date >= years[3,2] & speeches$date <= years[3,3], "Third Scottish Parliament",
                       ifelse(speeches$date >= years[4,2] & speeches$date <= years[4,3], "Fourth Scottish Parliament",
                       ifelse(speeches$date >= years[5,2] & speeches$date <= years[5,3], "Fifth Scottish Parliament",
                       ifelse(speeches$date >= years[6,2], "Sixth Scottish Parliament",
                       NA))))))

# Split into years

speeches_1 <- speeches %>% subset(speeches$parliament == "First Scottish Parliament") %>% unique()
speeches_2 <- speeches %>% subset(speeches$parliament == "Second Scottish Parliament") %>% unique()
speeches_3 <- speeches %>% subset(speeches$parliament == "Third Scottish Parliament") %>% unique()
speeches_4 <- speeches %>% subset(speeches$parliament == "Fourth Scottish Parliament") %>% unique()
speeches_5 <- speeches %>% subset(speeches$parliament == "Fifth Scottish Parliament") %>% unique()
speeches_6 <- speeches %>% subset(is.na(speeches$parliament)) %>% unique()



# Split MPs into years

MSPs_1 <- speeches_1 %>%
  select(parl_id, name, gender, wikidataid) %>%
  unique()

MSPs_2 <- speeches_2 %>%
  select(parl_id, name, gender, wikidataid) %>%
  unique()

MSPs_3 <- speeches_3 %>%
  select(parl_id, name, gender, wikidataid) %>%
  unique()

MSPs_4 <- speeches_4 %>%
  select(parl_id, name, gender, wikidataid) %>%
  unique()

MSPs_5 <- speeches_5 %>%
  select(parl_id, name, gender, wikidataid) %>%
  unique()
