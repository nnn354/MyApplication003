package com.example.myapplication003;

import android.content.Intent;
import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;

import androidx.fragment.app.Fragment;

import com.example.myapplication003.entity.User;

public class ProfileFragment  extends Fragment {
    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceStated){
        View view=inflater.inflate(R.layout.acti_profile,container,false);
//        ## 个人中心需要实现的 4 个功能
//
//        1. **显示真实用户信息**
//                - 姓名、学号、学院、专业
//                - 用 `getUser(currentuserid)` 查数据库填进去
//                - 现在全是写死的「XXX / 2024001 / 计算机学院 / 软件工程」
//
//        2. **退出登录**
//                - 按钮点了 → 清 `currentuserid = -1` → 跳回登录页 → `finish()`
//        - 现在按钮没监听，点了没反应
//
//        3. **给控件加 id**（前提）
//        - `acti_profile.xml` 里姓名/学号/学院/专业 4 个 TextView 和退出按钮全都没 id，代码接不上
//
//        4. **其他 20 个按钮全部 Toast 占位**
//                - 修改资料、修改密码、绑定手机、选课记录…… 一律弹个"功能开发中"
//                - 不要一个个接，         **核心就 2 件事：填数据 + 退出登录。其他全是 Toast。**
        TextView pro_name=view.findViewById(R.id.pro_name);
        TextView pro_userid=view.findViewById(R.id.pro_userid);
        TextView pro_college=view.findViewById(R.id.pro_college);
        TextView pro_major=view.findViewById(R.id.pro_major);
        TextView pro_banji=view.findViewById(R.id.pro_banji);
        User u=new DbManager(getContext()).getUser(MainActivity.currentuserid);
        if(u!=null){
            pro_userid.setText(String.valueOf(u.userId));
            pro_name.setText(u.name);
            pro_major.setText(u.major);
            pro_college.setText(u.college);
            pro_banji.setText(u.banji);
        }


        Button logout=view.findViewById(R.id.logout);
        logout.setOnClickListener(v->{
            MainActivity.currentuserid=-1;
            startActivity(new Intent(getContext(),LoginActivity.class));
            getActivity().finish();
        });
        View.OnClickListener totoast=v->{
            Toast.makeText(getContext(),"功能开发中",Toast.LENGTH_SHORT).show();
        };
        view.findViewById(R.id.search_infro).setOnClickListener(totoast);
        view.findViewById(R.id.update_infro).setOnClickListener(totoast);
        view.findViewById(R.id.updat_passwd).setOnClickListener(totoast);
        view.findViewById(R.id.tie_phone).setOnClickListener(totoast);
        view.findViewById(R.id.chosecourse).setOnClickListener(totoast);
        view.findViewById(R.id.search_selection).setOnClickListener(totoast);
        view.findViewById(R.id.delete_selection).setOnClickListener(totoast);
        view.findViewById(R.id.search_score).setOnClickListener(totoast);
        view.findViewById(R.id.system_setting).setOnClickListener(totoast);
        view.findViewById(R.id.message_notify).setOnClickListener(totoast);
        view.findViewById(R.id.clear_cache).setOnClickListener(totoast);
        view.findViewById(R.id.font_size).setOnClickListener(totoast);
        view.findViewById(R.id.help_feedback).setOnClickListener(totoast);
        view.findViewById(R.id.feedback).setOnClickListener(totoast);
        view.findViewById(R.id.user_guide).setOnClickListener(totoast);
        view.findViewById(R.id.faq).setOnClickListener(totoast);



        return view;
    }

}
