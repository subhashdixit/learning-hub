"""SQLite teaching fixture and expected-query checks. No external database needed."""
from pathlib import Path
import sqlite3,json
con=sqlite3.connect(':memory:');con.executescript(Path(__file__).with_name('setup.sql').read_text())
cases=json.loads(Path(__file__).with_name('query-cases.json').read_text())
for c in cases:
    actual=con.execute(c['sql']).fetchall();expected=[tuple(x) for x in c['expected']]
    assert actual==expected,(c['title'],actual,expected)
print('Passed',len(cases),'SQL query checks on local SQLite',sqlite3.sqlite_version)
