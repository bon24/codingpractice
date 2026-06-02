-- 코드를 입력하세요
select datetime
from animal_ins
where datetime = (select min(datetime) from animal_ins)