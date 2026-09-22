# Interview Training

## 这个 Skill 做什么

用于结构化面试训练：模拟问答、术语提取、答案压缩、追问、反馈分类和旧题复习。它不绑定具体 Agent 或编程工具。

## 使用者需要配置什么

- `config/current_template.txt`：默认训练模板，一行一个模板名。
- `private/candidate-profile.md`：目标岗位、真实经历与可公开口径。
- `private/interview-history.md`：历史问题、反馈与待复习题。
- `private/personal-style.md`：希望保留的表达习惯和反馈偏好。

后三项只保存在本地。运行根目录的 `python3 scripts/bootstrap_local.py --skill interview-training` 可从示例生成占位文件。

## 目录结构

```text
interview-training/
├── SKILL.md                         # 通用训练流程
├── README.md                        # 使用说明
├── config/current_template.txt      # 当前默认模板
├── templates/                       # 可切换训练模板
│   └── archive/                     # 停用模板，只归档不删除
├── scripts/select_template.py       # 模板选择与校验
└── private/                         # 本地个人资料与偏好
```

查看当前模板：

```bash
python3 scripts/select_template.py --path-only
```

临时切换模板不会修改默认配置：

```bash
python3 scripts/select_template.py --template mock-interview
```
