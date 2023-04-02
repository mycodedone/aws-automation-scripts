import boto3
client=boto3.client('ec2')
resp=client.describe_instances(Filters=[{
    'Name':'tag:env',
    'Values':['prod','stage']
}]) # filtering ec2 using tags

for i in resp['Reservations']:
    for j in i['Instances']:
        print(j['InstanceId'],j['InstanceType'])
