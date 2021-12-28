bonne_annee_nopos <- bonne_annee %>% filter(is.na(office_held))

gender_nopos <- bonne_annee_nopos %>%
    group_by(gender) %>%
    summarise(sum_syls = sum(syls))

gender_total_nopos <- gender_nopos[2,2] + gender_nopos[1,2] #m-f
prop_f_nopos <- gender_nopos[1,2]/gender_total_nopos
prop_m_nopos <- gender_nopos[2,2]/gender_total_nopos
