# LinkedIn Post Time Extractor

This is a small AWS Lambda function that extracts the posting time from a LinkedIn post URL. It's designed to be deployed with AWS CDK and works by creating a REST API with API Gateway that triggers the Lambda function.

## How it works

Given a LinkedIn post URL, the function extracts the post's unique ID and converts it to a Unix timestamp. This timestamp is then converted to a human-readable date and time in the Paris timezone.

## Deployment

The function is deployed using AWS CDK. The deployment script creates a Docker-based Lambda function and an API Gateway with a single POST endpoint. The endpoint is protected with an API key and has a usage plan with a rate limit and burst limit.

The deployment script is written in Python and uses the AWS CDK Python bindings. The Lambda function itself is also written in Python.

### Deployment Steps

1. Clone this repository to your local machine.
2. Navigate to the project directory.
3. Install the required dependencies with `pip install -r requirements.txt`.
4. Ensure you have the AWS CDK installed. If not, you can install it with `npm install -g aws-cdk`.
5. Deploy the stack with `cdk deploy`.

## Usage

Once deployed, you can call the API Gateway endpoint with a POST request. The body of the request should be a JSON object with a `linkedin_url` key, like this:

```json
{
  "linkedin_url": "https://www.linkedin.com/feed/update/urn:li:activity:7092562497743773696?updateEntityUrn=urn%3Ali%3Afs_feedUpdate%3A%28V2%2Curn%3Ali%3Aactivity%3A7092562497743773696%29"
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