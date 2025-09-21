#!/usr/bin/env python3
import sys, yaml, os
from scripts.narrator import render_audio

def main(n):
    text_path = f"Psalms/Awakening/psalm_{n}.md"
    meta_path = f"Psalms/Awakening/psalm_{n}.meta.yaml"
    output    = f"Assets/Audio/Psalm{n}.mp3"
    os.makedirs(os.path.dirname(output), exist_ok=True)

    lines = open(text_path).read().splitlines()
    meta  = yaml.safe_load(open(meta_path))

    if 'segments' in meta:
        # build combined placeholder file
        with open(output, 'w') as final:
            final.write("[MULTI-VOICE AUDIO PLACEHOLDER]\n")
            for i, seg in enumerate(meta['segments'], 1):
                seg_text = "\n".join(lines[seg['start_line']-1 : seg['end_line']])
                final.write(f"\n--- Segment {i} ---\n")
                final.write(f"Voice: {seg['voice']}\n")
                final.write(f"Tone: {seg['tone']}\n")
                final.write(f"Pace: {seg['pace']}\n")
                final.write(f"SFX: {', '.join(seg['sfx'])}\n\n")
                final.write(seg_text + "\n")
        print(f"🔊 Multi-voice rendering complete: {output}")
    else:
        # fallback to single-voice
        text = "\n".join(lines)
        render_audio(text, meta["voice"], meta["tone"], meta["pace"], meta["sfx"], output)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 -m scripts.narrate <psalm_number>")
        sys.exit(1)
    main(sys.argv[1])
