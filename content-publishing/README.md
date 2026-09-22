# Content Publishing

## 这个 Skill 做什么

把真实素材整理成长文、短内容或发布包，覆盖选题、起草、修改、内容复用、发布前检查和确认门槛，同时保护事实、个人文风与隐私。

## 使用者需要配置什么

- `config/current_template.txt`：默认内容模板。
- `private/brand-profile.md`：账号定位、受众、固定栏目、允许使用的品牌信息。
- `private/personal-style.md`：个人语言习惯、禁用表达与修改偏好。
- `private/assets/`：头像、品牌图、真实截图等不公开素材。

运行根目录的 `python3 scripts/bootstrap_local.py --skill content-publishing` 可生成本地配置占位文件。

## 目录结构

```text
content-publishing/
├── SKILL.md                         # 通用编辑流程
├── README.md                        # 使用说明
├── config/current_template.txt      # 当前默认模板
├── templates/                       # 长文、短内容、发布包模板
│   └── archive/                     # 停用模板
├── scripts/select_template.py       # 模板选择与校验
└── private/                         # 本地品牌、文风与素材
```
