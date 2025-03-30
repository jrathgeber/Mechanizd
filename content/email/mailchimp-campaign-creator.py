import requests
import json
from datetime import datetime, timedelta
import os


# Load environment variables from .env file
load_dotenv()

class MailchimpCampaign:
    def __init__(self, api_key=None, server_prefix=None):
        """
        Initialize the Mailchimp API client.
        
        Args:
            api_key: Your Mailchimp API key
            server_prefix: The server prefix from your API key (e.g., 'us6')
        """
        # Use environment variables if not provided explicitly
        self.api_key = api_key or os.getenv('MAILCHIMP_API_KEY')
        self.server_prefix = server_prefix or os.getenv('MAILCHIMP_SERVER_PREFIX')
        
        if not self.api_key or not self.server_prefix:
            raise ValueError("Missing Mailchimp API credentials. Provide them as parameters or in .env file.")
        
        self.base_url = f"https://{self.server_prefix}.api.mailchimp.com/3.0"
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': f'apikey {self.api_key}'
        }
    
    def get_lists(self):
        """Get all audience lists from Mailchimp account."""
        response = requests.get(f"{self.base_url}/lists", headers=self.headers)
        response.raise_for_status()
        return response.json()['lists']
    
    def create_campaign(self, list_id, subject, preview_text, title, from_name, reply_to):
        """
        Create a new email campaign.
        
        Args:
            list_id: The ID of the audience list
            subject: Email subject line
            preview_text: Preview text that appears in inbox
            title: Internal campaign name
            from_name: Sender's name
            reply_to: Reply-to email address
            
        Returns:
            Campaign ID if successful
        """
        payload = {
            "type": "regular",
            "recipients": {
                "list_id": list_id
            },
            "settings": {
                "subject_line": subject,
                "preview_text": preview_text,
                "title": title,
                "from_name": from_name,
                "reply_to": reply_to,
                "to_name": "*|FNAME|*"  # Personalization merge tag
            }
        }
        
        response = requests.post(
            f"{self.base_url}/campaigns",
            headers=self.headers,
            data=json.dumps(payload)
        )
        response.raise_for_status()
        return response.json()['id']
    
    def set_campaign_content(self, campaign_id, html_content):
        """
        Set the HTML content for a campaign.
        
        Args:
            campaign_id: The ID of the campaign
            html_content: HTML content for the email
        """
        payload = {
            "html": html_content
        }
        
        response = requests.put(
            f"{self.base_url}/campaigns/{campaign_id}/content",
            headers=self.headers,
            data=json.dumps(payload)
        )
        response.raise_for_status()
        return response.json()
    
    def schedule_campaign(self, campaign_id, schedule_time=None):
        """
        Schedule a campaign to be sent.
        
        Args:
            campaign_id: The ID of the campaign
            schedule_time: ISO formatted datetime string (if None, schedules for 30 min from now)
        """
        if schedule_time is None:
            # Default to 30 minutes from now
            schedule_time = (datetime.utcnow() + timedelta(minutes=30)).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"
        
        payload = {
            "schedule_time": schedule_time
        }
        
        response = requests.post(
            f"{self.base_url}/campaigns/{campaign_id}/actions/schedule",
            headers=self.headers,
            data=json.dumps(payload)
        )
        response.raise_for_status()
        return True
    
    def send_campaign_now(self, campaign_id):
        """
        Send a campaign immediately.
        
        Args:
            campaign_id: The ID of the campaign
        """
        response = requests.post(
            f"{self.base_url}/campaigns/{campaign_id}/actions/send",
            headers=self.headers
        )
        response.raise_for_status()
        return True
    
    def create_and_send_campaign(self, list_id, subject, preview_text, title, 
                               from_name, reply_to, html_content, schedule=False, 
                               schedule_time=None):
        """
        Create a campaign, set its content, and either send it immediately or schedule it.
        
        Args:
            list_id: The ID of the audience list
            subject: Email subject line
            preview_text: Preview text that appears in inbox
            title: Internal campaign name
            from_name: Sender's name
            reply_to: Reply-to email address
            html_content: HTML content for the email
            schedule: If True, schedule the campaign instead of sending immediately
            schedule_time: ISO formatted datetime string (if None and schedule=True, 
                          schedules for 30 min from now)
                          
        Returns:
            Campaign ID if successful
        """
        # Create the campaign
        campaign_id = self.create_campaign(list_id, subject, preview_text, title, from_name, reply_to)
        
        # Set the content
        self.set_campaign_content(campaign_id, html_content)
        
        # Send or schedule
        if schedule:
            self.schedule_campaign(campaign_id, schedule_time)
            print(f"Campaign scheduled{'.' if schedule_time else ' for 30 minutes from now.'}")
        else:
            self.send_campaign_now(campaign_id)
            print("Campaign sent immediately.")
        
        return campaign_id


# Example usage
if __name__ == "__main__":
    # Create a sample HTML content for testing
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>My Newsletter</title>
    </head>
    <body>
        <h1>Hello *|FNAME|*!</h1>
        <p>This is a test email sent through the Mailchimp API.</p>
        <p>You can include any HTML content here including images, links, and styling.</p>
        <div style="background-color: #f8f8f8; padding: 15px; border-radius: 5px;">
            <h2>Featured Article</h2>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus lacinia odio vitae vestibulum.</p>
            <a href="https://example.com/article" style="background-color: #0078d4; color: white; padding: 10px 15px; text-decoration: none; border-radius: 4px; display: inline-block;">Read More</a>
        </div>
        <p>Best regards,<br>Your Name</p>
        <p style="font-size: 12px; color: #666;">
            *|IF:FNAME|*To unsubscribe, <a href="*|UNSUB|*">click here</a>.*|END:IF|*
        </p>
    </body>
    </html>
    """
    
    try:
        # Initialize the Mailchimp client
        mailchimp = MailchimpCampaign()
        
        # Get available lists and use the first one
        lists = mailchimp.get_lists()
        if not lists:
            print("No audience lists found in your Mailchimp account.")
            exit()
        
        # Use the first list
        list_id = lists[0]['id']
        list_name = lists[0]['name']
        print(f"Using list: {list_name} (ID: {list_id})")
        
        # Create and send the campaign
        campaign_id = mailchimp.create_and_send_campaign(
            list_id=list_id,
            subject="Test Campaign from Python Script",
            preview_text="This is a test email generated by our Python script",
            title="Python API Test Campaign",
            from_name="Your Name",
            reply_to="your.email@example.com",
            html_content=html_content,
            schedule=True  # Set to True to schedule instead of sending immediately
        )
        
        print(f"Campaign created with ID: {campaign_id}")
        
    except Exception as e:
        print(f"Error: {str(e)}")
