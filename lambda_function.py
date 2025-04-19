def lambda_handler(event, context):
    print("===UPDATED===")
    return {
        'statusCode': 200,
        'body': 'Lambda updated via CodePipeline!'
    }
