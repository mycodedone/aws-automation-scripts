import boto3
ec2=boto3.resource('ec2')
sns_client=boto3.client('sns')
backup_filter=[
    {
    'Name':'tag:backup',
    'Values':['level1']
    }
]
snapshot_ids=[]
for instance in ec2.instances.filter(Filters=backup_filter):
    for vol in instance.volumes.all():
        snapshot=vol.create_snapshot(Description='created by boto3')
        snapshot_ids.append(snapshot.snapshot_id)

sns_client.publish(
    TopicArn='arn:aws:sns:ap-south-1:162290034861:snapshot',
    Subject=' ebs snapshots ',
    Message=str(snapshot_ids)
)