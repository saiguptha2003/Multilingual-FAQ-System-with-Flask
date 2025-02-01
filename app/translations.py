import boto3
from botocore.auth import SigV4Auth
from botocore.awsrequest import AWSRequest

def sign_request(method, url, payload, access_key, secret_key, region, service):
    session = boto3.Session(aws_access_key_id=access_key, aws_secret_access_key=secret_key)
    credentials = session.get_credentials()

    request = AWSRequest(method=method, url=url, data=payload, headers={"Content-Type": "application/json"})
    SigV4Auth(credentials, service, region).add_auth(request)

    return dict(request.headers)
