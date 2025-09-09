from pathlib import Path
def write_report(changed, rows, out_html):
    Path(out_html).parent.mkdir(parents=True, exist_ok=True)
    trs='\n'.join([f"<tr><td>{i}</td><td>{tid}</td><td>{score:.2f}</td><td>{reason}</td></tr>"
                    for i,(tid,score,reason) in enumerate(rows,1)])
    html = (
        "<!doctype html><html><head><meta charset='utf-8'>"
        "<style>"
        "body{font-family:Arial,Helvetica,sans-serif;margin:24px}"
        "table{border-collapse:collapse;width:100%;table-layout:fixed}"
        "td,th{border:1px solid #ddd;padding:8px;vertical-align:top;word-break:break-word}"
        "tr:nth-child(even){background:#fafafa}"
        "</style></head><body>"
        "<h1>CodeMapRT — Prioritized Test Execution Report</h1>"
        + "<p><b>Changed files:</b> " + ", ".join(changed) + "</p>"
        + "<table>"
        + "<colgroup><col style='width:6%'><col style='width:54%'><col style='width:10%'><col style='width:30%'></colgroup>"
        + "<tr><th>#</th><th>Test ID</th><th>Score</th><th>Reason</th></tr>"
        + trs +
        "</table></body></html>"
    )
    Path(out_html).write_text(html, encoding='utf-8')
