package com.example.myapplication003;

import android.content.Context;
import android.database.sqlite.SQLiteDatabase;
import android.database.sqlite.SQLiteOpenHelper;

public class MyDbHelper extends SQLiteOpenHelper {
//    MyDbHelper 继承 SQLiteOpenHelper，
//    在 onCreate(SQLiteDatabase db) 里用 db.execSQL(建表SQL) 执行建表语句。
     private static final String db_name="app01.db";
     private static final int db_version=3;
     private static final String sql_create_table_user="create table if not exists table_user" +
             "(userid integer primary key autoincrement,username text not null,passwd text not null," +
             "name text not null ,college text not null,major text not null,banji text not null)" ;
     private static final String sql_create_table_course="create table if not exists table_course " +
             "(courseid integer primary key autoincrement,coursename text not null,teacher text not null," +
             "credit double not null ,time text not null , location text not null ,capacity integer not null , type text not null ," +
             "selectedCount  integer not null ,isSelected boolean not null )";
     private static final String sql_create_table_selection="create table if not exists table_selection   " +
             "(selectionid integer primary key autoincrement," +
             "userid integer not null, " +
             "score double default 0, courseid integer not null,unique(userid,courseid))" ;

     public MyDbHelper(Context context){

         super(context,db_name,null,db_version);
     }
     @Override
    public void onCreate(SQLiteDatabase db){

         db.execSQL(sql_create_table_user);
         db.execSQL(sql_create_table_course);
         db.execSQL(sql_create_table_selection);
         // ===== 1 条用户 =====
         db.execSQL("insert into table_user(username,passwd,name,college,major,banji) "
                 + "values('2024001','123456','张三','计算机学院','软件工程','1班')");

// ===== 10 条课程 =====
         db.execSQL("insert into table_course(coursename,teacher,credit,time,location,capacity,type,selectedCount,isSelected) "
                 + "values('Java程序设计','张老师',3.0,'周一3-4节','实验楼A203',60,'专业课',45,0)");

         db.execSQL("insert into table_course(coursename,teacher,credit,time,location,capacity,type,selectedCount,isSelected) "
                 + "values('数据结构','李老师',4.0,'周一3-4节','实验楼A203',60,'专业课',58,0)");

         db.execSQL("insert into table_course(coursename,teacher,credit,time,location,capacity,type,selectedCount,isSelected) "
                 + "values('计算机网络','王老师',3.0,'周二1-2节','第一教学楼101',50,'专业课',30,0)");

         db.execSQL("insert into table_course(coursename,teacher,credit,time,location,capacity,type,selectedCount,isSelected) "
                 + "values('操作系统','赵老师',4.0,'周二3-4节','实验楼B305',45,'专业课',20,0)");

         db.execSQL("insert into table_course(coursename,teacher,credit,time,location,capacity,type,selectedCount,isSelected) "
                 + "values('数据库原理','陈老师',3.0,'周三1-2节','第一教学楼202',60,'专业课',40,0)");

         db.execSQL("insert into table_course(coursename,teacher,credit,time,location,capacity,type,selectedCount,isSelected) "
                 + "values('大学英语','刘老师',2.0,'周三5-6节','外语楼301',80,'公共课',75,0)");

         db.execSQL("insert into table_course(coursename,teacher,credit,time,location,capacity,type,selectedCount,isSelected) "
                 + "values('高等数学','孙老师',5.0,'周四1-2节','第一教学楼105',100,'公共课',0,0)");

         db.execSQL("insert into table_course(coursename,teacher,credit,time,location,capacity,type,selectedCount,isSelected) "
                 + "values('离散数学','周老师',3.0,'周四3-4节','第一教学楼106',60,'专业课',0,0)");

         db.execSQL("insert into table_course(coursename,teacher,credit,time,location,capacity,type,selectedCount,isSelected) "
                 + "values('软件工程','吴老师',3.0,'周五1-2节','实验楼C201',55,'专业课',0,0)");

         db.execSQL("insert into table_course(coursename,teacher,credit,time,location,capacity,type,selectedCount,isSelected) "
                 + "values('人工智能导论','郑老师',2.0,'周五3-4节','实验楼C202',40,'选修课',0,0)");
     }
     @Override
    public void onUpgrade(SQLiteDatabase db,int oldversion,int newversion){
db.execSQL("drop table if exists table_user");
db.execSQL("drop table if exists table_course");
db.execSQL("drop table if exists table_selection");
onCreate(db);
     }

}
