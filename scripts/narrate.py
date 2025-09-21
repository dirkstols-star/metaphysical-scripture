#!/usr/bin/env python3
import sys, yaml
from scripts.narrator import render_audio

def main(psalm_number):
    text_path   = f"Psalms/Awakening/psalm_{psalm_number}.md"
    meta_path   = f"Psalms/Awakening/psalm_{psalm_number}.meta.yaml"
    output_path = f"Assets/Audio/Psalm{psalm_number}.mp3"

    with open(text_path) as tf:
        text = tf.read()
    with open(meta_path) as mf:
        meta = yaml.safe_load(mf)

    render_audio(
        text,
        meta["voice"],
        meta["tone"],
        meta["pace"],
        meta["sfx"],
        output_path
    )

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 -m scripts.narrate <psalm_number>")
        sys.exit(1)
    main(sys.argv[1])
