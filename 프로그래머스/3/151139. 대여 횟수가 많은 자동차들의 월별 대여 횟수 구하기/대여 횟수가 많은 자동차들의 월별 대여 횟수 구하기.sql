-- 코드를 입력하세요
# GROUP BY하면 GROUP BY에 쓰인 컬럼만 SELECT 할수있어서 이렇게 된듯?
with car as(
select car_id from CAR_RENTAL_COMPANY_RENTAL_HISTORY 
where start_date between '2022-08-01' and '2022-10-31'
group by car_id having count(*)>=5)

select month(start_date) as month,car_id, count(*) as records
from CAR_RENTAL_COMPANY_RENTAL_HISTORY 
where car_id in (select car_id from car) and start_date between '2022-08-01' and '2022-10-31'
group by month(start_date),car_id
order by 1,2 desc