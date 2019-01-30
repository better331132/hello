//TryThis(1) Singer collection의 singer1 ~ singer10 가수에 대해 likecnt가 존재하면 1증가 하고, 없으면 1로 초기화 하시오.
for(var i=1; i<=10; i++){
    db.Singer.update(
        {name:'singer'+i},
        {$inc:{likecnt:1}},
        true)
}

//TryThis(2) Singer collection의 likecnt=1인 문서 전체를 likecnt++ 하시오.

db.runCommand({
			findAndModify: 'Singer',
			query: { likecnt: 1 },
			sort: { _id: -1},
			update: { $inc:{likecnt: 1 }},
			new: true      // 갱신 후
		})

db.runCommand({
			findAndModify: 'Singer',
			query: { likecnt: 1 },
			sort: { _id: -1},
			update: { $inc:{likecnt: 1 }}
		}).value

db.Singer.find()