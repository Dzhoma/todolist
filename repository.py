from database import db, cursor

class Data():
    def find_all(self):
        todos = cursor.execute("SELECT * FROM tasks").fetchall()
        return todos

    def add_one(self, todo):
        cursor.execute("insert into tasks(name, done) values (?, ?)", (todo["name"], todo["done"]))
        db.commit()

    def drop_one(self, id):
        cursor.execute("delete from tasks where id = ?", id)
        db.commit()

    def update_one(self, todo):
        cursor.execute("update tasks set done = ? where id = ?", (todo[2], todo[0]))
        db.commit()

    def find_one(self, id):
        todo = cursor.execute("select * from tasks where id = ?", id).fetchone()
        return list(todo)