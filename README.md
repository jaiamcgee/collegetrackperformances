# College Track Performances

Women's outdoor track and field results for five selected schools in each of four conference groups, from 2016 through 2026. The events are 400m, 100m hurdles (`100H`), 400m hurdles (`400H`), and long jump. These labels group schools for this project; they do not imply historical conference membership in every season.

## Schools and files

| Group | Schools | Combined results |
|---|---|---|
| SEC | Alabama, Florida, Georgia, Kentucky, South Carolina | `data/processed/sec_YYYY.csv` |
| ACC | Clemson, Duke, Florida State, Stanford, Virginia | `data/processed/acc_YYYY.csv` |
| Big Ten | Illinois, Nebraska, Oregon, USC, Washington | `data/processed/bigten_YYYY.csv` |
| Big 12 | Arizona, Baylor, BYU, Iowa State, Texas Tech | `data/processed/big12_YYYY.csv` |

Each group has an annual CSV for every year from 2016 to 2026. SEC school-year files are in `data/raw/<school>_<year>.csv`; ACC school-year files are in `data/raw/acc/<year>/<school>_<year>.csv`. Big Ten and Big 12 currently have combined annual files only. The empty 2020 ACC, SEC, and Big 12 CSVs retain a header so that the year is represented; Big Ten has four rows for 2020. Empty files do not prove that no qualifying competition occurred elsewhere.

## Data dictionary

The annual CSVs share these 18 fields:

| Field | Meaning |
|---|---|
| `athlete`, `school`, `conference`, `season` | Athlete, selected school and group, outdoor season year |
| `event`, `performance`, `unit` | Event and reported time or distance; track units appear as `s` or `seconds`, long jump as `m` |
| `class_year` | Reported academic year when available, often with an eligibility suffix |
| `birth_date`, `age_at_meet` | Blank unless reliably sourced; do not infer ages |
| `meet`, `meet_date`, `round`, `place`, `wind` | Competition details when available |
| `indoor_outdoor` | Outdoor |
| `source_url` | Link associated with the result |
| `data_status` | Source and review status |

Track rows retain separate listed races, including rounds when identifiable. Long jump retains the best listed mark per athlete and linked competition, not every attempt. Separate competition links from the same meet remain separate rows. `round` is often blank in the archived listings, so a blank value does not establish which round was run.

## Coverage and review status

| Group | Result rows | Review notes |
|---|---:|---|
| ACC | 3,082 | 117 older sourced rows have `legacy_source_needs_review` |
| SEC | 2,959 | 249 older sourced rows have `legacy_source_needs_review` |
| Big Ten | 3,065 | TFRRS listings; no separate school-year files yet |
| Big 12 | 3,511 | TFRRS listings; no separate school-year files yet |

These are counts after collapsing repeated long-jump attempts in the Big Ten and Big 12 files. They are not a guarantee of exhaustive coverage. The older ACC and SEC rows flagged for review were retained when they did not match the TFRRS all-performances listings. Review their linked sources and possible duplicates before using them as independently verified results. The files may omit meets that are absent from TFRRS, and 2026 represents the available source listings at the time of collection.

ACC and SEC audit counts are in `data/processed/acc_2016_2026_audit.csv` and `data/processed/sec_2016_2026_audit.csv`. For those groups, `scripts/build_acc_all_meets.py` and `scripts/build_sec_all_meets.py` fetch annual TFRRS listings; run them with a year argument, for example `python scripts/build_sec_all_meets.py 2024`. Their companion `audit_*_legacy.py` scripts merge unmatched historical rows from the recorded Git baseline and rewrite the audit files. Running a build script alone overwrites that year's retained legacy rows; run the appropriate legacy audit script afterward. Both audit scripts depend on the old Git commits in this repository's history, so a shallow clone may not suffice.

## Working with the data

For a single year and group, open the corresponding file under `data/processed/`. To combine groups for analysis, concatenate the annual files using the 18 named fields; do not interpret the selected conference labels as historical membership. Normalize `unit` before comparing track times. Check `data_status`, missing class years, wind, and source links for analyses where provenance matters.

The repository no longer includes empty conference-wide placeholder files or an empty `all_conferences.csv`. Produce an all-groups dataset from the annual files when needed, so it reflects the current data.

## Data Description

We collected women's outdoor college track and field results from the **Track & Field Results Reporting System (TFRRS)**. Our project covers available results from **2016 through 2026** for selected schools in the ACC, Big Ten, Big 12, and SEC.

We studied four events: **100-meter hurdles, 400-meter hurdles, 400 meters, and long jump**. We recorded details such as the athlete's name, school, event, meet date, season, performance, and eligibility year when available. We also recorded wind readings when they were listed.

### How We Cleaned the Data

An athlete can compete several times in one season, so we kept **one best result per athlete, per event, per outdoor season**.

- **Running events:** We kept the fastest recorded time.
- **Long jump:** We kept the farthest recorded jump.

We converted running times to seconds so we could compare them. For example, **1:01.47 became 61.47 seconds**. We left out entries without a valid result, such as unfinished races and foul jumps.

A **season best** means the best result we found in the records we collected. Some meets may be missing.

### Problems We Ran Into

- **Athlete names and transfers:** Some names were spelled differently or changed over time. Some athletes also transferred schools. We checked known name differences to help follow the same athlete across seasons.
- **Missing or conflicting eligibility years:** An athlete's outdoor eligibility year can differ from their academic year. When we couldn't resolve a missing or conflicting year, we left that case out of the regression models. The 100-meter hurdles received a more detailed review, so athlete names and eligibility years still need further checking for the other events.
- **Unusual results:** We kept the **32.80-second 100-meter hurdles result** in the main analysis and checked how much unusual results affected the model.
- **Missing wind readings:** We kept wind-assisted marks in the main analysis. When a wind reading was missing, we treated it as unknown.

### What the Spaghetti Plots Show

Each **dot** shows an athlete's best recorded performance for an observed school year. Each **line** connects results for the same athlete so we can follow their performance across years. The lines overlap, which is why the chart is called a spaghetti plot.

- **Running events:** A line going **down** means the athlete ran faster because their time decreased.
- **Long jump:** A line going **up** means the athlete jumped farther.
- **Missing years:** We leave a gap when we don't have a result for a year. Athletes with only one recorded year appear as a single dot.
- **Conference colors:** In the conference plots, each athlete keeps the color of their first recorded conference, even if they transfer.

The spaghetti plots show **how individual athletes performed across years**. The regression models summarize the **overall differences between outdoor eligibility years**.
### What We Saw in the Spaghetti Plots

The plots showed that **athletes did not all improve in the same way**. Some performed better in later years, some stayed close to their earlier results, and others improved one year but performed worse the next.

- **Running events:** A line going down shows a faster time.
- **Long jump:** A line going up shows a longer jump.
- **Gaps:** A break means we did not have a recorded result for that year.
- **Single dots:** We had only one recorded year for that athlete, so we could not tell how their performance changed over time.

The plots showed something an overall average can hide: **even though our models estimated better performances in later eligibility years, individual athletes followed different paths.**
