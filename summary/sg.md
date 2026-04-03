我先补一下仓库里 skill 这一层是怎么实现的，再结合 OpenAI Agents SDK 的能力，给你一个更贴近你们场景的架构建议。

搜索正则表达式 `class SkillLoader|def descriptions|def load|"load_skill"` (`**/agents/s_full.py`)，5 个结果

读取 [](file:///d%3A/registry/self/learn-claude-code/docs/en/s05-skill-loading.md)

读取 [](file:///d%3A/registry/self/learn-claude-code/skills/agent-builder/SKILL.md)

我的看法很明确：

**你们要做的核心产品，其实不是一个“agent SDK”，而是一个“Skill OS / Skill Hub + Agent Runtime”。**

OpenAI Agents SDK 没有把 skill 做成一等原语，这并不奇怪，也不一定是缺点。因为在工程上，skill 往往不是模型厂商定义的通用抽象，而是你们产品层自己的抽象。

从这个教学项目里也能看出来，skill 本质上是“按需注入的知识层”，不是底层循环本身的一部分：
s_full.py
s_full.py
s_full.py
s05-skill-loading.md

这个仓库里的 skill 设计非常接近 Claude Code 一类产品的关键思路：

1. 系统提示里只放 skill 的名字和简介
2. 真正需要时，再通过 load_skill 把完整内容按需注入
3. skill 不一定是“工具”，它更像“能力包 / 知识包 / 工作方式包”

这在 s05-skill-loading.md 里讲得很清楚。

所以先说结论：

**OpenAI Agents SDK 仍然可以用。**
但你不能指望它原生帮你做完整的 skill hub。
它更适合当“agent runtime 内核”，而你们自己做“skill 平台层”。

**为什么我不建议把 skill 绑死在某个 SDK 上**

因为你们的需求已经不是单纯“让模型调几个函数”了，而是下面这套完整系统：

1. 前端网页
2. 后端 API
3. 远程服务器执行 agent
4. skill 可内置、可自定义、可版本化
5. agent 能像 Claude Code 一样工作
6. 执行结果、过程事件、产物都要回传前端

这里面真正有产品壁垒的是：

1. skill 的组织方式
2. skill 的版本和权限
3. skill 如何影响 prompt、tools、MCP、审批、输出格式
4. skill 如何在运行时被选择、加载、组合
5. skill 如何做评测和发布

这些都不是某个 SDK 能替你定义好的。

换句话说：

**agent SDK 解决的是“怎么跑 agent”**
**skill hub 解决的是“agent 该带着什么能力包去跑”**

这是两层东西。

**我对 OpenAI Agents SDK 的判断**

它适合作为你们底层执行引擎，原因是它已经把很多通用 runtime 能力封装好了：

1. agent loop
2. tools
3. handoffs / agents as tools
4. sessions
5. human-in-the-loop
6. tracing
7. MCP 集成

所以如果你们选它，合理姿势不是“等它支持 skills”，而是：

**把 skill 实现为你们自己的上层抽象，再映射到 SDK 的 instructions、tools、MCP、handoffs、sessions。**

也就是说：

- skill 不是 SDK primitive
- skill 是你们编排层的 primitive

这是完全可行的，而且我认为是正确做法。

**我建议你们把 skill 定义成什么**

不要把 skill 只当一段 prompt markdown。

如果你们想做平台，skill 至少应该是一个“可发布的能力单元”，包含这些内容：

1. 元数据
skill id
name
version
author
description
tags
visibility
tenant scope

2. 触发信息
适用场景
关键词
路由规则
前置条件

3. 指令层
system augmentation
working style
约束
few-shot 示例

4. 资源层
参考文档
模板
示例代码
知识文件
外部链接

5. 工具层
允许使用哪些工具
工具参数约束
工具权限范围
是否需要审批

6. 执行层
是否需要专属子代理
是否需要 MCP server
是否需要独立沙箱
超时 / 重试 / 并发设置

7. 输出层
输出 schema
结果格式
前端渲染类型

8. 质量层
测试集
评测规则
上线门槛
版本回滚策略

你们可以把它理解成：

**skill = prompt + resources + tool policy + execution policy + output contract**

如果只做 prompt 包，很快就会不够用。

**结合你们场景，我建议的系统分层**

我建议把系统拆成 5 层。

**1. Skill Hub 平台层**
这是你们真正的产品核心。

职责：
1. 管理内置和自定义 skill
2. skill 版本化
3. skill 审核与发布
4. skill 搜索、标签、分类
5. skill 权限和租户隔离
6. skill 的 eval 和回滚

**2. Skill Resolution 层**
在一次请求开始时，决定该加载哪些 skill。

职责：
1. 根据用户意图检索 skill
2. 根据 workspace / tenant / policy 过滤 skill
3. 根据风险等级决定是否允许自动加载
4. 决定是直接装配，还是先让一个 router agent 选 skill

这层非常关键。因为 Claude Code 风格的体验，本质上不是“用户手动选 skill”，而是“系统能合理决定该用哪个 skill”。

**3. Agent Runtime 层**
这层可以用 OpenAI Agents SDK，也可以用别的。

职责：
1. 跑 agent loop
2. 管理 session / memory
3. 执行 tools / MCP / handoff
4. 流式事件输出
5. 人工审批暂停与恢复

**4. Tool Sandbox / Worker 层**
这层负责真正执行高风险动作。

职责：
1. 文件读写
2. shell / code execution
3. git 操作
4. 外部 API 调用
5. 资源配额控制
6. 审计日志

如果你们要“像 Claude Code 那样干活”，这层比 skill 文本更重要。
因为真正难的是“安全、隔离、可恢复地执行动作”。

**5. Frontend / Session UI 层**
职责：
1. 展示消息流
2. 展示工具调用过程
3. 展示 skill 选择和加载过程
4. 展示审批节点
5. 展示产物 diff、日志、文件结果

如果前端只显示最终答案，体验会很差。
Claude Code 类产品的关键体验之一，是“可见的执行过程”。

**OpenAI Agents SDK 在这里怎么用**

我建议你们把它放在第 3 层，也就是 runtime 层。

典型流程可以这样设计：

1. 前端发起任务
2. 后端先做 skill resolution
3. 把选中的 skill 装配成一次运行上下文
4. 基于这次上下文动态创建 agent
5. 将允许的 tools / MCP / 输出 schema / 审批规则一起注入
6. 运行 agent
7. 将流式事件返回前端

关键点在于：

**skill 不一定在 agent 运行过程中再“现学现用”**
你也可以在运行前先完成 skill 装配

这点很重要，因为很多 SDK 对“运行中动态修改工具集”支持并不是它的主要设计目标。
但如果你们做“两阶段执行”，就完全没问题：

**阶段 1：选 skill**
- 检索
- 评分
- 过滤
- 装配

**阶段 2：跑 agent**
- 用装配后的 instructions + tools + MCP + policy 去执行

这样会比在单个 loop 里临时热插拔 skill 稳很多。

**如果你们坚持做“运行中 load_skill”**

也不是不行，但我建议 skill 分两种：

1. 轻量 skill
只是知识注入
等价于这个教学项目里的 load_skill
参考：
s_full.py
s05-skill-loading.md

2. 重型 skill
会改变工具集、MCP、权限、审批策略、输出模式

对于重型 skill，不建议在同一个运行上下文里直接热插拔。
更稳妥的方式是：

1. 当前 agent 识别出需要某个 skill
2. 发起一次 handoff / subagent run
3. 用该 skill 的完整运行配置启动子代理
4. 子代理执行完返回结果

这和 OpenAI Agents SDK 的 handoffs 思路是兼容的。

所以你们完全可以实现一种产品语义：

- 轻量 skill = load 到当前上下文
- 重型 skill = 派生一个 skill-specific subagent 去执行

这个模型很实用。

**我对你们产品方向的建议**

如果你们是做 skill hub 平台，我会建议：

**不要围绕某个 SDK 的能力设计产品。**
应该反过来：

**先定义你们自己的 Skill Spec，再选一个 SDK 当执行后端。**

也就是说，先定义下面这些接口和契约：

1. Skill Manifest 长什么样
2. Skill 如何声明自己依赖的资源
3. Skill 如何声明自己允许的工具
4. Skill 如何声明自己要求的审批策略
5. Skill 如何声明输出格式
6. Skill 如何做版本与兼容性管理

然后做一个 runtime adapter：

- OpenAI Agents SDK adapter
- 未来也可以接 PydanticAI adapter
- 再未来甚至可以接自研 runtime adapter

这样你们不会被单个供应商锁死。

**如果只从“你们现在最适合用什么”来判断**

我会这样排：

**方案 A：OpenAI Agents SDK + 自研 Skill Hub**
这是我最推荐的折中方案。

优点：
1. runtime 不用从零造
2. 你们把精力放在真正有差异化的 skill 平台
3. handoff、session、tracing、HITL 这些通用件不用自己补太多

缺点：
1. skill 不是一等原语，要你们自己封装
2. 如果后面要深度做 durable workflow，可能还要再补一层

适合你们现在这个阶段。

**方案 B：PydanticAI + 自研 Skill Hub**
如果你们偏 Python 后端工程化、类型安全、评测和可观测很重，我会认真考虑它。

它比较适合 skill 平台这种“配置驱动 + 严格输出 + 强工程规范”的方向。
尤其当 skill 不只是 prompt，而是“有 schema、有依赖、有能力包”的时候，它会更顺手。

如果你们以后很强调：
1. typed outputs
2. MCP
3. evals
4. durable execution
5. model-agnostic

那它可能比 OpenAI Agents SDK 更贴近平台型产品。

**方案 C：自己继续扩展 learn-claude-code 这套**
我不建议直接这么做，除非目标只是内部原型。

原因不是它思路不对，而是生产缺的东西太多：
1. 多租户
2. 权限模型
3. 审批流
4. durable execution
5. 观测
6. 分布式 worker
7. 版本治理
8. 评测体系

这个项目适合你们“吃透模式”，不适合直接演进成平台底座。

**我对“像 Claude Code 那样干活”的额外提醒**

很多人会误以为 Claude Code 的核心是 skills。
其实不是。

skills 很重要，但它只是其中一层。
真正让系统“像 Claude Code 一样工作”的，通常还有：

1. 强文件 / shell / git 工具链
2. 受限但高可用的执行沙箱
3. 长任务状态管理
4. 上下文压缩与摘要
5. 子代理 / 分治
6. 工具调用可见性
7. 对失败的恢复能力
8. 清晰的审批与权限边界

这个教学项目里已经把其中几块思路展现出来了：
s_full.py
s_full.py
s_full.py
s_full.py
s_full.py

所以我的判断是：

**你们真正要做的不是“支持 skills 的 agent”。**
而是：

**一个以 skill 为配置中枢，以 agent runtime 为执行引擎，以 sandbox 为行动边界的平台。**

这才是对的产品定义。

**如果让我给你们一个很实际的落地方案**

我会建议第一版这么做：

1. Skill 先只支持两类
Knowledge Skill
Execution Skill

2. Knowledge Skill
作用：
注入领域知识、工作规范、输出模板
实现：
类似这个项目的 SkillLoader 机制
参考：
s_full.py

3. Execution Skill
作用：
声明专属工具集、MCP、审批策略、输出 schema
实现：
运行前装配，必要时起专属子代理

4. Runtime 先用 OpenAI Agents SDK
原因：
先把 loop、session、tool calling、streaming、tracing 跑起来

5. Skill Hub 自己做
包括：
数据库
对象存储
版本管理
发布流
权限模型
检索和推荐

6. Worker 独立部署
不要让 Web API 进程直接跑高风险 agent 任务

这样做，产品和底层都比较稳。

**一句话总结我的建议**

OpenAI Agents SDK 可以用，但别把“它不原生支持 skills”当成阻碍。
对你们这种 skill hub 产品来说，skills 本来就应该是你们自己定义的平台层抽象，而不是把产品核心外包给底层 SDK。

如果你愿意，我下一步可以直接继续给你两种更具体的输出之一：

1. 画一张适合你们场景的整体系统架构图
2. 帮你定义一版 Skill Manifest 规范，直接落到可实现的数据结构和字段设计