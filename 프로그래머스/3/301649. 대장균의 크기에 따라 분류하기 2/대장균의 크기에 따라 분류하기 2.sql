-- 코드를 작성해주세요
select t.id,case t.분위
when 1 then 'CRITICAL' 
when 2 then 'HIGH'
when 3 then 'MEDIUM'
when 4 then 'LOW'
end as colony_name
from (select ntile(4) over(order by size_of_colony desc) as 분위
, id,size_of_colony
from ecoli_data) as t
ORDER BY 1

