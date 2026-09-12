# Changelog

本文件记录 data-element-dx-skillkit 的所有重要变更。
格式参考 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.1.0/)，版本号遵循 [语义化版本](https://semver.org/lang/zh-CN/)。

## [2.0.3] - 2026-09-12

### ClawHub 收录完成（发布链路全通）
- 技能已在 **ClawHub** 公开收录：https://clawhub.ai/252881634-bit/skills/data-element-dx-skillkit
  - 安装：`openclaw skills install @252881634-bit/data-element-dx-skillkit`
  - 公共目录可搜索、可匿名下载（v2.0.3，74.9KB）。
- 新增根 **`SKILL.md`** 作为套件入口与路由文档（7 子技能 + `_shared` 相对引用在安装后保持有效）。
- **安全审计修复（AIG T02 Agent Memory Poisoning）**：彻底移除“agent 回写技能文档”语义——gotchas 沉淀改为仅由主理人在复盘时手工记录到 `CHANGELOG.md`，Agent 不参与任何技能文档修改；ClawHub 安全审计由 suspicious 修复为 **benign（clean）**。
- README 增加 ClawHub 徽章与一键安装命令（ClawHub/OpenClaw 生态）。

## [2.0.2] - 2026-09-12

### 修复（ClawHub 安全审查触发）
- **根 SKILL.md / dx-engagement-orchestrator**：gotchas 维护措辞改为“主理人复盘后人工维护、Agent 不自动修改”，消除“持久改写技能指令”语义（ClawHub AIG 扫描点）。

## [2.0.1] - 2026-09-12


### 修复（2026-09-12 Windows 实机试跑发现）
- **`maturity_score.py`**：Windows 下 PowerShell 写入的 UTF-8 JSON 带 BOM 导致 `json.load` 崩溃 → 读取改为 `utf-8-sig`。
- **`scan_assets.py`**：扫描 CSV 表头被 BOM 污染首列名（`﻿device_id`）→ 表头读取改为 `utf-8-sig`。
- **`gate_check.py`**：① 读取文档兼容 BOM（`utf-8-sig`）；② 修复"引号/括号内列举禁用词"误报（如校验表写"（保证/绝对）等用语"被抓）——新增引号对包裹豁免 + "承诺用语/复检/红线"语境豁免 + 否定词补充（未/未发现/未见）。
- 反向验证：真实违规用语（"保证……百分之百，必定成功"）仍能 100% 捕获。

### 新增
- **`README.en.md`** —— 英文版 README，主打公共数据运营 + 数据资产入表（国际差异化视角）。
- **`_shared/eval/trigger-eval.md`** —— 7 技能触发测试集（应触发/不应触发样例 + 交叉冲突收敛规则），用于 description 回归。
- **gotchas 沉淀**：`dx-data-baseline` +2（BOM 约定、DCMM 判定偏乐观提醒）；`dx-engagement-orchestrator` +2（gate_check 元文档误报、数字台账措辞漏检）。

### 修正
- **`01-OPEN-SOURCE-PLAN.md`**：对外目录结构去掉 `skills/` 子目录方案——与技能内 `../_shared` 相对引用不兼容，明确当前平级结构即发布结构（含 `_shared/eval/`）。

## [2.0.0] - 2026-09-12

七个技能全部升级为**生产级 v2.0**，套件具备开源条件。

### 新增
- **`_shared/scripts/gate_check.py`** —— 门禁四项自动检查（存在性 / 实质性 / 挂接性 / 一致性）+ 数字台账跨材料比对 + 绝对承诺用语检查（带反例语境豁免）。零依赖，已实跑验证。
- **`_shared/scripts/maturity_score.py`** —— DCMM 8 域加权评分与等级判定。零依赖，已实跑验证。
- **`_shared/scripts/scan_assets.py`** —— 数据资产扫描脚手架（Excel / CSV / 目录），零依赖，已实跑验证。
- **`_shared/assets/`** 七个模板：指标字典、交付计划、门禁报告、口径一致性校验表、七道工序全景图、数据资产目录、调研问卷。
- **`cases/CASE-PRIVACY.md`** —— 面向非技术用户的保密机制说明（三道闸门、三种保密强度、FAQ）。
- **`cases/sample-redacted/`** —— 完整可展示样例（主体"集团A"完全虚构）。
- **`HOW-TO-USE.md`** —— 安装、触发词对照、三个最小试跑示例。
- **`全景图.html`** —— 单文件可视化全景，纯本地无外链。
- **`docs/images/`** —— README 用视觉素材（课件总览、架构图）。

### 变更
- **`dx-engagement-orchestrator` → v2.0**：新增立项 8 问、标准交付链（6 步含门禁图）、跳步后果对照表、门禁四项检查、缺口处理规则、跨技能调用协定、案例沉淀流程。Gotchas 9 条。
- **`dx-data-quality` → v2.0**：融合 data-governance 三处实现。新增质量优先级矩阵（高频 × 对外，P0–P2）。执行步骤扩为 Step 0–7。Gotchas 6 → 13 条。
- **`dx-architecture-opt` → v2.0**：融合 des-governance-and-security。新增技术选型五条判断标准、HALT 七项 + 卡口执行规则 4 条。Gotchas 6 → 13 条。
- **`dx-industry-research` → v2.0**：政策层四件套、市场层三个必查问题、Step5 落回集团定位机会（四段结构）、新增图表要点规范。Gotchas 3 → 10 条。
- **`dx-competitor-scout` → v2.0**：新增差异化壁垒判断方法（四种壁垒强度排序）、Step4 口径对齐。Gotchas 3 → 12 条。
- **`dx-data-baseline` → v2.0**：四步法细化、脚本化盘点（工具决策树 + DuckDB 直扫）、访谈两轮制。Gotchas 8 条。
- **`dx-application-plan` → v2.0**：场景地图四象限、数据产品两类分表、入表路径四步、价值量化口径模板、汇报呈现规范。Gotchas 9 条。
- **frontmatter 规范化**：全部技能补 `description_en`、`allowed-tools`、`license`；中文 description 压缩至 ≤76 字符；`metadata` 统一为 `author / version / domain / fused_from`。
- **修正**：`dx-application-plan` 章节编号跳错（3 → 5 → 4 → 5）。
- **修正**：`~/.workbuddy/skills/` 下 `数据要素流通` 与 `数据交易所爬取` 原 frontmatter 为空 `{}`，导致模型无法自动触发 —— 已补齐 `name` + `description`。

### 安全
- `.gitignore` 调整：演示产出物（`_demo-run/`）改为**公开**（零敏感数据，是最有说服力的活演示），仅排除工具运行期临时文件。
- 全仓去敏感化复检通过（零真实客户标识）。

---

## [1.1.0] - 2026-09-12

### 新增
- **`01-OPEN-SOURCE-PLAN.md`** —— 开源化方案（定位 / 竞争格局 / 融合方案 / 对外目录 / License / 发布 checklist）。
- **`NOTICE.md`** —— 上游项目归属与许可证声明。
- **`cases/`** 案例层接口：`README.md`（接口规范 + 脱敏规则）、`_template/`、`sample-redacted/`。
- `.gitignore` —— 排除私有案例与敏感文件。

### 变更
- 能力融合：`dx-data-quality` 融合 data-governance 三处实现；`dx-architecture-opt` 融合 `des-governance-and-security`；`dx-data-baseline` 融合 `csv-data-wrangler` / `duckdb-skills`。

---

## [1.0.0] - 2026-09-12

### 新增
- 初始版本。7 个交付型 SKILL 骨架，以"七道工序（汇存治管服用模）"为骨架：
  `dx-engagement-orchestrator`、`dx-industry-research`、`dx-competitor-scout`、
  `dx-data-baseline`、`dx-architecture-opt`、`dx-data-quality`、`dx-application-plan`。
- 共享底座 `_shared/`（references / assets / scripts）。
- `00-PLANNING.md` 完整规划文档。
