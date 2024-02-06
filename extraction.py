import json

from utils.api_utils import get_data_from_api_and_save_to_hdfs, get_data_from_api, \
    get_data_with_pagination_from_api_and_save_to_hdfs, get_data_with_pagination_from_api


# Toutes les fonctions permettant de reccueillir les données depuis l'api
# devrons être appeler dans cette fonction
def extraction_from_api_and_save_to_hdfs(current_date: str):
    print("helloWord")
    competitionMatch(current_date=current_date)
    

def competitionMatch(current_date): 
    get_data_from_api_and_save_to_hdfs(api_url="https://api.football-data.org/v4/competitions/PL", 
                                       headers= {"X-Auth-Token": "3338355fcebf4b17b2ccfacbd4eba2b2"}, hdfs_path=f"/datalake/raw/match/{current_date}.json")

competitionMatch("2024-02-06")
    
# def find_popular_movies_and_save(current_date):
#     params = {
#         "api_key": "888d24dde3ad84956d00e02d0161d41f",
#         "page": 1
#     }
#     data = get_data_with_pagination_from_api_and_save_to_hdfs(
#         api_url="https://api.themoviedb.org/3/movie/popular",
#         total_page_key=["total_pages"],
#         total_page=500, data_key=["results"],
#         params=params, param_page_key=["page"], hdfs_path="/sda/")
#
#     print(json.dumps(data, indent=2))
#     print(len(data))


# find_popular_movies_and_save("")
