from .db_helper import query_db

class StudentCRUD:
    def get_profile(self, sid):
        return query_db("SELECT * FROM students WHERE id=?", (sid,), fetchone=True)

    def get_grades(self, sid):
        return query_db("SELECT subject, grade FROM grades WHERE student_id=?", (sid,))

    def get_classmates(self, class_id, my_id):
        return query_db("SELECT id, name, surname FROM students WHERE class_id=? AND status=1 AND id != ?", (class_id, my_id))
    
    def save_test_result(self, sid, subject, grade):
        query_db("INSERT INTO grades (student_id, subject, grade) VALUES (?, ?, ?)", (sid, subject, grade))