# Privacy boundary

## 已排除的内容类型

公开仓库不得包含：

- 真实姓名、昵称、账号名、邮箱、电话号码和联系方式；
- 任职公司、个人履历、未公开项目、面试记录和真实绩效数据；
- 个人固定文风、账号定位、固定口号和历史写作样本；
- 人物照片、个人头像、私有品牌素材和未经授权的组织素材；
- 密钥、令牌、Cookie、登录信息、绝对用户目录和本机环境变量值。

## 私有文件规则

将个人信息放在各 Skill 的 `private/` 目录中。可以从 `*.example.md` 复制生成实际配置，也可以运行：

```bash
python3 scripts/bootstrap_local.py
```

实际配置与 `private/assets/` 会被 Git 忽略。公开的 `README.md` 和 `*.example.md` 只能包含占位符和虚构示例。

## 自定义敏感词扫描

在仓库根目录创建 `.privacy-denylist`，每行填写一个不应公开的名称、品牌、账号或项目词。该文件不会被提交。运行：

```bash
python3 scripts/audit_repository.py
```

扫描器只报告文件位置，不回显敏感词正文。
