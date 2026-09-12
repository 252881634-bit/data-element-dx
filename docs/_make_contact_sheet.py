"""Render the 20-slide deck outline as a contact sheet for the README hero image.
Reuses the deck's own design tokens so the image matches the real PPTX."""
import os
from playwright.sync_api import sync_playwright

BASE = r"K:\workbuddy\星级SKILL- gihub\data-element-dx-skillkit"
OUT_DIR = os.path.join(BASE, "docs", "images")
os.makedirs(OUT_DIR, exist_ok=True)

GREEN = "#1F4E35"
NAVY = "#062032"
MINT = "#7FB89E"
PALE = "#F2F5F3"

# dividers carry their own chapter number so each thumbnail is truthful
DIVIDER_NO = {"3": "01", "6": "02", "10": "03", "15": "04", "17": "05"}

# (index, action-title, kind)  kind: cover|toc|divider|kpi|matrix|chain|gantt|risk|cards|decision
SLIDES = [
    (1,  "集团A 数据要素建设总体方案",                          "cover"),
    (2,  "本方案回答四个问题",                                  "toc"),
    (3,  "01 现状：有数据，但没有资产",                         "divider"),
    (4,  "20 年交易数据躺在系统里，既未确权、也未产生价值",      "summary"),
    (5,  "三个事实说明我们处在“有货无价”状态",                  "kpi"),
    (6,  "02 机会：政策窗口与独家数据",                         "divider"),
    (7,  "政策在推，而我们握着别人拿不到的价格数据",             "chain"),
    (8,  "四类价值：降本、增效、增收、风控",                     "kpi4"),
    (9,  "从“市场运营商”到“行业数据定价参考”",                 "matrix"),
    (10, "03 路径：先补地基，再上价值",                         "divider"),
    (11, "先补汇存治管地基，再上服用模价值层",                   "house"),
    (12, "一期 6 个月 / 二期 8 个月 / 三期 12 个月",             "gantt"),
    (13, "七道工序全景，本期建设“汇存治管”",                    "seven"),
    (14, "DCMM L2，接入 14 系统，库表千级",                     "kpi4"),
    (15, "04 见效：第一阶段就能看到什么",                       "divider"),
    (16, "3 个月内三项成果可见",                                "cards"),
    (17, "05 保障与决策",                                       "divider"),
    (18, "需新增专职 2–3 人，并建立 Owner 制",                  "cards"),
    (19, "确权是所有对外动作的唯一前置",                         "risk"),
    (20, "请领导决策三件事",                                    "decision"),
]


def card_body(kind, idx=0):
    """Miniature wireframe inside each slide thumbnail."""
    if kind == "cover":
        return f'<div style="height:100%;background:{NAVY};display:flex;align-items:center;padding:0 26px">' \
               f'<div><div style="font-size:19px;font-weight:500;color:#fff;line-height:1.35">集团A 数据要素<br />建设总体方案</div>' \
               f'<div style="font-size:8px;color:{MINT};margin-top:8px;letter-spacing:2px">DISCUSSION DRAFT · 2026</div></div></div>'
    if kind == "divider":
        no = DIVIDER_NO.get(str(idx), "01")
        label = {"01": ("现状", "PART ONE"), "02": ("机会", "PART TWO"), "03": ("路径", "PART THREE"),
                 "04": ("见效", "PART FOUR"), "05": ("保障与决策", "PART FIVE")}[no]
        return f'<div style="height:100%;background:{NAVY};display:flex;align-items:center;padding:0 22px;gap:14px">' \
               f'<div style="font-size:44px;font-weight:500;color:rgba(255,255,255,.13);line-height:1">{no}</div>' \
               f'<div style="width:.5px;height:46px;background:rgba(255,255,255,.2)"></div>' \
               f'<div style="font-size:11px;font-weight:500;color:#fff;line-height:1.4">{label[0]}<br />' \
               f'<span style="font-size:7px;color:rgba(255,255,255,.55);font-weight:400">{label[1]}</span></div></div>'
    if kind == "summary":
        return f'<div style="height:100%;padding:8px 10px;display:flex;flex-direction:column">' \
               f'<div style="height:2px;background:#000;margin-bottom:7px"></div>' \
               f'<div style="display:flex;gap:6px;flex:1">' + "".join(
                   f'<div style="flex:1"><div style="width:14px;height:1.5px;background:{GREEN};margin-bottom:4px"></div>'
                   f'<div style="height:{34 - i * 5}px;background:{PALE};border-radius:2px"></div></div>'
                   for i in range(3)) + \
               f'</div><div style="height:9px;background:{PALE};border-radius:2px;margin-top:6px"></div></div>'
    if kind in ("kpi", "kpi4"):
        n = 3 if kind == "kpi" else 4
        h = 40 if kind == "kpi" else 34
        # per-page real numbers so no two KPI slides look identical
        KPI = {
            5:  ["6家", "2套", "0个"],
            8:  ["百人日级", "T+3→T+1", "百万级", "不可见→可控"],
            14: ["L2", "14", "千级", "10"],
        }
        vals = KPI.get(idx, ["6家", "2套", "0个", "L2"])[:n]
        fs = 12 if kind == "kpi" else (8 if idx in (8, 14) else 11)
        return f'<div style="height:100%;padding:8px 10px;display:flex;flex-direction:column">' \
               f'<div style="height:2px;background:#000;margin-bottom:7px"></div>' \
               f'<div style="display:flex;gap:5px;height:{h}px">' + "".join(
                   f'<div style="flex:1;background:{GREEN if i % 3 == 0 else PALE};border-radius:2px;'
                   f'display:flex;align-items:flex-end;padding:4px;overflow:hidden">'
                   f'<div style="font-size:{fs}px;font-weight:500;line-height:1.1;color:{"#fff" if i % 3 == 0 else GREEN}">{v}</div></div>'
                   for i, v in enumerate(vals)) + \
               f'</div><div style="flex:1;background:{PALE};border-radius:2px;margin-top:6px"></div></div>'
    if kind == "chain":
        return f'<div style="height:100%;padding:8px 10px;display:flex;flex-direction:column">' \
               f'<div style="height:2px;background:#000;margin-bottom:7px"></div>' \
               f'<div style="display:flex;gap:2px;height:24px;align-items:center">' + "".join(
                   f'<div style="flex:1;height:22px;background:{c};border-radius:1px;display:flex;align-items:center;justify-content:center">'
                   f'<span style="font-size:6px;color:{"#fff" if c != MINT else NAVY}">{t}</span></div>'
                   for c, t in [(GREEN, "政策"), (NAVY, "独家数据"), (MINT, "定价参考")]) + \
               f'</div><div style="display:flex;gap:5px;flex:1;margin-top:6px">' + "".join(
                   f'<div style="flex:1;border-top:1.5px solid {GREEN};padding-top:4px"></div>' for _ in range(3)) + "</div></div>"
    if kind == "matrix":
        return f'<div style="height:100%;padding:8px 10px;display:flex;flex-direction:column">' \
               f'<div style="height:2px;background:#000;margin-bottom:7px"></div>' \
               f'<div style="display:flex;gap:6px;flex:1">' \
               f'<div style="flex:1.4;background:{PALE};position:relative">' \
               f'<div style="position:absolute;top:50%;left:0;right:0;height:.5px;background:#C4DBCF"></div>' \
               f'<div style="position:absolute;top:0;bottom:0;left:50%;width:.5px;background:#C4DBCF"></div>' \
               f'<div style="position:absolute;top:18%;left:62%;width:11px;height:11px;border-radius:50%;background:{GREEN}"></div>' \
               f'<div style="position:absolute;top:55%;left:34%;width:9px;height:9px;border-radius:50%;background:{NAVY}"></div>' \
               f'<div style="position:absolute;top:32%;left:16%;width:7px;height:7px;border-radius:50%;background:#C4DBCF"></div>' \
               f'<div style="position:absolute;bottom:14%;left:70%;width:7px;height:7px;border-radius:50%;background:{MINT}"></div></div>' \
               f'<div style="flex:1;background:{NAVY};border-radius:2px;padding:6px;display:flex;flex-direction:column;justify-content:center">' \
               f'<div style="height:1.5px;width:12px;background:{MINT};margin-bottom:5px"></div>' \
               f'<div style="height:22px;background:rgba(255,255,255,.14);border-radius:2px"></div></div></div></div>'
    if kind == "house":
        return f'<div style="height:100%;padding:8px 10px;display:flex;flex-direction:column;gap:3px">' \
               f'<div style="height:2px;background:#000;margin-bottom:4px"></div>' \
               f'<div style="display:flex;justify-content:center"><div style="width:0;height:0;border-left:26px solid transparent;border-right:26px solid transparent;border-bottom:13px solid {NAVY}"></div></div>' \
               f'<div style="height:8px;background:{NAVY};border-radius:1px"></div>' \
               f'<div style="display:flex;gap:3px;height:22px">' + "".join(
                   f'<div style="flex:1;background:{c};border-radius:1px"></div>' for c in [GREEN, GREEN, GREEN]) + "</div>" \
               f'<div style="height:8px;background:{MINT};border-radius:1px"></div>' \
               f'<div style="height:9px;background:#C4DBCF;border-radius:1px"></div></div>'
    if kind == "gantt":
        return f'<div style="height:100%;padding:8px 10px;display:flex;flex-direction:column;gap:6px">' \
               f'<div style="height:2px;background:#000;margin-bottom:2px"></div>' \
               f'<div style="display:flex;gap:5px;align-items:center"><div style="width:16px;height:.5px"></div>' \
               f'<div style="width:30%;height:9px;background:{GREEN};border-radius:1px"></div></div>' \
               f'<div style="display:flex;gap:5px;align-items:center"><div style="width:16px"></div>' \
               f'<div style="width:22%"></div><div style="width:40%;height:9px;background:#2F6A4E;border-radius:1px"></div></div>' \
               f'<div style="display:flex;gap:5px;align-items:center"><div style="width:16px"></div>' \
               f'<div style="width:62%"></div><div style="width:30%;height:9px;background:{MINT};border-radius:1px"></div></div>' \
               f'<div style="height:11px;background:{PALE};border-radius:2px;margin-top:2px"></div></div>'
    if kind == "seven":
        rows = [(GREEN, "汇 采集汇聚"), (GREEN, "存 存储计算"), (GREEN, "治 治理清洗"),
                ("#2F6A4E", "管 资产管理"), (PALE, "服 / 用 / 模")]
        return f'<div style="height:100%;padding:8px 10px;display:flex;flex-direction:column;gap:2.5px">' \
               f'<div style="height:2px;background:#000;margin-bottom:4px"></div>' + "".join(
                   f'<div style="flex:1;background:{c};border-radius:1px;display:flex;align-items:center;padding-left:5px">'
                   f'<span style="font-size:6px;color:{"#062032" if c == PALE else "#fff"}">{t}</span></div>'
                   for c, t in rows) + "</div>"
    if kind == "cards":
        return f'<div style="height:100%;padding:8px 10px;display:flex;flex-direction:column">' \
               f'<div style="height:2px;background:#000;margin-bottom:7px"></div>' \
               f'<div style="display:flex;gap:5px;flex:1">' + "".join(
                   f'<div style="flex:1;background:{GREEN if i == 2 else PALE};border-radius:2px;padding:5px">'
                   f'<div style="width:9px;height:9px;border-radius:50%;background:{MINT if i == 2 else GREEN}"></div>'
                   f'<div style="height:5px;background:{"rgba(255,255,255,.2)" if i == 2 else "#fff"};border-radius:1px;margin-top:5px"></div>'
                   f'<div style="height:3px;background:{"rgba(255,255,255,.12)" if i == 2 else "#E7E6E6"};border-radius:1px;margin-top:3px"></div></div>'
                   for i in range(3)) + \
               f'</div><div style="height:9px;background:{PALE};border-radius:2px;margin-top:6px"></div></div>'
    if kind == "risk":
        return f'<div style="height:100%;padding:8px 10px;display:flex;flex-direction:column">' \
               f'<div style="height:2px;background:#000;margin-bottom:7px"></div>' \
               f'<div style="display:flex;gap:6px;flex:1">' \
               f'<div style="flex:1;background:{PALE};border-radius:2px;padding:5px">' + "".join(
                   f'<div style="height:4px;background:#D3D1C7;border-radius:1px;margin-bottom:4px"></div>' for _ in range(4)) + "</div>" \
               f'<div style="flex:1;background:{GREEN};border-radius:2px;padding:5px">' + "".join(
                   f'<div style="height:4px;background:rgba(255,255,255,.3);border-radius:1px;margin-bottom:4px"></div>' for _ in range(4)) + "</div>" \
               f'</div><div style="height:10px;background:{PALE};border-radius:2px;margin-top:6px;display:flex;align-items:center;padding-left:5px">' \
               f'<div style="font-size:7px;font-weight:500;color:{GREEN}">3–6 月</div></div></div>'
    if kind == "decision":
        return f'<div style="height:100%;padding:8px 10px;display:flex;flex-direction:column">' \
               f'<div style="height:2px;background:#000;margin-bottom:7px"></div>' \
               f'<div style="display:flex;gap:5px;height:44px">' + "".join(
                   f'<div style="flex:1;background:{GREEN};border-radius:2px;padding:5px">'
                   f'<div style="font-size:11px;font-weight:500;color:{MINT};line-height:1">0{i + 1}</div>'
                   f'<div style="height:4px;background:rgba(255,255,255,.25);border-radius:1px;margin-top:5px"></div>'
                   f'<div style="height:3px;background:rgba(255,255,255,.14);border-radius:1px;margin-top:3px"></div></div>'
                   for i in range(3)) + \
               f'</div><div style="flex:1;background:{PALE};border-radius:2px;margin-top:6px"></div></div>'
    if kind == "toc":
        return f'<div style="height:100%;padding:8px 10px;display:flex;flex-direction:column">' \
               f'<div style="height:2px;background:#000;margin-bottom:7px"></div>' \
               f'<div style="display:flex;gap:5px;flex:1">' + "".join(
                   f'<div style="flex:1;background:{GREEN if i % 3 == 0 else PALE};border-radius:2px;padding:5px;display:flex;flex-direction:column">'
                   f'<div style="font-size:11px;font-weight:500;color:{"#fff" if i % 3 == 0 else GREEN};line-height:1">0{i + 1}</div>'
                   f'<div style="height:4px;background:{"rgba(255,255,255,.25)" if i % 3 == 0 else "#fff"};border-radius:1px;margin-top:6px"></div></div>'
                   for i in range(4)) + \
               f'</div><div style="display:flex;gap:5px;flex:1;margin-top:5px">' + "".join(
                   f'<div style="flex:1;background:{PALE};border-radius:2px;padding:5px;display:flex;flex-direction:column">'
                   f'<div style="font-size:11px;font-weight:500;color:{GREEN};line-height:1">{i + 5:02d}</div>'
                   f'<div style="height:4px;background:#fff;border-radius:1px;margin-top:6px"></div></div>'
                   for i in range(4)) + "</div></div>"
    return f'<div style="height:100%;background:{PALE}"></div>'


cells = []
for idx, title, kind in SLIDES:
    cells.append(f'''
    <div style="display:flex;flex-direction:column">
      <div style="width:296px;height:166.5px;background:#fff;border:0.5px solid #D8D6CE;border-radius:4px;overflow:hidden;position:relative">
        {card_body(kind, idx)}
        <div style="position:absolute;right:5px;bottom:3px;font-size:7px;color:#B4B2A9">{idx}</div>
      </div>
      <div style="width:296px;font-size:9.5px;color:#44546A;line-height:1.35;margin-top:5px;height:26px;overflow:hidden">{title}</div>
    </div>''')

html = f'''<!DOCTYPE html>
<html><head><meta charset="utf-8">
<style>
  * {{ box-sizing: border-box; }}
  body {{ margin:0; background:#fff; font-family: "Segoe UI","PingFang SC","Microsoft YaHei",sans-serif; }}
  .wrap {{ padding:26px 26px 22px; width:1310px; }}
  .hd {{ display:flex; align-items:baseline; gap:12px; margin-bottom:16px; }}
  .hd h1 {{ font-size:21px; font-weight:500; color:{NAVY}; margin:0; letter-spacing:.2px; }}
  .hd span {{ font-size:11px; color:#888780; }}
  .grid {{ display:grid; grid-template-columns:repeat(4,296px); gap:16px 14px; }}
</style></head>
<body><div class="wrap">
  <div class="hd"><h1>数据要素建设总体方案</h1><span>20 页 · 商务咨询风格 · 深绿 #1F4E35</span></div>
  <div class="grid">{''.join(cells)}</div>
</div></body></html>'''

hp = os.path.join(OUT_DIR, "_contact_sheet.html")
with open(hp, "w", encoding="utf-8") as f:
    f.write(html)

with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": 1310, "height": 900}, device_scale_factor=2)
    pg.goto("file:///" + hp.replace("\\", "/"))
    pg.wait_for_timeout(700)
    el = pg.query_selector(".wrap")
    el.screenshot(path=os.path.join(OUT_DIR, "deck-overview.png"))
    b.close()

print("contact sheet ->", os.path.join(OUT_DIR, "deck-overview.png"))
