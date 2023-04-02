import boto3

region_name = 'ap-south-1'
ec2 = boto3.client('ec2', region_name=region_name)

instance_id = 'i-0bf34dd89d3fb7a66'
image_ids = []

image = ec2.create_image(
    InstanceId=instance_id,
    Name='demo image - '+ instance_id,
    Description='created by boto - ' + instance_id
)
image_ids.append(image['ImageId'])
print('this is the ami id ' + image['ImageId'])

client = boto3.client('ec2', region_name=region_name)
waiter = client.get_waiter('image_available')

waiter.wait(Filters=[{'Name': 'image-id', 'Values': image_ids}])

# copy ami to another region
destination_region = 'us-east-1'

client = boto3.client('ec2', region_name=destination_region)
for i in image_ids:
    client.copy_image(Name='boto3', SourceImageId=i, SourceRegion=region_name)
