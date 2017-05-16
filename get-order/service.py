import boto3

def lambda_handler(event, context):
    order_id = event['order_id']
    print("Order Id %s"%order_id)
    orders = boto3.resource('dynamodb').Table('orders')
    return orders.get_item(Key={'order_id': order_id})['Item']