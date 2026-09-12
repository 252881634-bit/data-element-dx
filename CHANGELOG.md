# Changelog

本文件记录 data-element-dx-skillkit 的所有重要变更。
格式参考 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.1.0/)，版本号遵循 [语义化版本](https://semver.org/lang/zh-CN/)。

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
