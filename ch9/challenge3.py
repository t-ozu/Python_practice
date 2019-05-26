import csv

test_list = [["Top Gun", "Riskey Business", "Minority Report"],["Titanic","The Revenant","Inception"],["Training Day","Man on fire","Flight"]]
with open("test.csv", "w", newline='') as f:
    st = csv.writer(f,delimiter=",")
    st.writerow(test_list[0])
    st.writerow(test_list[1])
    st.writerow(test_list[2])
