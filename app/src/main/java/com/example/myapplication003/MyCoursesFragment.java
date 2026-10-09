package com.example.myapplication003;

import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;
import android.widget.Toast;

import androidx.fragment.app.Fragment;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import com.example.myapplication003.entity.Course;

import java.util.List;

public class MyCoursesFragment extends Fragment {
    private List<Course> list;
    private CourseAdapter adapter;
    private TextView tvScore;
    private  int userid=MainActivity.currentuserid;

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceStated){

        View view=inflater.inflate(R.layout.acti_mycourse,container,false);
        RecyclerView rv=view.findViewById(R.id.recycourse);
        rv.setLayoutManager(new LinearLayoutManager(getContext()));
        DbManager db= new DbManager(getContext());
tvScore=view.findViewById(R.id.course_score);
        list=db.searchclass(userid);
        adapter=new CourseAdapter(list,new CourseAdapter.OnCourseActionListener(){
            @Override
            public void onSelect(Course course){

                Toast.makeText(getContext(),getString(R.string.str60),Toast.LENGTH_SHORT).show();

            }

            @Override
            public  void onDrop(Course course){
     int courseid=Integer.parseInt(course.courseId);
     db.deleteSelection(userid,courseid);
     db.updateSelectedCount(courseid,-1);
     Toast.makeText(getContext(),getString(R.string.str53),Toast.LENGTH_SHORT).show();
     list.clear();
     list.addAll(db.searchclass(userid));
     adapter.notifyDataSetChanged();
     updateScore();
            }
        });

        rv.setAdapter(adapter);
        updateScore();
        return  view;
    }

    private  void updateScore(){
        double total_score=0;
        for(Course c:list){
            total_score+=c.credit;
        }
        tvScore.setText(getString(R.string.str54)+list.size()+getString(R.string.str55)+total_score+getString(R.string.str56));

    }
    @Override
    public  void onResume(){
        super.onResume();
        if(adapter==null)
        {
            return;
        }
        DbManager db=new DbManager(getContext());
        list.clear();
        list.addAll(db.searchclass(userid));
        adapter.notifyDataSetChanged();
        updateScore();
    }



}
