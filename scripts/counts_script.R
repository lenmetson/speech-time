# Version history
## Created script 03/11

# Packages

if(!require("tidyverse")) {install.packages("tidyverse"); library("tidyverse")}
if(!require("sylcount")) {install.packages("sylcount"); library("sylcount")}

speeches <- # file path and relevant function

syls <- sylcount(speeches$speeches)
