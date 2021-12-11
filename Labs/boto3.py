import boto3

client = client('EC2')
try:
    response = client.run_instances(
        ImageId='ami-02354e95b39ca8dec',
        InstanceType='t2.micro',
        KeyName='mageen-uvasom',
        SecurityGroupIds=[
            'sg-04262c688917e0891',
        ],
        SubnetId='subnet-b39b21c5',
        DryRun=False,
        MinCount=1,
        MaxCount=1,
        InstanceInitiatedShutdownBehavior='terminate',
        TagSpecifications=[
            {
                'ResourceType': 'instance',
                'Tags': [
                    {
                        'Key': 'Name',
                        'Value': 'boto3-created-instance'
                    },
                ]
            },
        ]
    )

    print(response)

except botocore.exceptions.ClientError as error:
    # Put your error handling logic here
    raise error

except botocore.exceptions.ParamValidationError as error:
    raise ValueError('The parameters you provided are incorrect: {}'.format(error))