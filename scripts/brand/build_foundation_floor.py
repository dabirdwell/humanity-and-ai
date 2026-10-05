#!/usr/bin/env python3
"""Foundation's floor, as a small mark for the website.

Brand architecture (approved Sep 27 2026): the house is the sky, Foundation is
the ground. The ground is Penrose tiles fitting edge to edge, sage with gold;
the tiles belong to Foundation only. Source:
/Users/david/Documents/Fawkes/Media and Outreach/Branding/HAI_Mark_Brief_2026-09-26.md, section 13.

The geometry is the show's own floor: a straight port of buildRhombi() in
/Users/david/Developer/show-graphics/galaxy-intro/src/stage/penrose.ts (P3 rhombs by
golden-ratio deflation, 7 generations, radius 150), cut to the patch at its center,
where the show's star lands and turns into the gold tile. So the website and the
intro draw the same floor. As in the intro, the thin rhombs are the lighter sage,
the wide rhombs the darker one, and the tile nearest the center is gold.

The patch is every tile within 3.6 tile edges of the center, which keeps the floor's
five-fold symmetry (a ten-pointed rosette). Only the gold tile breaks it: the newest
tile, just set.

Writes layouts/partials/foundation-floor.html. Each tile carries --d, its settle
delay: the floor is laid from the middle out around one empty place, and the gold
tile sets into that place last, as the star does in the intro. static/css/home.css
runs this once, when the section scrolls into view.

Usage: python3 scripts/brand/build_foundation_floor.py [--preview out.svg]
"""
import math, os, sys

PHI = (1 + 5 ** 0.5) / 2
GENERATIONS, RADIUS = 7, 150          # the intro's floor: buildRhombi(7, 150)
EDGE = RADIUS / PHI ** GENERATIONS    # one tile edge, about 5.17 units
REACH = 3.6 * EDGE                    # every tile whose center is this close is laid
SHRINK = 0.90                         # tiles drawn slightly small, so the seams show
SETTLE = 1.6                          # seconds from the first tile to the last plain tile
GOLD_AFTER = 0.35                     # the gold tile sets this long after the last one


def js_round(v):
    """Math.round, for matching the TypeScript edge keys exactly."""
    return math.floor(v + 0.5)


def rand(seed):
    x = math.sin(seed * 127.1 + 311.7) * 43758.5453
    return x - math.floor(x)


def mix(p, q, t):
    return (p[0] + (q[0] - p[0]) * t, p[1] + (q[1] - p[1]) * t)


def seed_wheel(radius):
    tris = []
    for i in range(10):
        a1 = (2 * i - 1) * math.pi / 10
        a2 = (2 * i + 1) * math.pi / 10
        b = (math.cos(a1) * radius, math.sin(a1) * radius)
        c = (math.cos(a2) * radius, math.sin(a2) * radius)
        if i % 2 == 0:
            b, c = c, b
        tris.append((True, (0.0, 0.0), b, c))
    return tris


def subdivide(tris):
    out = []
    for red, a, b, c in tris:
        if red:
            p = mix(a, b, 1 / PHI)
            out.append((True, c, p, b))
            out.append((False, p, c, a))
        else:
            q = mix(b, a, 1 / PHI)
            r = mix(b, c, 1 / PHI)
            out.append((False, r, c, a))
            out.append((False, q, r, b))
            out.append((True, r, q, a))
    return out


def build_rhombi(generations, radius):
    t = seed_wheel(radius)
    for _ in range(generations):
        t = subdivide(t)
    by_edge = {}
    order = []
    key = lambda p: f"{js_round(p[0] * 10)},{js_round(p[1] * 10)}"
    for tri in t:
        k = "|".join(sorted([key(tri[2]), key(tri[3])]))
        if k not in by_edge:
            by_edge[k] = []
            order.append(k)
        by_edge[k].append(tri)
    out = []
    for i, k in enumerate(order, start=1):
        twins = by_edge[k]
        if len(twins) == 2:
            pts = [twins[0][1], twins[0][2], twins[1][1], twins[0][3]]
        else:
            pts = [twins[0][1], twins[0][2], twins[0][3]]
        cx = sum(p[0] for p in pts) / len(pts)
        cy = sum(p[1] for p in pts) / len(pts)
        out.append({"pts": pts, "red": twins[0][0], "cx": cx, "cy": cy,
                    "dist": math.hypot(cx, cy), "seed": rand(i * 13 + 5)})
    return out


def laid(r):
    return r["dist"] <= REACH


def main():
    rh = [r for r in build_rhombi(GENERATIONS, RADIUS) if len(r["pts"]) == 4]
    land = min(rh, key=lambda r: r["dist"])
    tiles = [r for r in rh if laid(r)]
    far = max(r["dist"] for r in tiles)
    pad = 0.6 * EDGE
    lim = max(max(abs(p[0]), abs(p[1])) for r in tiles for p in r["pts"]) + pad
    f = lambda v: f"{v:.2f}"

    paths = []
    for r in sorted(tiles, key=lambda r: r["dist"]):
        pts = [(r["cx"] + (p[0] - r["cx"]) * SHRINK, r["cy"] + (p[1] - r["cy"]) * SHRINK) for p in r["pts"]]
        d = "M" + " L".join(f"{f(x)} {f(y)}" for x, y in pts) + " Z"
        if r is land:
            cls, delay = "ff-gold", SETTLE + GOLD_AFTER
        else:
            cls = "ff-thin" if r["red"] else "ff-wide"
            delay = SETTLE * (r["dist"] / far) ** 0.9
        paths.append(f'<path class="{cls}" style="--d:{delay:.2f}s" d="{d}"/>')

    w = 2 * lim
    svg = (
        f'<svg class="ff" viewBox="{f(-lim)} {f(-lim)} {f(w)} {f(w)}" role="img" '
        f'aria-labelledby="ff-title" focusable="false">'
        f'<title id="ff-title">Foundation: a floor of tiles that fit edge to edge, '
        f'with one gold tile just set</title>'
        + "".join(paths) + "</svg>"
    )
    head = ("{{- /* Generated by scripts/brand/build_foundation_floor.py. Do not edit by hand: "
            "change the script and run it again. */ -}}\n")
    root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    if "--preview" in sys.argv:
        out = sys.argv[sys.argv.index("--preview") + 1]
        style = ("<style>.ff-wide{fill:#3D5E54}.ff-thin{fill:#5A8A7A}.ff-gold{fill:#C8964E}</style>")
        with open(out, "w") as fh:
            fh.write(svg.replace('focusable="false">', 'focusable="false" xmlns="http://www.w3.org/2000/svg">' + style, 1))
        print("preview", out)
    dest = os.path.join(root, "layouts", "partials", "foundation-floor.html")
    with open(dest, "w") as fh:
        fh.write(head + svg + "\n")
    thin = sum(1 for r in tiles if r["red"] and r is not land)
    print(f"{len(tiles)} tiles ({thin} thin, {len(tiles) - thin - 1} wide, 1 gold); "
          f"edge {EDGE:.2f}; wrote {dest}")


if __name__ == "__main__":
    main()
