package com.example.myapplication003.entity;

public class Course {
    // 1. 课程基础信息
    public String courseId;       // 课程ID
    public String courseName;     // 课程名称
    public String teacher;        // 授课教师
    public double credit;         // 学分
    public String time;           // 上课时间（如“周一3-4节”）
    public String location;       // 上课地点（如“实验楼A203”）

    // 2. 容量信息
    public int capacity;          // 容量上限
    public int selectedCount;     // 已选人数

    // 3. 分类与状态
    public String type;           // 课程类型（公共课/专业课/选修课）
       // 当前用户是否已选（仅用于UI状态）

    // 空构造函数（保险起见留着，某些框架或反射会用到）
    public Course() {
    }

    // 全参构造函数（最常用，用于造假数据或从数据库读取时直接赋值）
    public Course(String courseId, String courseName, String teacher, double credit,
                  String time, String location, int capacity, int selectedCount,
                  String type) {
        this.courseId = courseId;
        this.courseName = courseName;
        this.teacher = teacher;
        this.credit = credit;
        this.time = time;
        this.location = location;
        this.capacity = capacity;
        this.selectedCount = selectedCount;
        this.type = type;

    }
}