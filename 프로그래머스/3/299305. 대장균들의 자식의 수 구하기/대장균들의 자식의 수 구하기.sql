-- 코드를 작성해주세요
with cnt as(
select parent_id,count(*) as cnt from ecoli_data where parent_id is not null group by parent_id)

select d.id, ifnull(cnt,0) as child_count
from ecoli_data d left join cnt c on d.id=c.parent_id
order by 1
