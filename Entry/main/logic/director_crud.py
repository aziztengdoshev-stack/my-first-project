from .db_helper import query_db

class DirectorCRUD:
    def get_all_teachers(self):
        sql = "SELECT id, first_name, last_name, username FROM auth_user WHERE is_staff = 1"
        return query_db(sql)

    def add_teacher(self, first_name, last_name, username, password):
        sql = """
            INSERT INTO auth_user (first_name, last_name, username, password, is_staff, is_active, is_superuser, date_joined)
            VALUES (?, ?, ?, ?, 1, 1, 0, datetime('now'))
        """
        return query_db(sql, (first_name, last_name, username, password))

    def delete_teacher(self, teacher_id):
        sql = "DELETE FROM auth_user WHERE id = ?"
        return query_db(sql, (teacher_id,))

    def get_all_classes(self):
        return query_db("SELECT * FROM school_classes")

    def add_teacher(self, first_name, last_name, username, password):
        sql = """
            INSERT INTO auth_user 
            (password, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined)
            VALUES (?, 0, ?, ?, ?, '', 1, 1, datetime('now'))
        """
        return query_db(sql, (password, username, first_name, last_name))
    
    def delete_class(self, class_id):
        query_db("DELETE FROM classes WHERE id=?", (class_id,))
    
    def update_teacher(self, teacher_id, first_name, last_name, username):
        sql = "UPDATE auth_user SET first_name = ?, last_name = ?, username = ? WHERE id = ?"
        return query_db(sql, (first_name, last_name, username, teacher_id))
    
    def get_teacher_info(self, teacher_id):
        sql = "SELECT id, first_name, last_name, username FROM auth_user WHERE id = ?"
        result = query_db(sql, (teacher_id,))
        
        if result:
            return result[0]
        return None

    def get_class_info(self, class_id):
        sql = "SELECT * FROM school_classes WHERE id = ?"
        return query_db(sql, (class_id,), fetchone=True)

    def get_students_by_class(self, class_id):
        sql = "SELECT * FROM students WHERE class_id = ?"
        return query_db(sql, (class_id,))