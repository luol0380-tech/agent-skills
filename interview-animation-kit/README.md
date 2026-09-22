# Interview Animation Kit

## 这个 Skill 做什么

把访谈或真实故事中的一个小片段转成可制作的短动画包，包括分秒脚本、角色锁定、独立分镜、素材编号、动作说明和交接清单。

## 使用者需要配置什么

- `config/current_template.txt`：默认制作模板。
- `private/project-context.md`：真实故事、人物关系、场景与授权边界。
- `private/personal-style.md`：画面风格、对白密度和表达偏好。
- `private/assets/`：人物照片、场景照片、品牌道具与已批准角色图。

这些内容只留本地。运行根目录的 `python3 scripts/bootstrap_local.py --skill interview-animation-kit` 可生成配置占位文件。

## 目录结构

```text
interview-animation-kit/
├── SKILL.md                         # 通用制作流程
├── README.md                        # 使用说明
├── config/current_template.txt      # 当前默认模板
├── templates/                       # 短插片、交接、角色连续性模板
│   └── archive/                     # 停用模板
├── scripts/select_template.py       # 模板选择与校验
└── private/                         # 故事、风格与参考素材
```
