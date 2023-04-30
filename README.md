
# Sea-Your-Info 정보바다

 **정보바다**는 학과 공지사항, 장학 선발 안내 등 충북대학교 게시판에 올라오는 정보를 크롤링해 보여주는 프로그램입니다. 이 프로젝트는 데이터를 가져와 저장하는 웹 크롤러와 데이터를 전송하는 REST API 서버, 받은 데이터를 표시해주는 GUI 프로그램으로 구성됩니다. GUI 이외에도 이메일을 통해 알림을 받을 수도 있습니다. 데이터베이스로는 MariaDB를 사용합니다.
 
 **Sea-Your-Info** is a computer software program, which crawls notice from school website and demonstrates with GUI and email. This project contains web crawler, REST API server which store and send data to GUI, and python GUI system. This program also sends you an email of the previous day school notice at every 10:00 am in the morning 

## 폴더 구조 - Folder structure

- 🖼️**client** : GUI 프로그램을 담고 있는 폴더(Contains GUI part)
- ⌨️**crawler** : 웹 크롤러를 담고 있는 폴더(Contains web crawling part)
- 🌐**server** : Django와 DjangoRestFramework를 통한 REST API 서버를 담고 있는 폴더(Contains REST API server of Django and DjangoRestFramework)
- ✉**mail_server** : 공지사항 메일 전송 프로그램을 담고 있는 폴더(Contains the report mail sending program)

## 개발자 - Developer

(가나다 순, arrange in Korean alphabetical order)
  * [김 성욱(Kim SeongWook)](https://github.com/sori9899)
  * [유 현진(Yoo HyeonJin)](https://github.com/yu-podong)
  * [이 우창(Lee WooChang)](https://github.com/changi1122)
  * [이 원중(Lee WonJoong)](https://github.com/WonJoongLee)

## Built With

![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![MySQL](https://img.shields.io/badge/mysql-%2300f.svg?style=for-the-badge&logo=mysql&logoColor=white)

