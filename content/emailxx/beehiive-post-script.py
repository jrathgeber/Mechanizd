import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class BeehiivePostManager:
    def __init__(self, beehiive_api_key, beehiive_endpoint):
        """
        Initialize the Beehiive post manager with API credentials
        
        :param beehiive_api_key: Your Beehiive API key
        :param beehiive_endpoint: The base URL for Beehiive API
        """
        self.api_key = beehiive_api_key
        self.endpoint = beehiive_endpoint
    
    def create_post(self, title, content, tags=None):
        """
        Create a post on Beehiive
        
        :param title: Title of the post
        :param content: Content of the post
        :param tags: Optional list of tags
        :return: Response from Beehiive API
        """
        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }
        
        payload = {
            'title': title,
            'content': content,
        }
        
        if tags:
            payload['tags'] = tags
        
        try:
            response = requests.post(
                f'{self.endpoint}/posts', 
                json=payload, 
                headers=headers
            )
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error creating Beehiive post: {e}")
            return None

class MailingListManager:
    def __init__(self, smtp_host, smtp_port, smtp_username, smtp_password):
        """
        Initialize the mailing list manager with SMTP credentials
        
        :param smtp_host: SMTP server host
        :param smtp_port: SMTP server port
        :param smtp_username: SMTP username
        :param smtp_password: SMTP password
        """
        self.smtp_host = smtp_host
        self.smtp_port = smtp_port
        self.smtp_username = smtp_username
        self.smtp_password = smtp_password
    
    def send_to_mailing_list(self, recipients, subject, body, html_body=None):
        """
        Send an email to a mailing list
        
        :param recipients: List of email addresses
        :param subject: Email subject
        :param body: Plain text email body
        :param html_body: Optional HTML version of the email
        :return: Boolean indicating success
        """
        try:
            # Create the email message
            message = MIMEMultipart('alternative')
            message['From'] = self.smtp_username
            message['To'] = ', '.join(recipients)
            message['Subject'] = subject

            # Attach plain text version
            message.attach(MIMEText(body, 'plain'))

            # Attach HTML version if provided
            if html_body:
                message.attach(MIMEText(html_body, 'html'))

            # Send the email
            with smtplib.SMTP(self.smtp_host, self.smtp_port) as server:
                server.starttls()
                server.login(self.smtp_username, self.smtp_password)
                server.sendmail(self.smtp_username, recipients, message.as_string())
            
            return True
        except Exception as e:
            print(f"Error sending email: {e}")
            return False

def main():
    # Configuration - REPLACE WITH YOUR ACTUAL CREDENTIALS
    BEEHIIVE_API_KEY = 'your_beehiive_api_key'
    BEEHIIVE_ENDPOINT = 'https://api.beehiive.com/v1'
    
    SMTP_HOST = 'smtp.yourdomain.com'
    SMTP_PORT = 587
    SMTP_USERNAME = 'your_email@yourdomain.com'
    SMTP_PASSWORD = 'your_smtp_password'
    
    MAILING_LIST = [
        'recipient1@example.com', 
        'recipient2@example.com'
    ]

    # Create Beehiive post
    beehiive_manager = BeehiivePostManager(BEEHIIVE_API_KEY, BEEHIIVE_ENDPOINT)
    post_data = beehiive_manager.create_post(
        title='My Latest Post', 
        content='This is the content of my post.', 
        tags=['news', 'update']
    )

    if post_data:
        # Send to mailing list
        mailing_list_manager = MailingListManager(
            SMTP_HOST, SMTP_PORT, 
            SMTP_USERNAME, SMTP_PASSWORD
        )
        
        email_body = f"""
        Check out our latest post!
        
        Title: {post_data.get('title', 'New Post')}
        Link: {post_data.get('url', 'No link available')}
        
        Read the full post on Beehiive!
        """
        
        html_email_body = f"""
        <html>
        <body>
            <h1>New Post Available!</h1>
            <p>Title: {post_data.get('title', 'New Post')}</p>
            <p>Link: <a href="{post_data.get('url', '#')}">Read Full Post</a></p>
        </body>
        </html>
        """
        
        mailing_list_manager.send_to_mailing_list(
            MAILING_LIST, 
            'New Post on Beehiive', 
            email_body, 
            html_email_body
        )

if __name__ == '__main__':
    main()
