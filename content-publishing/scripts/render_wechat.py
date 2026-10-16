#!/usr/bin/env python3
import base64
import html
import json
import mimetypes
import sys
from pathlib import Path


def data_uri(path):
    p = Path(path)
    if not p.is_file():
        raise FileNotFoundError(f"Image not found: {p}")
    mime = mimetypes.guess_type(p.name)[0] or "image/png"
    return f"data:{mime};base64," + base64.b64encode(p.read_bytes()).decode("ascii")


def esc(value):
    return html.escape(str(value), quote=True)


def block_html(block, template="ai-practice"):
    kind = block.get("type", "p")
    text = esc(block.get("text", ""))
    if template == "family-growth" and kind in ("p", "strong", "quote", "prompt", "final", "subhead"):
        color = "#222222" if block.get("role") == "reflection" or kind in ("quote", "final", "strong") else "#307dca"
        return f'<p style="margin:0 0 26px;line-height:2;font-size:17px;color:{color};letter-spacing:.5px;white-space:pre-line;">{text}</p>'
    pstyle = "margin:0 0 18px;line-height:1.95;font-size:16px;color:#3f4652;letter-spacing:.3px;text-align:justify;"
    if kind == "p":
        return f'<p style="{pstyle}">{text}</p>'
    if kind == "strong":
        return f'<section style="margin:24px 0;padding:18px 20px;background:#f3f6f8;border-radius:8px;"><p style="margin:0;line-height:1.85;font-size:17px;font-weight:700;color:#3f5875;">{text}</p></section>'
    if kind == "quote":
        return f'<section style="margin:22px 0;padding:18px 20px;background:#fbf8f1;border-radius:8px;"><p style="margin:0;white-space:pre-line;line-height:1.9;font-size:16px;color:#605744;">{text}</p></section>'
    if kind == "prompt":
        return f'<section style="margin:14px 0 24px;padding:18px 20px;background:#f5f7f8;border-left:3px solid #b9c9d9;border-radius:6px;"><p style="margin:0;white-space:pre-line;line-height:1.9;font-size:15px;color:#4d5968;">{text}</p></section>'
    if kind == "subhead":
        return f'<p style="margin:30px 0 12px;font-size:17px;line-height:1.6;font-weight:700;color:#46627f;">{text}</p>'
    if kind == "numbered":
        items = "".join(f'<li style="margin:5px 0;line-height:1.8;">{esc(x)}</li>' for x in block.get("items", []))
        return f'<ol style="margin:4px 0 22px;padding-left:26px;font-size:16px;color:#3f4652;">{items}</ol>'
    if kind == "image":
        src = data_uri(block["path"])
        caption = esc(block.get("caption", ""))
        return f'<section style="margin:24px 0 30px;"><img src="{src}" style="display:block;width:100%;height:auto;border-radius:6px;"/><p style="margin:10px 0 0;text-align:center;font-size:13px;line-height:1.6;color:#8b94a4;">▲ {caption}</p></section>'
    if kind == "image_pair":
        paths = block.get("paths", [])
        if len(paths) != 2:
            raise ValueError("image_pair requires exactly two paths")
        src1, src2 = map(data_uri, paths)
        caption = esc(block.get("caption", ""))
        return f'<section style="margin:24px 0 30px;"><table style="width:100%;border-collapse:collapse;table-layout:fixed;"><tr><td style="width:50%;padding:4px;vertical-align:middle;"><img src="{src1}" style="display:block;width:100%;height:auto;border-radius:6px;"/></td><td style="width:50%;padding:4px;vertical-align:middle;"><img src="{src2}" style="display:block;width:100%;height:auto;border-radius:6px;"/></td></tr></table><p style="margin:10px 0 0;text-align:center;font-size:13px;line-height:1.6;color:#8b94a4;">▲ {caption}</p></section>'
    if kind == "final":
        return f'<section style="margin:28px 0;padding:22px 18px;background:#eaf0f4;border-radius:10px;"><p style="margin:0;text-align:center;white-space:pre-line;line-height:2;font-size:18px;font-weight:700;color:#3d5875;">{text}</p></section>'
    raise ValueError(f"Unsupported block type: {kind}")


def render(payload):
    title = payload["title"]
    template = payload.get("layout_template", payload.get("template", "ai-practice"))
    if template not in ("ai-practice", "family-growth"):
        raise ValueError("Unknown layout template")
    parts = []
    if payload.get("cover"):
        parts.append(f'<img src="{data_uri(payload["cover"])}" style="display:block;width:100%;height:auto;margin:0 0 26px;border-radius:6px;"/>')
    if payload.get("series"):
        parts.append(f'<p style="margin:0 0 30px;padding:11px 16px;text-align:center;background:#f6f5f2;border-radius:6px;font-size:14px;line-height:1.7;color:#7b7b77;">{esc(payload["series"])}</p>')
    for section in payload.get("sections", []):
        heading = section.get("heading", "")
        if heading and template == "family-growth":
            parts.append(f'<h2 style="margin:48px 0 30px;text-align:center;font-size:20px;line-height:1.8;font-weight:500;color:#307dca;">{esc(heading)}</h2>')
        elif heading:
            parts.append(f'<h2 style="margin:44px 0 22px;padding:0 0 12px;border-bottom:1px solid #e8e5de;font-size:21px;line-height:1.55;font-weight:700;color:#3e5268;">{esc(heading)}</h2>')
        parts.extend(block_html(block, template) for block in section.get("blocks", []))
    footer = payload.get("footer", [])
    if footer:
        footer_html = "".join(f'<p style="margin:{"0 0 10px" if i < len(footer)-1 else "0"};font-size:14px;line-height:1.8;color:{"#59616a" if i == 0 else "#7b828a"};">{esc(value)}</p>' for i, value in enumerate(footer))
        parts.append(f'<section style="margin:42px 0 0;padding:22px 20px;border-top:1px solid #e8e5de;background:#f8f7f4;">{footer_html}</section>')
    article = "".join(parts)
    if template == "family-growth":
        article = article.replace('border-top:1px solid #e8e5de;background:#f8f7f4;', '')
    page_bg = "#fff" if template == "family-growth" else "#f4f3f0"
    return f'''<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{esc(title)}</title></head>
<body style="margin:0;background:{page_bg};font-family:-apple-system,BlinkMacSystemFont,'PingFang SC','Microsoft YaHei',sans-serif;">
<div style="position:sticky;top:0;z-index:10;padding:12px;background:rgba(255,255,255,.96);border-bottom:1px solid #e8e5de;color:#59616a;"><div style="max-width:677px;margin:auto;display:flex;gap:10px;align-items:center;justify-content:space-between;"><span style="font-size:13px;">公众号标题：{esc(title)}</span><button onclick="copyArticle()" style="flex:none;border:0;border-radius:18px;padding:9px 16px;background:#edd37c;color:#4b4f53;font-weight:700;cursor:pointer;">复制正文排版</button></div></div>
<main id="article" style="box-sizing:border-box;max-width:677px;margin:20px auto;padding:26px 28px 42px;background:#fff;">{article}</main>
<script>async function copyArticle(){{const el=document.getElementById('article');const h=el.innerHTML;const t=el.innerText;try{{await navigator.clipboard.write([new ClipboardItem({{'text/html':new Blob([h],{{type:'text/html'}}),'text/plain':new Blob([t],{{type:'text/plain'}})}})]);alert('已复制排版正文，请粘贴到公众号编辑器');}}catch(e){{const r=document.createRange();r.selectNodeContents(el);const s=window.getSelection();s.removeAllRanges();s.addRange(r);document.execCommand('copy');s.removeAllRanges();alert('已复制正文，请粘贴到公众号编辑器');}}}}</script></body></html>'''


def main():
    if len(sys.argv) != 3:
        raise SystemExit("Usage: render_wechat.py INPUT.json OUTPUT.html")
    source, target = map(Path, sys.argv[1:])
    payload = json.loads(source.read_text(encoding="utf-8"))
    target.write_text(render(payload), encoding="utf-8")
    print(target.resolve())


if __name__ == "__main__":
    main()
