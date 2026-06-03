# 1-3 4-6 7-9 10-12
select t.quarter,count(*) as ecoli_count
from (select id,
     case 
     when month(DIFFERENTIATION_DATE)>=1 and month(DIFFERENTIATION_DATE)<4      then '1Q'
     when month(DIFFERENTIATION_DATE)>=4 and month(DIFFERENTIATION_DATE)<7      then '2Q'
     when month(DIFFERENTIATION_DATE)>=7 and month(DIFFERENTIATION_DATE)<10      then '3Q'
     when month(DIFFERENTIATION_DATE)>=10 and month(DIFFERENTIATION_DATE)<13      then '4Q' end as quarter from ecoli_data ) as t
group by quarter order by 1