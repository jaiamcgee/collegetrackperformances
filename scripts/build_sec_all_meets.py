import csv
import re
import time
import sys
import urllib.request
from collections import Counter
from datetime import datetime
from pathlib import Path
from bs4 import BeautifulSoup

SCHOOLS = {
    'Alabama': 'AL_college_f_Alabama',
    'Florida': 'FL_college_f_Florida',
    'Georgia': 'GA_college_f_Georgia',
    'South Carolina': 'SC_college_f_South_Carolina',
    'Kentucky': 'KY_college_f_Kentucky',
}
EVENTS = {'400 Meters': '400m', '100 Hurdles': '100H',
          '400 Hurdles': '400H', 'Long Jump': 'Long Jump'}
FIELDS = ['athlete','school','conference','event','season','class_year',
          'birth_date','age_at_meet','performance','unit','meet','meet_date',
          'round','place','wind','indoor_outdoor','source_url','data_status']
YEAR = int(sys.argv[1]) if len(sys.argv) > 1 else 2023
LIST_SEASON = {2016:(1683,336), 2017:(1915,377), 2018:(2278,414),
               2019:(2573,453), 2020:(2906,496), 2021:(3200,530),
               2022:(3730,568), 2023:(4153,608), 2024:(4541,645),
               2025:(5027,681), 2026:(5771,730)}
list_hnd, season_hnd = LIST_SEASON[YEAR]
rows = []
for school, slug in SCHOOLS.items():
    url = f'https://www.tfrrs.org/all_performances/{slug}.html?list_hnd={list_hnd}&season_hnd={season_hnd}'
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, timeout=45) as response:
        soup = BeautifulSoup(response.read(), 'lxml')
    counts = Counter()
    school_rows = []
    for heading in soup.find_all('h3'):
        event = EVENTS.get(heading.get_text(' ', strip=True))
        if not event or not heading.parent:
            continue
        section = heading.parent.find_next_sibling('div', class_='performance-list')
        if not section:
            raise ValueError(f'Missing performance list for {school} {event}')
        for item in section.select('.performance-list-row'):
            values = {cell.get('data-label'): cell.get_text(' ', strip=True)
                      for cell in item.find_all('div', recursive=False) if cell.get('data-label')}
            athlete, mark, meet = values.get('Athlete',''), values.get('Time',values.get('Mark','')), values.get('Meet','')
            if not (athlete and mark and meet):
                raise ValueError(f'Incomplete row: {school} {event}: {values}')
            mark_link = item.find('div', attrs={'data-label': 'Time' if event != 'Long Jump' else 'Mark'})
            href = mark_link.find('a', href=True) if mark_link else None
            source_url = href['href'] if href else url
            date = datetime.strptime(values['Meet Date'], '%b %d, %Y').strftime('%Y-%m-%d')
            performance = re.sub(r'm$', '', mark) if event == 'Long Jump' else mark
            school_rows.append(dict(athlete=athlete, school=school, conference='SEC',
                event=event, season=YEAR, class_year=values.get('Year',''),
                birth_date='', age_at_meet='', performance=performance,
                unit='m' if event == 'Long Jump' else 'seconds', meet=meet,
                meet_date=date, round='', place=values.get('Place',''),
                wind=values.get('Wind',''), indoor_outdoor='Outdoor',
                source_url=source_url, data_status='TFRRS all_performances'))
            counts[event] += 1
    print(school, len(school_rows), dict(counts), url, flush=True)
    if not school_rows and YEAR != 2020:
        raise ValueError(f'Missing school or event coverage: {school} {counts}')
    # The TFRRS all-performances page lists individual long-jump attempts.
    # Keep the best mark for each athlete in each meet competition, matching
    # the repository's one-result-per-competition convention.
    best_jumps = {}
    kept = []
    for row in school_rows:
        if row['event'] != 'Long Jump':
            kept.append(row)
            continue
        key = (row['athlete'], row['meet_date'], row['source_url'])
        if key not in best_jumps or float(row['performance']) > float(best_jumps[key]['performance']):
            best_jumps[key] = row
    school_rows = kept + list(best_jumps.values())
    classes = {}
    for row in school_rows:
        if row['class_year']:
            classes.setdefault(row['athlete'], set()).add(row['class_year'])
    for row in school_rows:
        known = classes.get(row['athlete'], set())
        if not row['class_year'] and len(known) == 1:
            row['class_year'] = next(iter(known))
    unique = {}
    for row in school_rows:
        key = (row['athlete'], row['event'], row['meet'], row['meet_date'],
               row['performance'], row['wind'], row['source_url'])
        unique.setdefault(key, row)
    school_rows = list(unique.values())
    rows.extend(school_rows)
    time.sleep(0.3)

rows.sort(key=lambda r: (r['school'], r['meet_date'], r['event'], r['athlete'], r['performance']))
out = Path('data/processed') / f'sec_{YEAR}.csv'
out.parent.mkdir(parents=True, exist_ok=True)
with out.open('w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=FIELDS, lineterminator='\n')
    writer.writeheader()
    writer.writerows(rows)
for school in SCHOOLS:
    school_path = Path('data/raw') / f"{school.lower().replace(' ', '_')}_{YEAR}.csv"
    school_path.parent.mkdir(parents=True, exist_ok=True)
    with school_path.open('w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS, lineterminator='\n')
        writer.writeheader()
        writer.writerows(row for row in rows if row['school'] == school)
print('TOTAL',len(rows), 'BY SCHOOL',dict(Counter(r['school'] for r in rows)), 'BY EVENT',dict(Counter(r['event'] for r in rows)))
