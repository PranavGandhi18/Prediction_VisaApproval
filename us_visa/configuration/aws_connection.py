import boto3
import os
from us_visa.constants import AWS_SECRET_ACCESS_KEY_ENV_KEY, AWS_ACCESS_KEY_ID_ENV_KEY,REGION_NAME
from us_visa.logger import logging


class S3Client:

    s3_client=None
    s3_resource = None
    def __init__(self, region_name=REGION_NAME):
        """ 
        This Class gets aws credentials from env_variable and creates an connection with s3 bucket 
        and raise exception when environment variable is not set
        """
        print(S3Client.s3_resource)
        print(S3Client.s3_client)
        if S3Client.s3_resource==None or S3Client.s3_client==None:
            logging.info("Entered If condition of aws_connection file")
            __access_key_id = os.getenv(AWS_ACCESS_KEY_ID_ENV_KEY, )
            __secret_access_key = os.getenv(AWS_SECRET_ACCESS_KEY_ENV_KEY, )
            # __access_key_id = AWS_ACCESS_KEY_ID_ENV_KEY
            # __secret_access_key = AWS_SECRET_ACCESS_KEY_ENV_KEY
            # print(__access_key_id)
            # print(__secret_access_key)
            if __access_key_id is None:
                raise Exception(f"Environment variable: {AWS_ACCESS_KEY_ID_ENV_KEY} is not not set.")
            if __secret_access_key is None:
                raise Exception(f"Environment variable: {AWS_SECRET_ACCESS_KEY_ENV_KEY} is not set.")

            # session = boto3.session.Session(aws_access_key_id=__access_key_id,aws_secret_access_key=__secret_access_key,region_name=region_name)
            # S3Client.s3_client = session.client('s3')
            # S3Client.s3_resource = session.resource('s3')

            
             
            S3Client.s3_resource = boto3.resource('s3',
                                            aws_access_key_id=__access_key_id,
                                            aws_secret_access_key=__secret_access_key,
                                            region_name=region_name
                                            )
            S3Client.s3_client = boto3.client('s3',
                                        aws_access_key_id=__access_key_id,
                                        aws_secret_access_key=__secret_access_key,
                                        region_name=region_name
                                        )

            print(S3Client.s3_resource)
            print(S3Client.s3_client)

        self.s3_resource = S3Client.s3_resource
        self.s3_client = S3Client.s3_client
        