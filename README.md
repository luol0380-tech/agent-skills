# Reusable Agent Skills

一组可公开、可组合、跨 Agent/编程工具使用的 Skills。仓库只保存通用流程、模板和独立脚本；个人身份、写作风格、真实案例、账号配置及私密素材只保存在本地。

## 本地统一目录

将仓库克隆为一个固定的 `agent-skills/` 文件夹：

```bash
git clone <repository-url> agent-skills
cd agent-skills
python3 scripts/bootstrap_local.py
```

`bootstrap_local.py` 会根据公开的 `.example.md` 创建本地私有配置，但不会覆盖已经填写的文件。私有文件受 `.gitignore` 保护。

## 目录约定

每个 Skill 至少包含：

```text
skill-name/
├── SKILL.md
├── README.md
├── config/current_template.txt
├── templates/
├── scripts/
└── private/
```

- `SKILL.md`：平台中立的核心流程，只写工作方法与模板选择规则。
- `templates/`：可插拔模板，每个模板自带格式说明和最小示例。
- `config/current_template.txt`：未指定模板时使用的默认模板名。
- `scripts/`：仅使用 Python 标准库的可执行逻辑。
- `private/`：本地个人配置；只提交说明和示例文件。

## 已收录 Skills

- `interview-training/`：结构化面试训练与复习。
- `meeting-notes/`：会议纪要模板试点。
- `content-publishing/`：长文、短内容与发布包制作。
- `profile-poster-kit/`：人物介绍海报与角色设定图配套制作。
- `interview-animation-kit/`：访谈故事动画插片制作与交接。

## 校验

```bash
python3 scripts/audit_repository.py
```

如需扫描自定义敏感词，在仓库根目录创建不会被提交的 `.privacy-denylist`，每行写一个词，再运行同一命令。详见 [PRIVACY.md](PRIVACY.md)。
