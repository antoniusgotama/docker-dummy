import subprocess
import boto3
from datetime import datetime

def get_docker_logs(container_name):
    """Get logs from a specific Docker container using docker logs command"""
    try:
        result = subprocess.run(['docker', 'logs', container_name], 
                              capture_output=True, 
                              text=True)
        if result.returncode == 0:
            return result.stdout
        else:
            print(f"Error getting logs: {result.stderr}")
            return None
    except Exception as e:
        print(f"Error executing docker logs command: {e}")
        return None

def send_logs_to_s3(logs, bucket_name, file_name):
    """Send logs to AWS S3"""
    try:
        s3_client = boto3.client('s3')
        s3_client.put_object(
            Bucket=bucket_name,
            Key=file_name,
            Body=logs
        )
        print(f"Logs successfully uploaded to s3://{bucket_name}/{file_name}")
    except Exception as e:
        print(f"Error uploading to S3: {e}")

if __name__ == "__main__":
    # Configuration
    CONTAINER_NAME = "my-container"
    BUCKET_NAME = "test"
    FILE_NAME = f"docker-logs-{CONTAINER_NAME}-{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}.txt"

    # Get Docker logs
    logs = get_docker_logs(CONTAINER_NAME)
    if logs:
        # Send to S3
        send_logs_to_s3(logs, BUCKET_NAME, FILE_NAME)
