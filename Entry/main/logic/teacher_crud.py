from .db_helper import query_db

class TeacherCRUD:
    def auth_teacher(self, name, surname, password):
        user = query_db("SELECT * FROM teachers WHERE name=? AND surname=? AND password=?", 
                        (name, surname, password), fetchone=True)
        if user and user['status'] == 1:
            return user
        return None

    def get_class_list(self, class_id):
        return query_db("SELECT id, name, surname FROM students WHERE class_id=? AND status=1", (class_id,))

    def post_grade(self, student_id, subject, grade):
        if 2 <= int(grade) <= 5:
            query_db("INSERT INTO grades (student_id, subject, grade) VALUES (?, ?, ?)", 
                     (student_id, subject, grade))
            return True
        return False