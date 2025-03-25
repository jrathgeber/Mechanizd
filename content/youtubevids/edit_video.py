import moviepy.editor as mp
import numpy as np


def remove_silence_from_video(input_path, output_path, silence_threshold=-40, min_silence_duration=1):
    """
    Automatically remove silent sections from a video file.

    Parameters:
    - input_path: Path to the input video file
    - output_path: Path to save the edited video
    - silence_threshold: Audio decibel level below which is considered silence (default: -40 dB)
    - min_silence_duration: Minimum duration of silence to remove (in seconds)

    Returns:
    - Edited video file
    """
    try:
        # Load the video file
        video = mp.VideoFileClip(input_path)

        # Extract the audio
        audio = video.audio

        # Convert audio to numpy array for analysis
        audio_array = audio.to_soundarray()

        # Calculate the volume of the audio in decibels
        audio_volumes = 20 * np.log10(np.abs(audio_array))

        # Detect silent segments
        silent_segments = []
        is_silent = False
        silence_start = 0

        for i in range(len(audio_volumes)):
            time = i / audio.fps
            is_currently_silent = audio_volumes[i] < silence_threshold

            if is_currently_silent and not is_silent:
                # Start of a silent segment
                silence_start = time
                is_silent = True
            elif not is_currently_silent and is_silent:
                # End of a silent segment
                silence_duration = time - silence_start
                if silence_duration >= min_silence_duration:
                    silent_segments.append((silence_start, time))
                is_silent = False

        # Create a list of non-silent video clips
        final_clips = []
        last_end = 0

        for start, end in silent_segments:
            # Add non-silent clip before the silence
            if start > last_end:
                clip = video.subclip(last_end, start)
                final_clips.append(clip)
            last_end = end

        # Add the final clip if there's remaining video after last silence
        if last_end < video.duration:
            final_clips.append(video.subclip(last_end, video.duration))

        # Concatenate the clips
        final_video = mp.concatenate_videoclips(final_clips)

        # Write the final video
        final_video.write_videofile(output_path, codec='libx264')

        # Close video clips to free up resources
        video.close()
        final_video.close()
        for clip in final_clips:
            clip.close()

        print(f"Video edited successfully. Saved to {output_path}")

    except Exception as e:
        print(f"An error occurred: {e}")


# Example usage
if __name__ == "__main__":
    input_video = "input_video.mkv"
    output_video = "edited_video.mkv"

    # You can adjust these parameters as needed
    remove_silence_from_video(
        input_path=input_video,
        output_path=output_video,
        silence_threshold=-40,  # Adjust based on your video's audio characteristics
        min_silence_duration=1  # Minimum silence duration to remove (in seconds)
    )