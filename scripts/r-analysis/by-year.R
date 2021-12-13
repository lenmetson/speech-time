# By year

speeches_syl$year <- format(speeches_syl$date, format ="%Y")

ys_n_syls_f <- speeches_syl %>%
  filter(gender=="F") %>%
  group_by(year) %>%
  summarise(N_syls_F = sum(syls))

ys_n_syls_m <- speeches_syl %>%
  filter(gender=="M") %>%
  group_by(year) %>%
  summarise(N_syls_M = sum(syls))
year_summary <- left_join(ys_n_syls_f, ys_n_syls_m, by = "year")
rm(ys_n_syls_f, ys_n_syls_m)

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

colnames(year_summary) <- c("Year",
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

write.csv(year_summary, here("output_data", "summary_year.csv"))
