import logo from './logo.svg';
import './App.css';
import { useState } from 'react';
import { NULL } from 'mysql/lib/protocol/constants/types';

function App() {

  let post = '강남 우동 맛집';
  let [name, 상호명변경] = useState(['엽기떡볶이', '신전떡볶이', '킹콩떡볶이'])
  let [logo, setLogo] = useState(['ReactBlog'])
  let [좋아요, 좋아요변경] = useState(0); 
  let [모달, set모달] = useState('열림');


  // const handleModalToggle = () => {
  //   if (모달 === '열림') {
  //     set모달('닫힘');
  //   } else {
  //     set모달('열림');
  //   }
  // };

  return (
    <div className="App">
      <div className='black-nav'>
        <h4 style={{color : 'white', fontSize : '20px'}}>{logo}</h4>
      </div>

      {/* <button onClick={()=>{ 
          let copy = [...name];
          copy[2] = '킹콩털볶이'
          상호명변경(copy) }}>이름변경</button>

      <button onClick={()=>{ 
          let copy = [...name];
          copy = copy.sort();
          상호명변경(copy) }}>이름 정렬</button> */}

      {/* <div className='list'>
        <h4>{name[0]} <span onClick={()=>{좋아요변경(좋아요+1)}}>👍</span> {좋아요} </h4>
        <p>2월 17일 발행</p>
        <h4>{name[1]} </h4>
        <p>2월 17일 발행</p>
        <h4 onClick={handleModalToggle}>{name[2]}</h4>
        <p>2월 17일 발행</p>
        {
          모달 == '닫힘' ? <Modal/> : null
        }
      </div> */}


      <List></List>
      {/* <input onChange={(e)=>{입력값변경(e.target.value);}} /> */}

    </div>
  );
}

function List (){
  let [name, 상호명변경] = useState(['엽기떡볶이', '신전떡볶이', '킹콩떡볶이']);
  let [좋아요, 좋아요변경] = useState([0,0,0]); 
  let [modal, setModal] = useState(false); // 모달 상태를 관리합니다.
  let [title, setTitle] = useState(null); // 선택된 항목의 인덱스를 관리합니다.
  let [입력값, 입력값변경] = useState('')

  // const 추가하기 = () => {
  //   상호명변경(prev => [...prev, 입력값]); // 상태 업데이트 함수에 콜백을 사용하여 이전 상태를 기반으로 새 배열 생성
  //   입력값변경(''); // 입력 필드 초기화
  // };

  const handleModalToggle = () => {
    if (modal === false) {
      setModal(true);
    } else {
      setModal(false);
    }
  };

  return (
    <div className='list'>
      {name.map((itemName, index) => (
        <div key={index}>
          <h4 onClick={() => {
              handleModalToggle(true); // 모달을 열기
              setTitle(index); // 현재 클릭한 항목의 인덱스를 저장
            }}>
            {itemName}
            <span onClick={(e) => {
              e.stopPropagation(); // h4 클릭 이벤트가 발생하지 않도록 합니다.
              let newLikes = [...좋아요];
              newLikes[index] = 좋아요[index] + 1;
              좋아요변경(newLikes);
            }}>👍</span> {좋아요[index]}
          </h4>
          <p>몇월 몇일</p>
          {/* <button onClick={()=>{name.splice(index,1)}}>삭제하기</button> */}
          {/* <button onClick={() => {
            상호명변경(currentNames => currentNames.filter((_, filterIndex) => index !== filterIndex));
          }}>삭제하기</button> */}
          <button onClick={()=>{
            let copy = [...name];
            copy.splice(index,1)
            상호명변경(copy);}}>삭제</button>
        </div>
      ))}

      {/* <input value={입력값} onChange= {(e)=> 입력값변경(e.target.value)} /> */}
      <input onChange={(e)=>{
        입력값변경(e.target.value)
      }} />

      {/* <button onClick={추가하기}>추가하기</button> */}
      <button onClick={() => {
        let copy = [...name];
        copy.unshift(입력값);
        상호명변경(copy);
        입력값변경('');
      }}>추가하기</button>
      {modal == true ? <Modal 상호명변경={상호명변경} color={''} title={title !== null ? name[title] : ''} /> : null}
    </div>
  );
}

function Modal({title, color, 상호명변경}){
  return(
    <div className='modal' style={{background : color}}>
      <h4>{title}</h4> {/* 제목을 props로 받아와서 표시 */}
      <p>날짜</p>
      <p>상세내용</p>
      <button>제목 변경</button>
    </div>
  );
}


// function StoreComponent() {
//   const [name, setName] = useState(['엽기떡볶이', '신전떡볶이', '킹콩떡볶이']);

//   return (
//     <div>
//       {name.map((a, i) => (
//         <div className='list' key={i}>
//           <h4> {a}</h4>
//           <p>2월 17일 발행</p>
//         </div>
//       ))}
//     </div>
//   );
// }



export default App;
