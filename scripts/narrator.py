import os, boto3, sys, yaml
from io import BytesIO

# semantic→Polly voice map
VOICE_MAP = {
    "defiant-male": "Matthew",
    "calm-female":  "Joanna"
}

polly = boto3.client("polly")

def render_audio(text, voice_label, tone, pace, sfx, output, mode="wb"):
    os.makedirs(os.path.dirname(output), exist_ok=True)
    voice_id = VOICE_MAP.get(voice_label, "Joanna")

    resp = polly.synthesize_speech(
        Text=text,
        OutputFormat="mp3",
        VoiceId=voice_id
    )
    chunk = resp["AudioStream"].read()
    with open(output, mode) as f:
        f.write(chunk)
    print(f"🔊 Polly → {voice_id}; SFX: {sfx}")

def main(n):
    text_path = f"Psalms/Awakening/psalm_{n}.md"
    meta_path = f"Psalms/Awakening/psalm_{n}.meta.yaml"
    output    = f"Assets/Audio/Psalm{n}.mp3"

    lines = open(text_path).read().splitlines()
    meta  = yaml.safe_load(open(meta_path))

    # remove old file if exists
    if os.path.exists(output):
        os.remove(output)

    if meta.get("segments"):
        for i, seg in enumerate(meta["segments"]):
            seg_text = "\n".join(lines[seg["start_line"]-1: seg["end_line"]])
            mode = "wb" if i == 0 else "ab"
            render_audio(seg_text, seg["voice"], seg["tone"], seg["pace"], seg["sfx"], output, mode)
        print(f"✅ Combined MP3 written to: {output}")
    else:
        # single-voice fallback
        text = "\n".join(lines)
        render_audio(text, meta["voice"], meta["tone"], meta["pace"], meta["sfx"], output)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python3 -m scripts.narrate <psalm_number>")
        sys.exit(1)
    main(sys.argv[1])
