package com.example.myapplication003;

import static com.example.myapplication003.MainActivity.lang;

import android.content.Intent;
import android.content.res.Configuration;
import android.os.Bundle;
import android.util.Log;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

import java.util.Locale;
import android.content.Context;
public class LoginActivity extends AppCompatActivity {
    @Override
    protected void attachBaseContext(Context newBase) {
        Locale locale = new Locale(MainActivity.lang);
        Locale.setDefault(locale);
        Configuration cfg = new Configuration(newBase.getResources().getConfiguration());
        cfg.setLocale(locale);
        super.attachBaseContext(newBase.createConfigurationContext(cfg));
    }
    @Override
    protected void   onCreate(Bundle savedInstanceState){
        super.onCreate(savedInstanceState);
        setContentView(R.layout.acti_login);

        Button btnLang = findViewById(R.id.btn_lang);
        btnLang.setOnClickListener(v -> {
            String lang = MainActivity.lang;
            if (lang.equals("zh")) MainActivity.lang = "en";
            else if (lang.equals("en")) MainActivity.lang = "de";
            else MainActivity.lang = "zh";
            Log.d("LANG", "切换为: " + MainActivity.lang);   // ← 加这句
            recreate();
        });
       //什么都不填 → 提示“不能为空”
//乱填 → 提示“学号或密码错误”
//
//输入 2024001 / 123456 → 提示“登录成功”
        Button btnlogin=findViewById(R.id.btn1);
        btnlogin.setOnClickListener(v-> {
            EditText editid=findViewById(R.id.edit1);
            String stuid=editid.getText().toString();
            EditText editppasswd=findViewById(R.id.edit2);
            String passwd=editppasswd.getText().toString();
            if (stuid.isEmpty() || passwd.isEmpty()) {
                Toast.makeText(this, getString(R.string.str9), Toast.LENGTH_SHORT).show();
                return;
            }

                    int uid = new DbManager(this).checklogin(stuid, passwd);
                    if (uid > 0) {
                        MainActivity.currentuserid = uid;
                        Toast.makeText(this, getString(R.string.str58), Toast.LENGTH_SHORT).show();
                        startActivity(new Intent(this, MainActivity.class));
                        finish();
                    } else {
                        Toast.makeText(this, getString(R.string.str59), Toast.LENGTH_SHORT).show();
                    }

                });

//            EditText editid=findViewById(R.id.edit1);
//            String stuId=editid.getText().toString();
//            EditText editpasswd=findViewById(R.id.edit2);
//            String passwd=editpasswd.getText().toString();
////        String passwd=(String) findViewById(R.id.edit2);错误
//            //findViewById 返回的是一个 View（控件本身），它绝不可能直接变成 String（文字内容）
//            String str7=getString(R.string.str7);
//            String str8=getString(R.string.str8);
//
//            if(!stuId.isEmpty() && !passwd.isEmpty()){
//                if(stuId.equals(str7) && passwd.equals(str8)){
//                    String str12=getString(R.string.str12);
//                    Toast.makeText(LoginActivity.this,str12,Toast.LENGTH_SHORT).show();
//                    startActivity(new Intent(LoginActivity.this,MainActivity.class));
//                    finish();// 关闭登录页，防止按返回键又回到登录页
//
//                }
//                else if(!stuId.equals(str7) && passwd.equals(str8)){
//                    String str10=getString(R.string.str10);
//                    Toast.makeText(LoginActivity.this,str10,Toast.LENGTH_SHORT).show();
//
//                }
//                else if(stuId.equals(str7) && !passwd.equals(str8)){
//                    String str11=getString(R.string.str11);
//                    Toast.makeText(LoginActivity.this,str11,Toast.LENGTH_SHORT).show();
//                }
//                else{
//                    String str13=getString(R.string.str13);
//                    Toast.makeText(LoginActivity.this,str13,Toast.LENGTH_SHORT).show();
//
//                }
//
//            }
//            else{
//                String str9=getString(R.string.str9);
//                Toast.makeText(LoginActivity.this,str9,Toast.LENGTH_SHORT).show();
//            }
//
//        }
//        );
//
//}}
        Button btn2=findViewById(R.id.btn2);
        Button btn3=findViewById(R.id.btn3);
        Button btn4=findViewById(R.id.btn4);
        btn2.setOnClickListener(v->{
            startActivity(new Intent(this,ZhuceActivity.class));

        });
        btn3.setOnClickListener(v->{
            startActivity(new Intent(this,ZhuceActivity.class));

        });
        btn4.setOnClickListener(v->{
            startActivity(new Intent(this,ZhuceActivity.class));

        });

    }}