library(readr)
library(dplyr)
library(tidyr)
library(jsonlite)

# 1. Read the raw text file line by line
raw_lines <- read_lines("../../sheets/grady_ward_sheet/mobypos.txt")

# 2. Convert the lines into a data frame
moby_df <- tibble(raw = raw_lines) %>%
  filter(raw != "") %>%
  separate(raw, into = c("word", "pos_codes"), sep = "\\\\", extra = "merge", fill = "right") %>%
  mutate(
    word = trimws(word),
    pos_codes = trimws(pos_codes)
  )

# 3. Save your structured data frame to a JSON file
write_json(moby_df, "moby_pos_raw_parsed.json", pretty = TRUE)