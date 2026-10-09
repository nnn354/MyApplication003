package com.example.myapplication003;

import android.content.ContentValues;
import android.content.Context;
import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;

import com.example.myapplication003.entity.Course;
import com.example.myapplication003.entity.User;

import java.util.ArrayList;
import java.util.List;

public class DbManager {
//在 Activity 里实例化 DbManager，然后在子线程里调用它的方法
//    DbManager对数据增删改查
//    直接看四个核心方法的签名（参数类型 → 参数名 含义）：
//
//            **1. 增：`insert`**
//            `long insert(String table, String nullColumnHack, ContentValues values)`
//            *   `String table`：表名。
//            *   `String nullColumnHack`：一般直接传 `null`。
//            *   `ContentValues values`：封装要插入的键值对。
//
//            **2. 删：`delete`**
//            `int delete(String table, String whereClause, String[] whereArgs)`
//            *   `String table`：表名。
//            *   `String whereClause`：条件（如 `"userid = ?"`）。
//            *   `String[] whereArgs`：条件值数组（替换 `?`）。
//
//            **3. 改：`update`**
//            `int update(String table, ContentValues values, String whereClause, String[] whereArgs)`
//            *   `String table`：表名。
//            *   `ContentValues values`：要更新的键值对。
//            *   `String whereClause`：条件。
//            *   `String[] whereArgs`：条件值数组。
//
//            **4. 查：`query`**
//            `Cursor query(String table, String[] columns, String selection, String[] selectionArgs, String groupBy, String having, String orderBy)`
//            *   `String table`：表名。
//            *   `String[] columns`：要查的列名数组（传 `null` 查全部）。
//            *   `String selection`：条件（`WHERE` 后面的部分，不含 `WHERE`）。
//            *   `String[] selectionArgs`：条件值数组（替换 `?`）。
//            *   `String groupBy`：分组（不分组传 `null`）。
//            *   `String having`：分组过滤（不分组传 `null`）。
//            *   `String orderBy`：排序（不排序传 `null`）。
    private MyDbHelper helper;
    public DbManager (Context context){
       helper= new MyDbHelper(context);
    }
    public void insertUser(String username,String passwd,String name,String college,String major,String banji){
        SQLiteDatabase db =helper.getWritableDatabase();
       ContentValues values=new ContentValues();
       values.put("username",username);
       values.put("passwd",passwd);
        values.put("name", name);
        values.put("college", college);
        values.put("major", major);
        values.put("banji", banji);
       db.insert("table_user",null,values);
       db.close();
    }//加用户
    public void deleteSelection(int userid,int courseid){
      SQLiteDatabase db =helper.getWritableDatabase();
      ContentValues values=new ContentValues();
      db.delete("table_selection","userid=?  and courseid=?",new String[]{String.valueOf(userid),String.valueOf(courseid)});
      db.close();
    }//加用户  删选课记录  更新密码  查选的课
    public void updateUserInfro(int userid,String passwd,String newpasswd){
        SQLiteDatabase db =helper.getWritableDatabase();
        ContentValues values=new ContentValues();
        values.put("passwd",newpasswd);
        db.update("table_user",values,"userid=? and passwd=?",new String[]{String.valueOf(userid),String.valueOf(passwd)});
        db.close();
    }
    private Course toCourse(Cursor c){
        return  new Course(
            c.getString(0),
            c.getString(1),
            c.getString(2),
            c.getDouble(3),
            c.getString(4),
            c.getString(5),
            c.getInt(6),
            c.getInt(8),
            c.getString(7)
        );

    }
    public List<Course> searchclass(int userid){
        SQLiteDatabase db=helper.getReadableDatabase();
List<Course> result= new ArrayList<>();
//        选课记录在 table_selection，课程信息在 table_course。
//        先查这个用户选了哪些 courseId，再拿 courseId 去课程表查详情。
      String sql1="select c.* " +
              " from table_course c " +
              "inner join table_selection s " +
              "on c.courseid=s.courseid " +
              "where s.userid=? ";
      Cursor cursor=db.rawQuery(sql1,new String[]{String.valueOf(userid)});
while(cursor.moveToNext()){
    result.add(toCourse(cursor));
}
cursor.close();
db.close();
return result;
    }
    public int checklogin(String username,String passwd){
//       SQLiteDatabase db= helper.getReadableDatabase();
//        String sql2="select userid from table_user " +
//                " where username=? and passwd = ? ";
//       int check_userid= db.execSQL(sql2);
//       return check_userid;
        try(Cursor c=helper.getReadableDatabase().rawQuery(
                "select userid from table_user where username=? and passwd = ?" ,
                new String[]{username,passwd}
        )){
            return c.moveToFirst()?c.getInt(0): -1;
        }
    }
    public User getUser(int userid){
        try(Cursor c1=helper.getReadableDatabase().rawQuery(
                "select userid, username, passwd, name, college, major,banji from table_user where userid=?",
                new String[]{String.valueOf(userid)}
        )){
            if(c1.moveToFirst()){
               return new User(
                       c1.getInt(0),
                       c1.getString(1),
                       c1.getString(2),
                       c1.getString(3),
                        c1.getString(4),
                        c1.getString(5),
                       c1.getString(6)
               );
            }
        }
        return null;

    }
    public List<Course> getAllcourses(){
        List<Course> res=new ArrayList<>();
        try(Cursor c2=helper.getReadableDatabase().rawQuery(
                "select * from table_course",
                null
        )){
            while (c2.moveToNext()){
                res.add(toCourse(c2));
        }}
        return res;
            }
            public boolean insertSelection(int userid,int courseid){
        SQLiteDatabase db=helper.getWritableDatabase();
        ContentValues v=new ContentValues();
        v.put("userid",userid);
        v.put("courseid",courseid);
        long r=db.insertWithOnConflict("table_selection",null,v,SQLiteDatabase.CONFLICT_IGNORE);
        db.close();
        return r!=-1;
            }
            public boolean isSelected(int userid,int courseid){
        try(Cursor c=helper.getReadableDatabase().rawQuery("select 1 from table_selection where userid=? and courseid=?",new String[]{String.valueOf(userid),String.valueOf(courseid)})){
            return c.moveToFirst();
        }
            }
            public void updateSelectedCount(int courseid,int delta){
//        delta是变化量
        SQLiteDatabase db=helper.getWritableDatabase();
        db.execSQL("update table_course set selectedCount =? + selectedCount where courseid=?",new Object[]{delta,courseid});
        db.close();
            }
        }






