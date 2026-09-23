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
