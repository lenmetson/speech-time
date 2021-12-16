

speeches_syl$syls <- as.numeric(speeches_syl$syls)
speeches_syl$parl_id <- as.numeric(speeches_syl$parl_id)
####
syls_all_day <- speeches_syl %>%
  select(date, parl_id, syls, name, gender) %>%
  group_by(date) %>%
  summarise(total_syls = sum(syls))

syls_ns_day <- speeches_syl %>%
  select(date, parl_id, syls, name, gender) %>%
  filter(parl_id == 1848) %>%
  group_by(date) %>%
  summarise(ns_syls = sum(syls))

syls_total_day <- speeches_syl %>%
  select(date, parl_id, syls, name, gender) %>%
  group_by(date) %>%
  summarise(total_syls = sum(syls))


  
prop_ns <- full_join(syls_total_day, syls_ns_day, by = "date")
prop_ns[is.na(prop_ns)] <- 0

prop_ns$prop_ns <- prop_ns$ns_syls/prop_ns$total_syls

prop_ns_m <- prop_ns %>%
  group_by(month = lubridate::floor_date(date, "month")) %>%
  summarise(prop_ns = mean(prop_ns))

time_month_10_women <- speeches_top_10_women %>%
  group_by(month = lubridate::floor_date(date, "month")) %>%
  summarise(syls = sum(syls))


######
speeches_top_women <- speeches_syl %>%
  select(date, parl_id, syls, name, gender) %>%
  filter(gender=="F")

top_women <- speeches_top_women %>%
  group_by(parl_id) %>%
  summarise(total_syls = sum(syls))

top_10_women <- top_n(top_women, 10, total_syls)

speeches_syl$parl_id <- as.numeric(speeches_syl$parl_id)

speeches_top_10_women <- speeches_syl %>%
  select(date, parl_id, syls, name, gender) %>%
  filter(parl_id == top_10_women$parl_id) ## !!!! Some data being lost here


#test1 <- speeches_top_10_women %>%
#  group_by(parl_id) %>%
#  summarise(total_syls = sum(syls))


time_day_10_women <- speeches_top_10_women %>%
  group_by(date) %>%
  summarise(syls = sum(syls))

time_month_10_women <- speeches_top_10_women %>%
  group_by(month = lubridate::floor_date(date, "month")) %>%
  summarise(syls = sum(syls))

# total rows of the top 10 women by year

sp_women2 <- speeches_syl %>%
  select(date, parl_id, syls, name, gender) %>%
  filter(gender == "F") %>%
  group_by(date) %>% 
  top_n(10, syls)

# this gives up top 10 longest speeches by women on each day 

sp_women2_sum <- sp_women2 %>%
  group_by(date) %>%
  summarise(sum = sum(syls))


