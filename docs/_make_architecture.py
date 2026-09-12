"""Render the suite architecture diagram (orchestrator + 6 skills + shared base + gates)."""
import os
from playwright.sync_api import sync_playwright

BASE = r"K:\workbuddy\星级SKILL- gihub\data-element-dx-skillkit"
OUT_DIR = os.path.join(BASE, "docs", "images")
os.makedirs(OUT_DIR, exist_ok=True)

GREEN = "#1F4E35"
NAVY = "#062032"
MINT = "#7FB89E"
LIGHT = "#EAEFEC"
PALE = "#F2F5F3"
GREY = "#808080"

CHAIN = [
    ("行业研究", "政策·市场·玩家", "dx-industry-research"),
    ("竞品调研", "四维对标", "dx-competitor-scout"),
    ("现状摸底", "汇 + 存", "dx-data-baseline"),
    ("架构优化", "存 + 治 + 管", "dx-architecture-opt"),
    ("质量提升", "治", "dx-data-quality"),
    ("应用规划", "服 + 用 + 模", "dx-application-plan"),
]

cards = []
for i, (name, sub, slug) in enumerate(CHAIN):
    cards.append(f'''
    <div style="position:relative;width:168px">
      <div style="height:74px;background:#fff;border:0.5px solid #D8D6CE;border-radius:6px;
                  display:flex;flex-direction:column;justify-content:center;padding:0 12px">
        <div style="font-size:12.5px;font-weight:500;color:{NAVY}">{name}</div>
        <div style="font-size:10px;color:{GREY};margin-top:3px">{sub}</div>
        <div style="font-size:8px;color:#B4B2A9;margin-top:5px;font-family:monospace">{slug}</div>
      </div>
      <div style="position:absolute;top:-9px;left:9px;background:{GREEN};color:#fff;font-size:8px;
                  padding:1px 6px;border-radius:8px">{i + 1}</div>
      {"" if i == len(CHAIN) - 1 else
       f'<div style="position:absolute;right:-11px;top:36px;width:11px;height:1px;background:{MINT}"></div>'}
    </div>''')

base = f'''
  <div style="display:flex;gap:12px;margin-top:14px">
    <div style="flex:1;background:{PALE};border-radius:6px;padding:11px 13px">
      <div style="font-size:11px;font-weight:500;color:{GREEN};margin-bottom:5px">_shared / references</div>
      <div style="font-size:10px;color:{GREY};line-height:1.6">七道工序方法论 · DCMM-DMBOK 对标<br />数据要素政策索引 · 数据质量规则库</div>
    </div>
    <div style="flex:1;background:{PALE};border-radius:6px;padding:11px 13px">
      <div style="font-size:11px;font-weight:500;color:{GREEN};margin-bottom:5px">_shared / scripts（零依赖）</div>
      <div style="font-size:10px;color:{GREY};line-height:1.6;font-family:monospace">maturity_score.py · scan_assets.py<br />gate_check.py</div>
    </div>
    <div style="flex:1;background:{PALE};border-radius:6px;padding:11px 13px">
      <div style="font-size:11px;font-weight:500;color:{GREEN};margin-bottom:5px">cases / 可插拔案例层</div>
      <div style="font-size:10px;color:{GREY};line-height:1.6">接口开源 · 内容自建<br />脱敏三档 · 物理隔离</div>
    </div>
  </div>'''

html = f'''<!DOCTYPE html>
<html><head><meta charset="utf-8">
<style>
  * {{ box-sizing:border-box; }}
  body {{ margin:0; background:#fff; font-family:"Segoe UI","PingFang SC","Microsoft YaHei",sans-serif; }}
  .wrap {{ width:1160px; padding:26px 28px 24px; }}
  .top {{ display:flex; align-items:center; gap:14px; margin-bottom:4px; }}
  .orch {{ width:296px; background:{NAVY}; border-radius:8px; padding:14px 16px; }}
  .orch .t {{ font-size:13.5px; font-weight:500; color:#fff; }}
  .orch .s {{ font-size:10px; color:{MINT}; margin-top:4px; line-height:1.5; }}
  .orch .m {{ font-size:8px; color:rgba(255,255,255,.42); margin-top:7px; font-family:monospace; }}
  .arrow {{ font-size:16px; color:{MINT}; }}
  .row {{ display:flex; gap:12px; align-items:center; }}
  .lbl {{ font-size:11px; color:{GREY}; margin:16px 0 9px; }}
</style></head>
<body><div class="wrap">

  <div class="top">
    <div class="orch">
      <div class="t">编排总控 · Orchestrator</div>
      <div class="s">立项 8 问 → 强制因果顺序 → 阶段门禁 → 口径一致性校验</div>
      <div class="m">dx-engagement-orchestrator</div>
    </div>
    <div class="arrow">→</div>
    <div style="font-size:11.5px;color:{GREY};line-height:1.7">
      串起六个交付技能<br />
      顺序不可颠倒<br />
      空模板不算通过
    </div>
  </div>

  <div class="lbl">标准交付链（六步，每步过门禁）</div>
  <div class="row">{''.join(cards)}</div>

  <div class="lbl">共享底座与可插拔案例层</div>
  {base}

</div></body></html>'''

hp = os.path.join(OUT_DIR, "_architecture.html")
with open(hp, "w", encoding="utf-8") as f:
    f.write(html)

with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": 1160, "height": 460}, device_scale_factor=2)
    pg.goto("file:///" + hp.replace("\\", "/"))
    pg.wait_for_timeout(600)
    pg.query_selector(".wrap").screenshot(path=os.path.join(OUT_DIR, "architecture.png"))
    b.close()

print("architecture ->", os.path.join(OUT_DIR, "architecture.png"))
