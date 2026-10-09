package com.example.myapplication003.entity;

public class User {
  public int  userId;
    public String username;
    public String passwd;
    public String name;
    public String college;
    public  String major;
    public String  banji;
    public User(int userId, String username, String passwd, String name, String college, String major,String banji){
this.userId=userId;
this.username=username;
this.college=college;
this.major=major;
this.name=name;
this.passwd=passwd;
this.banji=banji;

    }
}
