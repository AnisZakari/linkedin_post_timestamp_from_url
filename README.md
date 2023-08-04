# LinkedIn Post Time Extractor

This is a small AWS Lambda function that extracts the posting time from a LinkedIn post URL. It's designed to be deployed with AWS CDK and works by creating a REST API with API Gateway that triggers the Lambda function.

## How it works

Given a LinkedIn post URL, the function extracts the post's unique ID and converts it to a Unix timestamp. This timestamp is then converted to a human-readable date and time in the Paris timezone.

## Deployment

The function is deployed using AWS CDK. The deployment script creates a Docker-based Lambda function and an API Gateway with a single POST endpoint. The endpoint is protected with an API key and has a usage plan with a rate limit and burst limit.

The deployment script is written in Python and uses the AWS CDK Python bindings. The Lambda function itself is also written in Python.

## Usage

Once deployed, you can call the API Gateway endpoint with a POST request. The body of the request should be a JSON object with a `linkedin_url` key, like this:

```json
{
  "linkedin_url": "https://www.linkedin.com/posts/alliekmiller_goodbye-mouse-clicks-othersideai-hyperwrite-ugcPost-7093310227491500032-TQ81?utm_source=share&utm_medium=member_desktop"
}
```

Here is a full example in python

```python
import requests

url = "url-to-the-api-getaway-endpoint"
api_key = "api-gateway-api-key"
linkedin_post_url = "your-linkedin-post-url"

headers = {"x-api-key": api_key}

payload = {
    "linkedin_url": linkedin_post_url
}

response = requests.post(url, headers=headers, json=payload)

print(response.text)
```

## Limitations

This function only works with public LinkedIn posts. The timestamp extraction relies on the structure of the post's unique ID and may not work if LinkedIn changes this structure.