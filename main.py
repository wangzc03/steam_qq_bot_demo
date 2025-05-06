import uvicorn
import a2s
import requests
from fastapi import FastAPI, Request
from concurrent.futures import ThreadPoolExecutor

# 改成你的ip 然后查看端口是27015还是别的什么
# http://api.steampowered.com/ISteamApps/GetServersAtAddress/v0001?addr=123.456.78.90
# 文档
# https://python-abc.xyz/qqbot/onebot-11/api/public
rsQuery = '越南1'
roQuery = '红管11'
testQuery = "ping"


def do_query_new(addresses, timeout=4):
    result = []
    with ThreadPoolExecutor(max_workers=10) as executor:  # 设置最大线程数
        futures = {executor.submit(query_server_new, address, timeout): address for address in addresses}
        for future in futures:
            try:
                ret_part = future.result()
                if ret_part:
                    result.append(ret_part)
            except Exception as e:
                custom_name, ip, port = futures[future]
                print(f"查询{ip}:{port}({custom_name})时发生错误: {e}")
    return ''.join(result)

def query_server_new(address, timeout):
    custom_name, ip, port = address
    try:
        server_data = a2s.info((ip, port), timeout=timeout)

        # 检查 map_name 是否以 "VNTE-" 开头，如果是则去掉这五个字符
        map_name = server_data.map_name[5:] if server_data.map_name.startswith("VNTE-") else server_data.map_name
        
        # 使用自定义的server_name，并添加分隔行与服务器信息到结果列表
        ret_part = "{},{},{}人\n".format(
            custom_name, 
            map_name,
            server_data.player_count
        )
        return ret_part
    except Exception as e:
        return None

def queryRo2():
    addresses = [
        ("sgs24h", "114.132.69.243", 27018),
        # EU
        ("EU-RO", "31.186.250.228", 27015),
        ("EU-RS", "185.107.96.131", 27015),

    ]
    return do_query_new(addresses)

def queryRs2():
    addresses = [
        # sea
        ("sea选图", "219.78.127.189", 34918),
        ("sea战役", "219.78.127.189", 27018),
        # [China]|ShangHai|MapVoting
        ("上海", "124.222.154.131", 27015),
     ]
    return do_query_new(addresses)






app = FastAPI()

@app.post("/onebot")
async def handle_message(request: Request):
    data = await request.json()   # 获取事件数据
    if data.get('post_type') == 'message' and data.get('message_type') == 'group':
        message_content = data['raw_message']
        group_id = data['group_id']
        sender_nickname = data['sender']['nickname']
        sender_card = data['sender']['card']
        print(f"Message from Group {group_id}: '{message_content}' (Sent by {sender_nickname} aka {sender_card})")
        if rsQuery in message_content:
            send_ping(group_id, queryRs2())
        if roQuery in message_content:
            send_ping(group_id, queryRo2())  
        if message_content.lower() == "ping":
            send_ping(group_id,"pong")    
            
    
    return {"status": "success"}


def send_ping(group_id: int,text: str):
    url = "http://127.0.0.1:3000/send_group_msg"
    headers = {'Content-Type': 'application/json'}
    data = {
        "group_id": group_id,
        "message": text,
        "auto_escape": False
    }
    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 200:
        print("Ping message sent successfully.")
    else:
        print(f"Failed to send ping message: {response.text}")



if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=9961)
