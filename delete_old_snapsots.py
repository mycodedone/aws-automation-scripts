from datetime import datetime,timedelta,timezone
import boto3
ec2=boto3.resource('ec2')
snapshots=ec2.snapshots.filter(OwnerIds=['self'])


for snapshot in snapshots:
    start_time=snapshot.start_time
    delete_time=datetime.now(tz=timezone.utc)-timedelta(days=15)
    if delete_time>start_time:
        print('snapshot taken on '+ start_time+' and the delete time is '+ delete_time)