
import json
from datetime import datetime

GUESTBOOK_ENTRIES_FILE = "entries.json"
entries = []

def init():
    global entries,GUESTBOOK_ENTRIES_FILE
    try:
        f = open(GUESTBOOK_ENTRIES_FILE)
        entries = json.loads(f.read())
        f.close()
    except:
        entries = []

def get_entries():
    global entries
    return entries

def add_entry(name, text):
    global entries, GUESTBOOK_ENTRIES_FILE
    now = datetime.now()
    # time_string = now.strftime("%b %d, %Y %-I:%M %p")
    # if you have an error using this format, just use
    time_string = str(now)
    try:
        with open(GUESTBOOK_ENTRIES_FILE,'r') as f:
            content=json.load(f)
            next_id=len(content)
            print(id_num)
    except:
        print('Error!')
    entry = {"author": name, "text": text, "timestamp": time_string, "id":str(next_id)}
    entries.insert(0, entry) ## add to front of list
    try:
        f = open(GUESTBOOK_ENTRIES_FILE, "w")
        dump_string = json.dumps(entries)
        f.write(dump_string)
        f.close()
    except:
        print("ERROR! Could not write entries to file.")

def delete_entry(id):
    global entries, GUESTBOOK_ENTRIES_FILE
    try:
        with open(GUESTBOOK_ENTRIES_FILE,'r+') as f:
            content=json.load(f)
            for i in content:
                if id == int(i['id']):
                    content.remove(i)
            f.seek(0)
            f.truncate()
            json.dump(content, f)
        f = open(GUESTBOOK_ENTRIES_FILE)
        entries = json.loads(f.read())
        f.close()
        # with open(GUESTBOOK_ENTRIES_FILE) as f:
        #     content=json.load(f)
        #     print(content)
        print('Deleted id:',id)
    except:
        print('Error!')

# delete_entry(7)
