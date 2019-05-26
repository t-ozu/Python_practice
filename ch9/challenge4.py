import csv

test_list = [["トップガン", "リスキービジネス", "マイノリティーレポート"],["タイタニック","レヴェナント","インセプション"],["トレーニングデイ","マンオンファイア","フライト"]]
with open("testja.csv", "w", encoding="cp932",newline='') as f:
    st = csv.writer(f,delimiter=",")
    st.writerow(test_list[0])
    st.writerow(test_list[1])
    st.writerow(test_list[2])
