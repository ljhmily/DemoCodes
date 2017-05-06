#!/usr/bin/python3
# coding=utf-8

import sqlite3


# 连接
# 表
# 录入学生信息
# 选课
# 查询学生信息
# 按学生查询选课
# 按课程查询课程信息
# 查询选择课程的学生列表

class Student:
    def __init__(self):
        pass

    def dbaccess(self):
        connect = sqlite3.connect('studb.sqlite', timeout=3)
        return connect

    def createdb(self):
        sql = ["""
               CREATE TABLE Student(
                   ID INTEGER PRIMARY KEY   AUTOINCREMENT,
                   StuId         INTEGER     NOT NULL,
                   NAME           TEXT      NOT NULL,
                   CLASS            INT       NOT NULL);
                   """,
               """
               CREATE TABLE Course(
                   ID INTEGER PRIMARY KEY   AUTOINCREMENT,
                   CourseId       INT       NOT NULL,
                   Name           TEXT      NOT NULL,
                   Teacher            TEXT       NOT NULL,
                   Classroom            TEXT      NOT NULL,
                   StartTime             CHAR(11),
                   EndTime                CHAR(11));
                   """,
               """
               CREATE TABLE Xuanke(
                   ID INTEGER PRIMARY KEY   AUTOINCREMENT,
                   StuId          INT         NOT NULL,
                   CourseId          INT         NOT NULL);
               """]
        conn = self.dbaccess()
        for s in sql:
            conn.execute(s)
        conn.commit()

    def insert(self):
        conn = self.dbaccess()
        stu_id = input("请输入学生编号: ")
        cur = conn.execute("select stuid from student WHERE stuid = %s;" % stu_id)
        row = cur.fetchone()
        if row:
            print("编号已存在, 请重新输入")
            self.insert()
        else:
            stu_name = str(input("请输入学生姓名: "))
            stu_class = input("请输入学生班级: ")
            sql = "INSERT INTO student (stuid, name, class) values (%s, '%s', %s);" % (stu_id, stu_name, stu_class)
            conn.execute(sql)
            conn.commit()
            print("学生信息登记完成")

    def xuenke(self):
        conn = self.dbaccess()
        stu_id = input("请输入选课的学生编号: \n")
        cur = conn.execute("select stuid from Student WHERE StuId = %s;" % stu_id)
        if cur.fetchone():
            print("课程列表: ")
            cur = conn.execute("SELECT courseid, name, teacher, classroom, starttime, endtime FROM Course;")
            for row in cur:
                print("课程：", row)
            cou_id = input("请输入选择的课程编号: \n")
            cur1 = conn.execute("SELECT courseid FROM Course WHERE CourseId = %s;" % cou_id)
            if cur1.fetchone():
                cur2 = conn.execute(
                    "SELECT courseid FROM Xuanke WHERE CourseId = %s AND StuId = %s;" % (cou_id, stu_id))
                if cur2.fetchone():
                    print("课程已选择, 不能重复选择")
                else:
                    conn.execute("INSERT INTO Xuanke (StuId, CourseId) VALUES (%s, %s);" % (stu_id, cou_id))
                    conn.commit()
                    print("课程选择成功")
            else:
                print("所选课程不存在")
        else:
            print("该学生编号不存在, 请核对后输入")
            self.xuenke()

    def stu_id_search(self):
        conn = self.dbaccess()
        stu_id = input("请输入查询的学生编号: \n")
        cur = conn.execute("SELECT * FROM Student WHERE StuId = %s;" % stu_id)
        row = cur.fetchone()
        if row:
            print("学生信息如下: ")
            print(row)
        else:
            print("该学生编号不存在, 请核对后输入")
            self.stu_id_search()

    def stu_id_course(self):
        conn = self.dbaccess()
        stu_id = input("请输入查询的学生编号: \n")
        cur = conn.execute("SELECT * FROM Student WHERE StuId = %s;" % stu_id)
        row = cur.fetchone()
        if row:
            cur1 = conn.execute(
                "SELECT s.StuId,s.NAME, c.* FROM Student s, Xuanke x, Course c WHERE s.StuID = %s AND s.StuId = x.StuId and x.CourseId = c.CourseId;" % stu_id)
            for row in cur1:
                print(row)
        else:
            print("该学生编号不存在, 请核对后输入")
            self.stu_id_course()

    def course_stu_id(self):
        conn = self.dbaccess()
        course_id = input("请输出查询的课程编号: \n")
        cur = conn.execute("SELECT courseid FROM Xuanke WHERE CourseId = %s;" % course_id)
        if cur.fetchone():
            cur1 = conn.execute(
                "SELECT s.StuId, s.NAME, x.CourseId, s.CLASS FROM student s, xuanke x WHERE x.CourseId = %s and x.StuId = s.StuId;" % course_id)
            for row in cur1:
                print(row)

    def menu(self):
        print('1.进入学生信息系统(学生信息录入)')
        print('2.进入学生选课系统(学生选课操作)')
        print('3.进入学生选课信息系统(学生信息查询和选课情况查询)')
        print('4.退出程序')

    def student(self):
        print('1.录入学生信息')
        print('2.返回主菜单')

    def Course(self):
        print('1.开始选课')
        print('2.返回主菜单')

    def information(self):
        print('1.按学号查询学生信息')
        print('2.按学号查看学生选课课程列表')
        print('3.按课程号查看选课学生列表')
        print('4.返回主菜单')


if __name__ == "__main__":
    student = Student()
    # student.createdb()
    # student.insert()
    # student.xuenke()
    # student.stu_id_course()
    # student.course_stu_id()
    while True:
        student.menu()
        x = input("请选择操作类型\n")
        if x == "1":
            student.student()
            stu = input("学生信息录入菜单, 请继续选择\n")
            if stu == "1":
                student.insert()
                continue
            elif stu == "2":
                continue
            else:
                print("非法选项, 请重新输入")
                continue
        elif x == "2":
            student.Course()
            cour = input("课程选择菜单\n")
            if cour == "1":
                student.xuenke()
                continue
            elif cour == "2":
                continue
            else:
                print("非法选项, 请重新输入")
                continue
        elif x == "3":
            student.information()
            info = input("查询菜单\n")
            if info == "1":
                student.stu_id_search()
                continue
            elif info == "2":
                student.stu_id_course()
            elif info == "3":
                student.course_stu_id()
                continue
            elif info == "4":
                continue
            else:
                print("非法选项, 请重新输入")
                continue
        elif x == "4":
            print("谢谢使用")
            exit(0)
        else:
            print("非法选项, 请重新输入")
            continue
