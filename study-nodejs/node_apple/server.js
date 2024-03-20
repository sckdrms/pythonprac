const express = require('express')
const app = express()

app.use(express.static(__dirname + '/public'))
app.set('view engine', 'ejs')

const { MongoClient } = require('mongodb')

let db
const url = 'mongodb+srv://devrmss:rms13597123@cluster0.r2sn0qx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'
new MongoClient(url).connect().then((client)=>{
  console.log('DB연결성공')
  db = client.db('forum')
  app.listen(8080, () => {
    console.log('http://localhost:8080 에서 서버 실행중')
})
}).catch((err)=>{
  console.log(err)
})



app.get('/', (요청, 응답) => {
  응답.send('반갑다')
}) 

app.get('/car', (요청, 응답)=>{
  let time = new Date()
  응답.sendfile(__dirname+'/index.html')
})

app.get('/news', (요청, 응답) => {
  db.collection('post').insertOne({title:'어쩌구'})
  // 응답.sendfile(__dirname + '/index.html')
}) 

app.get('/about', (요청, 응답)=>{
  응답.sendfile(__dirname+'/about.html')
})

app.get('/time', (요청, 응답)=>{
  let time = new Date()
  응답.render('time.ejs', { time : time })
})

app.get('/list', async (요청, 응답)=>{
  let result = await db.collection('post').find().toArray()
  응답.render('list.ejs', { post : result })
})
