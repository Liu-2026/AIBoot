<p align="center">
  <img src="docs/assets/aiboot-hero.png" alt="AIBoot — 做对项目，保持精简。" width="100%">
</p>

<p align="center">
  <strong>让 AI 懂工程，把想法做成好项目。</strong><br>
  方向清晰 · 善用成熟方案 · 专注交付
</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-2f855a" alt="MIT 许可证"></a>
  <a href="docs/setup.md"><img src="https://img.shields.io/badge/version-v0.2.0--alpha.5-2563eb" alt="v0.2.0-alpha.5"></a>
</p>

<p align="center">
  <a href="README.md">English</a> · <strong>简体中文</strong><br>
  <a href="#快速开始">快速开始</a> · <a href="#让合适的能力出现在合适的任务中">Skills 与工具</a> · <a href="docs/setup.md">接入指南</a> · <a href="CONTRIBUTING.md">参与贡献</a>
</p>

---

# AIBoot

**从一个清晰的想法，开始一个经过认真思考的项目。**

AIBoot 为 **Codex、Cursor、Claude Code** 带来实用的工程开发指导：帮助 AI 理清目标、
选择成熟方案、规划下一步，并通过与任务相关的验证完成交付。

**一份核心文件，沿用你喜欢的工具和技术栈。** 将 AIBoot 加入项目的原生指令入口，
然后描述你想完成的事情。英文核心指导与开发工具的规划、Skills、MCP 集成、
会话恢复和允许使用的子 Agent 协同工作。

## 为什么选择 AIBoot

好项目，始于好决策。AIBoot 将这些关键判断融入 AI 开发工作流：

- **清晰的起点。** 将想法转化为明确目标、合理的首个里程碑与可执行的开发任务。
- **善用成熟方案。** 在选择实现方式前，考虑成熟依赖、已有应用、官方脚手架和专项能力。
- **恰到好处的架构。** 根据用户与真实需求安排前端、后端、数据、部署和质量工作。
- **按场景选择能力。** 将设计、文档、服务集成和专业任务与适用的原生 Skills、工具匹配。
- **有价值的上下文。** 按需阅读专项参考，保留有助于后续判断和交接的项目事实。
- **明确的交付结果。** 验证相关成果，向用户准确、清晰地说明完成了什么。

从个人脚本、公司内部工具到面向客户的产品，AIBoot 都可以为下一次从零开发提供工程指导。

## 快速开始

### 1. 获取 AIBoot

运行 `git clone https://github.com/Liu-2026/AIBoot.git`，或
[下载 ZIP](https://github.com/Liu-2026/AIBoot/archive/refs/heads/main.zip)。

### 2. 加入核心指导

在目标项目目录中运行：

```sh
AIBOOT_SOURCE="/absolute/path/to/AIBoot"
test ! -e AGENTS.md && test ! -L AGENTS.md && \
  cp "$AIBOOT_SOURCE/scaffold/AGENTS.md" AGENTS.md
```

macOS/Linux 示例会保留已有文件与符号链接。项目已有规范时，在编辑器中合并适用指导；
Windows 用户可以手动复制同一个文件。详见[接入指南](docs/setup.md)。

选择当前工具的加载说明：

- **[Codex](adapters/codex/README.md)** — 项目 `AGENTS.md`。
- **[Cursor](adapters/cursor/README.md)** — 项目 `AGENTS.md`。
- **[Claude Code](adapters/claude-code/README.md)** — 支持时直接加载 `AGENTS.md`，
  或通过项目内的 `CLAUDE.md` 导入。

### 3. 描述你想完成的结果

可以直接使用英文提示词：

```text
Build a small booking app for our team.
Start with the simplest useful booking flow.
Consider suitable existing libraries and native Skills or tools.
Implement the first working result and show how you verified it.
```

研究与规划阶段，补充 “plan only; do not implement yet”。接续已有项目时，
描述下一项成果，并引用当前项目事实。

## 跨会话，持续推进

**更换会话或协作者，仍然知道下一步做什么。**

AIBoot 指导 AI 使用原生恢复能力与已有计划、Issue 或项目文档。
关键状态需要持久保存时，保留一份简短记录，涵盖目标、已验证成果、未完成事项、
阻塞、下一步和关键决策引用。

记录随里程碑与交接更新；接续开发时，核对实际文件状态与仍然适用的验证证据。
开发约定则从技术栈和团队共识中逐步形成。[查看连续开发说明](docs/setup.md#continue-work-across-sessions)。

## 让合适的能力出现在合适的任务中

**描述任务，让工程指导帮助 AI 找到合适的实现路径。**

默认核心包含任务触发条件与发现入口。新项目、任务性质明显变化或出现专项需求时，
它指导 AI 考虑适用的已安装 Skills、已连接工具和已有项目方法。

- **界面设计：** Impeccable 等适用的设计 Skill，可结合产品与用户形成鲜明的视觉方向。
- **SDK 与 API 开发：** 已连接的 Context7 或官方版本文档，可提供相关实现参考。
- **外部服务集成：** 已有集成与原生插件／MCP 发现，可帮助任务对接适用的服务能力。
- **日常修改：** 聚焦实现与相关检查，让小任务保持简洁顺畅。

需要补充能力时，可通过上游项目、skills.sh 和公开 MCP 元数据寻找候选；
私有集成使用组织来源。加载、授权与执行由开发工具负责。

可选的[能力参考](scaffold/capabilities.md)提供**十类专项路线**，覆盖文档查询、界面设计、
React、浏览器验证、Postgres、移动端、Azure SDK、安全审查、文档产物与服务集成。
[按需接入](docs/setup.md#optional-capability-discovery)，阅读与当前任务相关的部分。

## 贴合真实开发方式

- **开始一个新应用：** 明确首个有用流程，选择匹配的技术栈。
- **开发内部工具：** 研究适合的已有产品与成熟依赖。
- **制作品牌页面：** 将真实内容和视觉参考交给适用的设计 Skill。
- **完成局部修改：** 让实现与验证聚焦当前任务。
- **跨会话继续开发：** 从当前事实和仍然适用的证据继续推进。
- **为后续维护做好准备：** 随项目演进，重视清晰代码、合理边界与有用的项目知识。

## 轻量核心，广泛适用

```text
scaffold/AGENTS.md            # 核心工程指导
scaffold/capabilities.md      # 可选的专项能力参考
adapters/                    # 各开发工具的原生加载说明
docs/setup.md                # 接入、迁移、更新与移除
docs/assets/aiboot-hero.png   # 项目主视觉
```

AIBoot 工作在指令层。技术栈、业务目录、测试、CI 与现有文档由项目自己掌握；
原生工具负责执行，核心指导提供一致的工程思考方式。

## 一起把好方法做得更好

AIBoot 采用 **MIT 开源许可**。欢迎分享你的工作流与实际案例、完善能力路线，
或让工程指导更清晰、更好用。

- [贡献指南](CONTRIBUTING.md) — Git 工作方式与贡献说明。
- [接入指南](docs/setup.md) — 接入方式与项目生命周期。
- [Issues](https://github.com/Liu-2026/AIBoot/issues) — 建议、反馈与实用案例。

**喜欢这套思路？为 AIBoot 点一颗 Star，让更多开发者把想法做成好项目。**

## 开源许可

[MIT](LICENSE)。项目视觉素材为 AIBoot 原创制作。
