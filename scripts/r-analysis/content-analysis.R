speeches$speech <- speeches$speech %>% tolower() %>% removePunctuation()

speeches$about_gen <- NA

gen_dict <- "woman*|women*|female*|femin*|sexism"

speeches$about_gen <-  as.integer(str_detect(speeches$speech, gen_dict))

prop_about_gen <- mean(speeches$about_gen)

gender_focus <- speeches %>%
  select(gender, about_gen) %>%
  group_by(gender) %>%
  summarise(gender_focus = mean(about_gen))

#speeches$z <- c()
#speeches$z[speeches$z + speeches$z >= 1] <- 1
#speeches$z[speeches$z + speeches$z == 0] <- 0