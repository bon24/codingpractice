-- 코드를 입력하세요
with food as(SELECT sum(amount) as amount,product_id
from food_order 
where date_format(produce_date,'%Y-%m') = '2022-05'
group by product_id)

select product_id,product_name,price*amount as total_sales
from food_product p
join food f
using(product_id)
order by 3 desc, 1