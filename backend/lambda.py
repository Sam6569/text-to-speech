import boto3
import os
import uuid
import json
from datetime import datetime, timedelta
 
s3 = boto3.client('s3')
polly = boto3.client('polly')
translate = boto3.client('translate')
 
BUCKET = os.environ['AUDIO_BUCKET']

# Language to voice mapping
LANGUAGE_VOICES = {
    'en': ['Joanna', 'Matthew', 'Ivy', 'Justin', 'Kendra', 'Kimberly', 'Salli', 'Joey', 'Nicole', 'Russell', 'Amy', 'Brian', 'Emma'],
    'fr': ['Celine', 'Mathieu', 'Lea'],
    'es': ['Conchita', 'Enrique', 'Lucia', 'Mia'],
    'it': ['Carla', 'Giorgio', 'Bianca'],
    'de': ['Marlene', 'Hans', 'Vicki'],
    'tw': ['Joanna']  # Twi uses English voice as fallback
}
 
def handler(event, context):
    headers = {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Headers": "Content-Type",
        "Access-Control-Allow-Methods": "OPTIONS,POST"
    }
 
    try:
        # Parse JSON body
        body = json.loads(event['body'])
        text = body['text']
        voice = body.get('voice', 'Joanna')
        output_format = body.get('outputFormat', 'mp3')
        speed = body.get('speed', 'medium')
        target_language = body.get('targetLanguage', 'en')
        
        # Translate text if target language is not English
        translated_text = text
        if target_language != 'en':
            translate_response = translate.translate_text(
                Text=text,
                SourceLanguageCode='en',
                TargetLanguageCode=target_language
            )
            translated_text = translate_response['TranslatedText']
        
        # Wrap text with SSML for speed control
        ssml_text = f'<speak><prosody rate="{speed}">{translated_text}</prosody></speak>'
        
        file_name = f"{uuid.uuid4()}.{output_format}"
 
        # Call Polly
        response = polly.synthesize_speech(
            Text=ssml_text,
            TextType='ssml',
            OutputFormat=output_format,
            VoiceId=voice
        )
 
        # Upload to S3
        s3.put_object(
            Bucket=BUCKET,
            Key=file_name,
            Body=response['AudioStream'].read()
        )
 
        # Generate signed URL
        expires_in = 3600
        url = s3.generate_presigned_url(
            ClientMethod="get_object",
            Params={"Bucket": BUCKET, "Key": file_name},
            ExpiresIn=expires_in
        )
        
        expires_at = datetime.utcnow() + timedelta(seconds=expires_in)
 
        return {
            "statusCode": 200,
            "headers": headers,
            "body": json.dumps({
                "success": True,
                "data": {
                    "audioUrl": url,
                    "voice": voice,
                    "format": output_format,
                    "textLength": len(text),
                    "translatedText": translated_text if target_language != 'en' else None,
                    "targetLanguage": target_language,
                    "expiresAt": expires_at.isoformat() + "Z"
                }
            })
        }
 
    except Exception as e:
        print(f"Error: {str(e)}")
        import traceback
        print(f"Traceback: {traceback.format_exc()}")
        return {
            "statusCode": 500,
            "headers": headers,
            "body": json.dumps({
                "success": False,
                "error": str(e)
            })
        }
 
 