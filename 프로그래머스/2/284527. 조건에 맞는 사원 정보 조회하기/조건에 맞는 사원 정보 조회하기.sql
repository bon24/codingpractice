# 테이블에서 2022년도 한해 평가 점수가 가장 높은 사원 정보를 조회하려 합니다.
select SCORE, g.EMP_NO,EMP_NAME,POSITION,EMAIL
from hr_employees e
left join (select emp_no,sum(score) as score from hr_grade group by emp_no) g
on e.EMP_NO = g.EMP_NO
where score = (select max(score) from hr_employees e left join (select emp_no,sum(score) as score from hr_grade group by emp_no) g on e.EMP_NO = g.EMP_NO)


