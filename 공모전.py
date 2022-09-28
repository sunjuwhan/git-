# from cgitb import text
# import requests

# from bs4 import BeautifulSoup
# url ="https://comic.naver.com/webtoon/list?titleId=748105&weekday=thu"
# res=requests.get(url)

# res.raise_for_status()

# soup=BeautifulSoup(res.text,"lxml")
# cartoons=soup.find_all("",attrs={"class":"title"})
# title=cartoons[1].a.get_text()
# print(title)

# print(soup.title.get_text())  text파일로 출력 해준다.
# print(soup.a.attrs)  //a 속성 정보 출력
# print(soup.a["href"])
# print(soup.find("a",attrs={"class":"Nbtn_upload"}))


# rank1=soup.find("ul",attrs={"class":"menu_im"})
# rank2=rank1.select('p')

# rank2=soup.find_next_sibling("li")
# rank3=soup.find_next_sibling("p")
# print(rank3)
# rank1=soup.find("ol",attrs={"id":"realTimeRankFavorite"})
# rank1=soup.find("li",attrs={"class":"first"})  //
# rank2=soup.find_next_sibling("li")
# rank3=soup.find_next_sibling("li")
# print(rank3)  //식단표
# rank2=rank1.find_next_sibling("li")  #li에 해당하는 다음 클래스를 찾아준다 즉 rank 2를 찾아준다.
# print(rank2.a.get_text())
# rank3=rank2.find_next_sibling("li")
# print(rank3.a.get_text())
# print(rank1.get_text())
#한글인지 

string ="치즈스틱롤돈가스★￦ 5,000"
char="★￦ 5,000"
for x in range(len(char)):
    string=string.replace(char[x],"")
print(string)