# WeChat renderer JSON schema

Run:

```bash
python3 scripts/render_wechat.py article.json output.html
```

Top-level fields:

Optional `writing_template`, `cover_template`, `layout_template`: `ai-practice` or `family-growth`. Renderer uses `layout_template`, defaulting to `ai-practice`. Set block `role` to `reflection` for black reflection text in family layout. Supply series/footer only when approved for the writing template; never infer AI numbering or closing from the layout selection.

```json
{
  "title": "WeChat title field",
  "series": "Optional explicitly approved series label",
  "cover": "/absolute/path/cover.png",
  "sections": [],
  "footer": ["paragraph one", "paragraph two"]
}
```

Each section has `heading` and `blocks`. Use an empty heading for the introduction.

Supported blocks:

```json
{"type":"p","text":"Normal paragraph"}
{"type":"strong","text":"Highlighted conclusion"}
{"type":"quote","text":"Quoted input or short statement"}
{"type":"prompt","text":"Copyable prompt"}
{"type":"subhead","text":"01｜Short subheading"}
{"type":"numbered","items":["First","Second"]}
{"type":"image","path":"/absolute/path/a.png","caption":"Caption"}
{"type":"image_pair","paths":["/absolute/path/a.png","/absolute/path/b.png"],"caption":"Relationship caption"}
{"type":"final","text":"Two-line closing belief"}
```

All image paths must exist. The renderer embeds them as data URIs. Open the generated HTML, click `复制正文排版`, and paste into the WeChat editor. Confirm every image loaded before publication.
