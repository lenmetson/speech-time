# specify the url
url <- "https://dataverse.harvard.edu/api/access/datafile/4432885"

# download the file into a specified path - add your analysis folder in between " "
download.file(url, here("data_raw", "rawdata.csv"))
