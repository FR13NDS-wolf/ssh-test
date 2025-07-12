import sqlite3


def create_student_table():
    conn = sqlite3.connect('student.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        student_id TEXT NOT NULL UNIQUE,
        course TEXT NOT NULL,
        score REAL NOT NULL
    )
    ''')
    conn.commit()
    conn.close()
    print("已连接到数据库")
    print("数据表的建立成功")


def add_student():
    print("\n请输入学生信息：")
    name = input("请输入学生姓名：")
    student_id = input("请输入学号：")
    course = input("请输入课程名称：")
    score = input("请输入成绩：")

    conn = sqlite3.connect('student.db')
    cursor = conn.cursor()

    try:
        cursor.execute('''
        INSERT INTO students (name, student_id, course, score)
        VALUES (?, ?, ?, ?)
        ''', (name, student_id, course, score))
        conn.commit()
        print("成绩记录插入成功")
    except sqlite3.IntegrityError:
        print("错误：该学号已存在！")
    except sqlite3.Error as e:
        print(f"添加数据时出错: {e}")
    finally:
        conn.close()


def query_student():#查询单个学生
    student_id = input("\n请输入要查询的学号：")

    conn = sqlite3.connect('student.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students WHERE student_id=?", (student_id,))
    student = cursor.fetchone()

    if student:
        print("查询结果如下：")
        print(f"[{student}]")
    else:
        print("未找到该学号的学生")

    conn.close()


def list_all_students():#列出所有学生信息
    conn = sqlite3.connect('student.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    print("查询结果如下：")
    for student in students:
        print(f"[{student}]")

    conn.close()


def delete_student():
    student_id = input("\n请输入要删除成绩记录的学号：")

    conn = sqlite3.connect('student.db')
    cursor = conn.cursor()

    cursor.execute("DELETE FROM students WHERE student_id=?", (student_id,))
    conn.commit()

    if cursor.rowcount > 0:
        print("成绩记录删除成功")
    else:
        print("未找到该学号的学生")

    conn.close()


def show_menu():
    print("******************************")
    print("1. 插入学生成绩记录")
    print("2. 根据学号查询学生成绩")
    print("3. 显示所有学生信息")
    print("4. 删除指定学号学生成绩记录")
    print("5. 退出")
    print("******************************")


def main():
    create_student_table()

    while True:
        show_menu()
        choice = input("\n请选择操作(1-5): ")

        if choice == '1':
            add_student()
        elif choice == '2':
            query_student()
        elif choice == '3':
            list_all_students()
        elif choice == '4':
            delete_student()
        elif choice == '5':
            print("已退出程序！！！")
            break
        else:
            print("无效的输入，请重新选择！")


if __name__ == "__main__":
    main()

