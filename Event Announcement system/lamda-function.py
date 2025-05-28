
import json
import boto3

sns = boto3.client('sns')
TOPIC_ARN = 'arn:aws:sns:ap-south-1:253490781240:event-announcements'

def lambda_handler(event, context):
    print("Received event:", event)

    try:
        body = json.loads(event['body']) if 'body' in event else event
        message = body.get('message', 'No message provided')

        sns.publish(
            TopicArn=TOPIC_ARN,
            Message=message,
            Subject="New Event Announcement"
        )

        return {
            'statusCode': 200,
            'body': json.dumps('Event announced successfully!')
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f"Error: {str(e)}")
        }
