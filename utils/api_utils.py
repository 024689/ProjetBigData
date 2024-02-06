from typing import Optional
from .hdfs_utils import send_file_to_hdfs
import requests


def get_data_from_api(api_url: str, params: dict = None, headers: dict = None) -> Optional[dict]:
    try:
        response = requests.get(api_url, headers=headers, params=params)
        if response.status_code == 200:
            data = response.json()
            print(f"Data fetch successfully")
            return data
        else:
            print(f"Request failed with code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Some error occurred : {e}")
        return None


def get_data_from_api_and_save_to_hdfs(
        api_url: str, hdfs_path: str, params: dict = None,
        headers: dict = None) -> Optional[dict]:
    try:
        data = get_data_from_api(
            api_url=api_url, params=params, headers=headers)
        send_file_to_hdfs(json_data=data, hdfs_path=hdfs_path)
        return data
    except requests.exceptions.RequestException as e:
        print(f"Some error occurred : {e}")
        return None

#recupérer les données d'une api paginer
def get_data_with_pagination_from_api(
        api_url: str, total_page_key: [str], data_key: [str],
        param_page_key: [str], total_page: int = None,
        params: dict = None, headers: dict = None) -> [dict]:
    response = requests.get(api_url, headers=headers, params=params)
    data = response.json()
    data_res = data
    for key in data_key:
        data_res = data_res[key]
    print(len(data_res))
    result: [dict] = data_res
    data_res = data
    if total_page is None:
        for key in total_page_key:
            data_res = data_res[key]
        total_page = data_res
    for index in range(2, total_page + 1):
        params[param_page_key[0]] = index
        response = requests.get(api_url, headers=headers, params=params)
        data_res = response.json()
        for key in data_key:
            data_res = data_res[key]
        result += data_res
        print(len(result))
    return result


def get_data_with_pagination_from_api_and_save_to_hdfs(
        api_url: str, hdfs_path, data_key: [str],
        param_page_key: [str], total_page_key: [str],
        total_page: int = None,
        params: dict = None, headers: dict = None) -> Optional[dict]:
    try:
        data = get_data_with_pagination_from_api(
            api_url=api_url, data_key=data_key, total_page_key=total_page_key,
            param_page_key=param_page_key, total_page=total_page, params=params,
            headers=headers)
        send_file_to_hdfs(hdfs_path=hdfs_path, json_data=data)
        return data
    except requests.exceptions.RequestException as e:
        print(f"Some error occurred : {e}")
        return None
