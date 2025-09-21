import os

def render_audio(text, voice, tone, pace, sfx, output):
    # ensure the output folder exists
    os.makedirs(os.path.dirname(output), exist_ok=True)

    print(f"🔊 Rendering audio for Psalm…")
    print(f"Voice: {voice}, Tone: {tone}, Pace: {pace}, SFX: {sfx}")
    print(f"Saving to: {output}")
    with open(output, 'w') as f:
        f.write(
            "[AUDIO PLACEHOLDER]\n"
            f"Voice: {voice}\n"
            f"Tone: {tone}\n"
            f"Pace: {pace}\n"
            f"SFX: {', '.join(sfx)}\n\n"
            f"{text}"
        )
