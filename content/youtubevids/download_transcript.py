from youtube_transcript_api import YouTubeTranscriptApi


def fetch_it(video_id):

    video_id = 'SAUXDR4o1kA'
    transcript = YouTubeTranscriptApi.fetch(video_id)

    with open('transcript.txt', 'w') as file:
        for entry in transcript:
            file.write(f"{entry['text']}\n")

    return transcript

if __name__ == '__main__':
    fetch_it('SAUXDR4o1kA')