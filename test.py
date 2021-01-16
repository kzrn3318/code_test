"""
m,s,iは問題文と同じ役割としています。
"""

def convert(data: 'list[str]',m: int) -> dict:
    result_dict: dict = {}

    for line in read_data:
        
        line = line.replace("\n","")#fileを読み込んだ時に\nが入っていたので置換
        
        i: int = int(line.split(":")[0])#mと比べるためint型へ
        s: str = str(line.split(":")[1])#出力用のstr
        
        if m%i == 0:
            result_dict[i] = s
            
    return result_dict

if __name__=="__main__":
    with open('input.txt', mode='r', encoding='utf-8') as f:
        read_data = list(f)

    m = read_data[-1]  
    m: int = int(m.replace("\n",""))#fileを読み込んだ時に\nが入っていたので置換しint型に

    read_data: list = read_data[:-1]

    result_dict = convert(read_data,m)

    if len(result_dict)==0:#sの出力がないためmをそのまま出力
        print(m)
    else:
        result_dict = dict(sorted(result_dict.items(), key=lambda x:x[0]))
        result_str = list(result_dict.values())
        print("".join(result_str))
