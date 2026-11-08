#!/usr/bin/env python3
"""Render a hackathon architecture diagram (animated SVG) from a JSON spec. Stdlib only.

Usage: archgraph.py spec.json -o architecture.svg

Spec:
{
  "title": "...", "subtitle": "...",
  "lanes":  [{"id": "device", "label": "On-device", "color": "#22d3ee"}],   # columns, left -> right
  "nodes":  [{"id": "mic", "lane": "device", "label": "Mic stream", "sub": "16 kHz PCM",
              "status": "live|mock|roadmap", "hot": true}],                  # hot = the hard part (one!)
  "edges":  [{"from": "mic", "to": "asr", "label": "audio", "step": 1}],     # step => demo path (animated)
  "metrics":[{"value": "38 ms", "label": "p50 latency", "measured": true}]
}
"""
import argparse
import html
import json
import sys

PALETTE = ["#22d3ee", "#a78bfa", "#f472b6", "#34d399", "#fbbf24", "#60a5fa"]
NODE_W, NODE_H = 214, 68
LANE_W, LANE_GAP = 254, 44
PAD_X, TOP, NODE_GAP, LANE_HEAD = 48, 132, 50, 66
DEMO = "#22d3ee"
FONT = "Inter, ui-sans-serif, system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif"


def esc(s):
    return html.escape(str(s), quote=True)


def text_w(s, size):
    return len(str(s)) * size * 0.56


def validate(spec):
    lane_ids = {l["id"] for l in spec.get("lanes", [])}
    node_ids = set()
    errs = []
    for n in spec.get("nodes", []):
        if n.get("lane") not in lane_ids:
            errs.append(f"node '{n.get('id')}' has unknown lane '{n.get('lane')}'")
        if n.get("status", "live") not in ("live", "mock", "roadmap"):
            errs.append(f"node '{n['id']}' has bad status '{n['status']}'")
        node_ids.add(n["id"])
    for e in spec.get("edges", []):
        for k in ("from", "to"):
            if e.get(k) not in node_ids:
                errs.append(f"edge {e.get('from')}->{e.get('to')}: unknown node '{e.get(k)}'")
    hot = [n["id"] for n in spec.get("nodes", []) if n.get("hot")]
    if len(hot) > 1:
        errs.append(f"only one 'hot' node allowed (the hard part), got {hot}")
    for m in spec.get("metrics", []):
        if not m.get("measured"):
            errs.append(f"metric '{m.get('label')}' is not marked measured: measure it or remove it")
    if errs:
        sys.exit("spec errors:\n  " + "\n  ".join(errs))


def layout(spec):
    lanes = spec["lanes"]
    by_lane = {l["id"]: [] for l in lanes}
    for n in spec["nodes"]:
        by_lane[n["lane"]].append(n)
    max_n = max([len(v) for v in by_lane.values()] + [1])
    stack_max = max_n * NODE_H + (max_n - 1) * NODE_GAP
    lane_h = LANE_HEAD + stack_max + 48
    pos, lane_idx = {}, {}
    for i, l in enumerate(lanes):
        lane_idx[l["id"]] = i
        x = PAD_X + i * (LANE_W + LANE_GAP)
        l["_x"], l["_color"] = x, l.get("color", PALETTE[i % len(PALETTE)])
        nodes = by_lane[l["id"]]
        stack = len(nodes) * NODE_H + max(len(nodes) - 1, 0) * NODE_GAP
        y0 = TOP + LANE_HEAD + 20 + (stack_max - stack) / 2
        for j, n in enumerate(nodes):
            pos[n["id"]] = (x + (LANE_W - NODE_W) / 2, y0 + j * (NODE_H + NODE_GAP), l)
    width = PAD_X * 2 + len(lanes) * LANE_W + (len(lanes) - 1) * LANE_GAP
    return pos, lane_idx, width, lane_h


def edge_geom(a, b, lane_idx, order):
    """Returns (path d, label anchor, kind). kind: 'curve' | 'bracket'."""
    ax, ay, al = a
    bx, by, bl = b
    ia, ib = lane_idx[al["id"]], lane_idx[bl["id"]]
    if ia == ib and abs(order[0] - order[1]) > 1:  # same lane, not adjacent: bracket down the left gutter
        gx = ax - 12
        y1, y2 = ay + NODE_H / 2 + 10, by + NODE_H / 2 - 10 if by < ay else by + NODE_H / 2 + 10
        d = f"M{ax:.1f},{y1:.1f} H{gx:.1f} V{y2:.1f} H{bx:.1f}"
        return d, (gx, (y1 + y2) / 2), "bracket"
    if ib > ia:  # forward
        p0, p3 = (ax + NODE_W, ay + NODE_H / 2), (bx, by + NODE_H / 2)
        dx = (p3[0] - p0[0]) * 0.5
        p1, p2 = (p0[0] + dx, p0[1]), (p3[0] - dx, p3[1])
    elif ib < ia:  # backward: swing below
        p0, p3 = (ax + NODE_W / 2, ay + NODE_H), (bx + NODE_W / 2, by + NODE_H)
        p1, p2 = (p0[0], p0[1] + 70), (p3[0], p3[1] + 70)
    else:  # same lane, adjacent
        if by > ay:
            p0, p3 = (ax + NODE_W / 2, ay + NODE_H), (bx + NODE_W / 2, by)
        else:
            p0, p3 = (ax + NODE_W / 2, ay), (bx + NODE_W / 2, by + NODE_H)
        p1, p2 = p0, p3
    mid = tuple((p0[k] + 3 * p1[k] + 3 * p2[k] + p3[k]) / 8 for k in (0, 1))
    d = f"M{p0[0]:.1f},{p0[1]:.1f} C{p1[0]:.1f},{p1[1]:.1f} {p2[0]:.1f},{p2[1]:.1f} {p3[0]:.1f},{p3[1]:.1f}"
    return d, mid, "curve"


def lint(spec, lane_idx):
    """Warn about edges that will cross other nodes; the fix is usually reordering lanes or nodes."""
    lane_of = {n["id"]: n["lane"] for n in spec["nodes"]}
    for e in spec.get("edges", []):
        ia, ib = lane_idx[lane_of[e["from"]]], lane_idx[lane_of[e["to"]]]
        if ib < ia:
            print(f"warning: {e['from']}->{e['to']} flows right-to-left; reorder lanes or flip the edge", file=sys.stderr)
        elif ib - ia > 1:
            print(f"warning: {e['from']}->{e['to']} skips a lane and may cross nodes; consider moving a node", file=sys.stderr)


def pill(x, y, txt, color, filled=False):
    w = text_w(txt, 10) + 16
    fill = color if filled else "#0b1226"
    tc = "#0b1020" if filled else color
    return (f'<rect x="{x - w:.1f}" y="{y}" width="{w:.1f}" height="18" rx="9" fill="{fill}" '
            f'stroke="{color}" stroke-width="1"/>'
            f'<text x="{x - w / 2:.1f}" y="{y + 12.5}" text-anchor="middle" font-size="10" '
            f'font-weight="700" letter-spacing="0.08em" fill="{tc}">{esc(txt)}</text>')


def render(spec):
    validate(spec)
    pos, lane_idx, W, lane_h = layout(spec)
    lint(spec, lane_idx)
    order, seen = {}, {}
    for n in spec["nodes"]:
        order[n["id"]] = seen.get(n["lane"], 0)
        seen[n["lane"]] = order[n["id"]] + 1
    metrics = spec.get("metrics", [])
    H = TOP + lane_h + (130 if metrics else 40)
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
           f'font-family="{FONT}">']
    out.append(f"""<defs>
<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#070b19"/><stop offset="1" stop-color="#121a3a"/></linearGradient>
<radialGradient id="halo" cx="0.75" cy="0" r="0.9"><stop offset="0" stop-color="#7c3aed" stop-opacity="0.22"/><stop offset="1" stop-color="#7c3aed" stop-opacity="0"/></radialGradient>
<pattern id="dots" width="22" height="22" patternUnits="userSpaceOnUse"><circle cx="1" cy="1" r="1" fill="#94a3b8" fill-opacity="0.12"/></pattern>
<filter id="glow" x="-40%" y="-40%" width="180%" height="180%"><feGaussianBlur stdDeviation="9"/></filter>
<marker id="arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#64748b"/></marker>
<marker id="arrDemo" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="{DEMO}"/></marker>
<style>.flow{{stroke-dasharray:7 9;animation:flow 1.1s linear infinite}}@keyframes flow{{to{{stroke-dashoffset:-32}}}}
.pulse{{animation:pulse 2.4s ease-in-out infinite}}@keyframes pulse{{50%{{opacity:.45}}}}</style>
</defs>
<rect width="{W}" height="{H}" fill="url(#bg)"/><rect width="{W}" height="{H}" fill="url(#halo)"/><rect width="{W}" height="{H}" fill="url(#dots)"/>""")

    # header
    out.append(f'<text x="{PAD_X}" y="62" font-size="30" font-weight="800" fill="#f8fafc">{esc(spec.get("title", ""))}</text>')
    if spec.get("subtitle"):
        out.append(f'<text x="{PAD_X}" y="92" font-size="15" fill="#94a3b8">{esc(spec["subtitle"])}</text>')
    lx = W - PAD_X
    legend = [("demo path", None), ("live", "solid"), ("mock", "mock"), ("next", "dash")]
    for lbl, kind in reversed(legend):
        tw = text_w(lbl, 12)
        lx -= tw
        out.append(f'<text x="{lx:.1f}" y="66" font-size="12" fill="#cbd5e1">{lbl}</text>')
        lx -= 30
        if kind is None:
            out.append(f'<path d="M{lx},62 h24" stroke="{DEMO}" stroke-width="2.5" class="flow"/>')
        else:
            dash = ' stroke-dasharray="4 3"' if kind == "dash" else ""
            col = "#fbbf24" if kind == "mock" else "#cbd5e1"
            out.append(f'<rect x="{lx}" y="55" width="24" height="14" rx="4" fill="none" stroke="{col}"{dash}/>')
        lx -= 18

    # lanes
    for l in spec["lanes"]:
        x, c = l["_x"], l["_color"]
        out.append(f'<rect x="{x}" y="{TOP}" width="{LANE_W}" height="{lane_h}" rx="20" fill="{c}" fill-opacity="0.045" '
                   f'stroke="{c}" stroke-opacity="0.28"/>')
        out.append(f'<text x="{x + 20}" y="{TOP + 32}" font-size="12" font-weight="800" letter-spacing="0.16em" '
                   f'fill="{c}">{esc(l["label"].upper())}</text>')
        if l.get("sub"):
            out.append(f'<text x="{x + 20}" y="{TOP + 52}" font-size="11.5" '
                       f'fill="#7c8aa5">{esc(l["sub"])}</text>')

    # edges (under nodes); demo edges drawn last so they sit on top
    edges = sorted(spec.get("edges", []), key=lambda e: e.get("step") is not None)
    labels = []
    for e in edges:
        d, (mx, my), kind = edge_geom(pos[e["from"]], pos[e["to"]], lane_idx, (order[e["from"]], order[e["to"]]))
        if e.get("step") is not None:
            out.append(f'<path d="{d}" fill="none" stroke="{DEMO}" stroke-opacity="0.25" stroke-width="7"/>')
            out.append(f'<path d="{d}" fill="none" stroke="{DEMO}" stroke-width="2.5" class="flow" marker-end="url(#arrDemo)"/>')
        else:
            out.append(f'<path d="{d}" fill="none" stroke="#64748b" stroke-opacity="0.75" stroke-width="1.6" marker-end="url(#arr)"/>')
        labels.append((mx, my, e, kind))

    # nodes
    for n in spec["nodes"]:
        x, y, l = pos[n["id"]]
        c = l["_color"]
        status = n.get("status", "live")
        if n.get("hot"):
            out.append(f'<rect x="{x - 4}" y="{y - 4}" width="{NODE_W + 8}" height="{NODE_H + 8}" rx="18" fill="{c}" '
                       f'opacity="0.55" filter="url(#glow)" class="pulse"/>')
        dash = ' stroke-dasharray="6 4"' if status == "roadmap" else ""
        stroke = "#fbbf24" if status == "mock" else c
        op = ' opacity="0.55"' if status == "roadmap" else ""
        sw = 2.2 if n.get("hot") else 1.4
        out.append(f'<g{op}><rect x="{x}" y="{y}" width="{NODE_W}" height="{NODE_H}" rx="14" fill="#0b1226" '
                   f'fill-opacity="0.94" stroke="{stroke}" stroke-width="{sw}"{dash}/>')
        out.append(f'<rect x="{x}" y="{y + 14}" width="3.5" height="{NODE_H - 28}" rx="1.75" fill="{c}"/>')
        out.append(f'<text x="{x + 18}" y="{y + 30}" font-size="15" font-weight="700" fill="#f1f5f9">{esc(n["label"])}</text>')
        if n.get("sub"):
            out.append(f'<text x="{x + 18}" y="{y + 50}" font-size="12" fill="#94a3b8">{esc(n["sub"])}</text>')
        px = x + NODE_W - 10
        if n.get("hot"):
            out.append(pill(px, y - 9, "CORE", c, filled=True))
        elif status == "mock":
            out.append(pill(px, y - 9, "MOCK", "#fbbf24"))
        elif status == "roadmap":
            out.append(pill(px, y - 9, "NEXT", "#cbd5e1"))
        out.append("</g>")

    # edge labels + step badges on top of everything
    for mx, my, e, kind in labels:
        step, lbl = e.get("step"), e.get("label")
        if kind == "bracket":  # vertical label along the gutter
            if lbl:
                tw = text_w(lbl, 11) + 14
                out.append(f'<g transform="rotate(-90 {mx:.1f} {my:.1f})"><rect x="{mx - tw / 2:.1f}" y="{my - 10:.1f}" '
                           f'width="{tw:.1f}" height="20" rx="10" fill="#0b1020" stroke="#334155"/>'
                           f'<text x="{mx:.1f}" y="{my + 4:.1f}" text-anchor="middle" font-size="11" fill="#cbd5e1">{esc(lbl)}</text></g>')
            continue
        if lbl:
            tw = text_w(lbl, 11) + 14
            off = 13 if step is not None else 0
            lx0 = mx - tw / 2 + off
            out.append(f'<rect x="{lx0:.1f}" y="{my - 10:.1f}" width="{tw:.1f}" height="20" rx="10" fill="#0b1020" '
                       f'fill-opacity="0.92" stroke="#334155"/>')
            out.append(f'<text x="{lx0 + tw / 2:.1f}" y="{my + 4:.1f}" text-anchor="middle" font-size="11" '
                       f'fill="#cbd5e1">{esc(lbl)}</text>')
        if step is not None:
            bx = mx - (text_w(lbl, 11) + 14) / 2 if lbl else mx
            out.append(f'<circle cx="{bx:.1f}" cy="{my:.1f}" r="11" fill="{DEMO}"/>'
                       f'<text x="{bx:.1f}" y="{my + 4:.1f}" text-anchor="middle" font-size="11" font-weight="800" '
                       f'fill="#0b1020">{esc(step)}</text>')

    # metrics strip
    if metrics:
        my0 = TOP + lane_h + 28
        cw = (W - 2 * PAD_X - (len(metrics) - 1) * 16) / len(metrics)
        for i, m in enumerate(metrics):
            mx = PAD_X + i * (cw + 16)
            c = PALETTE[i % len(PALETTE)]
            out.append(f'<rect x="{mx:.1f}" y="{my0}" width="{cw:.1f}" height="76" rx="14" fill="#0b1226" stroke="{c}" stroke-opacity="0.35"/>')
            out.append(f'<text x="{mx + 20:.1f}" y="{my0 + 40}" font-size="26" font-weight="800" fill="{c}">{esc(m["value"])}</text>')
            out.append(f'<text x="{mx + 20:.1f}" y="{my0 + 62}" font-size="12" fill="#94a3b8">{esc(m["label"])}</text>')

    out.append("</svg>")
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("spec")
    ap.add_argument("-o", "--out", default="architecture.svg")
    args = ap.parse_args()
    with open(args.spec) as f:
        spec = json.load(f)
    svg = render(spec)
    with open(args.out, "w") as f:
        f.write(svg)
    print(f"wrote {args.out}")


if __name__ == "__main__":
    main()
