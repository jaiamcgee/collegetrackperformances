#!/usr/bin/env python3
"""Preserve sourced ACC rows absent from the TFRRS rebuild.

Run after build_acc_all_meets.py for each year. The baseline is the repository
revision before the 2016-2026 ACC replacement; its rows remain in Git history.
"""
import csv
import re
import subprocess
from collections import Counter
from datetime import date
from difflib import SequenceMatcher
from pathlib import Path

BASELINE = '97fbabf86c9592538ce293bce8f7e07b1aa52870'
SCHOOLS = ['Clemson', 'Duke', 'Florida State', 'Virginia', 'Stanford']
FIELDS = ['athlete','school','conference','event','season','class_year',
          'birth_date','age_at_meet','performance','unit','meet','meet_date',
          'round','place','wind','indoor_outdoor','source_url','data_status']

def name(s):
    return tuple(sorted(re.sub(r'[^a-z ]', '', s.lower()).split()))

def seconds(s):
    try:
        if ':' in s:
            minutes, rest = s.split(':', 1)
            return round(int(minutes) * 60 + float(rest), 3)
        return round(float(s), 3)
    except (ValueError, TypeError):
        return s

def near_date(a, b):
    try:
        return abs((date.fromisoformat(a) - date.fromisoformat(b)).days) <= 4
    except ValueError:
        return False

def same_competition(a, b):
    if a['school'] != b['school'] or a['event'] != b['event'] or name(a['athlete']) != name(b['athlete']):
        return False
    if not near_date(a['meet_date'], b['meet_date']):
        return False
    a_meet = re.sub(r'[^a-z0-9]', '', a['meet'].lower())
    b_meet = re.sub(r'[^a-z0-9]', '', b['meet'].lower())
    similar = SequenceMatcher(None, a_meet, b_meet).ratio() >= 0.6
    if a['event'] == 'Long Jump':
        return similar or a['meet_date'] == b['meet_date']
    return seconds(a['performance']) == seconds(b['performance']) and (similar or a['meet_date'] == b['meet_date'])

audit = []
for year in range(2016, 2027):
    path = Path(f'data/processed/acc_{year}.csv')
    with path.open(newline='', encoding='utf-8') as f:
        rows = list(csv.DictReader(f))
    baseline_path = f'data/processed/acc_{year}.csv'
    try:
        source = subprocess.check_output(['git', 'show', f'{BASELINE}:{baseline_path}'], text=True, stderr=subprocess.DEVNULL)
        old = list(csv.DictReader(source.splitlines()))
    except subprocess.CalledProcessError:
        old = []
    added = 0
    no_source = 0
    matched = 0
    for candidate in old:
        if not candidate.get('source_url', '').startswith('http'):
            no_source += 1
            continue
        if any(same_competition(candidate, row) for row in rows):
            matched += 1
            continue
        row = {field: candidate.get(field, '') for field in FIELDS}
        row['conference'] = 'ACC'
        row['indoor_outdoor'] = 'Outdoor'
        row['data_status'] = 'legacy_source_needs_review'
        for current in rows:
            if current['school'] == row['school'] and name(current['athlete']) == name(row['athlete']):
                row['athlete'] = current['athlete']
                if current['class_year']:
                    row['class_year'] = current['class_year']
                break
        rows.append(row)
        added += 1
    rows.sort(key=lambda row: (row['school'], row['meet_date'], row['event'], row['athlete'], row['performance']))
    with path.open('w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS, lineterminator='\n')
        writer.writeheader()
        writer.writerows(rows)
    for school in SCHOOLS:
        school_path = Path('data/raw/acc') / str(year) / f"{school.lower().replace(' ', '_')}_{year}.csv"
        school_path.parent.mkdir(parents=True, exist_ok=True)
        with school_path.open('w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=FIELDS, lineterminator='\n')
            writer.writeheader()
            writer.writerows(row for row in rows if row['school'] == school)
    audit.append({'season': year, 'old_rows': len(old), 'tfrrs_rows': len(rows)-added,
                  'legacy_rows_added': added, 'old_rows_matched': matched,
                  'old_rows_without_source': no_source, 'final_rows': len(rows),
                  'schools_with_rows': len(set(row['school'] for row in rows))})
    print(year, audit[-1])

report = Path('data/processed/acc_2016_2026_audit.csv')
with report.open('w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=list(audit[0]), lineterminator='\n')
    writer.writeheader()
    writer.writerows(audit)
