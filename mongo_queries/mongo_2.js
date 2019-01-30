db.Singer.find()

//TryThis(1) Singer collection의 singer3에 albums에 10을 push 하시오.
db.Singer.update({name: 'singer3'},
                  {$push:
                    {
                        albums: 10
                    }
                  })

//TryThis(2) singer4의 albums에 100 ~ 110 까지 $each를 사용하여 push하시오.

var ar =[];
for(let i=0; i <= 10; i++){
ar[i] = 100 + i
}
ar

db.Singer.update({name: 'singer4'}, 
                  {
                      $addToSet: {
                          albums:{
                              $each : ar
                              
                          }
                          
                      }
                      
                  })


//TryThis(3) singer4의 albums에 105번을 제거하시오.
db.Singer.update({name: 'singer4'},
                  {
                      $pull: {albums: 105}
                  }
                )


//TryThis(4) singer4의 albums에 103번 보다 작은 앨범을 제거하시오.
db.Singer.update({name: 'singer4'},
                  {
                      $pull: {
                          albums: {
                              $lte: 103
                          }
                      }
                  }
                )

//TryThis(5) singer4의 albums에 [107, 109]를 제거하시오.

db.Singer.update({name: 'singer4'}, 
                  {$pull : {
                      albums: {
                          $in: [107, 109]
                      }
                      
                  }
                 }
                )

db.Singer.findOne({name:'singer4'})