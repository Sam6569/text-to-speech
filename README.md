# SpeakEasy - Text-to-Speech Application

**Your words, spoken naturally**

A serverless text-to-speech application built with AWS services that translates and converts text into natural-sounding speech using AWS Polly and AWS Translate.

## Features

- **Multi-language Translation**: Translate English text to French, Spanish, Italian, or German
- **Voice Selection**: Choose from 26+ AWS Polly voices across different languages and regions
- **Audio Formats**: Generate speech in MP3, OGG, or PCM formats
- **Speed Control**: Adjust speech speed from extra slow to extra fast
- **Real-time Processing**: Fast serverless architecture with AWS Lambda
- **Audio Playback**: Built-in audio player with download functionality
- **Responsive Design**: Works on desktop and mobile devices

## Architecture

### AWS Services Used
- **AWS Lambda**: Serverless compute for text processing and speech generation
- **AWS Polly**: Text-to-speech synthesis with natural-sounding voices
- **AWS Translate**: Multi-language text translation
- **AWS S3**: Storage for audio files and static website hosting
- **AWS API Gateway**: RESTful API endpoint for frontend communication
- **AWS IAM**: Security and access management

### Infrastructure as Code
- **Terraform**: Complete infrastructure deployment and management
- **Modular Design**: Separate modules for API, Lambda, S3, and IAM resources

## Supported Languages

- **English** (Original)
- **French** (Français)
- **Spanish** (Español)
- **Italian** (Italiano)
- **German** (Deutsch)

## Available Voices

### English Voices
- Joanna, Matthew, Ivy, Justin, Kendra, Kimberly, Salli, Joey (US)
- Nicole, Russell (Australian)
- Amy, Brian, Emma (British)

### International Voices
- **French**: Celine, Mathieu, Lea
- **Spanish**: Conchita, Enrique, Lucia, Mia
- **Italian**: Carla, Giorgio, Bianca
- **German**: Marlene, Hans, Vicki

## Deployment

### Prerequisites
- AWS CLI configured with appropriate permissions
- Terraform installed
- PowerShell (for Windows deployment)

### Quick Deploy
```bash
cd backend
terraform init
terraform apply -auto-approve
```

### Manual Steps
1. **Deploy Infrastructure**:
   ```bash
   cd backend
   terraform init
   terraform plan
   terraform apply
   ```

2. **Upload Frontend**:
   ```bash
   cd frontend
   aws s3 cp index.html s3://[your-bucket-name]/
   ```

## Usage

1. **Enter Text**: Type or paste your English text (up to 3000 characters)
2. **Select Language**: Choose target language for translation
3. **Choose Voice**: Pick from available Polly voices
4. **Set Options**: Select audio format and speech speed
5. **Generate**: Click "Generate Speech" to create audio
6. **Listen & Download**: Play audio in browser or download file

## API Endpoints

### POST /speech
Generate speech from text with translation

**Request Body**:
```json
{
  "text": "Hello world",
  "targetLanguage": "fr",
  "voice": "Celine",
  "outputFormat": "mp3",
  "speed": "medium"
}
```

**Response**:
```json
{
  "success": true,
  "data": {
    "audioUrl": "https://...",
    "voice": "Celine",
    "format": "mp3",
    "textLength": 11,
    "translatedText": "Bonjour le monde",
    "targetLanguage": "fr",
    "expiresAt": "2025-09-18T09:12:30Z"
  }
}
```

## Configuration

### Environment Variables
- `AUDIO_BUCKET`: S3 bucket for storing generated audio files

### Terraform Variables
- `lambda_function_name`: Name for the Lambda function
- `api_gateway_name`: Name for the API Gateway
- `lambda_execution_role_name`: IAM role name for Lambda

## Security

- **CORS Enabled**: Proper cross-origin resource sharing configuration
- **IAM Roles**: Least privilege access for Lambda function
- **Signed URLs**: Temporary access to S3 audio files (1-hour expiration)
- **Input Validation**: Text length limits and sanitization

## Costs

Estimated costs for moderate usage:
- **Lambda**: ~$0.20 per 1M requests
- **Polly**: ~$4.00 per 1M characters
- **Translate**: ~$15.00 per 1M characters
- **S3**: ~$0.023 per GB storage
- **API Gateway**: ~$3.50 per 1M requests

## Limitations

- Maximum text length: 3000 characters
- Audio file expiration: 1 hour
- Supported translation pairs: English to target languages only
- File formats: MP3, OGG, PCM only

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is licensed under the MIT License.

## Support

For issues and questions:
- Check AWS service limits and quotas
- Verify IAM permissions
- Review CloudWatch logs for Lambda function errors
- Ensure S3 bucket policies allow public read access for audio files