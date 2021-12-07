# add in session names 

years <- read.csv(here("data_raw", "years.csv"))

years$Election.Date <- as.Date(years$Election.Date, format = "%d-%m-%Y")
years$Dissolution.Date <- as.Date(years$Dissolution.Date, format = "%d-%m-%Y")

speeches$date <- as.Date(speeches$date, format = "%Y-%m-%d")


# add code to add a varible called Parliament_name 