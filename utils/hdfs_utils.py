from hdfs import InsecureClient
import json


def send_file_to_hdfs(hdfs_path: str, json_data: dict) -> bool:
    try:
        hdfs_client = InsecureClient("http://localhost:9870")
        json_str = json.dumps(json_data)
        with hdfs_client.write(hdfs_path, encoding='utf-8', overwrite=True) as writer:
            writer.write(json_str)
        print("téléversement vers HDFS réussi")
        return True
    except Exception as e:
        print(f"Some error occurred during writing to hdfs: {e}")
        return False
