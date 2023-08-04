import json
import logging
import re
from datetime import datetime

import pytz

# Create a logger with the __name__ context
logger = logging.getLogger(__name__)


def get_post_id(linkedin_url):
    regex = re.compile(r"([0-9]{19})")
    match = regex.search(linkedin_url)
    if match:
        return match.group(0)
    return None


def extract_unix_timestamp(post_id):
    as_binary = bin(int(post_id))[2:]  # [2:] is used to remove the '0b' prefix
    first41_chars = as_binary[:41]
    timestamp = int(first41_chars, 2) / 1000  # Convert milliseconds to seconds
    return timestamp


def unix_timestamp_to_human_date(timestamp):
    date_object = datetime.utcfromtimestamp(timestamp)
    paris_tz = pytz.timezone("Europe/Paris")
    date_object = date_object.replace(tzinfo=pytz.timezone("UTC"))
    date_object = date_object.astimezone(paris_tz)
    human_date_format = date_object.strftime("%a, %d %b %Y %H:%M:%S (%Z)")
    return human_date_format


def get_date(linkedin_url):
    post_id = get_post_id(linkedin_url)
    if post_id is None:
        return "No valid Post ID found"
    unix_timestamp = extract_unix_timestamp(post_id)
    human_date_format = unix_timestamp_to_human_date(unix_timestamp)
    return human_date_format


def lambda_handler(event, context):
    logger.info("payload:")
    logger.info(event)
    linkedin_url = event["linkedin_url"]
    return get_date(linkedin_url)


def lambda_handler(event, context):
    logger.info("payload:")
    logger.info(event)
    try:
        # Parse the body from the event object
        body = json.loads(event["body"])

        # Get the linkedin_url from the body
        linkedin_url = body["linkedin_url"]

        logger.info(f"Received LinkedIn URL: {linkedin_url}")

        return get_date(linkedin_url)
    except KeyError:
        logger.error('The "linkedin_url" parameter was not found in the body of the event object')
        raise
