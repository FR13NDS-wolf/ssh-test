import sqlite3

def delete_book():
    conn = sqlite3.connect('info.db')
    cursor = conn.cursor()

    try:
        cursor.execute("DELETE FROM books WHERE name=?", ("活着",))
        conn.commit()

        if cursor.rowcount > 0:
            print("删除成功！")
        else:
            print("未找到这本书")

    except sqlite3.Error as e:
        print(f"删除数据时出错: {e}")
    finally:
        conn.close()


if __name__ == "__main__":
    delete_book()
