speeches_syl$speech <- speeches$speech %>% tolower() %>% removePunctuation()

speeches_syl$about_gen <- NA

gen_dict <- "feminis*|feminin*|patriarc*|sexis*|misogyn*|misandr*|victim blam*|women|woman|gender action plan|gender balance|gender based violence|gender bias*|gender equity|gender equality|gender gap|pay gap|gender rol*|gender stereotyp*|menstrual hygiene|sexual right*|reproductive right*|abortion*|sex work*|gender discrimina*|female*|girl*|sexual violence|sexual assaults|rape*|domestic violence|woman*|women*|female*|femin*|sexism|equal* pay|period poverty|sex* assault|menstrat*|abortion|matern*|contraception|reproductive rights|pro-life|pro-choice"

speeches_syl$about_gen <-  as.integer(str_detect(speeches$speech, gen_dict))

prop_about_gen <- mean(speeches$about_gen)

gender_focus <- speeches %>%
  select(gender, about_gen) %>%
  group_by(gender) %>%
  summarise(gender_focus = mean(about_gen))

#speeches$z <- c()
#speeches$z[speeches$z + speeches$z >= 1] <- 1
#speeches$z[speeches$z + speeches$z == 0] <- 0
