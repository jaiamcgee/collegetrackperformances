# College Track Performance Findings, 2016–2026

## Purpose and approach

This project looked at how women’s college track performances changed over time in the 100-meter hurdles (100H), 400-meter hurdles (400H), 400 meters (400m), and long jump. The data covered 2016–2026. Spaghetti plots showed each athlete’s recorded results, with time in seconds for races and distance in meters for long jump.

The x-axis started at each athlete’s first year in the data. This allowed us to compare athletes at similar points in their recorded careers, even if they competed in different calendar years. Year 1 did not necessarily mean freshman year. Separate plots also showed results by school and conference.

## What we found

The notebook included 12,576 valid performance records and excluded 41 records that did not meet its data checks. The event totals were 3,469 results for 100H, 2,702 for 400H, 3,261 for 400m, and 3,144 for long jump. These were recorded results, not just each athlete’s best performance.

To measure change, the notebook compared each athlete’s average result in their first and last recorded years. A lower race time counted as improvement, while a longer jump counted as improvement.

| Event | Athletes with multiple recorded years | Improved | Declined | Unchanged | Percentage who improved |
| --- | ---: | ---: | ---: | ---: | ---: |
| 100H | 181 | 138 | 43 | 0 | 76.2% |
| 400H | 140 | 96 | 44 | 0 | 68.6% |
| 400m | 261 | 157 | 104 | 0 | 60.2% |
| Long jump | 235 | 154 | 80 | 1 | 65.5% |

Most athletes with multiple recorded years improved in every event. The 100H had the highest percentage of athletes who improved, while the 400m had the lowest. This describes the athletes in these files; it does not prove that one event is easier to improve in than another.

For example, Aaliyah McCormick’s average 100H time decreased from about 13.084 seconds in her first recorded year to 12.709 seconds in her last, an improvement of about 0.375 seconds. Zoey Bonds’ average long jump increased from about 5.133 meters to 5.870 meters, an improvement of about 0.737 meters.

## Limits and meaning

Many athletes had only one recorded year: 219 in 100H, 136 in 400H, 313 in 400m, and 228 in long jump. They appeared in the plots but could not be compared across years. Athletes competing in multiple events could be counted in more than one event.

Wind, meet conditions, missing data, and different numbers of races or jumps could affect the averages. Matching athletes by name could also combine different people with the same name. The 100H graph displayed only 12–17 seconds, leaving 41 valid results outside its visible range; those results still remained in the comparison calculations.

The main finding was that most athletes with multiple recorded years had better average results by their last recorded year. This comparison does not show whether improvement happened every year or explain what caused it. The school and conference plots provide more detail, but this summary does not rank schools or conferences.

## Source

Results and examples were taken from the saved outputs in [the project’s spaghetti plot notebook](notebooks/college_track_all_results_spaghetti.ipynb), accessed October 14, 2026.
