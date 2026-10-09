package com.example.myapplication003;

import android.os.Bundle;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import androidx.fragment.app.Fragment;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import com.example.myapplication003.entity.Course;
import com.example.myapplication003.entity.User;

import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.Callable;

public class CourseHallFragment  extends Fragment {
    private CourseAdapter adapter;
    int userid=MainActivity.currentuserid;
    private DbManager db;
    private List<Course> list;
    public void  filter_class(String type){
        List<Course> filted_class= new ArrayList<>();
        for (Course c:db.getAllcourses()){
            if(c.type.equals(type)||type.equals("全部")){
//                判断按钮是不是"全部" → type.equals("全部")
//
//                判断课程类型和按钮一致 → c.type.equals(type)
                filted_class.add(c);
            }
        }
        list.clear();
        list.addAll(filted_class);
        adapter.notifyDataSetChanged();

    }
    public  List<Course> filter_selectedclass(int userid){
        List<Course> c = db.searchclass(userid);
        list.clear();
        list.addAll(c);
        adapter.notifyDataSetChanged();

        return c;
    }
    public void filter_confictclass(){
//        List<Course> confictclass=new ArrayList<>();
//       for(Course c:db.getAllcourses()){
//           if
//
//
//            }
//        };)
        Toast.makeText(getContext(),"功能开发中",Toast.LENGTH_SHORT).show();
    }


    //Fragment 是什么：
    //Android 系统提供的一个页面组件类。不能独立存在，必须依附于 Activity。
    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle saveInstanceState){
        View view=inflater.inflate(R.layout.acti_course,container,false);
        //onCreateView：创建并返回这个 Fragment 要显示的界面 View
        //参数意思
        //LayoutInflater inflater：布局加载器，把 XML “变成” Java 里的 View 对象。
        //ViewGroup container：父容器。Fragment 的界面最终要放到它里面，通常是 Activity 里的某个容器。
        //Bundle savedInstanceState：保存的状态。Fragment 被重建时可用它恢复数据；第一次创建通常是 null。
        //返回值
        //View：返回这个 Fragment 显示出来的界面。
        //inflater.inflate(...)：加载一个 XML 布局。
        //R.layout.fragment_hall：要加载的布局文件，即 res/layout/fragment_hall.xml。
        //container：给这个布局提供父容器参考，保证布局参数正确。
        //false：表示不要立刻把布局加到 container 里，只先创建并返回这个 View，后续由 Fragment 系统处理。
        //return：把这个创建好的界面返回给 Fragment。
        //一句话总结
        //把 fragment_hall.xml 解析成一个 View，并作为当前 Fragment 的界面返回显示。


        //extends RecyclerView.Adapter<CourseAdapter.VH>	继承 Adapter
        //onCreateViewHolder	造一行
        //onBindViewHolder	填数据
        //getItemCount	几行
        RecyclerView rv=view.findViewById(R.id.recycourse);
        rv.setLayoutManager(new LinearLayoutManager(getContext()));

//        List<Course> list=new ArrayList<>();
//        list.add(new Course("001","数据结构", "李老师", 4.0,"周一下午8-9节","第一教学楼", 30,0,"专业课"));
//        list.add(new Course("002","计算机网络", "王老师", 3.0,"周一下午8-9节","第一教学楼",30,0,"专业课"));
//        list.add(new Course("003","操作系统", "赵老师", 4.0,"周一下午8-9节","第一教学楼",30,0,"专业课"));
//        list.add(new Course("004","数据库原理", "陈老师", 3.0,"周一下午8-9节","第一教学楼",20,0,"专业课"));
        db=new DbManager(getContext());
        list=db.getAllcourses();
//        DbManager db = new DbManager(...);   // ← 带了类型声明，建的是局部变量
//        List<Course> list = db.getAllcourses();  // ← 同上
        Log.d("CourseHall",getString(R.string.str48)+"="+list.size());
        adapter= new CourseAdapter(list,new CourseAdapter.OnCourseActionListener(){
            @Override
            public void onSelect(Course course){
                int courseid=Integer.parseInt(course.courseId);
//                int userid=1;
                if(db.isSelected(userid,courseid)){
                    Toast.makeText(getContext(),getString(R.string.str49),Toast.LENGTH_SHORT).show();
                }
                else if(course.selectedCount>=course.capacity){
                    Toast.makeText(getContext(),getString(R.string.str50),Toast.LENGTH_SHORT).show();
                }
                else{
                    db.insertSelection(userid,courseid);
                    db.updateSelectedCount(courseid,+1);
                    Toast.makeText(getContext(),getString(R.string.str51),Toast.LENGTH_SHORT).show();
                    list.clear();
                    list.addAll(db.getAllcourses());
                    adapter.notifyDataSetChanged();
                }



            }

            @Override
            public void onDrop(Course course){
                int courseid=Integer.parseInt(course.courseId);
//                int userid=1;
                if(!db.isSelected(userid,courseid)){
                    Toast.makeText(getContext(),getString(R.string.str52),Toast.LENGTH_SHORT).show();
                }
                else{
                    db.deleteSelection(userid,courseid);
                    db.updateSelectedCount(courseid,-1);
                    Toast.makeText(getContext(),getString(R.string.str53),Toast.LENGTH_SHORT).show();
                    list.clear();
                    list.addAll(db.getAllcourses());
                    adapter.notifyDataSetChanged();

                }


            }
        });

        rv.setAdapter(adapter);


            EditText sea=view.findViewById(R.id.search_edit);
            Button search=view.findViewById(R.id.search_btn);
            search.setOnClickListener(v->{
                String keywords1=sea.getText().toString();
                List<Course>  result_list=new ArrayList<>();
                for(Course c:db.getAllcourses()){
                    if(c.courseName.contains(keywords1)||c.teacher.contains(keywords1) ||c.location.contains(keywords1)){
                        result_list.add(c);
                    }

                }
                list.clear();
                list.addAll(result_list);
                adapter.notifyDataSetChanged();
            });



//        Button all_course=view.findViewById(R.id.all_course);
//        Button common_course=view.findViewById(R.id.common_course);
//        Button choice_course=view.findViewById(R.id.choice_course);
//        Button necessary_course=view.findViewById(R.id.necessary_course);
//        Button selected_course=view.findViewById(R.id.selected_course);
//        Button conflict_course=view.findViewById(R.id.conflict_course);
//        all_course.setOnClickListener();
        view.findViewById(R.id.all_course).setOnClickListener(v -> filter_class("全部"));
        view.findViewById(R.id.common_course).setOnClickListener(v -> filter_class("公共课"));
        view.findViewById(R.id.necessary_course).setOnClickListener(v -> filter_class("专业课"));
        view.findViewById(R.id.choice_course).setOnClickListener(v -> filter_class("选修课"));

        view.findViewById(R.id.selected_course).setOnClickListener(v->filter_selectedclass(userid));
        view.findViewById(R.id.conflict_course).setOnClickListener(v->filter_confictclass());
//## 改法
//
//                **在 `CourseHallFragment` 里，把 6 个按钮的传参从 `getString(...)` 换成写死的中文**：
//
//```java
//        view.findViewById(R.id.all_course).setOnClickListener(v -> filter_class("全部"));
//        view.findViewById(R.id.common_course).setOnClickListener(v -> filter_class("公共课"));
//        view.findViewById(R.id.necessary_course).setOnClickListener(v -> filter_class("专业课"));
//        view.findViewById(R.id.choice_course).setOnClickListener(v -> filter_class("选修课"));
//```
//
//**原因**：
//        - 按钮**显示的文字**仍由 `android:text="@string/str42"` 控制，切语言会变
//                - 但**传进 `filter_class` 的 key**固定中文，`c.type.equals(type)` 就永远能匹配
//                - 不改的话，切英文后 `type` 变成 `"All"`，和数据库里的 `"专业课"` 永远不相等
//
//                ---
//
//                **只改这 4 个按钮的 `getString(...)`，其他不动。**
//
//**「已选」「冲突」两个不用改**，它们要单独实现（第 2 条），改法不一样。
//
//        改完编译，切到英文点筛选，能正常过滤了。
        return view;
//        new DbManager(getContext())：new 一个对象，getContext() 是 Fragment 里拿上下文
//
//        db.getAllcourses()：调你自己写的查询方法，返回 List<Course>
//
//                new CourseAdapter(list)：把数据传给 Adapter
    }
}
