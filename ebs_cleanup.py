import json
import boto3

def lambda_handler(event, context):
    # Initialize EC2 client
    ec2 = boto3.client('ec2')
    
    # Get all EBS snapshots - Handle pagination for large sets of snapshots
    snapshots = []
    next_token = None
    while True:
        if next_token:
            # Get snapshots in the same AWS account (self)
            response = ec2.describe_snapshots(OwnerIds=['self'], NextToken=next_token)
        else:
            # Get snapshots in the same AWS account (self)
            response = ec2.describe_snapshots(OwnerIds=['self'])
        
        snapshots.extend(response['Snapshots'])
        next_token = response.get('NextToken')
        if not next_token:
            break
    
    # Get all active EC2 instance IDs - Handle pagination for large sets of instances
    active_instance_ids = set()
    next_token = None
    while True:
        if next_token:
            # Filter for instances in the 'running' state (Modify 'running' if you want other states)
            instances_response = ec2.describe_instances(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}], NextToken=next_token)
        else:
            instances_response = ec2.describe_instances(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
        
        for reservation in instances_response['Reservations']:
            for instance in reservation['Instances']:
                active_instance_ids.add(instance['InstanceId'])  # Collect running instance IDs
        
        next_token = instances_response.get('NextToken')
        if not next_token:
            break
    
    # Iterate through each snapshot and delete if it's not attached to any volume or the volume is not attached to a running instance
    for snapshot in snapshots:
        snapshot_id = snapshot['SnapshotId']  # The unique ID of the snapshot
        volume_id = snapshot.get('VolumeId')  # The ID of the volume the snapshot is associated with
        
        if not volume_id:
            # Delete the snapshot if it's not attached to any volume
            try:
                ec2.delete_snapshot(SnapshotId=snapshot_id)  # Ensure proper IAM permissions to delete snapshots
                print(f"Deleted EBS snapshot {snapshot_id} as it was not attached to any volume.")
            except Exception as e:
                print(f"Failed to delete snapshot {snapshot_id}: {str(e)}")
        else:
            # Check if the volume still exists
            try:
                volume_response = ec2.describe_volumes(VolumeIds=[volume_id])
                
                if not volume_response['Volumes'][0]['Attachments']:
                    # The volume exists but is not attached to any instance, so delete the snapshot
                    ec2.delete_snapshot(SnapshotId=snapshot_id)
                    print(f"Deleted EBS snapshot {snapshot_id} as it was taken from a volume not attached to any running instance.")
            except ec2.exceptions.ClientError as e:
                if e.response['Error']['Code'] == 'InvalidVolume.NotFound':
                    # The volume associated with the snapshot is not found (it might have been deleted)
                    try:
                        ec2.delete_snapshot(SnapshotId=snapshot_id)
                        print(f"Deleted EBS snapshot {snapshot_id} as its associated volume was not found.")
                    except Exception as delete_exception:
                        print(f"Failed to delete snapshot {snapshot_id}: {str(delete_exception)}")
                else:
                    print(f"Error retrieving volume {volume_id} for snapshot {snapshot_id}: {str(e)}")
