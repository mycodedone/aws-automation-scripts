import boto3
client=boto3.client('ec2')
resp=client.terminate_instances(InstanceIds=['i-0b76daa92a2e0ad63'])
for i in resp['TerminatingInstances']:
    print('this is the'+ i['InstanceId'] + 'which is terminated')

