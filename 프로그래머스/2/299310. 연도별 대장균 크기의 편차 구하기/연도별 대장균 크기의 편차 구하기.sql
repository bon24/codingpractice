select d.year,size - size_of_colony as year_dev,id
from (select id,year(DIFFERENTIATION_DATE) as year,size_of_colony from ecoli_data) d 
left join (select max(size_of_colony) as size , year(DIFFERENTIATION_DATE) as year from ecoli_data group by year(DIFFERENTIATION_DATE)) n
on d.year = n.year
order by 1,2