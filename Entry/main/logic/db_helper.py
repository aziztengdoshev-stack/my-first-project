import sqlite3
from django.conf import settings

DB_PATH = settings.DATABASES['default']['NAME']

def query_db(sql, params=(), fetchone=False):
    with sqlite3.connect(DB_PATH) as conn:
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute(sql, params)
        conn.commit()
        if fetchone:
            res = cursor.fetchone()
            return dict(res) if res else None
        return [dict(r) for r in cursor.fetchall()]
    
def get_all_classes(self):
    sql = """
        SELECT sc.id, sc.class_name, au.first_name, au.last_name 
        FROM school_classes sc
        LEFT JOIN auth_user au ON sc.teacher_id = au.id
    """
    return self.query_db(sql)