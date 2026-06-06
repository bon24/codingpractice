-- 코드를 입력하세요
select i.animal_id,animal_type,name
from animal_outs o 
left join (SELECT animal_id from animal_ins where sex_upon_intake like 'Intact%') i 
on o.animal_id = i.animal_id
where (SEX_UPON_OUTCOME like 'Neutered%' or SEX_UPON_OUTCOME like 'Spayed%')
and i.animal_id is not null
order by 1