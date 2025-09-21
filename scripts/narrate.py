#!/usr/bin/env python3
import os, sys, yaml
from scripts.narrator import render_audio

def main(n):
    root   = "Psalms/Awakening"
    text   = open(f"{root}/psalm_{n}.md").read().splitlines()
    meta   = yaml.safe_load(open(f"{root}/psalm_{n}.meta.yaml"))
    out    = f"Assets/Audio/Psalm{n}.mp3"
    os.makedirs(os.path.dirname(out), exist_ok=True)
    if meta.get("segments"):
        for i, s in enumerate(meta["segments"]):
            segtxt = "\n".join(text[s["start_line"]-1:s["end_line"]])
            mode = "wb" if i == 0 else "ab"
            render_audio(segtxt, s["voice"], s["tone"], s["pace"], s["sfx"], out, mode)
        print(f"✅ Combined MP3 written to: {out}")
    else:
        render_audio("\n".join(text), meta["voice"], meta["tone"], meta["pace"], meta["sfx"], out)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 -m scripts.narrate <number>")
        sys.exit(1)
    main(sys.argv[1])
