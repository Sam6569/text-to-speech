variable "aws_region" {
  description = "AWS region to deploy resources"
  type        = string
  default     = "us-east-1"
}

variable "audio_bucket_name" {
  description = "S3 bucket name for storing audio files"
  type        = string
  default     = "text-to-speech-audio-bucket10"
}

variable "frontend_bucket_name" {
  description = "S3 bucket name for hosting static website"
  type        = string
  default     = "static-website-bucket10"
}

variable "lambda_function_name" {
  description = "Name of the Lambda function"
  type        = string
  default     = "text-to-speech"
}

variable "api_gateway_name" {
  description = "Name of the API Gateway"
  type        = string
  default     = "text-to-speech-api"
}

variable "lambda_execution_role_name" {
  description = "Name of the Lambda execution role"
  type        = string
  default     = "text-to-speech-execution-role"
}

variable "lambda_policy_name" {
  description = "Name of the Lambda policy"
  type        = string
  default     = "text-to-speech-policy"
}