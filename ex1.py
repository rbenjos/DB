import csv
from io import TextIOWrapper
from zipfile import ZipFile

MAX_LINES = 10000

# opens file for olympics table.
# CHANGE!
Olympics = open("Olympics.csv", 'w',)
Athlete = open("Athlete.csv", 'w',)
Team = open("Team.csv", 'w',)
Event = open("Event.csv", 'w',)
Competed_at = open("Competed_at.csv", 'w',)

outwriter_o = csv.writer(Olympics, delimiter=",", quoting=csv.QUOTE_NONE)
outwriter_a = csv.writer(Athlete, delimiter=",", quoting=csv.QUOTE_NONE)
outwriter_t = csv.writer(Team, delimiter=",", quoting=csv.QUOTE_NONE)
outwriter_e = csv.writer(Event, delimiter=",", quoting=csv.QUOTE_NONE)
outwriter_c = csv.writer(Competed_at, delimiter=",", quoting=csv.QUOTE_NONE)

# process_file goes over all rows in original csv file, and sends each row to process_row()
# DO NOT CHANGE!!!
def process_file():
    counter = 0
    with ZipFile('athlete_events.csv.zip') as zf:
        with zf.open('athlete_events.csv', 'r') as infile:
            reader = csv.reader(TextIOWrapper(infile, 'utf-8'))
            for row in reader:
                # pre-process : remove all quotation marks from input and turns NA into null value ''.
                row = [v.replace(',','') for v in row]
                row = [v.replace("'",'') for v in row]
                row = [v.replace('"','') for v in row]
                row = [v if v != 'NA' else "" for v in row]
                # in 'Sailing', the medal winning rules are different than the rest of olympic games, so they are discarded.
                if row[12] == "Sailing":
                    continue
                process_row(row)
                counter += 1
                if counter == MAX_LINES:
                    break


# process_row should splits row into the different csv table files
# CHANGE!!!
def process_row(row):
    outwriter_a.writerow([row[0],row[1],row[2],row[4],row[5]])
    outwriter_t.writerow([row[6],row[7]])
    outwriter_o.writerow([row[9],row[10],row[11]])
    outwriter_e.writerow([row[13],row[12],row[10],row[9]])
    outwriter_c.writerow([row[0],row[13],row[9],row[10],row[14],row[3]])

# return the list of all tables
# CHANGE!!!
def get_names():
    return ["Athlete",'Team','Olympics','Event','Competed_at']


if __name__ == "__main__":
    process_file()

