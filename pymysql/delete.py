import pymysql                                   # sqlite3 모듈 탑재
from select import select_all_books    # 데이터 조회용 함수 탑재


# 데이터 삭제용 함수
def delete_books():
    conn = pymysql.connect(host='127.0.0.1', user = 'root', password = '1234', db = 'testdb', charset = 'utf8')       # 데이터베이스 커넥션 생성
    cur = conn.cursor()                           # 커서 확보

    # 데이터 삭제 SQL ( 출판사가 ? 인 책을 삭제하라 )
    delete_sql = 'DELETE FROM mybooks WHERE publisher=%s'

    # 수정 SQL 실행
    cur.execute(delete_sql, 'A')

    conn.commit()                                   # 데이터베이스 반영
    conn.close()                                    # 커넥션 닫기

if __name__ == "__main__":		                # 외부에서 호출 시
    select_all_books()                              # 테이블 전체 데이터 확인
    delete_books()                                  # 데이터 삭제 함수 호출
    print('[데이터 삭제 완료] ================== ')
    select_all_books()                              # 테이블 전체 데이터 확인
