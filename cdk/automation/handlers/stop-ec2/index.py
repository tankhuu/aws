import json
import boto3

def handler(event, context):
  ec2 = boto3.resource('ec2')
  try:
    instances = ec2.instances.filter(
    Filters=[
      {'Name': 'instance-state-name', 'Values': ['running']},
      {'Name': 'tag:Name', 'Values': ['Jenkins']}
    ])
    for inst in instances:
      print('[INFO] gonna stop instances: ', inst)
      stop_result = inst.stop()
      print('[INFO] Instance is stopping', stop_result)
  except Exception as e:
    print(e)
    raise e

  return {
    "statusCode": 200,
    "body": json.dumps({
        "message": "Stopped ec2 parttime instances of EdulogVN"
    }),
  }