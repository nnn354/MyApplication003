# -*- coding: utf-8 -*-
"""生成「校园课栈 v2.0」全部页面目标效果图的 HTML（随后用无头 Chrome 渲染成 PNG）。"""
import os

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, ".mock_gen")
os.makedirs(OUT, exist_ok=True)

CSS = """
*{margin:0;padding:0;box-sizing:border-box;-webkit-font-smoothing:antialiased}
html,body{width:390px;height:844px;overflow:hidden}
body{font-family:-apple-system,"PingFang SC","Microsoft YaHei","Segoe UI",sans-serif;
 font-size:13px;color:#1B1B24;background:#F4F6FF;line-height:1.45}
.screen{width:390px;height:844px;display:flex;flex-direction:column;overflow:hidden;position:relative;background:#F4F6FF}
/* 状态栏 */
.sb{height:28px;flex:0 0 auto;display:flex;align-items:center;justify-content:space-between;
 padding:0 20px;font-size:12px;font-weight:700;color:#1B1B24;z-index:9}
.sb.light,.sb.light *{color:#fff}
.sb .r{display:flex;gap:6px;align-items:center}
.sb .bat{width:21px;height:11px;border:1.4px solid currentColor;border-radius:3px;position:relative;display:block}
.sb .bat:after{content:"";position:absolute;right:-3.5px;top:3px;width:2px;height:5px;background:currentColor;border-radius:0 1.5px 1.5px 0}
.sb .bat i{position:absolute;left:1.5px;top:1.5px;bottom:1.5px;width:12px;background:currentColor;border-radius:1.5px;display:block}
/* 顶栏 */
.hd{height:54px;flex:0 0 auto;display:flex;align-items:center;gap:10px;padding:0 16px;background:#fff}
.hd.flat{background:transparent}
.hd .back{width:34px;height:34px;border-radius:11px;background:#F0F3FF;display:flex;align-items:center;justify-content:center;color:#4A63E8}
.hd .t{font-size:17px;font-weight:800;letter-spacing:.2px}
.hd .act{margin-left:auto;font-size:13px;color:#6C4CF1;font-weight:700}
.hd svg{width:19px;height:19px}
.content{flex:1 1 auto;min-height:0;overflow:hidden;position:relative}
/* 底部导航 */
.nav{height:66px;flex:0 0 auto;background:#fff;border-top:1px solid #EAEEF9;
 display:flex;align-items:flex-start;justify-content:space-around;padding-top:9px}
.nav .it{display:flex;flex-direction:column;align-items:center;gap:4px;color:#9AA3B8;font-size:11px;font-weight:600;width:25%}
.nav .it.on{color:#6C4CF1}
.nav svg{width:22px;height:22px}
/* 通用 */
.pad{padding:0 16px}
.card{background:#fff;border-radius:16px;box-shadow:0 2px 12px rgba(80,100,180,.07)}
.mi{width:13px;height:13px;vertical-align:-2px;margin-right:4px;flex:0 0 auto}
.tag{font-size:10px;font-weight:800;padding:2px 8px;border-radius:6px;background:#EFECFF;color:#6C4CF1;flex:0 0 auto}
.tag.blue{background:#E8EFFF;color:#4A63E8}
.tag.green{background:#E6F7EC;color:#16A34A}
.tag.amber{background:#FFF4E0;color:#C77700}
.tag.red{background:#FFE9E9;color:#E23B3B}
.chips{display:flex;gap:8px;padding:0 16px;overflow:hidden}
.chip{flex:0 0 auto;padding:7px 15px;border-radius:999px;background:#fff;color:#6B7280;
 font-size:12.5px;font-weight:700;border:1px solid #EAEEF9}
.chip.on{background:linear-gradient(135deg,#6C4CF1,#4A63E8);color:#fff;border-color:transparent;
 box-shadow:0 4px 12px rgba(108,76,241,.28)}
.btn{height:50px;border-radius:15px;background:linear-gradient(135deg,#6C4CF1,#4A63E8);color:#fff;
 font-weight:800;display:flex;align-items:center;justify-content:center;font-size:15px;
 box-shadow:0 8px 20px rgba(108,76,241,.32);letter-spacing:.5px}
.btn.ghost{background:#fff;color:#4A63E8;border:1.5px solid #DFE6FB;box-shadow:none}
.btn.sm{height:38px;border-radius:11px;font-size:13px;box-shadow:0 4px 12px rgba(108,76,241,.25)}
.mini-btn{padding:6px 16px;border-radius:999px;background:linear-gradient(135deg,#6C4CF1,#4A63E8);
 color:#fff;font-size:12px;font-weight:800;box-shadow:0 4px 10px rgba(108,76,241,.28)}
.mini-btn.gray{background:#F0F3FF;color:#4A63E8;box-shadow:none}
.inp{height:52px;border-radius:14px;background:#fff;border:1.5px solid #EAEEF9;display:flex;
 align-items:center;gap:10px;padding:0 14px;color:#1B1B24}
.inp.err{border-color:#FFC9C9;background:#FFF7F7}
.inp .ph{color:#A6AEC2;font-size:13.5px}
.inp svg{width:18px;height:18px;color:#8A94AC;flex:0 0 auto}
.prog{height:6px;border-radius:999px;background:#EDF0FA;overflow:hidden;flex:1 1 auto}
.prog i{display:block;height:100%;border-radius:999px;background:linear-gradient(90deg,#6C4CF1,#4A63E8)}
.prog.warn i{background:linear-gradient(90deg,#F59E0B,#F97316)}
.prog.full i{background:linear-gradient(90deg,#EF4444,#DC2626)}
.avatar{border-radius:50%;background:linear-gradient(135deg,#8B6CF5,#5A8DE0);color:#fff;
 display:flex;align-items:center;justify-content:center;font-weight:800;flex:0 0 auto}
.row{display:flex;align-items:center}
.grow{flex:1 1 auto}
/* 列表条目 */
.li{background:#fff;border-radius:14px;display:flex;align-items:center;gap:12px;padding:14px;box-shadow:0 2px 10px rgba(80,100,180,.06)}
.li .ic{width:38px;height:38px;border-radius:12px;display:flex;align-items:center;justify-content:center;flex:0 0 auto}
.li .ic svg{width:19px;height:19px}
.li .tt{font-size:14px;font-weight:700}
.li .ss{font-size:11.5px;color:#8A94AC;margin-top:3px}
.li .ar{color:#C4CBDD}
.li .ar svg{width:16px;height:16px}
.grp{background:#fff;border-radius:16px;overflow:hidden;box-shadow:0 2px 12px rgba(80,100,180,.07)}
.grp .h{font-size:11.5px;font-weight:800;color:#8A94AC;letter-spacing:1px;padding:4px 4px 8px}
.sw{width:44px;height:30px;border-radius:999px;background:#E3E8F6;position:relative;flex:0 0 auto;transition:.2s}
.sw:after{content:"";position:absolute;left:3px;top:3px;width:24px;height:24px;border-radius:50%;background:#fff;box-shadow:0 1px 4px rgba(0,0,0,.2)}
.sw.on{background:linear-gradient(135deg,#6C4CF1,#4A63E8)}
.sw.on:after{left:17px}
.divider{height:1px;background:#F0F3FA;margin:0 14px}
"""

# ---------- 图标 ----------
I_BACK = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M15 5l-7 7 7 7"/></svg>'
I_BOOK = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg>'
I_CAL = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><rect x="3" y="4.5" width="18" height="17" rx="3"/><path d="M8 2.5v4M16 2.5v4M3 10h18"/></svg>'
I_CHART = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M4 20V10M10 20V4M16 20v-7M22 20H2"/></svg>'
I_USER = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="12" cy="8" r="4"/><path d="M4.5 21c0-4 3.5-6 7.5-6s7.5 2 7.5 6"/></svg>'
I_SEARCH = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"><circle cx="11" cy="11" r="7"/><path d="M20 20l-3.5-3.5"/></svg>'
I_BELL = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M18 8a6 6 0 1 0-12 0c0 7-3 8-3 8h18s-3-1-3-8"/><path d="M10.5 21a2 2 0 0 0 3 0"/></svg>'
I_CLOCK = '<svg class="mi" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="12" cy="12" r="9"/><path d="M12 7.5v5l3.2 2"/></svg>'
I_PIN = '<svg class="mi" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M12 21.5s7-6.2 7-11.5a7 7 0 1 0-14 0c0 5.3 7 11.5 7 11.5z"/><circle cx="12" cy="10" r="2.6"/></svg>'
I_LOCK = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><rect x="4" y="10" width="16" height="11" rx="3"/><path d="M8 10V7a4 4 0 1 1 8 0v3"/></svg>'
I_CARD = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><rect x="3" y="5" width="18" height="14" rx="3"/><path d="M3 10h18"/></svg>'
I_CAM = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M4 8h3l1.5-2h7L17 8h3v11H4z"/><circle cx="12" cy="13" r="3.2"/></svg>'
I_ARROW = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"><path d="M9 5l7 7-7 7"/></svg>'
I_STAR = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M12 3l2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1L3.2 9.5l6.1-.9z"/></svg>'
I_SHARE = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="18" cy="5" r="2.6"/><circle cx="6" cy="12" r="2.6"/><circle cx="18" cy="19" r="2.6"/><path d="M8.3 10.7l7.4-4.4M8.3 13.3l7.4 4.4"/></svg>'
I_GLOBE = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3a15 15 0 0 1 0 18M12 3a15 15 0 0 0 0 18"/></svg>'
I_SHIELD = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M12 3l7 3v5c0 5-3 8.5-7 10-4-1.5-7-5-7-10V6z"/></svg>'
I_DOC = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M6 2h8l5 5v15H6z"/><path d="M14 2v5h5"/></svg>'
I_TRASH = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M4 7h16M9 7V4.5h6V7M6 7l1 14h10l1-14"/></svg>'
I_GEAR = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="12" cy="12" r="3.2"/><path d="M12 2.5v3M12 18.5v3M2.5 12h3M18.5 12h3M5.2 5.2l2.1 2.1M16.7 16.7l2.1 2.1M18.8 5.2l-2.1 2.1M7.3 16.7l-2.1 2.1"/></svg>'
I_PLAN = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><rect x="3" y="4" width="18" height="17" rx="3"/><path d="M8 2.5v4M16 2.5v4M7.5 13l2.5 2.5L16 10"/></svg>'
I_HELP = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="12" cy="12" r="9"/><path d="M9.5 9.5a2.6 2.6 0 1 1 3.4 2.5c-.8.3-1.1.9-1.1 1.7"/><circle cx="11.8" cy="17" r=".9" fill="currentColor"/></svg>'
I_LOGOUT = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M15 4h3a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2h-3"/><path d="M10 12H3M6.5 8.5L3 12l3.5 3.5"/></svg>'


def sb(light=False):
    c = " light" if light else ""
    return ('<div class="sb' + c + '"><span>9:41</span><span class="r">'
            '<span style="font-size:10.5px">5G</span><span class="bat"><i></i></span></span></div>')


def nav(active):
    items = [("hall", "选课", I_BOOK), ("course", "课表", I_CAL),
             ("score", "成绩", I_CHART), ("me", "我的", I_USER)]
    h = '<div class="nav">'
    for k, label, ic in items:
        h += '<div class="it' + (" on" if k == active else "") + '">' + ic + '<span>' + label + '</span></div>'
    return h + '</div>'


def hd(title, right="", back=True, flat=False):
    h = '<div class="hd' + (" flat" if flat else "") + '">'
    if back:
        h += '<div class="back">' + I_BACK + '</div>'
    h += '<div class="t">' + title + '</div>'
    if right:
        h += '<div class="act">' + right + '</div>'
    return h + '</div>'


def page(body, cls=""):
    return ('<!DOCTYPE html><html lang="zh-CN"><head><meta charset="utf-8">'
            '<style>' + CSS + '</style></head><body>'
            '<div class="screen ' + cls + '">' + body + '</div></body></html>')


FONTGRAD = 'background:linear-gradient(160deg,#6C4CF1 0%,#5A5CE8 45%,#3F7BE0 100%);'

# ============================================================ 00 设计规范
spec_sw = [("#6C4CF1", "主色 / 品牌紫"), ("#4A63E8", "辅助 / 链接蓝"), ("#16A34A", "成功 / 可选"),
           ("#F59E0B", "警告 / 冲突"), ("#EF4444", "危险 / 退选")]
sw_html = ""
for c, n in spec_sw:
    sw_html += ('<div style="text-align:center;flex:1"><div style="height:52px;border-radius:12px;background:' + c +
                ';box-shadow:0 4px 12px rgba(80,100,180,.18)"></div>'
                '<div style="font-size:10px;color:#8A94AC;margin-top:6px;font-weight:700">' + c + '</div></div>')

neutral = [("#F4F6FF", "页面底"), ("#FFFFFF", "卡片"), ("#EAEEF9", "分隔线"), ("#6B7280", "次要文字"), ("#1B1B24", "正文")]
neu_html = ""
for c, n in neutral:
    neu_html += ('<div style="text-align:center;flex:1"><div style="height:44px;border-radius:11px;background:' + c +
                 ';border:1px solid #EAEEF9"></div><div style="font-size:10px;color:#8A94AC;margin-top:5px">' + n + '</div></div>')

P00 = sb() + hd("设计规范", "v2.0") + '''
<div class="content" style="overflow:hidden;padding:4px 16px 16px">
 <div style="font-size:11.5px;font-weight:800;color:#8A94AC;letter-spacing:1px;margin:6px 0 8px">品牌色</div>
 <div class="row" style="gap:8px">''' + sw_html + '''</div>
 <div style="font-size:11.5px;font-weight:800;color:#8A94AC;letter-spacing:1px;margin:18px 0 8px">中性色</div>
 <div class="row" style="gap:8px">''' + neu_html + '''</div>
 <div style="font-size:11.5px;font-weight:800;color:#8A94AC;letter-spacing:1px;margin:18px 0 8px">字阶</div>
 <div class="card" style="padding:14px">
   <div style="font-size:24px;font-weight:800">大标题 H1 · 24</div>
   <div style="font-size:17px;font-weight:800;margin-top:8px">页面标题 H2 · 17</div>
   <div style="font-size:14px;font-weight:700;margin-top:8px">卡片标题 Title · 14</div>
   <div style="font-size:13px;margin-top:8px;color:#3A3F52">正文 Body · 13</div>
   <div style="font-size:11px;margin-top:8px;color:#8A94AC">辅助说明 Caption · 11</div>
 </div>
 <div style="font-size:11.5px;font-weight:800;color:#8A94AC;letter-spacing:1px;margin:18px 0 8px">组件</div>
 <div class="card" style="padding:14px;display:flex;flex-direction:column;gap:12px">
   <div class="row" style="gap:10px"><div class="btn grow" style="height:44px">主要按钮</div><div class="btn ghost grow" style="height:44px">次要按钮</div></div>
   <div class="row" style="gap:8px"><div class="chip on">选中 Chip</div><div class="chip">默认 Chip</div><div class="mini-btn">操作</div></div>
   <div class="row" style="gap:8px"><span class="tag">专业课</span><span class="tag blue">公共课</span><span class="tag green">已选</span><span class="tag red">冲突</span></div>
   <div class="inp" style="height:46px">''' + I_SEARCH + '''<span class="ph">输入框 / 搜索框</span></div>
   <div class="row" style="gap:10px"><div class="prog"><i style="width:62%"></i></div><span style="font-size:11px;color:#8A94AC;font-weight:700">62%</span></div>
   <div class="row" style="gap:10px"><div class="avatar" style="width:40px;height:40px;font-size:14px">张</div><div style="font-size:12px;color:#6B7280">圆角 16dp · 卡片阴影 0/2/12</div></div>
 </div>
</div>'''

# ============================================================ 01 启动页
P01 = ('<div style="position:absolute;inset:0;' + FONTGRAD + '"></div>' + sb(True) + '''
<div class="content" style="display:flex;flex-direction:column;align-items:center;justify-content:center;padding-bottom:230px">
  <div style="width:96px;height:96px;border-radius:28px;background:rgba(255,255,255,.18);border:1.5px solid rgba(255,255,255,.35);display:flex;align-items:center;justify-content:center;box-shadow:0 16px 40px rgba(20,20,80,.35)">
     <svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" style="width:48px;height:48px"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg>
  </div>
  <div style="color:#fff;font-size:29px;font-weight:800;letter-spacing:4px;margin-top:26px">校园课栈</div>
  <div style="color:rgba(255,255,255,.78);font-size:12.5px;letter-spacing:2px;margin-top:8px">CAMPUSCOURSE · 智慧选课助手</div>
  <div class="row" style="gap:6px;margin-top:34px">
    <span style="width:7px;height:7px;border-radius:50%;background:#fff;opacity:.95"></span>
    <span style="width:7px;height:7px;border-radius:50%;background:#fff;opacity:.55"></span>
    <span style="width:7px;height:7px;border-radius:50%;background:#fff;opacity:.3"></span>
  </div>
  <div style="color:rgba(255,255,255,.62);font-size:11px;margin-top:12px">正在初始化数据…</div>
</div>
<div style="position:absolute;left:16px;right:16px;bottom:22px;background:#fff;border-radius:20px;padding:16px;box-shadow:0 -6px 30px rgba(20,20,80,.22)">
  <div style="font-size:14px;font-weight:800;margin-bottom:10px">隐私保护指引</div>
  <div style="font-size:12px;color:#5C6478;line-height:1.7">感谢使用校园课栈。为保障你的账号安全与选课数据同步，我们需要收集<b>学号、姓名、院系班级</b>等必要信息。请你阅读并同意
    <span style="color:#4A63E8;font-weight:700">《用户协议》</span> 与 <span style="color:#4A63E8;font-weight:700">《隐私政策》</span>。
  </div>
  <div class="row" style="gap:9px;margin-top:12px">
    <div style="width:19px;height:19px;border-radius:6px;background:linear-gradient(135deg,#6C4CF1,#4A63E8);display:flex;align-items:center;justify-content:center;flex:0 0 auto">
      <svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round" style="width:12px;height:12px"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg>
    </div>
    <div style="font-size:12px;color:#3A3F52">我已阅读并同意上述条款</div>
  </div>
  <div class="row" style="gap:10px;margin-top:14px">
    <div class="btn ghost grow" style="height:46px;font-size:14px">不同意并退出</div>
    <div class="btn grow" style="height:46px;font-size:14px">同意并继续</div>
  </div>
  <div style="text-align:center;font-size:10.5px;color:#A6AEC2;margin-top:10px">校园课栈 v2.0.0 (build 200)</div>
</div>''')

# ============================================================ 02 登录
P02 = sb() + '''
<div style="padding:8px 20px 0;display:flex;align-items:center">
  <div class="grow" style="font-size:12px;color:#8A94AC;font-weight:700">Welcome</div>
  <div class="chip" style="display:flex;align-items:center;gap:5px;padding:6px 11px;white-space:nowrap">''' + I_GLOBE + '''<span>简体中文</span></div>
</div>
<div class="content" style="padding:22px 24px 0">
  <div style="font-size:26px;font-weight:800;letter-spacing:.5px">欢迎回来 👋</div>
  <div style="font-size:13px;color:#8A94AC;margin-top:8px">登录后即可选课、查看课表与成绩</div>
  <div style="display:flex;flex-direction:column;gap:14px;margin-top:30px">
    <div class="inp">''' + I_USER + '''<span class="ph">学号 / 手机号</span></div>
    <div class="inp">''' + I_LOCK + '''<span class="ph" style="letter-spacing:2px">••••••••</span>
      <svg viewBox="0 0 24 24" fill="none" stroke="#8A94AC" stroke-width="2" stroke-linecap="round" style="width:18px;height:18px;margin-left:auto"><path d="M2 12s3.6-6 10-6 10 6 10 6-3.6 6-10 6-10-6-10-6z"/><circle cx="12" cy="12" r="2.6"/></svg>
    </div>
  </div>
  <div class="row" style="margin-top:14px">
    <div class="row" style="gap:8px"><div style="width:18px;height:18px;border-radius:6px;border:1.6px solid #C9D2E8"></div><span style="font-size:12.5px;color:#6B7280">记住我</span></div>
    <div class="grow"></div>
    <span style="font-size:12.5px;color:#4A63E8;font-weight:700">忘记密码？</span>
  </div>
  <div class="btn" style="margin-top:22px">登 录</div>
  <div class="row" style="gap:12px;margin-top:26px"><div class="grow" style="height:1px;background:#E6EAF6"></div><span style="font-size:11px;color:#A6AEC2">其他登录方式</span><div class="grow" style="height:1px;background:#E6EAF6"></div></div>
  <div class="row" style="gap:12px;margin-top:16px">
    <div class="btn ghost grow" style="height:46px;font-size:13px">手机验证码登录</div>
    <div class="btn ghost grow" style="height:46px;font-size:13px">统一身份认证</div>
  </div>
  <div style="text-align:center;font-size:13px;color:#6B7280;margin-top:28px">还没有账号？<span style="color:#6C4CF1;font-weight:800">立即注册</span></div>
</div>
<div style="padding:0 24px 22px;text-align:center;font-size:10.5px;color:#A6AEC2;line-height:1.7">登录即代表你已同意 <span style="color:#8B6CF5">《用户协议》</span> 和 <span style="color:#8B6CF5">《隐私政策》</span></div>'''

# ============================================================ 03 注册
P03 = sb() + hd("注册账号") + '''
<div class="content" style="padding:8px 20px 0;overflow:hidden">
  <div style="display:flex;flex-direction:column;align-items:center;margin-bottom:16px">
    <div style="position:relative">
      <div class="avatar" style="width:78px;height:78px;font-size:26px">张</div>
      <div style="position:absolute;right:-2px;bottom:-2px;width:28px;height:28px;border-radius:50%;background:linear-gradient(135deg,#6C4CF1,#4A63E8);border:2.5px solid #fff;display:flex;align-items:center;justify-content:center">
        <svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2.2" stroke-linecap="round" style="width:14px;height:14px"><path d="M4 8h3l1.5-2h7L17 8h3v11H4z"/><circle cx="12" cy="13" r="3.2"/></svg>
      </div>
    </div>
    <div style="font-size:11.5px;color:#8A94AC;margin-top:8px">点击上传头像（需相机 / 相册权限）</div>
  </div>
  <div style="display:flex;flex-direction:column;gap:12px">
    <div>
      <div class="inp err">''' + I_CARD + '''<span style="font-size:13.5px">2024001X</span></div>
      <div style="font-size:11px;color:#E23B3B;margin:5px 0 0 4px">学号已存在，请核对后重试</div>
    </div>
    <div class="inp">''' + I_USER + '''<span class="ph">真实姓名</span></div>
    <div class="inp">''' + I_LOCK + '''<span class="ph">设置密码（8-20位，含字母数字）</span></div>
    <div class="inp">''' + I_LOCK + '''<span class="ph">确认密码</span></div>
    <div class="inp">''' + I_CARD + '''<span class="ph">手机号</span><span style="margin-left:auto;font-size:12.5px;color:#4A63E8;font-weight:800">获取验证码</span></div>
    <div class="row" style="gap:12px">
      <div class="inp grow"><span style="font-size:13px;color:#1B1B24">计算机学院</span>
        <svg viewBox="0 0 24 24" fill="none" stroke="#8A94AC" stroke-width="2.4" stroke-linecap="round" style="width:15px;height:15px;margin-left:auto"><path d="M6 9l6 6 6-6"/></svg></div>
      <div class="inp grow"><span style="font-size:13px;color:#1B1B24">软件 2401 班</span>
        <svg viewBox="0 0 24 24" fill="none" stroke="#8A94AC" stroke-width="2.4" stroke-linecap="round" style="width:15px;height:15px;margin-left:auto"><path d="M6 9l6 6 6-6"/></svg></div>
    </div>
  </div>
  <div class="btn" style="margin-top:20px">注 册</div>
  <div style="text-align:center;font-size:13px;color:#6B7280;margin-top:16px">已有账号？<span style="color:#6C4CF1;font-weight:800">返回登录</span></div>
</div>'''

# ============================================================ 04 选课大厅
def course_card(name, tag, tagcls, teacher, credit, time, room, cur, cap):
    pct = int(cur * 100 / cap)
    cls = " full" if pct >= 100 else (" warn" if pct >= 80 else "")
    if pct >= 100:
        btn = '<div class="mini-btn" style="background:#EDF0FA;color:#A6AEC2;box-shadow:none">已满</div>'
    else:
        btn = '<div class="mini-btn">选课</div>'
    return ('<div class="card" style="padding:14px;margin-bottom:11px">'
            '<div class="row" style="gap:8px"><div class="grow" style="font-size:15px;font-weight:800">' + name + '</div>'
            '<span class="tag ' + tagcls + '">' + tag + '</span></div>'
            '<div style="font-size:12px;color:#6B7280;margin-top:6px">' + teacher + ' · ' + credit + ' 学分</div>'
            '<div style="font-size:12px;color:#5C6478;margin-top:8px">' + I_CLOCK + time + '</div>'
            '<div style="font-size:12px;color:#5C6478;margin-top:5px">' + I_PIN + room + '</div>'
            '<div class="row" style="gap:10px;margin-top:11px"><div class="prog' + cls + '"><i style="width:' + str(pct) + '%"></i></div>'
            '<span style="font-size:11px;color:#8A94AC;font-weight:700;flex:0 0 auto">' + str(cur) + '/' + str(cap) + '</span>' + btn + '</div>'
            '</div>')

P04 = sb() + '''
<div class="hd" style="padding-bottom:2px">
  <div class="t" style="font-size:19px">选课大厅</div>
  <div class="act" style="position:relative;margin-left:auto;color:#6C4CF1">''' + I_BELL + '''
    <span style="position:absolute;right:-1px;top:-1px;width:8px;height:8px;border-radius:50%;background:#EF4444;border:1.5px solid #fff"></span></div>
</div>
<div style="flex:1 1 auto;min-height:0;overflow:hidden">
<div style="padding:6px 16px 12px;display:flex;gap:10px;align-items:center">
  <div class="inp" style="height:44px;flex:1 1 auto;background:#fff">''' + I_SEARCH + '''<span class="ph">搜索课程名 / 教师 / 教室</span></div>
  <div style="width:44px;height:44px;border-radius:14px;background:#fff;display:flex;align-items:center;justify-content:center;color:#4A63E8;box-shadow:0 2px 10px rgba(80,100,180,.08)">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" style="width:19px;height:19px"><path d="M3 6h18M6 12h12M10 18h4"/></svg>
  </div>
</div>
<div class="chips" style="margin-bottom:12px">
  <div class="chip on">全部</div><div class="chip">专业课</div><div class="chip">公共课</div>
  <div class="chip">选修课</div><div class="chip">已选</div><div class="chip">冲突</div>
</div>
<div class="pad" style="overflow:hidden">
''' + course_card("Java 程序设计", "专业课", "", "李伟 教授", "3.0", "周一 1-2节 · 周三 3-4节", "实验楼 A203", 45, 60) \
    + course_card("数据结构", "专业课", "", "陈静 副教授", "4.0", "周二 3-4节 · 周四 5-6节", "信息楼 B401", 58, 60) \
    + course_card("大学英语（三）", "公共课", "blue", "Sarah 讲师", "2.0", "周三 1-2节", "外语楼 C105", 120, 120) \
    + course_card("人工智能导论", "选修课", "amber", "王强 教授", "2.0", "周四 3-4节", "信息楼 B301", 76, 90) + '''
  <div style="text-align:center;font-size:11px;color:#B6BDD0;margin-top:2px">已加载 4 / 12 · 上拉加载更多</div>
</div>
</div>''' + nav("hall")

# ============================================================ 05 课程详情
P05 = sb() + hd("课程详情", "收藏", flat=False) + '''
<div class="content" style="padding:4px 16px 0;overflow:hidden">
  <div style="border-radius:20px;padding:18px;''' + FONTGRAD + '''color:#fff;box-shadow:0 12px 28px rgba(80,70,200,.3)">
    <div class="row" style="gap:8px"><span class="tag" style="background:rgba(255,255,255,.22);color:#fff">专业课</span><span class="tag" style="background:rgba(255,255,255,.22);color:#fff">3.0 学分</span></div>
    <div style="font-size:21px;font-weight:800;margin-top:10px">Java 程序设计</div>
    <div style="font-size:12.5px;opacity:.85;margin-top:6px">李伟 教授 · 计算机学院 · 软件工程系</div>
    <div class="row" style="gap:14px;margin-top:14px;font-size:11.5px;opacity:.92">
      <span>课程代码 CS2001</span><span>学时 48</span><span>考核 考试</span>
    </div>
  </div>
  <div class="row" style="gap:10px;margin-top:12px">
    <div class="card grow" style="padding:12px;text-align:center"><div style="font-size:19px;font-weight:800;color:#6C4CF1">45</div><div style="font-size:10.5px;color:#8A94AC;margin-top:2px">已选人数</div></div>
    <div class="card grow" style="padding:12px;text-align:center"><div style="font-size:19px;font-weight:800;color:#4A63E8">60</div><div style="font-size:10.5px;color:#8A94AC;margin-top:2px">容量上限</div></div>
    <div class="card grow" style="padding:12px;text-align:center"><div style="font-size:19px;font-weight:800;color:#16A34A">3.0</div><div style="font-size:10.5px;color:#8A94AC;margin-top:2px">学分</div></div>
  </div>
  <div class="card" style="padding:14px;margin-top:12px">
    <div style="font-size:13.5px;font-weight:800;margin-bottom:9px">上课安排</div>
    <div class="row" style="gap:9px;margin-bottom:8px"><span style="width:22px;height:22px;border-radius:7px;background:#EFECFF;color:#6C4CF1;font-size:11px;font-weight:800;display:flex;align-items:center;justify-content:center;flex:0 0 auto">一</span><span style="font-size:12.5px;color:#3A3F52">第 1-2 节 · 08:00-09:40 · 实验楼 A203</span></div>
    <div class="row" style="gap:9px"><span style="width:22px;height:22px;border-radius:7px;background:#EFECFF;color:#6C4CF1;font-size:11px;font-weight:800;display:flex;align-items:center;justify-content:center;flex:0 0 auto">三</span><span style="font-size:12.5px;color:#3A3F52">第 3-4 节 · 10:00-11:40 · 实验楼 A203</span></div>
  </div>
  <div class="card" style="padding:14px;margin-top:12px;border:1.5px solid #FFE0C2;background:#FFFBF4">
    <div class="row" style="gap:8px"><span style="color:#C77700">''' + I_CARD.replace('<svg', '<svg style="width:16px;height:16px"') + '''</span><div style="font-size:13px;font-weight:800;color:#C77700">时间冲突提示</div></div>
    <div style="font-size:12px;color:#9A6A18;margin-top:6px;line-height:1.6">与已选课程《数据结构》<b>周二 3-4 节</b>时间重叠，如需选课请先退选冲突课程。</div>
  </div>
  <div class="card" style="padding:14px;margin-top:12px">
    <div style="font-size:13.5px;font-weight:800;margin-bottom:7px">课程简介</div>
    <div style="font-size:12px;color:#5C6478;line-height:1.75">本课程系统讲授 Java 语言基础、面向对象编程、集合框架、异常处理、I/O 与多线程，并结合 Android 平台完成一个完整的小型应用，为后续移动应用开发奠定基础。</div>
  </div>
  <div style="height:78px"></div>
</div>
<div style="position:absolute;left:0;right:0;bottom:0;background:#fff;border-top:1px solid #EAEEF9;padding:12px 16px;display:flex;align-items:center;gap:12px;box-shadow:0 -6px 20px rgba(80,100,180,.08)">
  <div style="flex:0 0 auto"><div style="font-size:15px;font-weight:800;color:#EF4444">余 15 席</div><div style="font-size:10.5px;color:#8A94AC">选课截止 10-15 23:59</div></div>
  <div class="btn grow" style="height:50px">加入课表</div>
</div>'''

# ============================================================ 06 我的课表
days = ["一", "二", "三", "四", "五", "六", "日"]
blocks = [
    (1, 2, 1, "大学英语", "c1"), (3, 4, 1, "Java程序设计", "c2"), (5, 6, 1, "大学物理", "c5"),
    (1, 2, 2, "高等数学", "c3"), (3, 4, 2, "数据结构", "c4"), (9, 10, 2, "马克思主义基本原理", "c1"),
    (1, 2, 3, "大学英语", "c1"), (5, 6, 3, "计算机网络", "c5"),
    (3, 4, 4, "人工智能导论", "c3"), (5, 6, 4, "数据结构实验", "c4"), (9, 10, 4, "军事理论", "c6"),
    (1, 2, 5, "体育（羽毛球）", "c6"), (3, 4, 5, "高等数学", "c3"),
]
bcss = {"c1": "#6C4CF1", "c2": "#4A63E8", "c3": "#16A34A", "c4": "#F59E0B", "c5": "#8B5CF6", "c6": "#EC4899"}
labels = ["1-2 节", "3-4 节", "5-6 节", "7-8 节", "9-10 节"]
tt = {}

def put(row, day, name, c, room="A203"):
    tt[(row, day)] = (name, c, room)

put(0, 0, "大学英语", "c1"); put(0, 1, "高等数学", "c3"); put(0, 2, "大学英语", "c1"); put(0, 4, "体育", "c6")
put(1, 0, "Java 程序设计", "c2"); put(1, 1, "数据结构", "c4"); put(1, 3, "人工智能导论", "c3"); put(1, 4, "高等数学", "c3")
put(2, 0, "大学物理", "c5", "B401"); put(2, 2, "计算机网络", "c5", "B301"); put(2, 3, "数据结构实验", "c4", "机房 2-3")
put(3, 1, "马克思主义基本原理", "c1", "C201")
put(4, 2, "军事理论", "c6", "C105")

grid = '<div style="padding:0 16px">'
grid += '<div class="row" style="gap:4px;margin-bottom:6px"><div style="width:32px;flex:0 0 32px"></div>'
for d in days:
    grid += '<div style="flex:1;text-align:center;font-size:11.5px;font-weight:800;color:#6B7280">' + d + '</div>'
grid += '</div>'
for ri, lb in enumerate(labels):
    grid += '<div class="row" style="gap:4px;margin-bottom:4px;align-items:stretch">'
    grid += '<div style="width:32px;flex:0 0 32px;display:flex;align-items:center;justify-content:center;font-size:9.5px;color:#A6AEC2;font-weight:700">' + lb + '</div>'
    for dc in range(7):
        if (ri, dc) in tt:
            name, c, room = tt[(ri, dc)]
            cell = ('<div style="background:' + bcss[c] + ';border-radius:10px;height:60px;padding:6px 5px;overflow:hidden;box-shadow:0 3px 9px ' + bcss[c] + '55">'
                    '<div style="font-size:10px;font-weight:800;color:#fff;line-height:1.22">' + name + '</div>'
                    '<div style="font-size:8.5px;color:rgba(255,255,255,.85);margin-top:4px">' + room + '</div></div>')
        else:
            cell = '<div style="background:#fff;border-radius:10px;height:60px;box-shadow:0 1px 4px rgba(80,100,180,.05)"></div>'
        grid += '<div style="flex:1">' + cell + '</div>'
    grid += '</div>'
grid += '</div>'

P06 = sb() + hd("我的课表", "", back=False) + '''
<div style="flex:1 1 auto;min-height:0;overflow:hidden">
<div class="pad" style="display:flex;align-items:center;gap:8px;margin-bottom:10px">
  <div class="chip">2025-2026 学年第 1 学期 ▾</div>
  <div class="grow"></div>
  <div class="row" style="gap:6px;background:#fff;border-radius:10px;padding:5px;border:1px solid #EAEEF9">
    <div style="width:30px;height:26px;border-radius:7px;background:linear-gradient(135deg,#6C4CF1,#4A63E8);display:flex;align-items:center;justify-content:center">
      <svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2" style="width:15px;height:15px"><rect x="3" y="4.5" width="18" height="17" rx="3"/><path d="M3 10h18"/></svg></div>
    <div style="width:30px;height:26px;border-radius:7px;display:flex;align-items:center;justify-content:center;color:#9AA3B8">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" style="width:15px;height:15px"><path d="M4 6h16M4 12h16M4 18h10"/></svg></div>
  </div>
</div>
<div class="pad">
  <div class="card" style="padding:13px;display:flex;align-items:center;margin-bottom:12px">
    <div style="text-align:center;padding:0 12px;border-right:1px solid #F0F3FA"><div style="font-size:18px;font-weight:800;color:#6C4CF1">7</div><div style="font-size:10px;color:#8A94AC">已选课程</div></div>
    <div style="text-align:center;padding:0 12px;border-right:1px solid #F0F3FA"><div style="font-size:18px;font-weight:800;color:#4A63E8">22.0</div><div style="font-size:10px;color:#8A94AC">总学分</div></div>
    <div style="text-align:center;padding:0 12px;border-right:1px solid #F0F3FA"><div style="font-size:18px;font-weight:800;color:#16A34A">17</div><div style="font-size:10px;color:#8A94AC">周学时</div></div>
    <div style="text-align:center;padding:0 12px"><div style="font-size:18px;font-weight:800;color:#F59E0B">1</div><div style="font-size:10px;color:#8A94AC">冲突</div></div>
  </div>
</div>
''' + grid + '''
<div style="padding:11px 16px 0"><div style="background:#FFF7F7;border:1px solid #FFE0E0;border-radius:12px;padding:10px 12px;font-size:11.5px;color:#C93B3B">⚠ 检测到 1 组时间冲突：数据结构 ↔ 人工智能导论（周四 3-4 节）</div></div>
</div>
''' + nav("course")

# ============================================================ 07 成绩查询
score_rows = [("Java 程序设计", "3.0", "92", "4.0", "优秀", "green"),
              ("数据结构", "4.0", "88", "3.7", "良好", "blue"),
              ("大学英语（三）", "2.0", "85", "3.5", "良好", "blue"),
              ("高等数学 A", "5.0", "78", "3.0", "中等", "amber"),
              ("人工智能导论", "2.0", "95", "4.0", "优秀", "green")]
srows = ""
for n, cr, sc, gp, lv, c in score_rows:
    srows += ('<div class="row" style="padding:12px 14px;gap:10px">'
              '<div class="grow"><div style="font-size:13.5px;font-weight:700">' + n + '</div>'
              '<div style="font-size:11px;color:#8A94AC;margin-top:3px">' + cr + ' 学分 · 绩点 ' + gp + '</div></div>'
              '<div style="font-size:17px;font-weight:800;color:' + ("#16A34A" if float(sc) >= 90 else "#1B1B24") + '">' + sc + '</div>'
              '<span class="tag ' + c + '">' + lv + '</span></div>')

bars = [("2023-1", 68), ("2023-2", 74), ("2024-1", 81), ("2024-2", 88), ("2025-1", 92)]
bar_html = ""
for i, (t, v) in enumerate(bars):
    bar_html += ('<div style="flex:1;display:flex;flex-direction:column;align-items:center;gap:6px">'
                 '<div style="font-size:10px;color:#8A94AC;font-weight:700">' + str(v) + '</div>'
                 '<div style="width:26px;height:' + str(int(v * 0.62)) + 'px;border-radius:8px;background:linear-gradient(180deg,#8B6CF5,#4A63E8);opacity:' + str(0.5 + i * 0.125) + '"></div>'
                 '<div style="font-size:9.5px;color:#A6AEC2">' + t + '</div></div>')

P07 = sb() + hd("成绩查询", "", back=False) + '''
<div class="content" style="padding:2px 16px 0;overflow:hidden">
  <div style="border-radius:20px;padding:18px;''' + FONTGRAD + '''color:#fff;box-shadow:0 12px 28px rgba(80,70,200,.3)">
    <div class="row"><div class="grow"><div style="font-size:11.5px;opacity:.85">平均学分绩点 GPA</div>
      <div style="font-size:34px;font-weight:800;line-height:1.15;margin-top:2px">3.72</div></div>
      <div style="text-align:right"><div style="font-size:11.5px;opacity:.85">专业排名</div><div style="font-size:20px;font-weight:800;margin-top:2px">12 <span style="font-size:12px;font-weight:600;opacity:.8">/ 168</span></div></div></div>
    <div class="row" style="gap:18px;margin-top:14px;font-size:11.5px;opacity:.92">
      <span>已修学分 86.0</span><span>挂科 0</span><span>较上学期 +0.15 ↑</span></div>
  </div>
  <div class="chips" style="padding:12px 0 10px">
    <div class="chip on">2025-2026-1</div><div class="chip">2024-2025-2</div><div class="chip">2024-2025-1</div>
  </div>
  <div class="card" style="padding:14px;margin-bottom:12px">
    <div class="row" style="margin-bottom:12px"><div style="font-size:13px;font-weight:800">学期成绩趋势</div><div class="grow"></div><span style="font-size:10.5px;color:#8A94AC">平均分</span></div>
    <div class="row" style="align-items:flex-end;height:96px">''' + bar_html + '''</div>
  </div>
  <div class="card" style="overflow:hidden">
    <div class="row" style="padding:12px 14px;border-bottom:1px solid #F2F5FC"><div style="font-size:13px;font-weight:800">2025-2026 学年第 1 学期</div><div class="grow"></div><span style="font-size:11px;color:#8A94AC">共 5 门</span></div>
    ''' + srows + '''
  </div>
</div>''' + nav("score")

# ============================================================ 08 学习计划
def task(name, sub, done=False, tag=""):
    box = ('<div style="width:22px;height:22px;border-radius:8px;background:linear-gradient(135deg,#6C4CF1,#4A63E8);display:flex;align-items:center;justify-content:center;flex:0 0 auto">'
           '<svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round" style="width:13px;height:13px"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg></div>') if done else \
          '<div style="width:22px;height:22px;border-radius:8px;border:1.8px solid #D3DBEE;flex:0 0 auto"></div>'
    tt = '<span style="text-decoration:line-through;color:#A6AEC2">' + name + '</span>' if done else name
    return ('<div class="card" style="padding:13px;margin-bottom:10px;display:flex;gap:12px;align-items:center">' + box +
            '<div class="grow"><div style="font-size:13.5px;font-weight:700">' + tt + '</div>'
            '<div style="font-size:11px;color:#8A94AC;margin-top:3px">' + sub + '</div></div>' +
            (tag if tag else '') + '</div>')

P08 = sb() + hd("学习计划", "＋ 新建") + '''
<div class="content" style="padding:4px 16px 0;overflow:hidden">
  <div class="card" style="padding:16px;display:flex;align-items:center;gap:16px;margin-bottom:14px">
    <div style="width:78px;height:78px;border-radius:50%;background:conic-gradient(#6C4CF1 0 62%,#EDF0FA 62% 100%);display:flex;align-items:center;justify-content:center;flex:0 0 auto">
      <div style="width:60px;height:60px;border-radius:50%;background:#fff;display:flex;flex-direction:column;align-items:center;justify-content:center">
        <div style="font-size:16px;font-weight:800;color:#6C4CF1;line-height:1">5/8</div><div style="font-size:9px;color:#8A94AC">本周</div>
      </div>
    </div>
    <div class="grow">
      <div style="font-size:15px;font-weight:800">本周任务完成 62%</div>
      <div style="font-size:11.5px;color:#8A94AC;margin-top:6px;line-height:1.6">已完成 5 项，剩余 3 项<br>连续打卡 <b style="color:#F59E0B">12 天</b> 🔥</div>
    </div>
  </div>
  <div style="font-size:11.5px;font-weight:800;color:#8A94AC;letter-spacing:1px;margin:0 4px 9px">今日待办 · 10月9日</div>
''' + task("完成 Java 课程设计实验报告", "截止 今天 22:00 · 实验楼 A203", False,
           '<span class="tag red">紧急</span>') \
    + task("复习数据结构 第 5 章 · 树与二叉树", "提醒 今晚 20:00", False,
           '<span class="tag blue">提醒</span>') \
    + task("背诵英语 Unit 6 单词", "已完成 · 09:20", True) \
    + task("提交高等数学作业（第 3 次）", "已完成 · 08:40", True) + '''
  <div style="text-align:center;font-size:11px;color:#B6BDD0;margin-top:4px">下拉查看本周全部任务</div>
</div>
<div style="position:absolute;right:18px;bottom:22px;width:56px;height:56px;border-radius:20px;background:linear-gradient(135deg,#6C4CF1,#4A63E8);display:flex;align-items:center;justify-content:center;box-shadow:0 10px 24px rgba(108,76,241,.42)">
  <svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2.6" stroke-linecap="round" style="width:26px;height:26px"><path d="M12 5v14M5 12h14"/></svg>
</div>'''

# ============================================================ 09 消息中心
def msg(ic, color, title, desc, time, unread=True):
    return ('<div class="card" style="padding:13px;margin-bottom:10px;display:flex;gap:12px;align-items:flex-start;' +
            ('border:1px solid #E7E9FF;' if unread else '') + '">'
            '<div style="width:38px;height:38px;border-radius:12px;background:' + color + ';display:flex;align-items:center;justify-content:center;flex:0 0 auto;color:#fff">' + ic + '</div>'
            '<div class="grow"><div class="row"><div style="font-size:13.5px;font-weight:800">' + title + '</div>'
            '<div class="grow"></div><div style="font-size:10.5px;color:#A6AEC2">' + time + '</div></div>'
            '<div style="font-size:11.5px;color:#6B7280;margin-top:5px;line-height:1.6">' + desc + '</div></div>'
            + ('<span style="width:7px;height:7px;border-radius:50%;background:#EF4444;flex:0 0 auto;margin-top:6px"></span>' if unread else '') +
            '</div>')

P09 = sb() + hd("消息中心", "全部已读") + '''
<div class="content" style="padding:4px 16px 0;overflow:hidden">
  <div style="background:linear-gradient(135deg,#FFF3E0,#FFE9D6);border-radius:14px;padding:12px 14px;display:flex;align-items:center;gap:10px;margin-bottom:12px">
    <span style="color:#C77700">''' + I_BELL + '''</span>
    <div class="grow" style="font-size:12px;color:#9A6A18;font-weight:600">开启通知，选课截止与成绩发布不再错过</div>
    <div class="mini-btn" style="background:#F59E0B;box-shadow:none">去开启</div>
  </div>
  <div class="chips" style="padding:0 0 12px"><div class="chip on">全部</div><div class="chip">选课</div><div class="chip">成绩</div><div class="chip">系统</div></div>
''' + msg(I_BOOK, "linear-gradient(135deg,#6C4CF1,#4A63E8)", "《数据结构》余量告急",
          "你关注的课程《数据结构》仅剩 2 个名额，请尽快确认。", "08:12") \
    + msg(I_CHART, "linear-gradient(135deg,#16A34A,#0EA271)", "成绩已发布",
          "2024-2025-2 学期成绩已发布，平均绩点 3.72，点击查看详情。", "昨天") \
    + msg(I_CAL, "linear-gradient(135deg,#F59E0B,#F97316)", "选课截止提醒",
          "本学年第一轮选课将于 10-15 23:59 截止，你还有 1 门课程未确认。", "昨天") \
    + msg(I_SHIELD, "linear-gradient(135deg,#8A94AC,#6B7280)", "账号安全提醒",
          "你的账号于 10-08 21:30 在广州登录，如非本人操作请及时修改密码。", "10-08", False) + '''
</div>'''

# ============================================================ 10 个人中心
P10 = sb(True) + '''
<div style="position:absolute;left:0;right:0;top:0;height:250px;''' + FONTGRAD + '''border-radius:0 0 30px 30px"></div>
<div class="content" style="padding:0 16px;overflow:hidden">
  <div class="row" style="height:44px;color:#fff"><div class="grow" style="font-size:18px;font-weight:800">个人中心</div>
    <span style="color:#fff">''' + I_BELL + '''</span></div>
  <div class="row" style="gap:14px;margin-top:8px">
    <div class="avatar" style="width:66px;height:66px;font-size:23px;border:2.5px solid rgba(255,255,255,.5)">张</div>
    <div class="grow" style="color:#fff">
      <div style="font-size:19px;font-weight:800">张三</div>
      <div style="font-size:11.5px;opacity:.85;margin-top:5px">2024001 · 计算机学院</div>
      <div style="font-size:11.5px;opacity:.85;margin-top:3px">软件工程 · 软件 2401 班</div>
    </div>
    <div class="mini-btn" style="background:rgba(255,255,255,.22);box-shadow:none;color:#fff">编辑</div>
  </div>
  <div class="card" style="padding:14px;display:flex;margin-top:18px">
    <div style="flex:1;text-align:center;border-right:1px solid #F0F3FA"><div style="font-size:18px;font-weight:800;color:#6C4CF1">7</div><div style="font-size:10px;color:#8A94AC;margin-top:2px">已选课程</div></div>
    <div style="flex:1;text-align:center;border-right:1px solid #F0F3FA"><div style="font-size:18px;font-weight:800;color:#4A63E8">22.0</div><div style="font-size:10px;color:#8A94AC;margin-top:2px">总学分</div></div>
    <div style="flex:1;text-align:center;border-right:1px solid #F0F3FA"><div style="font-size:18px;font-weight:800;color:#16A34A">86.0</div><div style="font-size:10px;color:#8A94AC;margin-top:2px">已修学分</div></div>
    <div style="flex:1;text-align:center"><div style="font-size:18px;font-weight:800;color:#F59E0B">3.72</div><div style="font-size:10px;color:#8A94AC;margin-top:2px">平均绩点</div></div>
  </div>
  <div style="display:flex;flex-direction:column;gap:10px;margin-top:14px">
''' + \
    ('<div class="li"><div class="ic" style="background:#EFECFF;color:#6C4CF1">' + I_CAL + '</div><div class="grow"><div class="tt">我的课表</div><div class="ss">7 门课程 · 本周 17 学时</div></div><div class="ar">' + I_ARROW + '</div></div>'
     '<div class="li"><div class="ic" style="background:#E6F7EC;color:#16A34A">' + I_CHART + '</div><div class="grow"><div class="tt">我的成绩</div><div class="ss">平均绩点 3.72 · 排名 12/168</div></div><div class="ar">' + I_ARROW + '</div></div>'
     '<div class="li"><div class="ic" style="background:#FFF4E0;color:#C77700">' + I_PLAN + '</div><div class="grow"><div class="tt">学习计划</div><div class="ss">今日 2 项待办</div></div><div class="ar">' + I_ARROW + '</div></div>'
     '<div class="li"><div class="ic" style="background:#E8EFFF;color:#4A63E8">' + I_BELL + '</div><div class="grow"><div class="tt">消息通知</div><div class="ss">3 条未读</div></div><div class="ar">' + I_ARROW + '</div></div>'
     '<div class="li"><div class="ic" style="background:#F0F3FF;color:#6B7280">' + I_GEAR + '</div><div class="grow"><div class="tt">设置</div><div class="ss">主题 · 语言 · 隐私</div></div><div class="ar">' + I_ARROW + '</div></div>') + '''
  </div>
  <div class="btn ghost" style="margin-top:16px;height:46px;color:#EF4444;border-color:#FFDCDC">退出登录</div>
</div>''' + nav("me")

# ============================================================ 11 编辑资料
def field(label, val, ph=False, disabled=False):
    color = "#A6AEC2" if ph else ("#9AA3B8" if disabled else "#1B1B24")
    return ('<div style="margin-bottom:13px"><div style="font-size:11.5px;color:#8A94AC;font-weight:700;margin:0 0 6px 4px">' + label + '</div>'
            '<div class="inp" style="height:48px">' + ('<span style="font-size:13.5px;color:' + color + '">' + val + '</span>') +
            ('<svg viewBox="0 0 24 24" fill="none" stroke="#8A94AC" stroke-width="2.4" stroke-linecap="round" style="width:15px;height:15px;margin-left:auto"><path d="M6 9l6 6 6-6"/></svg>' if label in ("学院", "专业", "班级") else '') +
            '</div></div>')

P11 = sb() + hd("编辑资料", "保存") + '''
<div class="content" style="padding:6px 20px 0;overflow:hidden">
  <div style="display:flex;flex-direction:column;align-items:center;margin-bottom:18px">
    <div style="position:relative">
      <div class="avatar" style="width:84px;height:84px;font-size:28px">张</div>
      <div style="position:absolute;right:-3px;bottom:-3px;width:30px;height:30px;border-radius:50%;background:linear-gradient(135deg,#6C4CF1,#4A63E8);border:2.5px solid #fff;display:flex;align-items:center;justify-content:center">
        <svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2.2" stroke-linecap="round" style="width:15px;height:15px"><path d="M4 8h3l1.5-2h7L17 8h3v11H4z"/><circle cx="12" cy="13" r="3.2"/></svg>
      </div>
    </div>
    <div class="row" style="gap:16px;margin-top:12px">
      <span style="font-size:12px;color:#4A63E8;font-weight:700">拍照</span>
      <span style="font-size:12px;color:#4A63E8;font-weight:700">从相册选择</span>
      <span style="font-size:12px;color:#A6AEC2;font-weight:700">移除</span>
    </div>
  </div>
''' + field("姓名", "张三") + field("学号", "2024001", disabled=True) + field("手机号", "138****6688") \
    + field("学院", "计算机学院") + field("专业", "软件工程") + field("班级", "软件 2401 班") \
    + field("个性签名", "代码写得好，头发掉得少", ph=True) + '''
  <div class="btn" style="margin-top:8px">保存修改</div>
</div>'''

# ============================================================ 12 设置
def setting_row(ic, color, title, right):
    return ('<div class="row" style="padding:14px;gap:12px"><div class="ic" style="width:34px;height:34px;border-radius:11px;background:' + color + ';display:flex;align-items:center;justify-content:center">' + ic + '</div>'
            '<div class="grow" style="font-size:13.5px;font-weight:700">' + title + '</div>' + right + '</div>')

P12 = sb() + hd("设置") + '''
<div class="content" style="padding:6px 16px 0;overflow:hidden">
  <div class="grp" style="padding:6px 0;margin-bottom:14px"><div style="display:flex;flex-direction:column">
    ''' + setting_row(I_STAR, "#EFECFF;color:#6C4CF1", "深色模式",
                      '<div class="row" style="gap:4px;background:#F2F5FC;border-radius:9px;padding:3px"><span style="font-size:11px;padding:4px 9px;border-radius:7px;color:#6B7280">跟随系统</span><span style="font-size:11px;padding:4px 9px;border-radius:7px;background:#fff;color:#6C4CF1;font-weight:800;box-shadow:0 1px 3px rgba(0,0,0,.08)">浅色</span><span style="font-size:11px;padding:4px 9px;border-radius:7px;color:#6B7280">深色</span></div>') + '''
    <div class="divider"></div>
    ''' + setting_row(I_GLOBE, "#E8EFFF;color:#4A63E8", "语言 / Language",
                      '<div class="row" style="gap:6px"><span style="font-size:12.5px;color:#8A94AC">简体中文</span><span class="ar" style="color:#C4CBDD">' + I_ARROW + '</span></div>') + '''
  </div></div>
  <div class="grp" style="padding:6px 0;margin-bottom:14px"><div style="display:flex;flex-direction:column">
    ''' + setting_row(I_BELL, "#FFF4E0;color:#C77700", "选课提醒",
                      '<div class="sw on"><i></i></div>'.replace("<i></i>", "")) + '''
    <div class="divider"></div>
    ''' + setting_row(I_CHART, "#E6F7EC;color:#16A34A", "成绩发布通知", '<div class="sw on"></div>') + '''
    <div class="divider"></div>
    ''' + setting_row(I_SHIELD, "#EFECFF;color:#6C4CF1", "系统通知", '<div class="sw"></div>') + '''
  </div></div>
  <div class="grp" style="padding:6px 0;margin-bottom:14px"><div style="display:flex;flex-direction:column">
    ''' + setting_row(I_TRASH, "#F0F3FF;color:#6B7280", "清除缓存",
                      '<span style="font-size:12.5px;color:#8A94AC">12.6 MB</span>') + '''
    <div class="divider"></div>
    ''' + setting_row(I_DOC, "#E8EFFF;color:#4A63E8", "检查更新", '<span style="font-size:12.5px;color:#16A34A;font-weight:700">已是最新</span>') + '''
    <div class="divider"></div>
    ''' + setting_row(I_HELP, "#F0F3FF;color:#6B7280", "关于我们与隐私政策",
                      '<span class="ar" style="color:#C4CBDD">' + I_ARROW + '</span>') + '''
  </div></div>
  <div class="btn ghost" style="height:46px;color:#EF4444;border-color:#FFDCDC">退出登录</div>
  <div style="text-align:center;font-size:10.5px;color:#B6BDD0;margin-top:14px">校园课栈 v2.0.0 · 备案号 粤ICP备2026xxxxxx号</div>
</div>'''

# ============================================================ 13 关于与隐私政策
P13 = sb() + hd("关于我们") + '''
<div class="content" style="padding:10px 16px 0;overflow:hidden">
  <div style="display:flex;flex-direction:column;align-items:center;margin:6px 0 16px">
    <div style="width:66px;height:66px;border-radius:20px;''' + FONTGRAD + '''display:flex;align-items:center;justify-content:center;box-shadow:0 10px 24px rgba(108,76,241,.3)">
      <svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" style="width:34px;height:34px"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg>
    </div>
    <div style="font-size:17px;font-weight:800;margin-top:10px">校园课栈</div>
    <div style="font-size:11.5px;color:#8A94AC;margin-top:4px">v2.0.0 (build 200) · 2026-10-09</div>
  </div>
  <div class="card" style="padding:6px 0;margin-bottom:14px">
    <div class="row" style="padding:13px 14px;gap:10px"><span style="color:#6C4CF1">''' + I_DOC + '''</span><div class="grow" style="font-size:13.5px;font-weight:700">用户服务协议</div><span class="ar" style="color:#C4CBDD">''' + I_ARROW + '''</span></div>
    <div class="divider"></div>
    <div class="row" style="padding:13px 14px;gap:10px"><span style="color:#16A34A">''' + I_SHIELD + '''</span><div class="grow" style="font-size:13.5px;font-weight:700">隐私政策</div><span class="ar" style="color:#C4CBDD">''' + I_ARROW + '''</span></div>
    <div class="divider"></div>
    <div class="row" style="padding:13px 14px;gap:10px"><span style="color:#4A63E8">''' + I_STAR + '''</span><div class="grow" style="font-size:13.5px;font-weight:700">开源许可证明</div><span class="ar" style="color:#C4CBDD">''' + I_ARROW + '''</span></div>
  </div>
  <div class="card" style="padding:14px">
    <div style="font-size:13.5px;font-weight:800;margin-bottom:8px">隐私政策（摘要）</div>
    <div style="font-size:11.5px;color:#5C6478;line-height:1.85">
      一、信息收集：我们仅收集为提供选课服务所必需的学号、姓名、院系班级信息，不会收集你的通讯录、位置、通话记录等无关数据。<br>
      二、信息使用：你的信息仅用于课程容量校验、课表生成与成绩查询，不会用于任何商业推广。<br>
      三、权限说明：相机与相册权限仅在你主动更换头像时申请；通知权限用于选课截止与成绩发布提醒。<br>
      四、信息存储与安全：数据加密传输，密码经加盐哈希后存储，服务器保留 180 天访问日志。<br>
      五、你的权利：你可以随时在「设置 - 账号」中注销账号并申请删除全部个人数据。
    </div>
    <div style="font-size:11.5px;color:#4A63E8;font-weight:800;margin-top:10px">查看完整版 →</div>
  </div>
</div>'''

# ============================================================ 14 全局状态
def state_card(color, title, desc, action, skel=False):
    inner = ('<div style="display:flex;flex-direction:column;gap:7px;width:100%">'
             + "".join(['<div style="height:11px;border-radius:6px;background:linear-gradient(90deg,#EEF1F9,#E3E8F6,#EEF1F9);width:' + str(w) + '%"></div>' for w in (100, 82, 64)])
             + '</div>') if skel else \
            ('<div style="font-size:12px;color:#8A94AC;line-height:1.6;text-align:center">' + desc + '</div>' +
             ('<div class="mini-btn" style="margin-top:10px;background:' + color + ';box-shadow:none">' + action + '</div>' if action else ''))
    return ('<div class="card" style="padding:16px;margin-bottom:12px">'
            '<div class="row" style="gap:10px;margin-bottom:12px"><span style="width:8px;height:8px;border-radius:50%;background:' + color + '"></span>'
            '<div style="font-size:13.5px;font-weight:800">' + title + '</div></div>'
            '<div style="display:flex;flex-direction:column;align-items:center;min-height:64px;justify-content:center">' + inner + '</div></div>')

P14 = sb() + hd("全局状态规范") + '''
<div class="content" style="padding:6px 16px 0;overflow:hidden">
  <div style="font-size:11.5px;color:#8A94AC;line-height:1.7;margin-bottom:14px">所有列表 / 详情页统一具备四种状态，禁止出现「白屏无反馈」。</div>
  ''' + state_card("#4A63E8", "① 加载中 Loading", "", "", skel=True) \
    + state_card("#8A94AC", "② 空数据 Empty", "还没有选课记录<br>点击下方按钮去选课大厅逛逛吧", "去选课", False) \
    + state_card("#EF4444", "③ 网络错误 Error", "网络开小差了，请检查网络后重试<br>(错误码 NET-503)", "重新加载", False) \
    + state_card("#F59E0B", "④ 权限/未登录", "登录状态已过期，请重新登录以继续", "重新登录", False) + '''
</div>'''

PAGES = [
    ("00_设计规范", P00), ("01_启动页", P01), ("02_登录页", P02), ("03_注册页", P03),
    ("04_选课大厅", P04), ("05_课程详情", P05), ("06_我的课表", P06), ("07_成绩查询", P07),
    ("08_学习计划", P08), ("09_消息中心", P09), ("10_个人中心", P10), ("11_编辑资料", P11),
    ("12_设置", P12), ("13_关于与隐私政策", P13), ("14_全局状态规范", P14),
]

for name, body in PAGES:
    with open(os.path.join(OUT, name + ".html"), "w", encoding="utf-8") as f:
        f.write(page(body))
print("生成完成:", len(PAGES), "个页面 ->", OUT)
