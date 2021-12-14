# By year

speeches_syl$year <- format(speeches_syl$date, format ="%Y")

ys_n_f_spoke <- speeches_syl %>%
  select(year, parl_id, gender) %>% 
  unique %>%
  filter(gender == "F") %>%
  group_by(year) %>% 
  summarise(n_f_spoke = n())

ys_n_m_spoke <- speeches_syl %>%
  select(year, parl_id, gender) %>% 
  unique %>%
  filter(gender == "M") %>%
  group_by(year) %>% 
  summarise(n_m_spoke = n())

year_summary <- left_join(ys_n_f_spoke, ys_n_m_spoke, by = "year")
rm(ys_n_f_spoke, ys_n_m_spoke)

year_summary$n_msps_spoke <- year_summary$n_f_spoke+year_summary$n_m_spoke

ys_n_syls_f <- speeches_syl %>%
  filter(gender=="F") %>%
  group_by(year) %>%
  summarise(N_syls_F = sum(syls))
year_summary <- left_join(year_summary, ys_n_syls_f, by = "year")
rm(ys_n_syls_f)

ys_n_syls_m <- speeches_syl %>%
  filter(gender=="M") %>%
  group_by(year) %>%
  summarise(N_syls_M = sum(syls))
year_summary <- left_join(year_summary, ys_n_syls_m, by = "year")
rm(ys_n_syls_m)


ys_n_syls <- speeches_syl %>%
  group_by(year) %>%
  summarise(N_syls = sum(syls))
year_summary <- left_join(year_summary, ys_n_syls, by = "year")
rm(ys_n_syls)

year_summary$p_syls_f <- year_summary$N_syls_F/year_summary$N_syls
year_summary$p_syls_m <- year_summary$N_syls_M/year_summary$N_syls
#year_summary$p_syl_check <- year_summary$p_syls_f + year_summary$p_syls_m


ys_n_sp_f <- speeches_syl %>%
  filter(gender=="F") %>%
  group_by(year) %>%
  summarise(N_sp_F = n())
year_summary <- left_join(year_summary, ys_n_sp_f, by = "year")
rm(ys_n_sp_f)

ys_n_sp_m <- speeches_syl %>%
  filter(gender=="M") %>%
  group_by(year) %>%
  summarise(N_sp_M = n())
year_summary <- left_join(year_summary, ys_n_sp_m, by = "year")
rm(ys_n_sp_m)

ys_n_sp <- speeches_syl %>%
  group_by(year) %>%
  summarise(N_sp = n())
year_summary <- left_join(year_summary, ys_n_sp, by = "year")
rm(ys_n_sp)

year_summary$p_sp_f <- year_summary$N_sp_F/year_summary$N_sp
year_summary$p_sp_m <- year_summary$N_sp_M/year_summary$N_sp
#year_summary$p_sp_check <- year_summary$p_sp_f + year_summary$p_sp_m

ys_p_focus_f <- speeches_syl %>%
  filter(gender=="F") %>%
  group_by(year) %>%
  summarise(P_focus_f = mean(about_gen))
year_summary <- left_join(year_summary, ys_p_focus_f, by = "year")
rm(ys_p_focus_f)

ys_p_focus_m <- speeches_syl %>%
  filter(gender=="M") %>%
  group_by(year) %>%
  summarise(P_focus_m = mean(about_gen))
year_summary <- left_join(year_summary, ys_p_focus_m, by = "year")
rm(ys_p_focus_m)

ys_p_focus <- speeches_syl %>%
  group_by(year) %>%
  summarise(P_focus = mean(about_gen))
year_summary <- left_join(year_summary, ys_p_focus, by = "year")
rm(ys_p_focus)

#rm(year_summary)

n_gender <- summary[1:5, 5:9]
years_2 <- years[1:5,]
n_gender <- cbind(years_2, n_gender)

# now all i need to do is merge in within a time range (maybe I acc need to do that to speeches syl, before it gets based on year)

colnames(year_summary) <- c("Year",
                            "Number of women who spoke", 
                            "Number of men who spoke",
                            "Number of MSPs who spoke",
                            "Number of syllables by women",
                            "Number of syllables by men",
                            "Total number of syllables",
                            "Proportion of syllables by women",
                            "Proportion of syllables by men",
                            "Number of speeches by women",
                            "Number of speeches by men",
                            "Total number of speeches",
                            "Proportion of speeches by women",
                            "Proportion of speeches by men",
                            "Proportion of women-focussed speeches by women",
                            "Proportion of women-focussed speeches by men",
                            "Proportion of women-focussed speeches")

#rownames(year_summary) <- year_summary$year

ggplot(year_summary, aes(x=Year, y =`Proportion of women-focussed speeches by women`)) + geom_bar(stat="identity")

ggplot(year_summary, aes(x=`Proportion of women-focussed speeches by men`, y =`Proportion of women-focussed speeches by women`)) + geom_point() +
  geom_abline(intercept = 0, slope = 1) + xlim(0.0, 0.11) + ylim(0.0, 0.11) + xlab("Men") + ylab("Women") + ggtitle("Speeches about women's issues by...") + theme_apa()

date_about_women <- speeches_syl %>% 
  group_by(date) %>%
  summarise(sp_about_women = mean(about_gen))

ggplot(date_about_women, aes(x=`date`, y =`sp_about_women`)) + geom_point() +
 theme_apa()

geom_path()write.csv(year_summary, here("output_data", "summary_year.csv"))
