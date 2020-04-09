wget -O Data.csv "https://docs.google.com/spreadsheets/d/1428VV2rRFcZaWi-rsagQ16CMOkQYM6wBT3tbo8RjfH4/export?format=csv"
python3 gdocs2hugo/transformer.py
rm -r hugo_site/content/talk
mv talk hugo_site/content/talk
rm hugo_site/static/talks_calendar.ical
mv talks_calendar.ical hugo_site/static/
hugo -s hugo_site
git add -A
git commit -m "Routine update"
git push