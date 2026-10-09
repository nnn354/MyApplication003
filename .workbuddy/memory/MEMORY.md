# 项目长期记忆 — MyApplication003（校园课栈）

## 交付物归档约定（2026-10-09 用户明确要求，务必遵守）
- 项目根目录下建 `ui-target/`，其下按轮次建 `target1.0/`、`target2.0/`、`target3.0/`…
- **每一轮新生成的交付物（HTML 报告 / 效果图 PNG / 生成脚本等）都放进当轮的 `targetN.0/`**，不要留在项目根目录。
- `target1.0/` 已归档：`升级蓝图_校园课栈v2.html` + `升级效果图/`（15 张页面 PNG + `_总览_15个页面.png` + `_源文件/` 生成脚本）。
- 下一轮开始编号 `target2.0`，依次递增。

## 工作方式约定（延续）
- 用户要求：**只诊断/规划，不代写业务代码**（.java/.xml 未经明确要求不得修改）。产出以报告/计划/效果图为主。
- HTML 交付物背景：**一律淡蓝色**（此前短暂要求深蓝，已被"淡蓝"取代）。淡蓝基准：页底 `#EAF3FB`、白卡片、主色 `#378ADD`、标题 `#14456F`。

## 项目关键事实
- Android Java + XML；包名 `com.example.myapplication003`；AppCompat 1.6.1；SQLite（MyDbHelper，db_version=3）。
- 命令行编译必须用 Android Studio 自带 JDK：`JAVA_HOME="D:\aaaaa_安卓开发\jbr" ./gradlew assembleDebug`。
- 模拟器：雷电9，`D:\aaaaa_安卓开发\雷电模拟器9\leidian\LDPlayer9\ldconsole.exe`；adb 在 `D:\a_studio\aa_studio\platform-tools\adb.exe`。
- 6 张目标效果图原始需求在 `app/src/main/ui_photo/`。
