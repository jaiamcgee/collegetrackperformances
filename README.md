# College Track Performances

This project looks at how women's outdoor college track and field performances change across seasons. We wanted to see how individual athletes' results changed over time and whether season-best performances differed by outdoor eligibility year.

We collected available results from 2016 through 2026 for 20 selected schools across four conference groups. We focused on four events: the 100-meter hurdles (100H), 400-meter hurdles (400H), 400 meters (400m), and long jump. The conference labels organize schools for this project. They do not necessarily reflect each school's conference membership in every season.

## Where to Find the Data on GitHub

| Folder | What it contains |
| --- | --- |
| [`data/raw/`](data/raw/) | Source files organized by school and year where available. |
| [`data/processed/`](data/processed/) | Combined results by conference group and season, plus the ACC and SEC audit files. |
| [`data/processed/by_event/`](data/processed/by_event/) | Results grouped by event: 100H, 400H, 400m, and long jump. |
| [`notebooks/`](notebooks/) | Jupyter notebooks used to explore the data and make plots. |

If you want all available 400-meter hurdles results in one file, start with [`400H_2016_2026.csv`](data/processed/by_event/400H_2016_2026.csv). If you want one group and one year, open the corresponding annual file under `data/processed/`. For example, `sec_2024.csv` contains that year's collected SEC group results.

### Schools and Annual Files

| Group | Selected schools | Annual file pattern |
| --- | --- | --- |
| SEC | Alabama, Florida, Georgia, Kentucky, South Carolina | `data/processed/sec_YYYY.csv` |
| ACC | Clemson, Duke, Florida State, Stanford, Virginia | `data/processed/acc_YYYY.csv` |
| Big Ten | Illinois, Nebraska, Oregon, USC, Washington | `data/processed/bigten_YYYY.csv` |
| Big 12 | Arizona, Baylor, BYU, Iowa State, Texas Tech | `data/processed/big12_YYYY.csv` |

Replace `YYYY` with the season year. SEC school-year files are under `data/raw/`, and ACC school-year files are under `data/raw/acc/<year>/`. Use the combined annual files for the Big Ten and Big 12.

## How We Found the Data

We used the Track & Field Results Reporting System (TFRRS) to find outdoor performances listed for the selected schools. We checked results by school, season, and event. When available, we recorded the athlete's name, school, meet, date, time or jump distance, class year, and wind reading. We kept source links so the results could be checked later.

For the ACC and SEC, we also compared older project records with the TFRRS listings. When an older sourced result did not match a listing, we kept it in the archive and flagged it for review.

## How We Cleaned the Data

The result files and the analysis tables serve different purposes. The result files retain individual listed races and the best listed long jump mark per athlete and linked competition. For the season-best analysis, we narrowed those records down to one result per athlete, event, and outdoor season.

1. We kept outdoor results for the four events in the project.
2. We converted running times to seconds so we could compare them. For example, `1:01.47` became `61.47` seconds. Long jump distances stayed in meters.
3. We left out entries without a valid performance, such as unfinished races and foul jumps.
4. We checked known name differences and transfers to help connect results for the same athlete across seasons.
5. We kept the fastest recorded time for each running event and the longest recorded distance for long jump.

A season best means the best result in the records we collected. It may differ from an athlete's true season best if a meet or result was missing.

## Data Issues and Review Status

- Athlete names and transfers: Names sometimes appeared with different spellings or last names. A school change could also make an athlete's records harder to match.
- Eligibility year: Outdoor eligibility year can differ from academic year. We excluded unresolved cases from the regression models instead of guessing. The 100-meter hurdles received a more detailed review, so athlete identities and eligibility years for the other events still need further checking.
- Missing information: Some records lacked wind readings or race round details. We treated missing values as unknown and kept wind-assisted marks in the main analysis.
- Unusual times: We kept the 32.80-second 100-meter hurdles result in the main analysis and checked how unusual results affected the model.
- Incomplete coverage: The 2020 ACC, SEC, and Big 12 files contain headers but no results, while the Big Ten file contains four rows. Empty files show what we collected and do not establish that no competitions took place. The 2026 files reflect what was available at the time of collection.

| Group | Archived result rows | Review notes |
| --- | ---: | --- |
| ACC | 3,082 | 117 older sourced rows are flagged for review. |
| SEC | 2,959 | 249 older sourced rows are flagged for review. |
| Big Ten | 3,065 | Compiled from TFRRS listings. |
| Big 12 | 3,511 | Compiled from TFRRS listings. |

These counts describe the archived results before selecting season bests. See the [ACC audit](data/processed/acc_2016_2026_audit.csv) and [SEC audit](data/processed/sec_2016_2026_audit.csv) for more detail. Check `source_url` and `data_status` before treating flagged records as verified.

## Data Dictionary

The annual CSV files use these 18 fields:

| Fields | What they show |
| --- | --- |
| `athlete`, `school`, `conference`, `season` | Athlete name, school, project conference group, and outdoor season year. |
| `event`, `performance`, `unit` | Event, reported result, and unit. Running times use `s` or `seconds`, and long jump uses `m`. |
| `class_year` | Class label as reported in the source, sometimes with an eligibility suffix. |
| `birth_date`, `age_at_meet` | Birth date and age when reliably sourced. Otherwise, these fields are blank. |
| `meet`, `meet_date`, `round`, `place`, `wind` | Competition details when available. A blank round does not tell us which round was run. |
| `indoor_outdoor` | Whether the result was recorded indoors or outdoors. This project focuses on outdoor results. |
| `source_url`, `data_status` | Source link and review status. |

## Spaghetti Plots

Each dot shows an athlete's best recorded performance for an observed school year. Lines connect results for the same athlete. With many athletes on one chart, the lines overlap and look like spaghetti.

- Running events: A line going down means the athlete ran faster because their time decreased.
- Long jump: A line going up means the athlete jumped farther.
- Missing years: A gap means we did not find a result for that year. A single dot means we found results for only one year.
- Conference colors: In the conference plots, athletes keep the color of their first recorded conference group even if they transfer.

### What We Saw

Athletes followed different paths. Some recorded better results in later years, some stayed close to their earlier performances, and others improved one year and performed worse the next. The plots make those individual changes easier to see. The regression models summarize overall differences by outdoor eligibility year, while the spaghetti plots show how results changed for each athlete across observed school years.

## Rebuilding the Annual Files

The [scripts folder](scripts/) contains the ACC and SEC build scripts and their companion legacy audit scripts. To rebuild a season, run the corresponding build script with the year, such as `python scripts/build_sec_all_meets.py 2024`. Then run the matching legacy audit script to restore and flag unmatched older records. The audit scripts use earlier Git commits, so they may require the full repository history.