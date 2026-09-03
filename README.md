# College Track Performances

## Project Overview

This independent study project analyzes women's NCAA Division I track and field performances across four major conferences.

The project focuses on athlete performance and development in the 400m, 100m hurdles, 400m hurdles, and long jump from the 2023 through 2026 outdoor seasons.

Unlike a season-best-only dataset, this project collects individual performances from each meet so that athlete development can be examined both within and across seasons.

## Research Question

How do individual women's track and field athletes develop and improve over time across top NCAA Division I programs and conferences?

## Conferences

The project includes five women's programs from each of four conferences based on their placement at the 2026 conference outdoor championships.

### SEC

* Florida
* Alabama
* Georgia
* South Carolina
* Kentucky

### ACC

* Clemson
* Duke
* Stanford
* Florida State
* Virginia

### Big Ten

* Oregon
* Illinois
* USC
* Washington
* Nebraska

### Big 12

* Texas Tech
* BYU
* Arizona
* Iowa State
* Baylor

## Events

The following women's events are included:

* 400 meters
* 100 meter hurdles
* 400 meter hurdles
* Long jump

## Seasons

* 2023
* 2024
* 2025
* 2026

Only outdoor track and field performances are included in the primary analysis.

## Data Collection

The project aims to collect each available meet performance for athletes competing in the selected events.

Each observation represents an athlete's performance at a meet.

Data fields include:

* Athlete
* School
* Conference
* Event
* Season
* Class year
* Birth date, when available
* Age at meet, when birth date is available
* Performance
* Unit
* Meet
* Meet date
* Round
* Place
* Wind, when applicable
* Indoor/outdoor designation
* Source URL

## Data Sources

The primary source is TFRRS (Track & Field Results Reporting System).

Additional sources may be used to obtain or verify athlete information, particularly birth dates:

* University athletics websites
* World Athletics
* Athletic.net
* NCAA results

Missing birth dates and ages will remain missing rather than being estimated.

## Repository Structure

`data/raw/` contains performance data organized by conference and school.

`data/processed/` will contain cleaned and combined datasets.

`notebooks/` will contain notebooks for data cleaning, exploratory analysis, athlete improvement analysis, and conference comparisons.

`src/` will contain reusable Python code for data collection, cleaning, and analysis.

`figures/` will contain charts and other visualizations produced during the project.

## Project Goals

1. Track individual athlete performance across meets.
2. Measure improvement within individual seasons.
3. Measure improvement across collegiate seasons.
4. Compare athlete development between schools.
5. Compare athlete development between conferences.
6. Examine performance patterns by event.
7. Explore athlete age in relation to performance and improvement.
