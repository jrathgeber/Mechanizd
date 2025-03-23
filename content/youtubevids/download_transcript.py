from youtube_transcript_api import YouTubeTranscriptApi

video_id = 'SAUXDR4o1kA'
transcript = YouTubeTranscriptApi.get_transcript(video_id)

with open('transcript.txt', 'w') as file:
    for entry in transcript:
        file.write(f"{entry['text']}\n")