// insert, update, save, set, unset

// Try this(1)

var s = db.Singer
for (let i=1; i <= 100; i++) {
		s.insert({name:'singer' + i, company: 'company' + i, likecnt: i})
	}
// db.Singer.drop()
db.Song.find()
db.Singer.find()
// Try this(2)
var aa = db.Singer.findOne({name: 'singer1'})
aa.albums = [1, 2, 3]
// db.Singer.update({name:'singer1'}, aa)
db.Singer.save(aa)

// Try this(3-1)
db.Singer.update( {name:'singer1'}, 
				 { 
					$set: { hitsongs: [
					    {title:'24/7', albumId: 1}, 
					    {title:'222', albumId: 2}
					    ] 
					} 
				 }
                )
// Try this(3-2)
var s2 = db.Singer.findOne({name: 'singer2'})
s2.hitsongs = [{title: '24/7', albumId: 1}, {title: '222', albumId: 2}]

db.Singer.save(s2)

//Try this(4)
db.Singer.update({name:'singer1'},{
                                    $unset : { likecnt:1}
                                    }
                )

