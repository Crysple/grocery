import os
import string
import psycopg2
import random
from faker import Faker

USER = ''
HOST = ''
PASSWORD = ''

try:
    conn = psycopg2.connect("dbname='proj1part2' user='{}' host='{}' password='{}'".format(USER, HOST, PASSWORD))
except:
    print("Error: unable to connect to the database")
    raise


# Database operation
def select_from(columns, table):
    cur = conn.cursor()
    if isinstance(columns, list):
        columns = ','.join(columns)
    sql = "SELECT {} FROM {}".format(columns, table)
    cur.execute(sql)
    return cur.fetchall()

def insert_into(values, table):
    '''Insert values into table
    values: a list of value according to order in the database'''
    cur = conn.cursor()
    if type(values) not in [list, tuple]:
        values = (values, )
    values = tuple(values)
    n_value = len(values)
    try:
        sql = "INSERT INTO {} VALUES ({})".format(table, "%s"+",%s"*(n_value-1))
        cur.execute(sql, values)
    except:
        print("Error: Insert Failed\n With SQL: {}\n Values:{}".format(sql, values))
        raise
    
def mul_insert_into(values_set, table):
    for values in values_set:
        insert_into(values, table)

def extract_first_column(res, trans=lambda x:x):
    return [trans(row[0]) for row in res]


# Populate Functions

def random_string(stringLength=-1):
    """Generate a random string of fixed length """
    if stringLength == -1:
        stringLength = random.randint(3,8)
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

def generate_src_code_urls(nums=10):
    urls = []
    for _ in range(nums):
        url = 'www.github.com/{}/{}'.format(random_string(), random_string())
        urls += url,
    return urls

def generate_dirs(num=10, level=4):
    """Generate a list of directory path
    num: length of list
    level: level of each path
    """
    dirs = []
    for _ in range(num):
        path = "/home/"
        for _ in range(level):
            path = os.path.join(path, random_string())
        dirs += path,
    return dirs

def generate_image_path(num=10, level=4):
    """Generate a list of image path
    num: length of list
    level: level of each path
    """
    dirs = generate_dirs(num=10, level=4)
    extension = ['.png', '.jpg', '.tiff', '.jpeg']
    paths = [os.path.join(d, random_string()+random.sample(extension, 1)[0]) for d in dirs]
    return paths

def generate_description(prefix='', num=17):
    return prefix + ' '.join([random_string() for _ in range(num)])
    
def populate_hasSkill():
    ids = extract_first_column(select_from(['user_id'], 'person'), int)
    skill_names = extract_first_column(select_from(['skill_name'], 'skill'))
    mul_insert_into([*zip(ids[:16], skill_names[:16])], 'hasSkill')
    conn.commit()

def populate_projects(num):
    #project_ids = [*range(12)]
    owner_ids = extract_first_column(select_from(['user_id'], 'person'), int)
    #contribute_ids = list(owner_ids)
    src_code_links = generate_src_code_urls(num)
    image_path = generate_image_path(num)
    
    for pid in range(num):
        description = generate_description('A project for ')
        values = (pid, owner_ids[pid], description, src_code_links[pid], image_path[pid])
        insert_into(values, 'project')
    conn.commit()

def populate_tasks(num):
    pids = extract_first_column(select_from(['proj_id'], 'project'), int)
    fake = Faker()
    for pid in pids:
        for tid in range(num):
            description = generate_description('A task aims at ')
            ddl = str(fake.date_time_between(start_date='+1m', end_date='+1y'))
            values = (tid, ddl, description, pid)
            insert_into(values, 'task')
    conn.commit()

def populate_require_skill(num):
    skill_names = extract_first_column(select_from(['skill_name'], 'skill'))
    pids = extract_first_column(select_from(['proj_id'], 'project'), int)
    tids = [*set(extract_first_column(select_from(['task_id'], 'task'), int))]
    
    values_added = set()
    for _ in range(num):
        while True:
            skill = random.sample(skill_names, 1)[0]
            pid = random.sample(pids, 1)[0]
            tid = random.sample(tids, 1)[0]
            values = (tid, pid, skill)
            if values not in values_added:
                values_added.add(values)
                break
        insert_into(values, 'requireSkill')
    conn.commit()

def populate_assigned_and_contribute(num):
    pids = extract_first_column(select_from(['proj_id'], 'project'), int)
    tids = [*set(extract_first_column(select_from(['task_id'], 'task'), int))]
    contrib_ids = extract_first_column(select_from(['contrib_id'], 'Contributor'), int)
    
    assigned_added = set()
    contri_added = set()
    for _ in range(num):
        while True:
            contrib_id = random.sample(contrib_ids, 1)[0]
            pid = random.sample(pids, 1)[0]
            tid = random.sample(tids, 1)[0]
            assigned = (tid, pid, contrib_id)
            if assigned not in assigned_added:
                assigned_added.add(assigned)
                break
        insert_into(assigned, 'Assigned')
        contri = (pid, contrib_id)
        if contri not in contri_added:
            insert_into(contri, 'Contributes')
            contri_added.add(contri)
    conn.commit()

def get_owner2contri():
    cur = conn.cursor()
    sql = "SELECT owner_id, contrib_id FROM project NATURAL JOIN contributes"
    cur.execute(sql)
    owner_has_contri = dict()
    for owner_id, contrib_id in cur.fetchall():
        owner_id, contrib_id = int(owner_id), int(contrib_id)
        if owner_id not in owner_has_contri:
            owner_has_contri[owner_id] = set()
        owner_has_contri[owner_id].add(contrib_id)
    return owner_has_contri
    
    
def populate_evalutes_and_evalution(num):
    owner_has_contri = get_owner2contri()
    added = set()
    for eval_id in range(num):
        score = random.randint(0, 9)
        comment = generate_description('', 30)
        evaluation = (eval_id, score, comment)
        
        while True:
            owner_id = random.sample(owner_has_contri.keys(), 1)[0]
            contrib_id = random.sample(owner_has_contri[owner_id], 1)[0]
            evaluates = (eval_id, owner_id, contrib_id)
            if evaluates[-2:] not in added:
                added.add(evaluates[-2:])
                break
        insert_into(evaluation, 'evaluation')
        insert_into(evaluates, 'evaluates')
    conn.commit()


if __name__ == '__main__':
    populate_hasSkill()
    populate_projects(10)
    populate_require_skill(200)
    populate_assigned_and_contribute(300)
    populate_evalutes_and_evalution(120)
