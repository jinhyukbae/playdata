import pymysql                                # sqlite3 모듈 탑재
from select import select_one_book    # 데이터 조회용 함수 탑재


# 데이터 수정용 함수
def update_books():
    conn = pymysql.connect(host='127.0.0.1', user = 'root', password = '1234', db = 'testdb', charset = 'utf8')       # 데이터베이스 커넥션 생성
    cur = conn.cursor()  # 커서 확보

    # 데이터 수정 SQL ( 제목이 ? 인 책의 추천 유무를 ? 로 변경하라 )
    update_sql = 'UPDATE mybooks SET recommendation=%s WHERE title=%s'

    # 수정 SQL 실행
    cur.execute(update_sql, (1, '개발자의 코드'))

    conn.commit()                                   # 데이터베이스 반영
    conn.close()                                    # 커넥션 닫기

if __name__ == "__main__":		                # 외부에서 호출 시
    select_one_book()
    update_books()                                  # 데이터 수정 함수 호출
    print('[데이터 수정 완료] ================== ')
    select_one_book()
