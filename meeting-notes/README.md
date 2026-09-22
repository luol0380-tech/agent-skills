# Meeting Notes

## 这个 Skill 做什么

把录音转写、聊天记录或零散笔记整理成可信的会议纪要，保留讨论、决定、风险、待确认事项和行动项之间的差别。

## 使用者需要配置什么

- `config/current_template.txt`：默认纪要模板。
- `private/personal-style.md`：标题习惯、语言风格、敏感内容处理方式。

个人配置只保存在本地。运行根目录的 `python3 scripts/bootstrap_local.py --skill meeting-notes` 可生成占位文件。

## 目录结构

```text
meeting-notes/
├── SKILL.md                         # 通用整理流程
├── README.md                        # 使用说明
├── config/current_template.txt      # 当前默认模板
├── templates/                       # brief、detailed、for-boss
│   └── archive/                     # 停用模板，只归档不删除
├── scripts/select_template.py       # 模板选择与校验
└── private/                         # 本地风格与敏感配置
```

指定模板：

```bash
python3 scripts/select_template.py --template detailed
```
