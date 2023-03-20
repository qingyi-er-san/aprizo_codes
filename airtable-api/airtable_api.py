import requests

# Airtable API基础URL和认证信息
API_URL = "https://api.airtable.com/v0/"
API_KEY = "patcCfV1FtoIjy1ke.d1a85b707f707558f64dab03a881c6c6f4e8256ecbaf582cf58c5ca400abe11e"



def get_table(base_id,table_id):
    url = f"{API_URL}{base_id}/{table_id}"
    headers = {"Authorization": f"Bearer {API_KEY}"}
    response = requests.get(url, headers=headers)
    return response.json()



# 获取记录
def get_record(base_id, table_name, record_id):
    url = f"{API_URL}{base_id}/{table_name}/{record_id}"
    headers = {"Authorization": f"Bearer {API_KEY}"}
    response = requests.get(url, headers=headers)
    return response.json()

# 创建记录
def create_record(base_id, table_name, data):
    url = f"{API_URL}{base_id}/{table_name}"
    headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
    response = requests.post(url, json=data, headers=headers)
    return response.json()

# 更新记录
def update_record(base_id, table_name, record_id, data):
    url = f"{API_URL}{base_id}/{table_name}/{record_id}"
    headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
    response = requests.patch(url, json=data, headers=headers)
    return response.json()

# 删除记录
def delete_record(base_id, table_name, record_id):
    url = f"{API_URL}{base_id}/{table_name}/{record_id}"
    headers = {"Authorization": f"Bearer {API_KEY}"}
    response = requests.delete(url, headers=headers)
    return response.json()

if __name__ == '__main__':
    base_id = "appajB79eLdP5AJEu"
    table_name = "Employe"

    # 获取记录
    record_id = "recb4jOp8VQesMiFA"
    record = get_record(base_id, table_name, record_id)
    print(record)

    """# 创建记录
    data = {"fields": {
                "Prenom": "Prenom6",
                "Nom": "Nom6\n",
                "salaire": 6666,
                "TéléTravailler": "oui",
      }}
    new_record = create_record(base_id, table_name, data)
    print(new_record)
    """

  
    # 更新记录
    data1 = {"fields":{
                "Prenom": "KFC",
                "Nom": "KFC\n",
                "salaire": 1230,
                "TéléTravailler": "oui",
                "mission":[
                    "recO10fsNoGE2pKfT"   
                ]
            }
    }

    update= update_record(base_id,table_name,record_id,data1)
    print(update)

    '''
    # 删除记录
    delete = delete_record(base_id,table_name,record_id)
    '''
    