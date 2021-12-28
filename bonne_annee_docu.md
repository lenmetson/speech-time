# bonne_annee.csv
This is our main output data. It contains total syllables as well as associated meta data.

## Variables 

| name           | type | description                                                                                                                                                                                          |
|----------------|------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `parl_id`      | int  | MSP's unique parliamentary ID number                                                                                                                                                                 |
| `syls`         | int  | Sum of syllables for each MSP in a given parliamentary session                                                                                                                                       |
| `parly`        | chr  | Parliamentary session the row refers to. There are 5 in total since the opening of the Scottish Parliament.                                                                                          |
| `gender`       | chr  | MSP's gender. "M" = Male, "F" = Female. There was no provision  for non-binary genders in original meta data.                                                                                        |
| `name`         | chr  | MSP's name.                                                                                                                                                                                          |
| `wikidataid`   | chr  | MSP's unique identifier to access to the relational database,  Wikidata.                                                                                                                             |
| `constituency` | chr  | Constituency the MSP represents (NA for regional MSPs)                                                                                                                                               |
| `region`       | chr  | Region the MSP represents (either the region they are elected to represent, or for constituency MSPs, the region their  constituency is in.                                                          |
| `msp_type`     | chr  | Whether the MSP is a regional or constituency MSP. Constituency MSPs are elected by single-member district plurality elections. Regional MSPs are elected by party-list proportional representation. |
| `office_held`  | chr  | Details of any parliamentary offices held by the MSP at the time.  NA if non                                                                                                                         |
