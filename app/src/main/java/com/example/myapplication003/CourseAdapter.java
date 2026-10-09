package com.example.myapplication003;

import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;

import androidx.recyclerview.widget.RecyclerView;

import com.example.myapplication003.entity.Course;

import java.util.List;

public class CourseAdapter extends RecyclerView.Adapter<CourseAdapter.VH> {

    public interface OnCourseActionListener{
        void onSelect(Course course);
        void onDrop(Course course);

    }
    private OnCourseActionListener listener;

    //extends  RecyclerView.Adapter<CourseAdapter.VH>	继承 Adapter
    //onCreateViewHolder	造一行
    //onBindViewHolder	填数据
    //getItemCount	几行
    List<Course>list;
    public CourseAdapter (List<Course> list,OnCourseActionListener listener){
        this.list=list;
        this.listener=listener;
    }
//    Adapter	定义接口、绑按钮、点按钮时调 listener.onSelect(c)
//    Fragment	实现接口、写判断、写数据库、刷新列表

    @Override
    public VH onCreateViewHolder(ViewGroup parent,int viewType){
        View v= LayoutInflater.from(parent.getContext())
                .inflate(R.layout.item_courselist,parent,false);
        return new VH(v);

    }
    @Override
    public void onBindViewHolder(VH holder,int position){
        Course c=list.get(position);
        holder.tvName.setText(c.courseName);
        holder.tvTeacher.setText(c.teacher);
        holder.tvCredit.setText(String.valueOf(c.credit));
        holder.tvRemain.setText(String.valueOf(c.capacity-c.selectedCount));
        holder.btnSelect.setOnClickListener(v->{
            if(listener!=null){
                listener.onSelect(c);
            }
        });
        holder.btnDrop.setOnClickListener(v->{
            if (listener!=null){
                listener.onDrop(c);
            }
        });

    }
    @Override
    public int getItemCount(){
        return list.size();

    }
    static class VH extends RecyclerView.ViewHolder{
        TextView tvName, tvTeacher, tvCredit, tvRemain;
        Button btnSelect,btnDrop;
        VH(View v){
            super(v);
            tvName    = v.findViewById(R.id.course_name);
            tvTeacher = v.findViewById(R.id.course_teacher);
            tvCredit  = v.findViewById(R.id.course_credit);
            tvRemain  = v.findViewById(R.id.course_remain);
            btnSelect=v.findViewById(R.id.choosecourse);
            btnDrop=v.findViewById(R.id.unchoosecourse);


        }
    }




}
