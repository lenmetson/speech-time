#
if(!require("here"))install.packages("here")
source(here("scripts", "r-analysis", "r-packages.R"))

# We need to source our summary data
#source(here("scripts", "download-csv-http.R"))# If you haven't downloaded the data yet, uncomment this line

source(here("scripts", "r-analysis", "clean-data.R"))
source(here("scripts", "r-analysis", "MSPs-count.R"))
source(here("scripts", "r-analysis", "agg-speech-count.R"))

# Make results table

# n_m | n_f | p_m | p_f | n_msps_m | n_msps_f | p_msps_m | p_msps_f | n_total
n_m <- c(n_speeches_m1, n_speeches_m2, n_speeches_m3, n_speeches_m4, n_speeches_m5, ((n_speeches_m1 + n_speeches_m2 + n_speeches_m3 + n_speeches_m4 + n_speeches_m5)/5))
n_f <- c(n_speeches_f1, n_speeches_f2, n_speeches_f3, n_speeches_f4, n_speeches_f5, ((n_speeches_f1 + n_speeches_f2 + n_speeches_f3 + n_speeches_f4 + n_speeches_f5)/5))
p_m <- c(prop_speeches_m1, prop_speeches_m2, prop_speeches_m3, prop_speeches_m4, prop_speeches_m5, ((prop_speeches_m1 + prop_speeches_m2 + prop_speeches_m3 + prop_speeches_m4 + prop_speeches_m5)/5))
p_f <- c(prop_speeches_f1, prop_speeches_f2, prop_speeches_f3, prop_speeches_f4, prop_speeches_f5, ((prop_speeches_f1 + prop_speeches_f2 + prop_speeches_f3 + prop_speeches_f4 + prop_speeches_f5)/5))
n_msps_m <- c(nm1, nm2, nm3, nm4, nm5, ((nm1+nm2+nm3+nm4+nm5)/5))
n_msps_f <- c(nf1, nf2, nf3, nf4, nf5, ((nf1+nf2+nf3+nf4+nf5)/5))
n_total <- c(n_msp1, n_msp2, n_msp3, n_msp4, n_msp5, ((n_msp1 + n_msp2 + n_msp3 + n_msp4 + n_msp5)/5))
p_msps_m <- c(pm1, pm2, pm3, pm4, pm5, ((pm1+pm2+pm3+pm4+pm5)/5))
p_msps_f <- c(pf1, pf2, pf3, pf4, pf5, ((pf1+pf2+pf3+pf4+pf5)/5))



summary <- data.frame(n_m, n_f, p_m, p_f, n_msps_m, n_msps_f, n_total, p_msps_m, p_msps_f)

rownames(summary) <- c("First Parliament", "Second Parliament", "Third Parliament",
                       "Fourth Parliament", "Fifth Parliament", "Mean")

colnames(summary) <- c("Number speeches by men", "Number of speeches by women",
                      "Proportion of speeches by men", "Proportion of speeches by women",
                      "Number of men", "Number of women", "Number of MSPs", "% MSPs who are men",
                      "% MSPs who are women")

write.csv(summary, here("output_data", "summary.csv"))
write.csv(MSPs, here("output_data", "MSPs.csv"))

#rm(list=ls()[! ls() %in% c("summary", "gender", "years"])


# Speeches

#source(here("scripts", "r-analysis", "speech-count.R"))

# Syllables

source(here("scripts", "r-analysis", "syl-count.R"))

syls_all <- rbind(syls_1, syls_2, syls_3, syls_4, syls_5)


syls_summary <-
  syls_all %>%
  group_by(gender) %>%
  summarise(syls = mean(syls))

write.csv(syls_all, here("output_data", "results1.csv"))

# add names
MSPs_names <- MSPs %>% select(parl_id, name)

feliz_navidad <- left_join(syls_all, MSPs_names, by = "parl_id") %>% unique()
write.csv(feliz_navidad, here("output_data", "feliz_navidad.csv"))

MSPs_meta <- MSPs %>% select(!"gender") %>% unique()

bonne_annee <- left_join(syls_all, MSPs_meta, by = c("parl_id", "parly")) %>% unique()
write.csv(bonne_annee, here("output_data", "bonne_annee.csv"))

head(bonne_annee)

# Content analysis
source(here("scripts", "r-analysis", "content-analysis.R"))

# view % speeches about women
prop_about_gen*100

# view % speeches about women by women

gfp_f <- gender_focus[1,2]
gfp_m <- gender_focus[2,2]

gfp_f-gfp_m

gfp_m*100
gfp_f*100


lm <- lm(about_gen~gender, data = speeches)
#summary(lm)
#summ(lm, digits = 4)
export_summs(lm)


gender_focus_msps <- speeches %>%
  select(parl_id, about_gen) %>%
  group_by(parl_id) %>%
  summarise(gender_focus = mean(about_gen))

name_id <- MSPs %>% select(name, parl_id, gender) %>% unique()
gender_focus_msps <- left_join(gender_focus_msps, name_id, by = "parl_id")

write.csv(gender_focus_msps, here("output_data", "gender_focus_msps.csv"))

boxplot_gen_focus <- ggplot(gender_focus_msps, aes(gender, gender_focus)) +
  ggtitle("Gender-focus and Gender") +
  xlab("Gender") + ylab("% Speeches about women's issues") +
  geom_boxplot(notch=TRUE, outlier.stroke = TRUE, notchwidth = 0.7, fill = '#B5B5B5') +
  coord_flip() +
  #geom_jitter(shape=16, position=position_jitter(0.2)) +
  theme_apa()

boxplot_gen_focus

ggsave(here("output_data", "boxplot.png"), boxplot_gen_focus,
       width = 7,
       height = 5)

# Create a summary csv for years

source(here("scripts", "r-analysis", "by-year.R"))


# Gap ratio

summary$ratio_women <- summary$`Proportion of speeches by women`/summary$`% MSPs who are women`

summary$parliament <- rownames(summary)

ggplot(summary, aes(x=parliament, y=ratio_women)) + geom_bar(stat="identity")


#

source(here("scripts", "r-analysis", "top_women.R"))

time_day_10_women$date

ggplot(time_day_10_women, aes(x=date, y=syls)) +
  #geom_line() +
  geom_point() +
  geom_smooth(method=lm) +
  theme_apa()


ggplot(time_month_10_women, aes(x=month, y=syls))  + geom_bar(stat = "identity") +
  theme_apa()


ggplot(sp_women2_sum, aes(x=date, y=sum)) + geom_point()

ggplot(sp_women2_sum, aes(x=date, y=sum))  + geom_bar(stat = "identity") +
  theme_apa()

ggplot(syls_ns_day, aes(x=date, y=ns_syls))  + geom_point() +
  theme_apa()

nicola <- ggplot(prop_ns_m, aes(x=month, y=prop_ns)) +
  ggtitle("Proportion of syllables spoken by Sturgeon on each day") +
  xlab("Day") + ylab("% syllables spoken by Nicola Sturgeon \n (smoothed by loess regression)") +
  #geom_line() +
  #geom_point() +
  geom_smooth(method = loess, se=FALSE, color ="black") +
  theme_apa()

ggsave(here("output_data", "nicola-r-plot.png"), nicola,
       width = 7,
       height = 5)

write.csv(prop_ns_m, (here("output_data", "nicola.csv")))

# Exclude positions
source(here("scripts", "r-analysis",  "no_positions.R"))
