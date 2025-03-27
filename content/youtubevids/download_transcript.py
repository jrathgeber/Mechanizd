from youtube_transcript_api import YouTubeTranscriptApi


def fetch_it(video_id):

    print(video_id)

    ytt_api = YouTubeTranscriptApi()

    transcript = ytt_api.fetch(video_id)

    transcript_text = ""

    with open('transcript.txt', 'w') as file:
        for snippet in transcript:
            transcript_text += snippet.text
            print(snippet.text)

    return transcript_text


if __name__ == '__main__':
    fetch_it('SAUXDR4o1kA')
