package com.example.myapplication003;

import android.os.Bundle;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;
import androidx.fragment.app.Fragment;

import com.google.android.material.bottomnavigation.BottomNavigationView;
import android.content.res.Configuration;
import android.widget.Button;
import java.util.Locale;
import android.content.Context;
public class MainActivity extends AppCompatActivity {
    public static String lang="zh";
    public static int currentuserid=-1;

   private Fragment [] fragments={
           new CourseHallFragment(),new MyCoursesFragment(), new ProfileFragment()
    };
    @Override
    protected void attachBaseContext(Context newBase) {
        Locale locale = new Locale(MainActivity.lang);
        Locale.setDefault(locale);
        Configuration cfg = new Configuration(newBase.getResources().getConfiguration());
        cfg.setLocale(locale);
        super.attachBaseContext(newBase.createConfigurationContext(cfg));
    }
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);


        setContentView(R.layout.activity_main);
        //搭建主容器 + 底部导航 + 3个空Fragment。
        //
        //简单来说，就是登录成功后能跳到一个新页面，这个页面底部有三个Tab（选课大厅、我的课表、个人中心），
        // 点击Tab能切换页面。这三个页面暂时只放一段文字，证明能切换就行。
        //. FrameLayout（帧布局 / 容器）  BottomNavigationView（底部导航栏
        // menu（菜单资源）
        //是什么：res/menu 目录下的 XML 文件。  有什么用：定义底部导航栏长什么样（有几个 Tab、每个 Tab 叫什么名字、用什么图标）。
        // Fragment（碎片 / 片段）
        //组件，代表具体的页面内容（选课大厅、我的课表、个人中心）。它被“塞”进 FrameLayout 里


        //在 onCreate 里，先设置默认显示的 Fragment（通常用选课大厅）。
        //拿到 BottomNavigationView。
        //设置点击监听。
        //点击“选课大厅” -> 替换 FrameLayout 为 CourseHallFragment。
        //点击“我的课表” -> 替换 FrameLayout 为 MyCoursesFragment。
        //点击“个人中心” -> 替换 FrameLayout 为 ProfileFragment。
        //把 Fragment 提前放进数组，用下标切换
        // 默认显示第0个（选课大厅）
        getSupportFragmentManager().beginTransaction().replace(R.id.fram,fragments[0]).commit();
        //R.id.fram	容器 ID  fragments[0]	要放进去的 Fragment 实例
        //把 R.id.fram 这个容器里原来的 Fragment 移除，然后把 fragments[0] 添加进去

        BottomNavigationView bottom= findViewById(R.id.bottom);
        bottom.setOnItemSelectedListener(item->{
            int index=0;
           int  selectId=item.getItemId();
           if(selectId==R.id.nav_my){
               index=1;
           }
           else if(selectId==R.id.nav_profile){
               index=2;
           }
           else{
               index=0;
           }
           getSupportFragmentManager().beginTransaction().replace(R.id.fram,fragments[index]).commit();
           return true;
        });


        Button btnLang = findViewById(R.id.btn_lang);
        btnLang.setOnClickListener(v -> {
            if (lang.equals("zh")) lang = "en";
            else if (lang.equals("en")) lang = "de";
            else lang = "zh";
            recreate();
        });








    };
    }
