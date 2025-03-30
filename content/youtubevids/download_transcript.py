from youtube_transcript_api import YouTubeTranscriptApi
import configparser

config = configparser.ConfigParser()
config.read('C:\\etc\\properties.ini')
code_path = config['blog']['blog_temp']


def fetch_it(video_id):

    print(video_id)

    ytt_api = YouTubeTranscriptApi()

    transcript = ytt_api.fetch(video_id)

    transcript_text = ""
    transcript_path = code_path
    transcript_name = video_id

    file_to_download =  transcript_path + "youtube_transcript_" + transcript_name + ".txt"

    with open(file_to_download, 'w') as file:
        for snippet in transcript:
            transcript_text += snippet.text
            print(snippet.text)

    return transcript_text


if __name__ == '__main__':
    fetch_it('SAUXDR4o1kA')
