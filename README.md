# College Track Performances

This project analyzes NCAA Division I women's outdoor track and field performances across selected schools from the SEC, ACC, Big Ten, and Big 12.

## Project Scope

The dataset covers the **2016–2026 outdoor seasons** and focuses on four events:

- 400 meters
- 100-meter hurdles
- 400-meter hurdles
- Long jump

The goal is to collect **meet-by-meet athlete performances**, not only season-best marks. Separate preliminary, quarterfinal, semifinal, and final races are stored as separate rows when available.

For long jump, the dataset stores **one official result per athlete per competition**, rather than every individual jump attempt.

## Schools

The project uses five women's teams from each conference group.

### SEC
- Florida
- Alabama
- Georgia
- South Carolina
- Kentucky

### ACC
- Clemson
- Duke
- Stanford
- Florida State
- Virginia

### Big Ten
- Oregon
- Illinois
- USC
- Washington
- Nebraska

### Big 12
- Texas Tech
- BYU
- Arizona
- Iowa State
- Baylor

> Conference labels represent the conference group used for this project. Some schools changed conferences during the 2016–2026 period, so historical conference membership may differ from the project grouping.

## Dataset Fields

Each school-year CSV follows this schema:

| Field | Description |
|---|---|
| `athlete` | Athlete name |
| `school` | School name |
| `conference` | Project conference group |
| `event` | 400m, 100H, 400H, or Long Jump |
| `season` | Outdoor season year |
| `class_year` | FR, SO, JR, SR, GR, or redshirt equivalent |
| `birth_date` | Birth date when reliably available |
| `age_at_meet` | Athlete age at meet when reliably available |
| `performance` | Time or official long-jump mark |
| `unit` | Seconds or meters |
| `meet` | Meet name |
| `meet_date` | Meet date |
| `round` | Preliminary, first round, quarterfinal, semifinal, final, etc. |
| `place` | Finishing place when available |
| `wind` | Wind reading when reported |
| `indoor_outdoor` | Outdoor |
| `source_url` | Source used to verify the result |
| `data_status` | Verification/completeness status |

Missing birth dates or ages are left blank rather than estimated.

## Data Sources

Historical and recent performances are verified using sources such as:

- Official university athletics records
- NCAA championship results
- Conference championship results
- TFRRS athlete and meet-result pages
- World Athletics
- Athletic.net

Older seasons may require multiple sources because historical result indexing can be incomplete. Files that still need a complete season-coverage audit are marked accordingly in `data_status`.

## Repository Structure

```text
collegetrackperformances/
├── data/
│   ├── raw/
│   │   └── individual school-year CSV files
│   └── processed/
│       └── combined conference/year datasets
├── notebooks/
├── src/
├── figures/
├── README.md
├── requirements.txt
└── .gitignore
```

## Current Progress

### Historical SEC Collection

The project is currently expanding backward from the recent seasons to **2016**.

Current 2016 SEC progress:

- Florida — added
- Alabama — added
- Georgia — added
- South Carolina — added
- Kentucky — next

After all five SEC schools are complete for 2016, they can be combined into:

```text
data/processed/sec_2016.csv
```

The same workflow will then continue through 2017 and 2018 before moving into later historical batches.

### Existing Recent Data

Existing work from the 2023–2025 seasons remains part of the project and will be audited later for missing school-year files and completeness.

The 2023 and 2024 SEC datasets have already been developed substantially. The 2025 files should be treated as working datasets until a full season-coverage check is completed.

The 2026 season will also be reviewed during the final recent-year audit.

## Quality-Control Rules

Before a school-year file is considered complete:

1. Every available target-event performance should be represented.
2. Separate rounds should remain separate rows.
3. Long jump should contain one official result per athlete per meet.
4. DNF, DQ, FS, FOUL, and similar official results should be preserved.
5. Class year should be verified when possible.
6. Birth date and age should never be guessed.
7. Duplicate rows should be checked.
8. Meet dates and source URLs should be retained.
9. Historical files should not be labeled exhaustive until coverage has been checked across available sources.

## Special Note for 2020

The 2020 NCAA outdoor track and field season was disrupted by COVID-19. The project will document legitimately missing or canceled outdoor competition rather than inventing normal-season results.

## Project Goals

The completed dataset will support analysis of:

- Athlete improvement across a season
- Athlete improvement across multiple seasons
- School-level performance trends
- Conference-level comparisons
- Event-specific patterns
- Long-term performance development
- Athlete age and class-year relationships where reliable data are available
