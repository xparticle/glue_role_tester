import boto3

def role_arn_to_session(**args):
    """
    Usage :
        session = role_arn_to_session(
            RoleArn='arn:aws:iam::012345678901:role/example-role',
            RoleSessionName='ExampleSessionName')
        client = session.client('sqs')
    """
    client = boto3.client('sts')
    response = client.assume_role(**args)
    return boto3.Session(
        aws_access_key_id=response['Credentials']['AccessKeyId'],
        aws_secret_access_key=response['Credentials']['SecretAccessKey'],
        aws_session_token=response['Credentials']['SessionToken'])


def main():
    session = role_arn_to_session(
            RoleArn='arn:aws:iam::012345678901:role/glue_app1',
            RoleSessionName='GlueH9VVSession')
    glue_client = session.client('glue')
    response = glue_client.get_table(
        CatalogId='012345678901',
        DatabaseName='db1_for_app1',
        Name='table_a'
    )
    logger.info(response)

if __name__ == '__main__':
    import logging
    import logging.config
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger('glue_role_tester')
    main()