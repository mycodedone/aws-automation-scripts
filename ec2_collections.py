import boto3

ec2 = boto3.resource('ec2')

# Get a list of running instances
instances = ec2.instances.filter(Filters=[
    {
        'Name': 'instance-state-name',
        'Values': ['running']
    }
])

# Stop each instance
for i in instances:
    i.stop()
    print('the instance ID is ' + i.instance_id + ', the instance type is ' + i.instance_type)
