package com.example.myapplication003.entity;

public class Selection {
    // 1. 选课记录基础信息
    public int selectionid;           // 记录ID（主键，自增）
    public int userId;       // 关联的用户ID
    public String courseId;  // 关联的课程ID
    public boolean isSelected;
public double score;
    // 空构造函数（保险起见留着）
    public Selection() {
    }

    // 全参构造函数（用于创建记录或从数据库读取时赋值）
    public Selection(int selectionid, int userId, double score,String courseId, boolean isSelected) {
        this.selectionid = selectionid;
        this.userId = userId;
        this.courseId = courseId;
        this.score=score;
        this.isSelected = isSelected;
    }

    // 为了方便插入数据，再提供两个参数的构造函数（不需要传id，因为数据库会自动生成）
    public Selection(int userId, String courseId) {
        this.userId = userId;
        this.courseId = courseId;
    }
}