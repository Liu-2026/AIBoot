<p align="center">
  <img src="docs/assets/aiboot-hero.png" alt="AIBoot — 做对项目，保持精简。" width="100%">
</p>

<p align="center">
  <strong>让 AI 开发，从写出代码走向完整交付。</strong><br>
  从想法到产品，为你的 AI 配备一套工程开发方法。
</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-2f855a" alt="MIT 许可证"></a>
  <a href="docs/setup.md"><img src="https://img.shields.io/badge/version-v0.2.0--alpha.7-2563eb" alt="v0.2.0-alpha.7"></a>
</p>

<p align="center">
  <a href="README.md">English</a> · <strong>简体中文</strong><br>
  <a href="#快速开始">快速开始</a> · <a href="#如何使用-aiboot">使用方法与提示词</a> · <a href="#让合适的-skills-与工具在需要时发挥作用">Skills 与工具</a> · <a href="CONTRIBUTING.md">参与贡献</a>
</p>

---

# AIBoot

**让有价值的想法，成长为经过认真设计的软件。**

AIBoot 为 **Codex、Cursor、Claude Code** 提供一套共享的工程开发方法：明确需求、
研究成熟方案、选择架构、规划任务、实现集成，再完成可用交付。
从项目起步到跨会话开发和后续维护，给 AI 一条贯穿项目生命周期的工作路径。

**一份核心文件，沿用你喜欢的工具和技术栈。** 将英文核心指导加入项目的原生指令入口，
然后描述你想完成的结果。开发工具提供执行、规划、Skills、MCP 连接、会话恢复和允许的协作；
AIBoot 将这些能力与实际工程决策衔接起来。

**开发结果优先。** 根据产品需要投入分析、设计、文档和验证，
让架构与流程服务真实用户、实际约束和业务价值。

## 为什么选择 AIBoot

- **起步有方向。** 将想法转化为明确范围、可观察的验收要求与可执行的计划。
- **站在成熟方案之上。** 实现前考虑维护良好的依赖、已有应用、官方脚手架与专项能力。
- **架构贴合实际。** 根据产品需要和团队维护能力安排前端、后端、数据与部署。
- **需求与交付相连。** 在正常项目记录中，将重要需求关联到任务、实现和完成证据。
- **开发持续推进。** 将目标、决策、已验证进展和下一步留给后续会话或协作者。
- **在需要时引入专业能力。** 按界面设计、SDK 集成、专项产物和外部服务匹配原生 Skills 与工具。
- **为后续演进做好准备。** 随项目发展，处理集成、审查、运行说明、兼容性与重要维护问题。

个人脚本、公司内部工具、面向客户的产品，以及包含多个模块和里程碑的大项目，
都可以使用这套工程指导。

## 快速开始

### 1. 准备你自己的项目目录

开发新产品时，创建独立目录，按需要用 `git init` 初始化 Git；
接入已有软件时，打开它当前的项目根目录。
AIBoot 提供工程指导，业务工程的结构由选定技术栈、适用脚手架和项目实际需要决定。

### 2. 加入核心指导

**最直接的方式：** [下载核心文件](https://raw.githubusercontent.com/Liu-2026/AIBoot/main/scaffold/AGENTS.md)，
将内容保存为**你自己项目根目录中的 `AGENTS.md`**。
已有同名文件时，在编辑器中合并适用指导，保留项目原来的开发约定。

想获取全部参考资料，可以运行
`git clone https://github.com/Liu-2026/AIBoot.git`，或
[下载 ZIP](https://github.com/Liu-2026/AIBoot/archive/refs/heads/main.zip)。
然后在 macOS/Linux 的目标项目目录中执行以下命令，并替换来源路径：

```sh
AIBOOT_SOURCE="/absolute/path/to/AIBoot"
test ! -e AGENTS.md && test ! -L AGENTS.md && \
  cp "$AIBOOT_SOURCE/scaffold/AGENTS.md" AGENTS.md
```

该命令会保留已有文件或符号链接；如果未复制，在编辑器中合并。
Windows 用户可以通过文件管理器，将 `AIBoot\scaffold\AGENTS.md` 复制到自己的项目根目录；
目标已有规范时先合并。再分发 AIBoot 内容时保留其 [MIT 声明](LICENSE)，产品自身许可继续保留。

最小目标目录如下：

```text
MyProject/
├── AGENTS.md          # AIBoot 指导 + 你的项目约定
├── .git/              # 产品自己的 Git 历史
└── ...                # 按选定技术栈创建的业务文件
```

Clone AIBoot 得到的是来源套件，分发核心位于 `scaffold/`。
开发自己的应用时，将它复制或合并到目标项目的原生入口；参与 AIBoot 本身开发时，使用 AIBoot 仓库。

### 3. 在目标项目中打开开发工具

- **Codex：** 使用根目录 `AGENTS.md`，启动新的项目会话。
  如果 `AGENTS.override.md` 生效，按优先级将适用指导合并到实际入口。
  [Codex 加载说明](adapters/codex/README.md)。
- **Cursor：** 使用根目录 `AGENTS.md`，打开项目并启动新的 Agent 会话。
  保留原有局部规则的用途，避免再配置一份始终加载的重复核心。
  [Cursor 加载说明](adapters/cursor/README.md)。
- **Claude Code：** 在支持的配置中直接使用 `AGENTS.md`。
  当 `CLAUDE.md` 是实际入口时，保留已有内容，并加入以下项目内导入。
  [Claude Code 加载说明](adapters/claude-code/README.md)。

```text
@AGENTS.md
```

上面的导入写入实际生效的 `CLAUDE.md`，路径相对于该文件。
可以通过工具提供的指令或上下文视图查看加载情况；实际加载遵循工具版本、设置和指令优先级。

### 4. 描述项目，开始工作

你可以使用熟悉的语言交流，也可以直接使用下面的英文示例：

```text
Build a room-booking app for our small team.
Staff should view, create, and cancel bookings; overlapping bookings are disallowed.
Use a simple deployment we can maintain. Consider suitable existing solutions,
libraries, and native Skills or tools before choosing the implementation.
Establish the project brief and actionable plan in suitable project records.
Implement the agreed scope in working stages. Deliver usable run instructions
and an accurate account of verification and remaining work.
```

提供真实用户、使用流程、必需行为、约束和有用示例；有参考资料或已有计划时一并引用。
AIBoot 通过普通任务请求提供指导，可以先要求规划，也可以明确授权实施。

## 如何使用 AIBoot

### 先研究规划，再实施

范围或技术选择需要讨论时，可以这样开始：

```text
Plan an inventory tool for our operations team.
We need item search, stock adjustments, and CSV export.
Compare suitable existing solutions and choose an approach for our actual needs.
Record scope, acceptance examples, consequential decisions, milestones, and dependencies.
Plan only; do not implement or deploy yet.
```

结果应说明已约定需求、相关选型和下一步工作。
确认重要选择后，再让 AI 实施已约定的计划。

### 根据已确认计划开发

```text
Implement the agreed scope in [plan or issue reference].
Check the current project state and finish the work in integrated stages.
Keep requirements connected to tasks, implementation, and completion evidence.
Update affected progress and decisions; make blockers or scope changes explicit.
```

将方括号替换为真实文档路径或 Issue 引用。对于实质项目，核心要求保留持久的项目知识，
可以复用已有 Issue、计划或文档。没有合适入口时，一份简明项目记录可以先容纳需求概要、
决策、计划和进度；随着内容规模、负责人员或使用方式变化，再按实际需要拆分。

例如，可以用 `docs/project.md` 保存这些信息，在 `AGENTS.md` 中留一个简短指针。
这是可选布局，并非固定文件名或必建文档套餐。共享记录按照你自己项目的 Git 策略管理。

### 新会话继续，或交接给协作者

```text
Continue from [current project record or issue reference].
Reconcile recorded progress with actual files and applicable evidence.
Complete the next agreed milestone and update the affected project records.
Leave the next action clear for the following session or collaborator.
```

优先使用工具的原生会话恢复。更换工具或协作者时，也可以依靠同一份持久记录与实际生效的指令入口。
里程碑处记录重要变化、阻塞和下一步；未改变的事实无需反复生成报告。
[连续开发说明](docs/setup.md#continue-work-across-sessions)。

### 完成一个局部修改

```text
Change [the specific behavior or text] to [the requested result].
Preserve unrelated behavior and existing conventions.
Review the affected change and perform relevant verification.
```

普通修改沿用已有上下文并聚焦当前工作。变更确实影响需求或架构时，再展开相应研究与规划。

### 审查交付，或准备维护

```text
Review this milestone against the agreed requirements.
Connect each important requirement to its implementation and evidence.
Check usable run instructions and relevant integration or migration needs.
Report remaining, blocked, deferred, and unverified work accurately.
```

重构时说明已经出现的问题与需要保持的行为；核心指导 AI 关注受影响接口、依赖模块，
以及实际需要的数据迁移或回滚。发布和部署沿用你的既有授权。
[查看更多任务提示词](docs/prompts.md)。

## 贯穿项目的工程流程

**需求 → 研究选型 → 设计规划 → 实现集成 → 验证审查 → 交付接续**

重要需求保留来源与约定状态、可观察的验收示例、相关任务和依赖、实现引用，
以及完成证据或验证缺口。在已有记录中使用链接与简短标识即可，里程碑结束前核对完整约定范围。

例如：**“禁止重叠预约” → 预约冲突任务 → 预约模块 → 相关行为证据。**
规则变化时，同步调整受影响的计划、接口和证据；进度由实际成果和当前状态说明，估算给出依据。

多模块或允许的原生子 Agent 工作中，先约定接口、共享变更的负责人和集成顺序，
明确组合成果的交付责任。开发工具管理协作与执行。
[开发流程说明](docs/setup.md#follow-the-development-workflow)。

## 让合适的 Skills 与工具在需要时发挥作用

**描述实际任务，让专业能力发挥在关键环节。**

默认核心提供任务触发条件与发现入口。新项目、任务性质明显变化或出现专项需要时，
指导 AI 将任务与已安装 Skills、已连接工具和现有项目方法匹配。

- **界面设计：** Impeccable 等适用指导，可以结合用户、内容和视觉参考形成鲜明产品方向。
- **SDK 与 API：** 已连接的 Context7 或官方版本文档，为实现提供相关依据。
- **外部服务：** 已连接集成与原生插件／MCP 发现，帮助寻找适合当前任务的服务能力。
- **专业工作：** 根据实际需要，选择数据库、浏览器、安全审查、移动端和文档产物方法。

存在有用的能力缺口时，定向上游搜索、skills.sh 和公开 MCP 元数据提供候选，
私有集成使用组织来源。安装、加载、连接、权限和执行由开发工具管理。
AIBoot 提供选择与失败处理指导；复制参考文件本身不会连接服务或安装第三方 Skills。

### 接入可选能力参考

默认核心已经包含发现指导。需要十类精选路线时，将 `scaffold/capabilities.md`
复制到适合的位置，例如 `docs/aiboot-capabilities.md`；目标已有文件时先合并。
然后在实际生效的项目指令入口中加入这个普通指针：

```text
When a task needs a specialized capability or existing methods leave a useful gap,
consult the matching section of docs/aiboot-capabilities.md on demand.
```

保持按需阅读。[能力接入说明](docs/setup.md#optional-capability-discovery)
提供带保护的复制命令，以及选择和访问指导。

## 在项目中更新 AIBoot

1. 获取新版核心，与已安装版本及本地修改对比。
2. 合并适用变更，保留项目约定和已有记录。
3. 在正常 Git 变更说明中记录来源版本或提交。
4. 刷新工具的项目会话，查看实际生效的指令入口。

可选参考采用相同方式更新。移除 AIBoot 时，移除可辨认的指导或导入，保留有用的项目事实与本地修改。
[更新与移除说明](docs/setup.md#update-and-remove)。

## 套件内容

```text
scaffold/AGENTS.md            # 共享工程开发方法
scaffold/capabilities.md      # 可选专项能力路线
adapters/                    # 原生加载说明
docs/setup.md                # 详细接入与生命周期指南
docs/prompts.md              # 规划、实施、续接和交付提示词
docs/assets/aiboot-hero.png   # 项目主视觉
```

核心指导适用于不同技术栈。产品自己的目录、依赖、测试、CI、文档和发布流程由项目掌握。

## 一起把好方法做得更好

AIBoot 采用 **MIT 开源许可**。欢迎分享实际工作流、完善能力路线，
让指导更清晰、更好用。

- [贡献指南](CONTRIBUTING.md) — 贡献与 Git 工作方式。
- [接入指南](docs/setup.md) — 项目接入与生命周期。
- [任务提示词](docs/prompts.md) — 可以直接改用的起步示例。
- [Issues](https://github.com/Liu-2026/AIBoot/issues) — 反馈、想法与实际案例。

**为 AIBoot 点一颗 Star，让更好的工程习惯融入 AI 开发。**

## 开源许可

[MIT](LICENSE)。项目视觉素材为 AIBoot 原创制作。
