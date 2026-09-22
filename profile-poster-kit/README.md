# Profile Poster Kit

## 这个 Skill 做什么

从人物照片和已核实资料生成一组相互一致的人物介绍海报与角色设定图，重点保证同一张脸、同一套服装、成人比例、准确文字和跨图一致性。

## 使用者需要配置什么

- `config/current_template.txt`：默认输出模板。
- `private/brand-style.md`：私有品牌名、版式、色彩、字体与禁用元素。
- `private/subject-profile.md`：人物姓名、职位、履历与授权范围。
- `private/assets/`：人物照片、背景、标识和风格参考图。

这些文件只留本地。运行根目录的 `python3 scripts/bootstrap_local.py --skill profile-poster-kit` 可生成配置占位文件。

## 目录结构

```text
profile-poster-kit/
├── SKILL.md                         # 通用制作流程
├── README.md                        # 使用说明
├── config/current_template.txt      # 当前默认模板
├── templates/                       # 海报、角色卡、成套模板
│   └── archive/                     # 停用模板
├── scripts/select_template.py       # 模板选择与校验
└── private/                         # 人物、品牌与图片素材
```
