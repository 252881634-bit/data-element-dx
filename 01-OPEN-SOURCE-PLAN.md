# 开源化方案（Open-Source Plan）

> 项目：`data-element-dx-skillkit` — 数据要素 × 传统集团数字化转型交付套件
> 版本：v1.0 ｜ 日期：2026-09-12 ｜ 作者：李可顺（大数据猎人）
> **重要约束：案例层不含任何真实客户数据，由作者后续按接口自建；公开仓只放接口规范与脱敏样例。**

---

## 1. 开源定位（一句话）

> **面向中国国企与线下平台型集团的数据要素转型交付套件——不是教程，是能直接交给董事长的东西。**

面向人群：数据要素/数据治理从业者、国企/集团数字化团队、咨询顾问、数商。
产出定位：**交付物**（指标字典、资产清单、架构蓝图、入表路径、汇报材料），而非知识点。

---

## 2. 竞争格局：有"零件"，没有"整机"

调研（2026-09-12）确认：现有主流/高星 Skill 全部集中在**单点技术能力**，无一做端到端交付。

| 现有 Skill | 覆盖 | 缺口 |
|---|---|---|
| `data-governance`（skillkit.io / cbrock84/headcount / omer-metin/skills-for-antigravity，Apache-2.0） | 数据目录、血缘、质量规则、owner | 仅"治"，无摸底/架构/应用/入表 |
| `des-governance-and-security`（DKSang/DES-SKILL） | 权限/RLS/PII/保留期/审计 | 纯技术治理，无方法论 |
| `gtm-agents/data-governance` | 数据契约、consent、身份解析 | 营销自动化场景 |
| `data-analyst` / `csv-data-wrangler` / `duckdb-skills` | 数据分析技术动作 | 无集团/咨询视角 |
| **本套件** | **端到端交付链 + 编排 + 七道工序** | — |

### 2.1 我们的四条真差异化
1. **交付型 vs 工具型**：别人给"能力原子"，我们给"交付流水线 + 阶段门禁 + 实物成果"。
2. **中文国资语境的独有骨架**：七道工序（汇存治管服用模）、DCMM（GB/T 36073）对标、数据二十条/入表暂行规定/公共数据授权运营政策锚点。
3. **编排层（生态空白）**：`dx-engagement-orchestrator` 强制因果顺序与阶段门禁——**现有任何 skill 都没有编排层**，这是最难复制的部分。
4. **真实项目反哺的 gotchas**：血泪教训（抽象化后开源）是抄不走的资产。

### 2.2 劣势与对策（诚实评估）
| 风险 | 对策 |
|---|---|
| 无技术壁垒（全 Markdown，可 Fork） | 壁垒在方法论 + 案例 + 持续迭代，不在代码 |
| 受众窄（政企/咨询，非大众开发者） | 受众窄但专业，走专业影响力而非 star 路线 |
| 中文/政策绑定 | 服务国内市场足够；可出英文版讲"公共数据运营" |
| 无法自动验证交付质量 | 用 skill-creator eval + 案例回归测触发准确率 |
| 甲方信任成本 | 用专著《国企数据突围》+ 脱敏案例背书 |

---

## 3. 与现有 data-governance 类技能的融合方案

> 原则：**不重造轮子，把成熟单点能力"吃进"我们的交付链**，并在 SKILL.md 中显式标注 `fused_from`。

### 3.1 融合映射表
| 来源 Skill | 吸收的能力 | 落点技能 |
|---|---|---|
| `data-governance`（三处实现） | **指标字典（Metric Dictionary）**、具名 Owner、血缘、质量"实测而非宣称"、默认开放访问 | **dx-data-quality**（已融合 ✅） |
| `des-governance-and-security` | RBAC + RLS/列级安全、PII 分类、脱敏/令牌化、保留期与删除、审计日志、**HALT 停机卡口** | **dx-architecture-opt**（已融合 ✅） |
| `csv-data-wrangler` | 按规模选 tool 的决策树（pandas→Polars/DuckDB→Spark） | **dx-data-baseline**（已融合 ✅） |
| `duckdb-skills` / `duckdb-analytics` | DuckDB 直查 CSV/Parquet 做表画像 | **dx-data-baseline**（脚本化盘点） |
| `pandas-pro` | 清洗/透视/时序处理 | dx-data-quality（清洗规则） |
| `data-analyst`（What/So What/Now What） | 分析叙事框架 | dx-application-plan（呈现） |

### 3.2 融合后的能力对比
| 能力 | 纯 data-governance | 本套件融合后 |
|---|---|---|
| 指标口径 | ✅ 指标字典 | ✅ 指标字典 **+ 中文国资场景预设** |
| 所有权 | ✅ 具名 owner | ✅ + 主数据唯一标识规则 |
| 质量 | ✅ 实测告警 | ✅ + 绑定业务语义的可机检规则 |
| 访问/合规 | ⚠️ 部分（des-governance） | ✅ 默认开放 + 受限数据卡口 |
| 摸底/盘点 | ❌ | ✅ 脚本化盘点 + DCMM 评分 |
| 架构/蓝图 | ❌ | ✅ 七道工序分层 + 治理卡口 |
| 应用/入表 | ❌ | ✅ 场景地图 + 财政部规定口径 |
| 编排/门禁 | ❌ | ✅ orchestrator |
| 交付物 | 治理文档 | 全链实物成果 |

### 3.3 融合的工程做法
1. 每个来源在目标 SKILL.md 的 `metadata.fused_from` 中标注（**保留 Apache-2.0 归属**）。
2. 在根目录建 `NOTICE.md` 列明上游项目与许可证。
3. 能力吸收后**不照抄文本**，改写为中文国资语境 + 补充 gotchas。

---

## 4. 对外目录结构（公开仓）

> **结构约束（重要）**：技能内对共享底座是**相对路径引用**（`../_shared/...`），
> 因此 **`dx-*` 技能目录必须与 `_shared/` 同级**，发布结构与本地结构保持一致。
> 早期规划的 `skills/` 子目录方案与相对引用不兼容（拆入子目录后 `../_shared` 即断链），已弃用。
> 安装到用户技能目录时同样保持同级（见 `HOW-TO-USE.md`）。

```
data-element-dx/
├── README.md                      # 中文主 README
├── README.en.md                   # 英文 README（国际差异化：公共数据运营+入表）
├── LICENSE                        # Apache-2.0
├── NOTICE.md                      # 上游项目归属（data-governance 等）
├── 00-PLANNING.md                 # 规划（可开源）
├── 01-OPEN-SOURCE-PLAN.md         # 本方案
├── HOW-TO-USE.md                  # 安装与试跑说明
├── CHANGELOG.md                   # 版本变更
├── CONTRIBUTING.md                # 贡献指南
├── 全景图.html                    # 一页可视化全景
├── dx-engagement-orchestrator/    # 7 个技能（与 _shared 同级，相对引用生效）
├── dx-industry-research/
├── dx-competitor-scout/
├── dx-data-baseline/
├── dx-architecture-opt/
├── dx-data-quality/
├── dx-application-plan/
├── _shared/
│   ├── references/                # 七道工序方法论/DCMM对标/政策索引/规则库
│   ├── assets/                    # 指标字典/调研问卷/资产目录/架构蓝图模板
│   ├── scripts/                   # maturity_score.py / scan_assets.py / gate_check.py
│   └── eval/                      # 触发测试集（应触发/不应触发样例）
├── cases/                         # 案例层（接口开源，内容自建）
│   ├── README.md                  # 接口规范 ✅
│   ├── _template/                 # 空白模板 ✅
│   └── sample-redacted/           # 脱敏样例（虚构集团A）✅
├── docs/images/                   # README 视觉素材
├── _demo-run/                     # 端到端试跑产物（零敏感数据，公开）
├── .gitignore                     # 排除 cases/*/ 私有案例
└── CONTRIBUTING.md                # 贡献指南
```

---

## 5. MVP 范围（先做最小可用，再铺全）

**不要先开源 7 个空壳。** 建议 MVP 只放 2–3 个"能跑通真实交付"的技能：

| 优先级 | 内容 | 理由 |
|---|---|---|
| P0 | `_shared/` 底座 + `dx-data-baseline` + `dx-engagement-orchestrator` | 摸底是门禁第一关，编排是差异化核心；**有 1 个真实案例即可开源** |
| P1 | `dx-data-quality`（已融合指标字典） | 融合后价值密度最高，易出彩 |
| P2 | 其余 4 个 | 按项目节奏补齐 |

**开源门槛（Gate）**：MVP 至少包含 1 个**脱敏真实案例** + 2 个技能的完整可用版 + README 双语。

---

## 6. License 与合规

- **License：Apache-2.0**（与融合来源一致，含专利授权与归属条款，商企友好）。
- **NOTICE.md**：列明 `data-governance` 三处实现、`des-governance-and-security` 等上游归属。
- **案例层合规**：公开仓 **零真实客户数据**；`cases/*/` 进 `.gitignore`；只开源 `_template/` 与 `sample-redacted/`。
- 政策引用（数据二十条等）属公开信息，可引用；引用需标注来源。

---

## 7. README 双版策略

### README.md（中文，主打）
结构：一句话定位 → 差异化（对比表）→ 七道工序全景图 → 6 技能速览 → 快速开始（装 + 跑一次摸底）→ 案例（脱敏）→ 路线图 → 贡献 → License。
**关键词前置**：数据要素、国企数字化转型、DCMM、数据资产入表、数据治理、指标体系。

### README.en.md（英文，次打）
定位改为："Data-Element Transformation Delivery Kit for China's SOEs and Traditional Conglomerates"。
重点讲**公共数据运营 + 数据资产入表**这一国际少见视角（**这是英文区的差异化**）。

---

## 8. 发布渠道与节奏

| 渠道 | 作用 | 动作 |
|---|---|---|
| GitHub | 主仓、技术影响力 | 公开仓 `data-element-dx`，Apache-2.0 |
| SkillsMP / ClawHub / AgentSkillsHub | 分发与曝光 | 提交收录，靠 description 关键词提触发率 |
| 公众号（大数据猎人） | 方法论内容 + 导流 | 每篇讲一个工序，文末挂 GitHub |
| 专著《国企数据突围》 | 信任背书 | 书内/后续版本引用本套件 |

**节奏**：Day 0 MVP 上线 → Day 7 第一篇方法论文章 → Day 30 第二个技能 + 第二个案例 → 季度节奏补技能与案例。

---

## 9. 质量门禁与迭代（eval loop）

- **触发准确率**：每个技能写 3–5 条"应触发/不应触发"样例，回归测试 description。
- **交付完整性**：每个技能末尾的检查表必须可勾选。
- **案例回归**：新案例跑通后，回写 gotchas 到对应 SKILL.md。
- **版本 pin**：生产项目锁定技能版本，避免自动更新破坏交付口径。
- **泛化而非过拟合**：技能改动用"解释为什么"而非堆砌"必须"（skill-creator 核心洞察）。

---

## 10. 维护与可持续性

- **单维护者风险**：明确 CONTRIBUTING.md，开放社区补案例（案例层天然适合众包）。
- **迭代纪律**：每交付一个真实项目 → 沉淀 1 个脱敏案例 + 回写 gotchas。
- **不承诺 SLA**：个人项目，明确"best effort"，避免咨询客户误当产品。
- **商业化留白**：开源方法论层，保留**定制咨询/内训/行业案例库**作为商业化路径（与开源不冲突）。

---

## 11. 发布 Checklist（上线前逐项打勾）

- [ ] LICENSE（Apache-2.0）+ NOTICE.md（上游归属）已就位
- [ ] README.md + README.en.md 双语完成
- [ ] 公开仓 **零真实客户数据**（`.gitignore` 生效，人工复核一遍）
- [ ] MVP 技能（data-baseline + orchestrator）可用版完成
- [ ] 至少 1 个脱敏案例（虚构集团）可展示格式
- [ ] `_shared/scripts/` 两个脚本在干净环境跑通（零依赖）
- [ ] 每个 SKILL.md 有 gotchas 段与交付物检查表
- [ ] 提交到 SkillsMP / ClawHub 收录
- [ ] 公众号首篇方法论文章草稿就绪

---

## 12. 后续可选演进

1. **案例层众包**：开放社区提交脱敏案例，形成"行业 × 案例"矩阵。
2. **英文版独立仓**：面向公共数据运营/入表的国际受众。
3. **工具化**：把 `maturity_score.py` / `scan_assets.py` 扩展为可安装 CLI（`npx data-element-dx`）。
4. **可视化**：七道工序全景图做成可交互 HTML（对接你的 demo/PPT 视觉体系）。
5. **评测集**：构建"交付质量评估集"，用 skill-creator 的 Grader/Comparator 思路做回归。

---

*本方案不含任何真实客户数据。案例层由作者后续按 `cases/README.md` 接口自建，公开仓仅保留模板与脱敏样例。*
