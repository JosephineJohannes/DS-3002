import boto3

response = client.run_instances(
  ImageId='ami-02354e95b39ca8dec',
  InstanceType='t2.micro',
  KeyName='<YOUR_KEY_NAME>',
  SecurityGroupIds=[
    '<YOUR_SECURITY_GROUP>',
  ],
  SubnetId='<YOUR_SUBNET>',
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